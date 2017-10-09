#!/usr/bin/python

import tkinter as tk
from tkinter import filedialog
from program.App import App


class GUI:
    def __init__(self):
        self.app = App

        # root
        self.root = tk.Tk()
        self.root.title('°º¤ø,¸¸,ø¤º°  google  °º¤ø,¸¸,ø¤º°')
        self.root.minsize(700, 500)

        # top label
        self.label = tk.Label(self.root, text="Welcome in google!")
        self.label.pack(side="top", fill="both", ipady=5, expand=False)

        # buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(side="top", fill="both", ipady=5, expand=False)

        self.load_documents_button = tk.Button(self.buttons_frame, text='Load documents', command=self.load_documents)
        self.load_documents_button.pack(side="left", fill="both", expand=True)

        self.load_terms_button = tk.Button(self.buttons_frame, text='Load terms', command=self.load_documents)
        self.load_terms_button.pack(side="left", fill="both", expand=True)

        self.save_terms_button = tk.Button(self.buttons_frame, text='Save transformed terms',
                                           command=self.save_terms_file)
        self.save_terms_button.pack(side="left", fill="both", expand=True)

        self.save_documents_button = tk.Button(self.buttons_frame, text='Save transformed documents',
                                               command=self.save_documents_file)
        self.save_documents_button.pack(side="left", fill="both", expand=True)

        # enter bar
        self.enter_frame = tk.Frame(self.root)
        self.enter_frame.pack(side="top", fill="both", ipady=5, expand=False)

        self.edit = tk.Entry(self.enter_frame, width=80)
        self.edit.pack(side="left", fill="both", expand=True)

        self.enter_button = tk.Button(self.enter_frame, text='Query', command=self.save_documents_file)
        self.enter_button.pack(ipady=1, side="left", fill="both", expand=True)

        # listbox
        self.listbox = tk.Listbox(self.root, width=100)
        self.listbox.pack(ipady=1, ipadx=1, side="left", fill="both", expand=True)

        self.root.mainloop()

    def load_documents(self):
        try:
            filename = filedialog.askopenfilename(initialdir="/", title="Select documents file",
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            self.app.load_documents(filename)
            
        except:
            pass

    def load_terms(self):
        try:
            filename = filedialog.askopenfilename(initialdir="/", title="Select terms file",
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            self.app.load_terms(filename)
        except:
            pass

    def save_documents_file(self):
        documents = self.app.get_transformed_documents()
        self.save_file(documents)

    def save_terms_file(self):
        terms = self.app.get_transformed_documents()
        self.save_file(terms)

    def save_file(self, text_to_save):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text2save = text_to_save
        f.write(text2save)
        f.close()
