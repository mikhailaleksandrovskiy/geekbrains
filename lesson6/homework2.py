class Road:
    def __init__(self, _length, _width):
        self._length = int(_length)
        self._width = int(_width)

    def mass(self):
        return self._length * self._width

class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

test = MassCount(15, 5000, 50)
print(test.mass())
