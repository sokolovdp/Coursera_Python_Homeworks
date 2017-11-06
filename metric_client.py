import socket
import time
from collections import defaultdict

SOCKET_BUFFER_SIZE = 100
SERVER_OK = 'ok\n\n'
SERVER_ERROR = 'error\nwrong command\n\n'


class ClientError(BaseException):
    pass


class Client:
    def __init__(self, ip_addr_str: str, port_numb: int, timeout=None):
        self.ip = ip_addr_str
        self.port = port_numb
        self.timeout = timeout
        self.server_socket = socket.create_connection((ip_addr_str, port_numb), timeout)

    def get(self, metric):
        client_message = f"get {metric}\n"
        try:
            self.server_socket.sendall(client_message.encode("utf-8"))
        except socket.timeout:
            print("client send data timeout")
        except socket.error as ex:
            print("client send data error:", ex)
        try:
            server_message = self.server_socket.recv(SOCKET_BUFFER_SIZE).decode('utf-8')
        except socket.timeout:
            print("client recv data timeout")
        except socket.error as ex:
            print("client recv data error:", ex)
        else:
            metrics_values = server_message.split('\n')
            if metrics_values[0] != 'ok':
                raise ClientError
            if len(metrics_values) == 3:
                return {}
            metrics_values = metrics_values[1:-2]
            answer = defaultdict(list)
            for metric in metrics_values:
                name, value, timestamp = metric.split(' ')
                answer[name].append((int(timestamp), float(value)))
            return answer

    def put(self, metric: str, value: float, timestamp=None):
        timestamp = timestamp or int(time.time())
        client_message = f"put {metric} {round(value,2)} {timestamp}\n"
        try:
            self.server_socket.sendall(client_message.encode("utf-8"))
        except socket.timeout:
            print("client send data timeout")
        except socket.error as ex:
            print("client send data error:", ex)
        try:
            server_message = self.server_socket.recv(SOCKET_BUFFER_SIZE).decode('utf-8')
        except socket.timeout:
            print("client recv data timeout")
        except socket.error as ex:
            print("client recv data error:", ex)
        else:
            if server_message != SERVER_OK:
                raise ClientError

    def close(self):
        self.server_socket.close()
