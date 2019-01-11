import cv2
import dlib
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
while cap.isOpened():
    _,frame = cap.read()
    dets = detector(frame, 1)
    for idx, face in enumerate(dets):
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0,255,0), 3)
    cv2.imshow("face-detection", frame)
    cv2.waitKey(5)


