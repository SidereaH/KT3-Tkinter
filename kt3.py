import module
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
root = Tk()
root.title("КТ3 - Хуторной Андрей")
root.geometry("450x200")
answer = []
answfilt = []
res2ex = []
convToCortg = []
books = StringVar(value=answer)


def updateList():
    path = entryPath.get()
    if(path == ""):
        showerror("Ошибка!", "Введите путь к файлу")
    else:
        answerget = module.get_books(path)
        #очистка списка answer
        answer.clear()

        for book in answerget: #добавляем каждый элемент из answerget в список answer
            answer.append(book)
        res2ex.append(module.unitofautAndBooks(answerget))

        books.set(answer)
def filterByString():
    filter = entryFilter.get()
    if(filter == ""):
        showerror("Ошибка!", "Не введен фильтр")
    else:
        resForS = answer
        resultsearch = module.filtername(resForS, filter)

        answfilt.clear()
        for book in resultsearch:
            answfilt.append(resultsearch)
        books.set(answfilt)

def countByNum():
    resForS = answer
    convertToCortege = module.convertToCortage(resForS)
    for cortege in convertToCortege:
        convToCortg.append(cortege)

    books.set(convToCortg)

main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)

sec = Frame(main_frame)
sec.pack(fill=X,side=BOTTOM)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)
x_scrollbar.pack(side=BOTTOM,fill=X)
y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas["xscrollcommand"] = x_scrollbar.set
my_canvas["yscrollcommand"] = y_scrollbar.set
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL)))

frameText = Frame(my_canvas)
listbox = Listbox(frameText, listvariable=books, width = 50)
frameText.pack(side = LEFT, padx=10, pady=10)
frameTextScroll = Frame(frameText)
frameTextScroll.pack(fill=X,side=BOTTOM)
scrollbar = ttk.Scrollbar(frameText ,orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

boottomScroll = ttk.Scrollbar(frameTextScroll, orient="horizontal", command=listbox.xview)

boottomScroll.pack(side=BOTTOM, fill = X)

frameUser = Frame(my_canvas)
frameUser.pack(side = LEFT, padx=10, pady=10)

labelInfo = ttk.Label(frameText, text="Выберите файл")
labelInfo.pack()
listbox.pack()
entryPath = ttk.Entry(frameUser)
entryPath.pack(fill=X)
task1Button = ttk.Button(frameUser, text="Вывести файл", command= updateList)
task1Button.pack(fill=X)
entryFilter = ttk.Entry(frameUser, text = "Фильтр")
entryFilter.pack(fill=X)
task2Button = ttk.Button(frameUser, text= "Фильтровать", command=filterByString)
task2Button.pack(fill=X)
labelCortage = ttk.Label(frameUser, text="Задание 3")
labelCortage.pack()
task3Button = ttk.Button(frameUser, text= "Вывод Кортежей", command=countByNum)
task3Button.pack(fill=X)
listbox["yscrollcommand"] = scrollbar.set
listbox["xscrollcommand"] = boottomScroll.set
root.mainloop()


