from re import T
from tkinter import *

root = Tk()
root.title("Ko GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

root.mainloop()