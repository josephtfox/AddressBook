# Title: Address Book
# Author: Joseph Fox
# Email: josephtfox@gmail.com

from tkinter import *

win = Tk()
win.title('Address Book')
win.geometry('500x500')

data = []

def add():
    global data
    data.append([Name.get(), Number.get(), Address.get(), City.get(), State.get(),Zip.get(), Country.get()])
    update()
    return
def update():
    select_box.delete(0, END)
    select_box.insert(END, *data)
    return
def delete():
    del data[select_box.curselection()]
    update()
    return


Name = StringVar()
Number = StringVar()
Address = StringVar()
City = StringVar()
State = StringVar()
Zip = StringVar()
Country = StringVar()

Label(win, text='Name:', font='arial 14 bold').grid(row=1, column=0)
Entry(win, textvariable=Name, width=40).grid(row=1, column=1)

Label(win, text='Phone Number:', font='arial 14 bold').grid(row=2, column=0)
Entry(win, textvariable=Number, width=40).grid(row=2, column=1)

Label(win, text='Address:', font='arial 14 bold').grid(row=3, column=0)
Entry(win, textvariable=Address, width=40).grid(row=3, column=1)

Label(win, text='City:', font='arial 14 bold').grid(row=4, column=0)
Entry(win, textvariable=City, width=40).grid(row=4, column=1)

Label(win, text='State:', font='arial 14 bold').grid(row=5, column=0)
Entry(win, textvariable=State, width=40).grid(row=5, column=1)

Label(win, text='Zip Code:', font='arial 14 bold').grid(row=6, column=0)
Entry(win, textvariable=Zip, width=40).grid(row=6, column=1)

Label(win, text='Country:', font='arial 14 bold').grid(row=7, column=0)
Entry(win, textvariable=Country, width=40).grid(row=7, column=1)

select_box = Listbox(win, height=15, width=40)
select_box.place(x=110, y=210)

Button(win, text='ADD', font='arial 14 bold', padx=20, pady=20, command=add).grid(row=11, column=0)
Button(win, text='VIEW', font='arial 14 bold', padx=20, pady=20, command=add).grid(row=12, column=0)
Button(win, text='DELETE', font='arial 14 bold', padx=15, pady=15, command=delete).grid(row=13, column=0)
Button(win, text='RESET', font='arial 14 bold', padx=20, pady=20, command=add).grid(row=15, column=0)

win.mainloop()
