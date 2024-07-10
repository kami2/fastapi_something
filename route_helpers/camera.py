import socket
import json
import re
import time

yi_ip = "192.168.42.1"
yi_port = 7878
yi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
yi_token = 0


def main():
    global yi_socket, yi_token

    try:
        print(f"Establishing connection to {yi_ip}")
        yi_socket.connect((yi_ip, yi_port))
        print("Connection established!")

        send_command({"msg_id": 257, "token": 0})

        while True:
            if not get_token():
                get_token()

            send_command({"msg_id": 259, "token": yi_token, "param": "none_force"})
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        yi_socket.close()


def send_command(command):
    global yi_socket

    command_json = json.dumps(command)
    yi_socket.sendall(bytes(command_json, 'utf-8'))


def get_token():
    global yi_socket, yi_token

    try:
        yi_data = yi_socket.recv(512)
        d = yi_data.decode('utf-8')

        if "rval" in d:
            matches = re.findall(r'"param":(\d+)', d)
            if matches:
                yi_token = int(matches[0])
                return True

        return False

    except socket.error as e:
        print(f"Socket error: {e}")
        return False


if __name__ == "__main__":
    main()
