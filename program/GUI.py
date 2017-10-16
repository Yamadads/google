#!/usr/bin/python

import tkinter as tk
from tkinter import filedialog
from program.App import App
from tkinter import messagebox

settings_string = "app:settings"


class GUI:
    def __init__(self):
        self.app = App()

        # root
        self.root = tk.Tk()
        self.root.title('°º¤ø,¸¸,ø¤º°  google  °º¤ø,¸¸,ø¤º°')
        self.root.minsize(750, 500)

        # top label
        self.label = tk.Label(self.root, text="Welcome in google!")
        self.label.pack(side="top", fill="both", ipady=5, expand=False)

        # buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(side="top", fill="both", ipady=5, expand=False)

        self.load_stopwards_button = tk.Button(self.buttons_frame, text='Load \nstopwords', command=self.load_stopwords)
        self.load_stopwards_button.pack(side="left", fill="both", expand=True)

        self.load_terms_button = tk.Button(self.buttons_frame, text='Load \nterms', command=self.load_terms)
        self.load_terms_button.pack(side="left", fill="both", expand=True)

        self.load_documents_button = tk.Button(self.buttons_frame, text='Load \ndocuments', command=self.load_documents)
        self.load_documents_button.pack(side="left", fill="both", expand=True)

        self.get_t_terms_button = tk.Button(self.buttons_frame, text='Show \ntrans. terms',
                                            command=self.show_t_terms)
        self.get_t_terms_button.pack(side="left", fill="both", expand=True)

        self.get_t_documents_button = tk.Button(self.buttons_frame, text='Show \ntrans. documents',
                                                command=self.show_t_documents)
        self.get_t_documents_button.pack(side="left", fill="both", expand=True)

        self.get_terms_button = tk.Button(self.buttons_frame, text='Show \nterms',
                                          command=self.show_terms)
        self.get_terms_button.pack(side="left", fill="both", expand=True)

        self.get_documents_button = tk.Button(self.buttons_frame, text='Show \ndocuments',
                                              command=self.show_documents)
        self.get_documents_button.pack(side="left", fill="both", expand=True)

        self.save_file = tk.Button(self.buttons_frame, text='Save list',
                                   command=self.save_file)
        self.save_file.pack(side="left", fill="both", expand=True)

        # enter bar
        self.enter_frame = tk.Frame(self.root)
        self.enter_frame.pack(side="top", fill="both", ipady=5, expand=False)

        self.edit = tk.Entry(self.enter_frame, width=80)
        self.edit.pack(side="left", fill="both", expand=True)
        self.edit.bind('<Return>', lambda _: self.query())

        self.enter_button = tk.Button(self.enter_frame, text='Relevance Feedback Query', command=self.relevance_feedback_query, width=20)
        self.enter_button.pack(ipady=1, side="right", fill="y", expand=False)

        # listbox
        self.listbox = tk.Listbox(self.root, width=100)
        self.listbox.pack(ipady=1, ipadx=1, side="left", fill="both", expand=True)
        self.listbox.bind('<Double-Button-1>', self.on_select_listbox)

        self.documents_status = {}
        self.root.mainloop()

    def load_stopwords(self):
        try:
            filename = filedialog.askopenfilename(initialdir="/home/debian/Pobrane/ezi/google/google/input",
                                                  title="Select documents file",
                                                  filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            if filename == "":
                return
            print(filename)
            self.app.load_stopwords(filename)
            self.fill_listbox(self.app.get_stopwords(), "List of stopwords")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def load_documents(self):
        try:
            filename = filedialog.askopenfilename(initialdir="/home/debian/Pobrane/ezi/google/google/input",
                                                  title="Select documents file",
                                                  filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            if filename == "":
                return
            print(filename)
            self.app.load_documents(filename)
            self.fill_listbox(self.app.get_documents_list(), "List of documents")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def show_documents(self):
        try:
            self.fill_listbox(self.app.get_documents_list(), "List of documents")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def show_terms(self):
        try:
            self.fill_listbox(self.app.get_terms_list(), "List of terms")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def load_terms(self):
        try:
            filename = filedialog.askopenfilename(initialdir="/home/debian/Pobrane/ezi/google/google/input",
                                                  title="Select terms file",
                                                  filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            if filename == "":
                return
            print(filename)
            self.app.load_terms(filename)
            self.fill_listbox(self.app.get_terms_list(), "List of terms")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def show_t_documents(self):
        try:
            documents = self.app.get_transformed_documents()
            self.fill_listbox(documents, "List of transfered documents")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def show_t_terms(self):
        try:
            terms = self.app.get_transformed_terms()
            self.fill_listbox(terms, "List of transfered terms")
            self.documents_status = {}
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def save_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text_to_save = ""
        for line in self.listbox.get(0, tk.END):
            text_to_save += line
            text_to_save += "\n"
        f.write(text_to_save)
        f.close()

    def fill_listbox(self, list, list_name):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, list_name)
        self.listbox.insert(tk.END, "")
        for i in list:
            self.listbox.insert(tk.END, i)

    def on_select_listbox(self, event):
        if self.documents_status == {}:
            return
        widget = event.widget
        list_index = int(widget.curselection()[0])
        document_index = list_index - 2
        if list_index <2:
            return
        (doc_title, value, status) = self.documents_status[document_index]
        if status == 'not_selected':
            widget.itemconfig(list_index, {'bg': '#b3fa87'})
            self.documents_status[document_index] = (doc_title, value, 'good')
        if status == 'good':
            widget.itemconfig(list_index, {'bg': '#feabab'})
            self.documents_status[document_index] = (doc_title, value, 'bad')
        elif status == 'bad':
            widget.itemconfig(list_index, {'bg': '#ffffff'})
            self.documents_status[document_index] = (doc_title, value, 'not_selected')

    def query(self):
        try:
            if self.edit.get() == "":
                return
            if settings_string in self.edit.get():
                settings_request_result = self.app.settings_request(self.edit.get())
                self.fill_listbox(settings_request_result, "Settings")
                self.documents_status = {}
            else:
                query_result, self.documents_status = self.app.query(self.edit.get())
                self.fill_listbox(query_result, "Search results")
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))

    def relevance_feedback_query(self):
        try:
            if self.edit.get() == "":
                return
            if settings_string in self.edit.get():
                return
            else:
                query_result, self.documents_status = self.app.relevance_feedback_query(self.edit.get(), self.documents_status)
                self.fill_listbox(query_result, "Search results")
        except Exception as e:
            messagebox.showinfo("Error", e)
            print(str(e))
