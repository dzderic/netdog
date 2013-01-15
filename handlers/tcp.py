import socket

from handlers.base import Listenable

class TcpHandler(Listenable):
    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.url.hostname, self.url.port))
        sock.listen(1)

        while True:
            conn, _ = sock.accept()
            fp = conn.makefile()
            while True:
                data = fp.readline()
                if data:
                    self._queue.append(data)
                else:
                    break
