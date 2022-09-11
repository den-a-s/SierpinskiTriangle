from cProfile import label
import tkinter as tk
from point import Point

# TODO запретить увеличивать окно
# TODO настроить размер окна в зависимости от виджетов
class TS2:
    def __init__(self, title: str) -> None:
        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        self.width = 700
        self.height = 700
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack(side='right')
        frameLabel = tk.Frame(self.root)
        frameLabel.pack(side='left')
        frameLeft = tk.Frame(frameLabel)
        frameLeft.pack(side='right')
        frameRight = tk.Frame(frameLeft)
        frameRight.pack(side='right')

        tk.Label(frameLabel, text='A', font='Arial 15').pack()
        tk.Label(frameLabel, text='B', font='Arial 15').pack()
        tk.Label(frameLabel, text='C', font='Arial 15').pack()

        self.Ax = tk.Entry(frameLeft)
        self.Ay = tk.Entry(frameRight)
        self.Ax.pack(anchor='w')
        self.Ay.pack(anchor='s')

        self.Bx = tk.Entry(frameLeft)
        self.By = tk.Entry(frameRight)
        self.Bx.pack()
        self.By.pack(anchor='w')

        self.Cx = tk.Entry(frameLeft)
        self.Cy = tk.Entry(frameRight)
        self.Cx.pack()
        self.Cy.pack(anchor='w')

        frameButton = tk.Frame(self.root)
        frameButton.pack(side='bottom')

        tk.Button(frameButton, text='Построить треугольник', command = self.__add_points).pack(anchor='sw')
        self.points = [Point(), Point(), Point()]
    
    def __add_points(self):
        
        self.points[0] = Point(float(self.Ax.get()), float(self.Ay.get()))
        self.points[1] = Point(float(self.Bx.get()), float(self.By.get()))
        self.points[2] = Point(float(self.Cx.get()), float(self.Cy.get()))
        print(self.points)

    def start(self) -> None:
        tk.mainloop()




        