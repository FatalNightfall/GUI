# -*- coding: utf8 -*-
import tkinter
import tkinter.messagebox

def DeleteEntryValue(event):

    entry_box.delete(0, tkinter.END)

def check(event):
    global val1
    global val2
    global val3

    text = ""

    if val1.get() is True:
        text += "項目1はチェックされています\n"
    else:
        text += "項目1はチェックされていません\n"

    if val2.get() is True:
        text += "項目2はチェックされています\n"
    else:
        text += "項目2はチェックされていません\n"

    if val3.get() is True:
        text += "項目3はチェックされています\n"
    else:
        text += "項目3はチェックされていません\n"

    tkinter.messagebox.showinfo('info', text)

make_window = tkinter.Tk()
make_window.title("HW Monitor")
make_window.geometry("640x480")

cpu_label = tkinter.Label(text='CPU', background='#ffaacc')
cpu_label.pack()
cpu_label.place(x=15, y=15)

DRAM_label = tkinter.Label(text='DRAM', background='#ffaacc')
DRAM_label.pack()
DRAM_label.place(x=15, y=45)

entry_box = tkinter.Entry(width=48)
entry_box.pack()
entry_box.place(x=15, y=450)

monitoring = tkinter.Button(text='Start Monitoring')
monitoring.bind("<Button-1>", DeleteEntryValue)
monitoring.pack()
monitoring.place(x=520, y=450)

val1 = tkinter.BooleanVar()
val2 = tkinter.BooleanVar()
val3 = tkinter.BooleanVar()

val1.set(False)
val2.set(True)
val3.set(False)

check_box1 = tkinter.Checkbutton(text="項目1", variable=val1)
check_box1.pack()
check_box1.place(x=15, y=420)

check_box2 = tkinter.Checkbutton(text="項目2", variable=val2)
check_box2.pack()
check_box2.place(x=15, y=400)

check_box3 = tkinter.Checkbutton(text="項目3", variable=val3)
check_box3.pack()
check_box3.place(x=15, y=380)

check_button = tkinter.Button(make_window, text='チェックの取得', width=16)
check_button.bind("<Button-1>", check)
check_button.pack()
check_button.place(x=360, y=450)

make_window.mainloop()