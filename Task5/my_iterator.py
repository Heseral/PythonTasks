class MyIterator:
    def __iter__(self):
        return self

    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = -1

    def __next__(self):
        if self.counter < len(self.iterable):
            self.counter += 1
            return self.iterable[self.counter]
        else:
            raise StopIteration
