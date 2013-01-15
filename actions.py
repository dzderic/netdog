import time
import urlparse
from collections import deque

from handlers import tcp

HANDLERS = {
    'tcp': tcp.TcpHandler,
}

def initialize_handlers(action, urls):
    parsed = [urlparse.urlparse(i) for i in urls]
    return [HANDLERS[i.scheme](action, i, deque()) for i in parsed]

def listen(args):
    sources = initialize_handlers('listen', args.sources)
    for source in sources:
        source.start()

    while True:
        for source in sources:
            try:
                print source.pop(),
            except IndexError:
                time.sleep(0.01)
    
    for source in sources:
        source.stop()

def connect(args):
    pass
