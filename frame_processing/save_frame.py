import cv2
import os

video_path = "dur.mp4"
output_folder = "framesDur"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_frequancy = int(3)


frame_count = 0
saved = 0

while True:
    succes, frame = cap.read()
    if not succes:
        break

    if frame_count % frame_frequancy == 0:
        file_name = f"frame_{saved}.jpg"
        cv2.imwrite(os.path.join(output_folder, file_name), frame)
        saved += 1
    
    frame_count += 1