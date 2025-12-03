import cv2
import mediapipe as mp
import os
import csv

# mediapipe oluşturulur 
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=True,
                       max_num_hands=1,
                       min_detection_confidence=0.5)

input_folder = "framesGeri"
output_csv = "data/el_noktalariGeri.csv"

with open(output_csv, mode="w", newline='') as file:
    writer = csv.writer(file)

    header = ["frame"]
    for i in range(21):
        header += [f"x{i}", f"y{i}", f"z{i}"] 
    writer.writerow(header)

    for img_name in os.listdir(input_folder):
        img_path = os.path.join(input_folder, img_name)
        frame = cv2.imread(img_path)

        if frame is None:
            continue

        h, w, c = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        row = [img_name]

        if result.multi_hand_landmarks:
            handLms = result.multi_hand_landmarks[0]

            # Bilek noktası kaydedilir
            wrist = handLms.landmark[0]
            wrist_x = wrist.x * w
            wrist_y = wrist.y * h
            wrist_z = wrist.z 

            for lm in handLms.landmark:
                cx = lm.x * w
                cy = lm.y * h
                cz = lm.z  

                # noktalar bilek noktasına göre kaydedilir
                rel_x = cx - wrist_x
                rel_y = cy - wrist_y
                rel_z = cz - wrist_z

                row += [rel_x, rel_y, rel_z]

        else:
            row += [0] * 63

        writer.writerow(row)

        if result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
print("Tüm framelerin normalize edilmiş XYZ el noktaları CSV’ye kaydedildi:", output_csv)