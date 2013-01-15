import threading


class Handler(threading.Thread):
    def __init__(self, action, url, queue):
        super(Handler, self).__init__()
        self.action = action
        self.url = url
        self._queue = queue

    def pop(self):
        return self._queue.popleft()

    def run(self):
        # Action is one of 'listen' or 'connect' (methods that need to be implemented)
        getattr(self, self.action)()

class Listenable(Handler):
    def listen(self, *args, **kwargs):
        raise NotImplementedError()

class Connectable(Handler):
    def connect(self, *args, **kwargs):
        raise NotImplementedError()
