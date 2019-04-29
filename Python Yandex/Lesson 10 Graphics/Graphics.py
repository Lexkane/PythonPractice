from tkinter import *


def main():
    pass


class Main (Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self)
        self.label.pack()
        self.button = Button(self, text="Say 'hello'", command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        self.label.configure(text='Hello, world')

    def create_widgets_pack(self):
        button1 = Button(self, text='1')
        button1.pack(side='left', fill='y', expand=True)
        button2 = Button(self, text='2')
        button2.pack(side='top')
        button3 = Button(self, text='3')
        button3.pack(side='left')
        button4 = Button(self, text='4')
        button4.pack(side='right')

    def create_widgets_grid(self):
        button1 = Button(self, text='1')
        button1.grid(row=0, column=1)
        button2 = Button(self, text='2')
        button2.grid(row=1, column=0, columnspawn=2, sticky='nsew')
        button3 = Button(self, text='3')
        button3.grid(row=1, column=2, rowspan=2)
        button4 = Button(self, text='4')
        button4.grid(row=2, column=0)


root = Tk()
frame = Main(root)
frame.mainloop()
