from queue import Queue

class Work(Queue):

    def _init(self, maxsize):
        Queue._init(self, maxsize)
        self._done = set()

    def _put(self, item):
        if item not in self._done:
            Queue._put(self, item)
            self._done.add(item)
