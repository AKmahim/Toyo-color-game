import cv2

cap = cv2.VideoCapture()

for i in range(10):
    cap.open(i)
    if cap.isOpened():
        print(f"Camera index {i} is available")
        cap.release()
