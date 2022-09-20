from point import Point
from tkinter import Canvas

class TriangleSerpinskyi:

    TAG = 'TS'
    DEEP = 6

    def __init__(self, A: Point, B: Point, C: Point, n: int):
        ab = A.lengthBetweenPoints(B)
        ac = A.lengthBetweenPoints(C)
        bc = B.lengthBetweenPoints(C)

        if ab - bc > ac or ac - bc > ab or ac - ab > bc:
            raise "Треугольник не существует"

        self.A = A
        self.B = B
        self.C = C
        TriangleSerpinskyi.DEEP = n

    def draw(self, canvas: Canvas):
        #canvas.create_polygon(self.A.x, self.A.y, self.B.x, self.B.y, self.C.x, self.C.y, fill='black', tags=(TriangleSerpinskyi.TAG))
        TriangleSerpinskyi.__draw(canvas, self.A, self.B, self.C, 0)

    def __draw(canvas: Canvas, X: Point, Y: Point, Z: Point, depth: int):
        if TriangleSerpinskyi.DEEP  == depth:
           return

        #Рисуем треугольники у углов

        canvas.create_polygon(X.x, X.y, Y.x, Y.y, Z.x, Z.y, fill='black', tags=(TriangleSerpinskyi.TAG))

        XY = Point.DSR(X, Y, 2, 1)
        XZ = Point.DSR(X, Z, 2, 1)

        YX = Point.DSR(Y, X, 2, 1)
        YZ = Point.DSR(Y, Z, 2, 1)

        ZY = Point.DSR(Z, Y, 2, 1)
        ZX = Point.DSR(Z, X, 2, 1)

        YZm = Point.DSR(Y, Z, 1, 1)
        center = Point.DSR(X, YZm, 1, 2)

        canvas.create_polygon(center.x, center.y, XY.x, XY.y, XZ.x, XZ.y, fill='white', tags=(TriangleSerpinskyi.TAG))
        canvas.create_polygon(center.x, center.y, YX.x, YX.y, YZ.x, YZ.y, fill='white', tags=(TriangleSerpinskyi.TAG))
        canvas.create_polygon(center.x, center.y, ZY.x, ZY.y, ZX.x, ZX.y, fill='white', tags=(TriangleSerpinskyi.TAG))

        TriangleSerpinskyi.__draw(canvas, X,      XY, XZ, depth + 1)
        TriangleSerpinskyi.__draw(canvas, Y,      YX, YZ, depth + 1)
        TriangleSerpinskyi.__draw(canvas, Z,      ZY, ZX, depth + 1)

        TriangleSerpinskyi.__draw(canvas, center, XY, YX, depth + 1)
        TriangleSerpinskyi.__draw(canvas, center, YZ, ZY, depth + 1)
        TriangleSerpinskyi.__draw(canvas, center, ZX, XZ, depth + 1)
        