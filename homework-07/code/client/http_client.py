import socket
import settings


class HttpClient:
    host = settings.MOCK_HOST
    port = int(settings.MOCK_PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)

    def connect(self):
        self.client.connect((self.host, self.port))

    def post(self, params):
        method = "POST"
        post_params = f"/post_surname/{params}"
        return self.send(method, post_params)

    def put(self, params):
        method = "PUT"
        put_params = f"/put_surname/{params}"
        return self.send(method, put_params)

    def delete(self, params):
        method = "DELETE"
        delete_params = f"/delete_surname/{params}"
        return self.send(method, delete_params)

    def get(self, params):
        method = "GET"
        get_params = f"/get_surname/{params}"
        return self.send(method, get_params)

    def send(self, method, params):
        request = f'{method} {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        self.client.send(request.encode())
        response = self.receive()
        return response

    def receive(self):
        data = self.client.recv(4096)
        total_data = []
        while True:
            if data:
                total_data.append(data.decode())
                break
            else:
                #self.client.close()
                break
        return ''.join(total_data).splitlines()

    def close(self):
        self.client.close()
