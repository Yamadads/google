#!/usr/bin/python

from tkinter import *
from tkinter import filedialog
from .App import App


def load_documents():
    filename = filedialog.askopenfilename(initialdir="/", title="Select documents file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    app.load_documents(filename)


def load_terms():
    filename = filedialog.askopenfilename(initialdir="/", title="Select terms file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    app.load_terms(filename)


def save_documents_file():
    documents = app.get_transformed_documents()
    save_file(documents)


def save_terms_file():
    terms = app.get_transformed_documents()
    save_file(terms)


def save_file(text_to_save):
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text2save = text_to_save
    f.write(text2save)
    f.close()

app = App
root = Tk()
root.minsize = [300, 300]

label = Label(root, text="Welcome in google!")
label.pack()

load_documents_button = Button(root, text='Load docuements', command=load_documents)
load_documents_button.pack()

load_terms_button = Button(root, text='Load terms', command=load_documents)
load_terms_button.pack()


root.mainloop()
root.destroy()
