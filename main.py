import re
import tkinter
from tkinter import messagebox
from turtle import onclick

# 创建窗口
window = tkinter.Tk()
window.title("计算器")  # 设定标题
window.geometry("300x210")  # 设定窗口大小
window.resizable(False, False)  # 禁止重设窗口大小

# 创建窗口内容
contentVar = tkinter.StringVar(window, '')  # 自动刷新字符串变量
contentEntry = tkinter.Entry(window, textvariable=contentVar)  # 创建单行文本框
contentEntry['state'] = 'readonly'  # 设置文本框为只读
contentEntry.place(x=20, y=10, width=560, height=50)  # 设置文本框坐标及宽高

# 显示按钮内容
bvalue = ['C', '+', '-', 'CE', '1', '2', '3', '√', '3', '4', '5', '*', '6', '7', '8', '/', '9', '0', '.', '=']
index = 0
for row in range(5):  # 将按钮以5x4放置
    for col in range(4):
        d = bvalue[index]
        index += 1
        btnDigit = tkinter.Button(window, text=d, command=lambda x=d: onclick(x))
        btnDigit.place(x=20 + col * 70, y=50 + row * 30, width=50, height=20)


# 定义点击事件并根据不同的按钮作出不同的反应
def onclick(btn):
    operation = ('+', '-', '*', '/', '**', '//')  # 定义运算符
    content = contentVar.get()  # 获取文本框中的内容
    if content.startswith('.'):  # 如果已有内容是以小数点开头的，在前面加 0
        content = '0' + content
    if btn in '0123456789':  # 按下 0-9 在 content 中追加
        content += btn
    elif btn == '.':
        lastPart = re.split(r'[+\-*/]', content)[-1]  # 将 content 从 +-*/ 这些字符的地方分割开来
        if '.' not in lastPart:
            content += btn
        else:
            tkinter.messagebox.showerror('错误', '重复出现的小数点')  # 信息提示对话框
            return
    elif btn == 'C':  # 清除文本框
        content = ''
    elif btn == '=':  # 对输入的表达式求值
        try:
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('', '表达式有误')
            return
    elif btn in operation:
        if content.endswith(operation):
            tkinter.messagebox.showerror('', '不允许存在连续运算符')
            return
        content += btn
    elif btn == '√':
        n = content.split('.')  # 从 . 处分割存入 n，n 是一个列表
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    contentVar.set(content)  # 将结果显示到文本框中


window.mainloop()
