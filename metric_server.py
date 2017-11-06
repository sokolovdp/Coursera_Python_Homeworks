import asyncio
from collections import defaultdict

# import chardet

SERVER_OK = 'ok\n'
SERVER_ERROR = 'error\nwrong command\n\n'


class ClientServerProtocol(asyncio.Protocol):
    data_base = defaultdict(list)

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            server_response = self._process_data(data.decode())
        except UnicodeDecodeError:
            # encoding = chardet.detect(data)['encoding']
            # print(encoding, data.decode(encoding))
            pass
        else:
            self.transport.write(server_response.encode())

    def _get(self, parameter_name: str) -> str:
        answer = SERVER_OK
        if parameter_name == '*':
            for parameter_name in self.data_base:
                for values in self.data_base[parameter_name]:
                    answer += f'{parameter_name} {values[1]} {values[0]}\n'
            answer += '\n'
        elif parameter_name not in self.data_base:
            answer += '\n'
        else:
            for values in self.data_base[parameter_name]:
                answer += f'{parameter_name} {values[1]} {values[0]}\n'
            answer += '\n'
        return answer

    def _put(self, parameter_string: str) -> str:
        try:
            key, value_str, timestamp_str = parameter_string.split(' ')
            value = float(value_str)
            timestamp = int(timestamp_str)
        except ValueError:
            return SERVER_ERROR
        else:
            self.data_base[key].append((timestamp, value))
            return SERVER_OK + '\n'

    def _process_data(self, client_command: str) -> str:
        try:
            command, payload = client_command.lower().strip().split(" ", 1)
        except ValueError:
            return SERVER_ERROR
        else:
            if command == 'get':
                answer = self._get(payload)
            elif command == 'put':
                answer = self._put(payload)
            else:
                answer = SERVER_ERROR
            return answer


def run_server(host: str, port: int):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)
