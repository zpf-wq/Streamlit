import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

# 第一个文本框，输入数字
e = tk.Entry(window, show=None, width=10)
e.place(x=10,y=10)

# 显示运算符标签
var1 = tk.StringVar()
l = tk.Label(window, bg='white', width=4, textvariable=var1)
l.place(x=100,y=10)

# 第二个文本框，输入数字
d = tk.Entry(window, show=None, width=10)
d.place(x=150,y=10)

# 设置运算符选择列表
var2 = tk.StringVar()
lb = tk.Listbox(window, listvariable=var2, height=4)
list_items = ['+', '-', '*', '/']
for item in list_items:
    lb.insert('end', item)
lb.place(x=10,y=40)

# =字符
l = tk.Label(window, bg='white', width=4, text='=')
l.place(x=250,y=10)

# 设置选择键
def num_char():
    value=lb.get(lb.curselection())
    var1.set(value)
# 设置第二个按钮，选择运算符
b2=tk.Button(window,text='选择运算符',width=15,height=2,command=num_char)
b2.place(x=160,y=40)

# 主要运算程序
def num():
    num1 = eval(e.get())
    num2 = eval(d.get())
    num3 = num1+num2
    num4 = num1-num2
    num5 = num1*num2
    num6 = num1/num2
    ls = [num1, num2, num3, num4, num5, num6]
    value = lb.get(lb.curselection())
    if value == '+':
        a = ls[2]
        t.insert('insert', a)
        t.insert('insert', '\n')
    elif value == '-':
        a = ls[3]
        t.insert('insert', a)
        t.insert('insert', '\n')
    elif value == '*':
        a = ls[4]
        t.insert('insert', a)
        t.insert('insert', '\n')
    elif value == '/':
        a = ls[5]
        t.insert('insert', a)
        t.insert('insert', '\n')

# 设置第一个按钮，一键运算
b1 = tk.Button (window, text = '一键运算', width = 15, height = 2, command = num)
b1.place(x=160,y=80)

# 第三个文本框，输出结果
t=tk.Text(window,width=20,height=5)
t.place(x=300,y=10)

window.mainloop()