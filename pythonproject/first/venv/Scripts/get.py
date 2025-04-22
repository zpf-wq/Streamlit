import requests
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

# 第一个文本框，输入地址
e = tk.Entry(window, show=None, width=30)
e.place(x=10,y=10)

def query():
    address=e.cget('text')
    r = requests.get(address)
    t.insert('insert', r.status_code)
#print(r.status_code)#状态码
#print(type(r))#响应文件类型
#print(r.text)#请求头、url等信息
#print(r.cookies)#cookies信息

# 设置第一个按钮，一键运算
b1 = tk.Button (window, text = '一键运算', width = 15, height = 2, command = query)
b1.place(x=160,y=80)

# 第三个文本框，输出结果
t=tk.Text(window,width=20,height=5)
t.place(x=300,y=10)

window.mainloop()