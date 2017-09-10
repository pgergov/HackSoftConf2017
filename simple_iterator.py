class MyIterator:
    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3]

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 1

        try:
            return self.data[index]
        except IndexError:
            raise StopIteration
