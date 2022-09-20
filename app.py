import tkinter as tk
from PIL import ImageGrab
from tkinter import messagebox
from point import Point
from triangle_serpinskyi import TriangleSerpinskyi


class App:
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
        tk.Label(frameLabel, text='n', font='Arial 15').pack()

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

        self.n = tk.Entry(frameLeft)
        self.n.pack()

        self.size = 0

        frameButton = tk.Frame(self.root)
        frameButton.pack(side='bottom')

        tk.Button(frameButton, text='Построить треугольник', command = self.__add_points).pack(anchor='sw')
        tk.Button(frameButton, text='Сохранить как картинку' , command = self.__save_image).pack(anchor='sw')
        self.points = [Point(), Point(), Point()]
        self.root.bind('<Left>',  self.left)
        self.root.bind('<Right>', self.right)
        self.root.bind('<Up>',    self.up)
        self.root.bind('<Down>',  self.down)
        self.root.bind('-',  self.zoom_in)
        self.root.bind('+', self.zoom_out)

    def __add_points(self):
        try:
            self.points[0] = Point(float(self.Ax.get()), float(self.Ay.get()))
            self.points[1] = Point(float(self.Bx.get()), float(self.By.get()))
            self.points[2] = Point(float(self.Cx.get()), float(self.Cy.get()))
            self.size      = int(self.n.get())
            ts = TriangleSerpinskyi(*self.points, n = self.size)
            ts.draw(self.canvas)
        except:
            messagebox.askquestion(title="Ошибка", message="Не правильно введены точки")

    def __save_image(self):
        x= self.root.winfo_rootx()+self.canvas.winfo_x()
        y= self.root.winfo_rooty()+self.canvas.winfo_y()
        x1=x+self.canvas.winfo_width()
        y1=y+self.canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save("triangle.jpg")

    def left(self, event):
        self.canvas.move(TriangleSerpinskyi.TAG, -10, 0)

    def right(self, event):
        self.canvas.move(TriangleSerpinskyi.TAG, 10, 0)

    def up(self, event):
        self.canvas.move(TriangleSerpinskyi.TAG, 0, -10)

    def down(self, event):
        self.canvas.move(TriangleSerpinskyi.TAG, 0, 10)

    def zoom_in(self, event):
        self.canvas.scale(TriangleSerpinskyi.TAG, self.width / 2, self.height / 2, 2, 2)

    def zoom_out(self, event):
        self.canvas.scale(TriangleSerpinskyi.TAG, self.width / 2, self.height / 2, 0.5, 0.5)

    def start(self) -> None:
        tk.mainloop()
        