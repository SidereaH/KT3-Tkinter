from tkinter import *
from tkinter import ttk

import kt3

text = StringVar()
root = Tk()

root.title("В1")
root.geometry("450x200")
frameBot = Frame(root)
frameText = Frame(frameBot)
frameAct = Frame(frameBot)

labelName = ttk.Label(root, text="КТ3 Хуторной Андрей Анреевич")

labelText = ttk.Label(frameText, textvariable=text)
entryPath = ttk.Entry(frameAct)
button1 = ttk.Button(text="Открыть файл")
entryFilter = ttk.Entry(frameAct)
button2 = ttk.Button(frameAct, text= "Отфильтровать")

