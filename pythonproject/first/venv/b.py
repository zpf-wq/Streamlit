import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

couter=0
class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('200x200')
        initface(self.root)

class initface():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='green')
        # 基准界面initface
        self.initface = tk.Frame(self.master)
        self.initface.pack()
        btn = tk.Button(self.initface, text='change', command=self.change)
        btn.pack()

        def change(self, ):
            self.initface.destroy()
            face1(self.master)

class face1():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = tk.Frame(self.master, )
        self.face1.pack()
        btn_back = tk.Button(self.face1, text='face1 back', command=self.back)
        btn_back.pack()

        def back(self):
            self.face1.destroy()
            initface(self.master)

            if __name__ == '__main__':
                root = tk.Tk()
                basedesk(root)

            root.mainloop()


def do_job2():
    face2 = tk.Frame(window)
    e = tk.Entry(window, show=None, width=6)
    e.place(x=50, y=50)

l=tk.Label(window,text='',bg='green')
l.place(x=30,y=300)

menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=basedesk)
filemenu.add_command(label='Open',command=do_job2)
filemenu.add_command(label='Save',command=do_job2)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

edimenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edimenu)
edimenu.add_command(label='New',command=basedesk)
edimenu.add_command(label='Open',command=do_job2)
edimenu.add_command(label='Save',command=do_job2)

window.config(menu=menubar)
window.mainloop()