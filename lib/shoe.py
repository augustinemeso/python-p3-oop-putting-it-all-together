class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Internal storage for size
        self.size = size  # Set via the setter
        self.condition = "New"  # Default condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
