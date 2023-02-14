import cv2


def camera_video(cam):
    camera = cv2.VideoCapture(cam)
    while True:
        x, img_frame = camera.read() 
        if not x:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', img_frame)
            img_frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_frame + b'\r\n')   