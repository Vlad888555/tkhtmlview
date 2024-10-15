from tkinter import *
import os
from tkhtmlview import HTMLLabel
import chardet


def display_html(event):

    list_index = listbox.curselection()[0]
    selected_file = a[list_index]


    with open(selected_file, 'rb') as source_file:
        raw_data = source_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(selected_file, 'r', encoding=encoding, errors='replace') as source_file:
        html_result = source_file.read()

    my_html.set_html(html_result)



root = Tk()
root.geometry("1280x900")
root.title("--Трато времени")


os.chdir("Documents")
a = os.listdir()


frame = Frame(root, bg="lightblue")
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)

lbl = Label(frame, text="Файлы", font=("Arial", 16), bg="lightblue").pack(pady=10)
listbox = Listbox(frame, width=40, height=400, font=("Arial", 14))
listbox.pack(padx=10, pady=10)


frame2 = Frame(root, bg="white")
frame2.place(relx=0.301, rely=0, relwidth=0.7, relheight=1)


my_html = HTMLLabel(frame2, html="", width=400, height=900)
my_html.pack(padx=10, pady=10)


for i in range(len(a)):
    with open(a[i], 'rb') as source_file:
        raw_data = source_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(a[i], 'r', encoding=encoding, errors='replace') as source_file:
        html_result = source_file.read()
        h1_start = html_result.find("<h1>")
        h1_end = html_result.find("</h1>")
        p = html_result[h1_start + 4:h1_end]
        listbox.insert(END, p)


listbox.bind("<<ListboxSelect>>", display_html)


root.mainloop()
