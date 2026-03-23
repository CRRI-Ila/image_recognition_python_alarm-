# Webcam Feed Project

This repository is the first step of my project.

## First Milestone
The goal of this step was to connect my laptop webcam to Python and display a live camera feed.

## What I learned
- How to use OpenCV in Python
- How to access my laptop webcam
- How to capture frames from the camera
- How to display a live webcam feed in a window
- How to stop the feed safely

<img width="2543" height="1349" alt="image" src="https://github.com/user-attachments/assets/f66d4fb8-d52c-476a-a67b-69a2c8532b35" />

## Code used

```python
import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    cv2.imshow("Webcam Feed", frame)
    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()
