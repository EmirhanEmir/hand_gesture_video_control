import pickle
import cv2
import mediapipe as mp
import numpy as np
import time

# Modelleri yükle
with open("logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler_model.pkl", "rb") as f:
    scaler = pickle.load(f)

# mediapipe tespit ayarları
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

hareketler = {"başla":0, "dur":1, "ileri":2, "geri":3}

# Video ve kamera
video_path = "ornek_video/ornek_video.mp4"
cam_cap = cv2.VideoCapture(0)
video_cap = cv2.VideoCapture(video_path)

cam_width, cam_height = 160, 120  # Küçük kamera penceresi boyutu

ileri_sar = 300
geri_sar = 300
oynat = True
son_tetikleme = time.time()

if not video_cap.isOpened():
    print("Video açılamadı!")
    exit()
if not cam_cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:

    if oynat:
        video_ret, video_frame = video_cap.read()
        if not video_ret:
            break
    else:
        current_frame = video_cap.get(cv2.CAP_PROP_POS_FRAMES)
        video_cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    cam_ret, cam_frame = cam_cap.read()

    if not cam_ret:
        break

    h, w, c = cam_frame.shape
    rgb_frame = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(cam_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Bilek noktasına göre normalize
        wrist = hand_landmarks.landmark[0]
        wrist_x = wrist.x * w
        wrist_y = wrist.y * h
        wrist_z = wrist.z

        landmarks = []
        for lm in hand_landmarks.landmark:
            cx = lm.x * w
            cy = lm.y * h
            cz = lm.z
            rel_x = cx - wrist_x
            rel_y = cy - wrist_y
            rel_z = cz - wrist_z
            landmarks.extend([rel_x, rel_y, rel_z])

        landmarks = np.array(landmarks).reshape(1, -1)
        landmarks_scaled = scaler.transform(landmarks)

        # Tahmin
        prediction = model.predict(landmarks_scaled)
        predicted_class = prediction[0]
        probs = model.predict_proba(landmarks_scaled)
        max_prob = np.max(probs)

        if max_prob > 0.8:
            cv2.putText(cam_frame, f"Hareket: {predicted_class}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.putText(cam_frame, "Hareket: bilinmiyor", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            

        
        if time.time() - son_tetikleme > 3:
            current_frame = video_cap.get(cv2.CAP_PROP_POS_FRAMES)
            video_son_kare = video_cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1

            if predicted_class == 3:  # ileri
                video_cap.set(cv2.CAP_PROP_POS_FRAMES, min(current_frame + ileri_sar, video_son_kare))
                video_ret, video_frame = video_cap.read()
            elif predicted_class == 2:  # geri                   
                video_cap.set(cv2.CAP_PROP_POS_FRAMES, max(current_frame - geri_sar, 0))
                video_ret, video_frame = video_cap.read()
            elif predicted_class == 0:  # başla
                oynat = True
            elif predicted_class == 1:  # dur
                oynat = False

            son_tetikleme = time.time()
        


        
    # Kamerayı videonun üzerine küçük pencere olarak ekle
    frame_cam_small = cv2.resize(cam_frame, (cam_width, cam_height))
    vh, vw, _ = video_frame.shape
    x_offset = 10   
    y_offset = 10   
    video_frame[y_offset:y_offset+cam_height, x_offset:x_offset+cam_width] = frame_cam_small

    cv2.imshow("Video + Kamera", video_frame)  # tek pencere olarak gösteriyoruz

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Program kapatılıyor...")
        break

cam_cap.release()
video_cap.release()
cv2.destroyAllWindows()
