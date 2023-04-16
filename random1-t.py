# 导入tkinter模块
import tkinter as tk
# 导入random模块
import random

# 创建一个窗口对象，命名为window
window = tk.Tk()
# 设置窗口的标题为"号码抽签"
window.title("号码抽签")
# 设置窗口的大小为300x200像素
window.geometry("300x200")

# 创建一个标签对象，命名为label1
label1 = tk.Label(window, text="请输入抽签的范围：")
# 使用grid方法设置标签在窗口中的位置和大小
label1.grid(row=0, column=0, sticky="w")

# 创建一个文本框对象，命名为entry1
entry1 = tk.Entry(window)
# 使用grid方法设置文本框在窗口中的位置和大小
entry1.grid(row=0, column=1)

# 创建一个标签对象，命名为label2
label2 = tk.Label(window, text="到")
# 使用grid方法设置标签在窗口中的位置和大小
label2.grid(row=0, column=2)

# 创建一个文本框对象，命名为entry2
entry2 = tk.Entry(window)
# 使用grid方法设置文本框在窗口中的位置和大小
entry2.grid(row=0, column=3)

# 创建一个按钮对象，命名为button
button = tk.Button(window, text="开始抽签")
# 使用grid方法设置按钮在窗口中的位置和大小
button.grid(row=1, column=0, columnspan=4)

# 创建一个标签对象，命名为label3
label3 = tk.Label(window, text="抽到的号码是：")
# 使用grid方法设置标签在窗口中的位置和大小
label3.grid(row=2, column=0, sticky="w")

# 创建一个StringVar对象，命名为number
number = tk.StringVar()
# 设置number的初始值为空字符串
number.set("")

# 创建一个标签对象，命名为label4
label4 = tk.Label(window, textvariable=number)
# 使用grid方法设置标签在窗口中的位置和大小
label4.grid(row=2, column=1)

# 定义一个函数，用来处理按钮的点击事件
def button_click():
  # 获取文本框中输入的范围
  start = int(entry1.get())
  end = int(entry2.get())
  # 随机从范围中抽取一个号码
  result = random.randint(start, end)
  # 设置number为结果
  number.set(str(result))

# 绑定按钮的点击事件到button_click函数
button["command"] = button_click

# 进入窗口的主循环
window.mainloop()