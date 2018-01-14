import sys
from random import randint, sample
from .fuzzer import Fuzzer

class AlphaNumericFuzzer(Fuzzer):
    """
    A fuzzer that produces unstructured alphanumeric output
    """
    def __init__(self, min_length, max_length):
        super().__init__()
        self._min_length = min_length
        self._max_length = max_length

        self._alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

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
            data.append(sample(self._alphabet, 1)[0])

        self._cases.append("".join(data))

        return "".join(data)

