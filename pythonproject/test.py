import tkinter as tk

window = tk.Tk()
window.title("   ")
window.geometry('200x200')

l = tk.Label(window, text='', bg='yellow')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

exitmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=exitmenu)
exitmenu.add_command(label='New', command=do_job)
exitmenu.add_command(label='Open', command=do_job)
exitmenu.add_command(label='Save', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='import', menu=submenu)
submenu.add_command(label='subme', command=do_job)

window.config(menu=menubar)

window.mainloop()

