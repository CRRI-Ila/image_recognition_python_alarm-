import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    cv2.imshow("Webcam Feed", frame)
    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()