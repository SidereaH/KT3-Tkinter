from tkinter.messagebox import showerror, showwarning, showinfo
def get_books(bookpath):
    try:
        books = open(bookpath, encoding='utf-8')
    except FileNotFoundError():
        showerror("Error!", "FileNotFoundError")


    lines = books.read()

    books.close()

    booklist = lines.split('\n')

    reslist = []

    for line in booklist:
        line = line.split('|')

        reslist.append(line)

    return reslist


def unitofautAndBooks(books):
    newreslist = []

    for bookline in books:
        bookname = bookline[1]

        bookauthor = bookline[2]

        bookline[1] = (bookname + " , " + bookauthor)

        bookline.pop(2)

        newreslist.append(bookline)

    return newreslist


def filtername(resourselist, stringToSearch):
    resserch = []

    for lines in resourselist:

        stringToSearch.lower()

        lines[1].lower()

        searching = lines[1].find(stringToSearch)

        if searching != -1:
            resserch.append(lines)

    return resserch


def convertToCortage(list):
    resConvert = []

    list.pop(0)

    for podlist in list:
        quantity = podlist[2]

        price = podlist[3]

        total = float(quantity) * float(price)

        cortage = (podlist[0], total)

        resConvert.append(cortage)

    return resConvert