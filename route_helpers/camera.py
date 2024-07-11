import socket
import re
import json
import logging
from app import config


def connect_camera():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    token = 0
    host_ip = "192.168.42.1"
    host_port = 7878
    logging.info(f"Host IP: {host_ip}:{host_port}")

    client_socket.connect((host_ip, host_port))

    command_json = json.dumps({"msg_id": 257, "token": 0})
    client_socket.sendall(bytes(command_json, 'utf-8'))
    try:
        while True:
            data = client_socket.recv(4 * 1024)
            decoded_data = data.decode('utf-8')

            if "rval" in decoded_data:
                matches = re.findall(r'"param":(\d+)', decoded_data)
                if matches:
                    token = int(matches[0])

            command_json = json.dumps({"msg_id": 259, "token": token, "param": "none_force"})
            client_socket.sendall(bytes(command_json, 'utf-8'))

    except socket.error as e:
        logging.error(f"Socket error: {e}")


if __name__ == "__main__":
    config.initialize()
    connect_camera()
