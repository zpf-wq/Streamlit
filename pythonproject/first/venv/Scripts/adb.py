import uiautomator2 as u2
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

d = u2.connect('8KE5T19611001178')

#显示连接状态
def show():
    t.insert('insert',d)

b1 = tk.Button (window, text = '返回连接状态', width = 15, height = 2, command = show)
b1.place(x=160,y=80)

t=tk.Text(window,width=100,height=4)
t.place(x=0,y=5)

#前进按键定义
def run():
    d.long_click(0.388, 0.165)
b2=tk.Button(window,text='前进',width=15,height=2,command=run)
b2.place(x=160,y=120)

#向左按键定义
def left():
    d.long_click(0.164, 0.491)
b2=tk.Button(window,text='左转',width=15,height=2,command=left)
b2.place(x=20,y=170)

#向右按键定义
def right():
    d.long_click(0.62, 0.508)
b2=tk.Button(window,text='右转',width=15,height=2,command=right)
b2.place(x=300,y=170)

#后退按键定义
def back():
    d.long_click(0.402, 0.843)
b2=tk.Button(window,text='后退',width=15,height=2,command=back)
b2.place(x=160,y=220)

#循迹按键定义
def track():
    d.click(0.75, 0.317)
b2=tk.Button(window,text='循迹',width=15,height=2,command=track)
b2.place(x=20,y=220)

#避障按键定义
def aviod():
    d.click(0.83, 0.334)
b2=tk.Button(window,text='避障',width=15,height=2,command=aviod)
b2.place(x=300,y=220)

#设置路径选择框
var2 = tk.StringVar()
lb = tk.Listbox(window, listvariable=var2, height=4)
list_items = ['run', 'left', 'right', 'back']
for item in list_items:
    lb.insert('end', item)
lb.place(x=10,y=300)

# 显示第一个行动方式标签
var1 = tk.StringVar()
l1 = tk.Label(window, bg='white', width=4, textvariable=var1)
l1.place(x=10,y=400)

# 设置第一个选择键
def num_char():
    value=lb.get(lb.curselection())
    var1.set(value)
# 设置第一个按钮，选择行动方式
b2=tk.Button(window,text='选择行动方式',width=10,height=2,command=num_char)
b2.place(x=10,y=430)

# 第一个文本框，输入第一个行动时间
e1 = tk.Entry(window, show=None, width=4)
e1.place(x=50,y=400)

# 显示第二个行动方式标签
var2 = tk.StringVar()
l2 = tk.Label(window, bg='white', width=4, textvariable=var2)
l2.place(x=120,y=400)

# 设置第二个选择键
def num_char():
    value=lb.get(lb.curselection())
    var2.set(value)
# 设置第二个按钮，选择行动方式
b2=tk.Button(window,text='选择行动方式',width=10,height=2,command=num_char)
b2.place(x=120,y=430)

# 第二个文本框，输入第二个行动时间
e2 = tk.Entry(window, show=None, width=4)
e2.place(x=160,y=400)

# 显示第三个行动方式标签
var3 = tk.StringVar()
l3 = tk.Label(window, bg='white', width=4, textvariable=var3)
l3.place(x=230,y=400)

# 设置第三个选择键
def num_char():
    value=lb.get(lb.curselection())
    var3.set(value)
# 设置第三个按钮，选择运算符
b2=tk.Button(window,text='选择行动方式',width=10,height=2,command=num_char)
b2.place(x=230,y=430)

# 第三个文本框，输入第三个行动时间
e3 = tk.Entry(window, show=None, width=4)
e3.place(x=270,y=400)

# 显示第四个行动方式标签
var4 = tk.StringVar()
l4 = tk.Label(window, bg='white', width=4, textvariable=var4)
l4.place(x=340,y=400)

# 设置第四个选择键
def num_char():
    value=lb.get(lb.curselection())
    var4.set(value)
# 设置第四个按钮，选择运算符
b2=tk.Button(window,text='选择行动方式',width=10,height=2,command=num_char)
b2.place(x=340,y=430)

# 第四个文本框，输入第四个行动时间
e4 = tk.Entry(window, show=None, width=4)
e4.place(x=380,y=400)

#设置进程函数
def process():
    time1 = eval(e1.get())
    time2 = eval(e2.get())
    time3 = eval(e3.get())
    time4 = eval(e4.get())

    text1 = l1.cget("text")
    if text1 == 'run':
        d.long_click(0.388, 0.165,time1)
    elif text1 == 'left':
        d.long_click(0.164, 0.491,time1)
    elif text1 == 'right':
        d.long_click(0.620, 0.508,time1)
    elif text1 == 'back':
        d.long_click(0.402, 0.843,time1)

    text2 = l2.cget("text")
    if text2 == 'run':
        d.long_click(0.388, 0.165, time2)
    elif text2 == 'left':
        d.long_click(0.164, 0.491, time2)
    elif text2 == 'right':
        d.long_click(0.620, 0.508, time2)
    elif text2 == 'back':
        d.long_click(0.402, 0.843, time2)

    text3 = l3.cget("text")
    if text3 == 'run':
        d.long_click(0.388, 0.165, time3)
    elif text3 == 'left':
        d.long_click(0.164, 0.491, time3)
    elif text3 == 'right':
        d.long_click(0.620, 0.508, time3)
    elif text3 == 'back':
        d.long_click(0.402, 0.843, time3)

    text4 = l4.cget("text")
    if text4 == 'run':
        d.long_click(0.388, 0.165, time4)
    elif text4 == 'left':
        d.long_click(0.164, 0.491, time4)
    elif text4 == 'right':
        d.long_click(0.620, 0.508, time4)
    elif text4 == 'back':
        d.long_click(0.402, 0.843, time4)

# 设置第五个按钮，运行进程
b2=tk.Button(window,text='START',width=15,height=3,command=process)
b2.place(x=340,y=300)
window.mainloop()

