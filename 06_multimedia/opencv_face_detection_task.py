import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # ('D','I','V','X')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

# xml 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)

    cv2.imshow('frame',frame)
    # 1000->1초,10->0.01초
    if cv2.waitKey(10) == 13:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
