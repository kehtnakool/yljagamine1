from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from Model import Model

class View:

    def __init__(self):
        self.model = Model()
        canvas = Tk()
        canvas.title("Õpilastele ülesannete jagamine")
        Button(canvas, text="Ava õpilaste fail", command=self.display_students).grid(column=0, row=0, sticky="W")
        Button(canvas, text="Ava ülesannete fail", command=self.display_tasks).grid(column=1, row=0, sticky="W")
        Button(canvas, text="Jaga ülesanded", command=self.display_shuffle).grid(column=2, row=0, sticky="W")
        Button(canvas, text="Salvesta ülesanded csv faili", command=self.save_csv).grid(column=3, row=0, sticky="E")
        self.students_text = StringVar()
        self.students_text.set("ÕPILASED:")
        self.tasks_text = StringVar()
        self.tasks_text.set("ÜLESANDED:")
        self.shuffle_text = StringVar()
        self.shuffle_text.set("")
        ttk.Label(canvas, textvariable=self.students_text).grid(column=0, row=1, sticky="NW")
        ttk.Label(canvas, textvariable=self.tasks_text).grid(column=1, row=1, sticky="NW")
        ttk.Label(canvas, textvariable=self.shuffle_text).grid(column=2, row=1, columnspan=2, sticky="NW")
        canvas.mainloop()

    def display_students(self):
        self.model.sdudentsfile = fd.askopenfilename()
        self.students_text.set(self.model.return_students())

    def display_tasks(self):
        self.model.tasksfile = fd.askopenfilename()
        self.tasks_text.set(self.model.return_tasks())

    def display_shuffle(self):
        self.shuffle_text.set(self.model.allocate_tasks())

    def save_csv(self):
        self.model.csvfile = fd.asksaveasfilename()
        self.shuffle_text.set(self.model.save_csv())
