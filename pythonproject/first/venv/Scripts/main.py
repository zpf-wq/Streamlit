import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

# 设置单位选择列表
var2 = tk.StringVar()
lb = tk.Listbox(window, listvariable=var2, height=4)
list_items = ['kΩ', 'Ω']
for item in list_items:
    lb.insert('end', item)
lb.place(x=10, y=40)

#设置第一个文本框
e = tk.Entry(window, show=None, width=6)
e.place(x=10, y=10)

#设置第一个单位显示标签
var1 = tk.StringVar()
l1 = tk.Label(window, bg='white', width=4, textvariable=var1)
l1.place(x=60,y=10)

def num_char():
    value=lb.get(lb.curselection())
    var1.set(value)
# 设置第二个按钮，选择单位符
b1=tk.Button(window,text='选择单位',width=15,height=2,command=num_char)
b1.place(x=160,y=40)

#第一个//标签
q1 = tk.Label(window, bg='white', width=4, text='//')
q1.place(x=300,y=200)

#设置第二个文本框
d = tk.Entry(window, show=None, width=6)
d.place(x=100,y=10)

#设置第二个单位显示标签
var2 = tk.StringVar()
l2 = tk.Label(window, bg='white', width=4, textvariable=var2)
l2.place(x=150,y=10)

def num_char():
    value=lb.get(lb.curselection())
    var2.set(value)

# 设置第三个按钮，选择单位符
b2=tk.Button(window,text='选择单位',width=15,height=2,command=num_char)
b2.place(x=300,y=300)

#第二个//标签
q2 = tk.Label(window, bg='white', width=4, text='//')
q2.place(x=300,y=250)

#设置第三个文本框
f = tk.Entry(window, show=None, width=6)
f.place(x=190,y=10)

#设置第三个单位显示标签
var3 = tk.StringVar()
l3 = tk.Label(window, bg='white', width=4, textvariable=var3)
l3.place(x=240,y=10)

def num_char():
    value=lb.get(lb.curselection())
    var3.set(value)

# 设置第四个按钮，选择单位符
b3=tk.Button(window,text='选择单位',width=15,height=2,command=num_char)
b3.place(x=400,y=400)

#=标签
q3 = tk.Label(window, bg='white', width=4, text='=')
q3.place(x=320,y=10)

def num():
    num1 = eval(e.get())
    num11 = num1 * 1000
    ls1 = [num1, num11]
    text1 = l1.cget("text")
    if text1 == "kΩ":
        a = ls1[1]
    else:
        a = ls1[0]
    num2 = eval(d.get())
    num22 = num2 * 1000
    ls1 = [num2, num22]
    text2 = l2.cget("text")
    if text2 == "kΩ":
        b = ls1[1]
    else:
        b = ls1[0]
    num3 = eval(f.get())
    num33 = num3 * 1000
    ls1 = [num3, num33]
    text3 = l3.cget("text")
    if text3 == "kΩ":
        c = ls1[1]
    else:
        c = ls1[0]

    sum = 1 / a + 1 / b + 1 / c
    t.insert('insert', 1 / sum)
    t.insert('insert', 'Ω')
    t.insert('insert', '\n')


# 设置第一个按钮，一键运算
b1 = tk.Button (window, text = '一键运算', width = 15, height = 2, command = num)
b1.place(x=160,y=80)

t=tk.Text(window,width=10,height=7)
t.place(x=390,y=10)
window.mainloop()