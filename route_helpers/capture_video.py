import cv2


def capture_video():
    stream = cv2.VideoCapture("rtsp://192.168.42.1/live")
    while stream.isOpened():
        ret, frame = stream.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    stream.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_video()