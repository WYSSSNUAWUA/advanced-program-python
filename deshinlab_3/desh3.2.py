class MultiplesOfThree:
    def __init__(self, start, limit):
        self.limit = limit
        self.current = start if start % 3 == 0 else start + (3 - start % 3)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        result = self.current
        self.current += 3
        return result


# Example
for n in MultiplesOfThree(1, 20):
    print(n)
