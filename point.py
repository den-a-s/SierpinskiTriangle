from math import sqrt

class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def lengthBetweenPoints(self, p):
        return sqrt( ( self.x - p.x ) ** 2 + ( self.y - p.y ) ** 2 )

    def DSR(p1, p2, numerator: int, denominator: int):
        """
        Создание точки по формуле деления отрезка в данном отношении.
        """
        return Point( ( numerator * p1.x + denominator * p2.x ) / ( numerator + denominator ), \
            ( numerator * p1.y + denominator * p2.y ) / ( numerator + denominator ) )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'({self.x};{self.y})'
