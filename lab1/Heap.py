
class Heap:
    def __init__(self, cmp):
        self._val = []
        self._cmp = max_cmp if cmp is None else cmp

    def is_empty(self):
        return len(self._val) == 0

    def heapify(self, id):
        while id > 0:
            if self._cmp(self._val[(id-1)//2], self._val[id]):
                return
            self._val[(id-1)//2], self._val[id] = self._val[id], self._val[(id-1)//2]
            id = (id-1)//2

    def heapify_all(self):
        l = len(self._val)
        if l <= 1:
            return
        id = 0
        while id*2+1 < l and self._cmp(self._val[id*2+1], self._val[id]):
            self._val[id * 2 + 1], self._val[id] = self._val[id], self._val[id*2+1]
            id = id*2+1

    def push(self, el):
        self._val += [el]
        self.heapify(len(self._val)-1)

    def top(self):
        if self.is_empty():
            return None
        res = self._val[0]
        self._val[0] = self._val[-1]
        self._val.pop(-1)
        self.heapify_all()
        return res


def max_cmp(a, b):
    return a > b



