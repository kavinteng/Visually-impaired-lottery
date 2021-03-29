import cv2
import math
import playsound
import time

def is_close(p1, p2):
    dst = math.sqrt(p1 ** 2 + p2 ** 2)
    return dst

def main():
    num = 1
    z = 1
    starttime = 0
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            dx, dy = (x - x+w), (y - y+h)
            distance = int(is_close(dx, dy))
            # print(distance)
            if distance > 200 and z == 1:
                playsound.playsound('hello.mp3', True)
                z=0
                # เปลี่ยนตำแหน่งบันทึกไฟล์
                out = cv2.VideoWriter("../camera_distance/saved/video%d.mp4" % (num),
                                      cv2.VideoWriter_fourcc(*'MP4V'), 25.0, (frame_width, frame_height))
                num += 1
                starttime = time.time()
            if z == 0:
                out.write(img)
            if time.time()>starttime+300:
                z=1

        cv2.imshow('img', img)
        k = cv2.waitKey(1) & 0xff
        if k==ord('q'):
            break
    cap.release()
    try:
        out.release()
    except:
        pass
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()