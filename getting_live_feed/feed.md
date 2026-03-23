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

## What Does it do
This code uses the OpenCV library to access your laptop’s webcam and display a live video feed. It starts by importing cv2, which provides tools for working with images and cameras. The line cv2.VideoCapture(0) opens the default webcam (camera index 0). Then, a loop runs continuously as long as the camera is open. Inside the loop, cam.read() captures a frame from the webcam, returning both a success flag (ret) and the image itself (frame). The captured frame is then displayed in a window using cv2.imshow(), and cv2.waitKey(1) allows the window to refresh quickly so the images appear as a smooth video stream. After the loop ends, cam.release() turns off the camera, and cv2.destroyAllWindows() closes any open display windows.

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
