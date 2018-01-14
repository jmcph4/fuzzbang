import sys
from random import randint
from .fuzzer import Fuzzer

class BinaryFuzzer(Fuzzer):
    """
    Fuzzer that produces unstructured binary output
    """
    def __init__(self, min_length, max_length=None):
        super().__init__()
        self._min_length = min_length
        self._max_length = max_length

    @property
    def min_length(self):
        return self._min_length

    @property
    def max_length(self):
        return self._max_length

    def generate(self):
        data = []

        start = self.min_length
        end = 0

        if self.max_length is not None:
            end = randint(start, self.max_length)
        else:
            end = randint(start, sys.maxsize)

        for i in range(start, end):
            data.append(randint(0, 255))

        self._cases.append(bytes(data))

        return bytes(data)

