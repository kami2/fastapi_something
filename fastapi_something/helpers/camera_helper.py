import socket
import re
import cv2
import threading
import json
import logging
import asyncio
from fastapi_something.config import Config


class CameraHelper:

    def __init__(self, test=False):
        self.host_ip = Config.CAMERA_HOST_IP
        self.host_port = Config.CAMERA_HOST_PORT
        self.rtsp = Config.CAMERA_RTSP_ADDRESS
        self.token = 0
        self.test = test

    def connect_camera(self):

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info(f"Connecting to: {self.host_ip}:{self.host_port}")

            client_socket.connect((self.host_ip, self.host_port))
            logging.info("Connection established")

            command_json = json.dumps({"msg_id": 257, "token": self.token})
            client_socket.sendall(bytes(command_json, 'utf-8'))

            while True:
                data = client_socket.recv(4 * 1024)
                decoded_data = data.decode('utf-8')

                if "rval" in decoded_data:
                    matches = re.findall(r'"param":(\d+)', decoded_data)
                    if matches:
                        self.token = int(matches[0])

                command_json = json.dumps({"msg_id": 259, "token": self.token, "param": "none_force"})
                client_socket.sendall(bytes(command_json, 'utf-8'))

        except socket.error as e:
            logging.error(f"Socket error: {e}")

    @staticmethod
    def render_video_in_window():
        stream = cv2.VideoCapture(Config.CAMERA_RTSP_ADDRESS)
        while stream.isOpened():
            ret, frame = stream.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        stream.release()
        cv2.destroyAllWindows()

    @staticmethod
    async def generate_frames():
        stream = cv2.VideoCapture(Config.CAMERA_RTSP_ADDRESS)
        while True:
            ret, frame = stream.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            await asyncio.sleep(0.01)
        stream.release()

    def run(self):
        logging.info("Starting camera connection thread")
        connection = threading.Thread(target=self.connect_camera)
        connection.start()
        logging.info("Camera connection thread started")

        if self.test:
            logging.info("Starting capture video thread")
            capture_video = threading.Thread(target=self.render_video_in_window)
            capture_video.start()
            logging.info("Capture video thread started")


if __name__ == "__main__":
    Config.initialize()
    cam = CameraHelper(test=True)
    cam.run()
