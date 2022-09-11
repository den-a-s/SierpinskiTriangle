class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'({self.x};{self.y})'
