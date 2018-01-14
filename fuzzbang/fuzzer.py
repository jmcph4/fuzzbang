class Fuzzer(object):
    """
    Represents a general fuzzer
    """
    def __init__(self):
        self._num_cases = 0
        self._cases = []

    @property
    def num_cases(self):
        return self._num_cases

    @property
    def cases(self):
        return self._cases

    def get_case(self, pos):
        return self._cases[pos]

    def generate(self):
        pass

