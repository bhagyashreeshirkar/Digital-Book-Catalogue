from tkinter import *
import backend


# function to be called when mouse selects a row
# event is mandatory parameter which holds the information about event type(get_selected_row) inside the bind function
def get_selected_row(event):
    global selected_tuple  # global variables can be called anywhere throughout the code
    index = listbox.curselection()[0]  # [0] - selects 1st element of a tuple
    selected_tuple = listbox.get(index)  # gets index of selected row ie,[0] and assigns to variable selected_tuple

    # fills the entries after selecting a row
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])  # inserts new entry at the end of current entry

    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])  # inserts new entry at the end of current entry

    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])  # inserts new entry at the end of current entry

    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])  # inserts new entry at the end of current entry

    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[5])  # inserts new entry at the end of current entry


def view_command():
    # by clicking on 'View All' button consecutively it prints same list of books again and again(duplicate of list)
    # hence we need to use delete function so that after clicking consecutively it deletes previous list from listbox temporarily
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)  # inserts new row at the end of current row


def search_command():
    listbox.delete(0, END)
    for row in backend.search(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()):
        listbox.insert(END, row)


def add_command():
    backend.add_data(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get(), description_entry.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get(), description_entry.get()))
    # if we don't start with END then it adds a new entry at the start of all previous books


def delete_command():
    backend.delete(selected_tuple[0])  # as we want the id of selected row; we use [0]


def update_command():
    backend.update(selected_tuple[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get(), description_entry.get())
    # as we want to update selected row by keeping id same thus, we use selected_tuple[0]


# create a window
window = Tk()


# create a title
window.title('Digital Book Catalogue')


# change window size (Width x Height)
window.geometry('850x520')
window.resizable(False, False)  # by using this you cannot change size of the window(it freezes the window)


# set window icon
window.iconbitmap(r'book_icon.ico')


# add background image
bg = PhotoImage(file='C:\\Users\\Rsc\\Desktop\\bg.png')
my_label = Label(window, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


# add labels to the window
lb1 = Label(window, text='Title of a Book:', font='Times 15', bg='Lavender', fg='Navy')
lb1.grid(row=0, column=0, padx=5, pady=5, sticky=E)

lb2 = Label(window, text='Author:', font='Times 15', bg='Lavender', fg='Navy')
lb2.grid(row=0, column=3, padx=5, pady=5, sticky=E)

lb3 = Label(window, text='Year of Publication:', font='Times 15', bg='Lavender', fg='Navy')
lb3.grid(row=1, column=0, padx=5, sticky=E)

lb4 = Label(window, text='ISBN:', font='Times 15', bg='Lavender', fg='Navy')
lb4.grid(row=1, column=3, padx=5, pady=5, sticky=E)  # ISBN stands for International Standard Book Number

lb5 = Label(window, text='Description:', font='Times 15', bg='Lavender', fg='Navy')
lb5.grid(row=10, column=0, padx=5, pady=5)


# create entry boxes
title_entry = StringVar()
entry1 = Entry(window, text=title_entry, font='Times 12')
entry1.grid(row=0, column=1, ipadx=20, sticky=W)

author_entry = StringVar()
entry2 = Entry(window, text=author_entry, font='Times 12')
entry2.grid(row=0, column=4, ipadx=20, sticky=W)

year_entry = StringVar()
entry3 = Entry(window, text=year_entry, font='Times 12')
entry3.grid(row=1, column=1, ipadx=20, sticky=W)

isbn_entry = StringVar()
entry4 = Entry(window, text=isbn_entry, font='Times 12')
entry4.grid(row=1, column=4, ipadx=20, sticky=W)

description_entry = StringVar()
entry5 = Entry(window, text=description_entry, font='Times 13', width='30')
entry5.grid(row=10, column=1, columnspan=4, ipadx=120, ipady=20, pady=5, sticky=W)


# create a listbox
listbox = Listbox(window, height=16, width=70, font='Times 11', fg='Crimson')
listbox.grid(row=2, column=0, rowspan=6, columnspan=3, padx=15, pady=5)


# create scrollbars
scrollbar1 = Scrollbar(window, orient='vertical')
scrollbar1.grid(row=2, column=3, rowspan=6, ipadx=1, ipady=104)

listbox.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=listbox.yview)


scrollbar2 = Scrollbar(window, orient='horizontal')
scrollbar2.grid(row=9, column=0, pady=7, columnspan=3, ipadx=110, ipady=1)

listbox.configure(xscrollcommand=scrollbar2.set)
scrollbar2.configure(command=listbox.xview)


scrollbar3 = Scrollbar(window, orient='horizontal')
scrollbar3.grid(row=11, column=1, pady=3, columnspan=3, ipadx=100, ipady=1, sticky=E)

entry5.configure(xscrollcommand=scrollbar3.set)
scrollbar3.configure(command=entry5.xview)

# get id of selected row so that we can deleted that row by clicking on the Delete Selected button
# listbox.bind('<<event type>>', function with you bind to the event type)
listbox.bind('<<ListboxSelect>>', get_selected_row)


# create buttons
bt1 = Button(window, text='View Book List', font='Times 11', fg='DarkGreen', bg='PowderBlue', width=19, command=view_command)
bt1.grid(row=2, column=4, ipady=2)

bt2 = Button(window, text='Search Entry', font='Times 11', fg='DarkGreen', bg='PowderBlue', width=19, command=search_command)
bt2.grid(row=3, column=4, ipady=2)

bt3 = Button(window, text='Add Book Details', font='Times 11', fg='DarkGreen', bg='PowderBlue', width=19, command=add_command)
bt3.grid(row=4, column=4, ipady=2)

bt4 = Button(window, text='Update Details', font='Times 11', fg='DarkGreen', bg='PowderBlue', width=19, command=update_command)
bt4.grid(row=5, column=4, ipady=2)

bt5 = Button(window, text='Delete Selected Book', font='Times 11', fg='DarkGreen', bg='PowderBlue', width=19, command=delete_command)
bt5.grid(row=6, column=4, ipady=2)

bt6 = Button(window, text='Quit', font='Times 11', fg='DarkGreen', bg='PowderBlue', width=19, command=window.destroy)
bt6.grid(row=7, column=4, ipady=2)


# it is used to run the application
window.mainloop()

