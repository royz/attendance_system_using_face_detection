import subprocess
try:
    import cv2
except ModuleNotFoundError:
    print('opencv not installed.\ninstalling opencv...')
    subprocess.run('pip install opencv-python', shell=True)
    import cv2
print('press "Q" to exit')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_stream = cv2.VideoCapture(0)

while video_stream.isOpened():
    _, img = video_stream.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_stream.release()
