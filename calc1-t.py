# 导入tkinter模块
import tkinter as tk
# 导入math模块
import math

# 创建一个窗口对象，命名为window
window = tk.Tk()
# 设置窗口的标题为"简单计算器"
window.title("简单计算器")

# 创建一个StringVar对象，命名为expression
expression = tk.StringVar()
# 设置expression的初始值为空字符串
expression.set("")

# 创建一个文本框对象，命名为entry
entry = tk.Entry(window, textvariable=expression)
# 使用grid方法设置文本框在窗口中的位置和大小
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# 定义一个函数，用来处理按钮的点击事件
def button_click(event):
  # 获取按钮上的文本
  text = event.widget["text"]
  # 如果文本是"="，则计算文本框中的算式，并显示结果
  if text == "=":
    try:
      # 使用eval函数在一个安全的环境中计算表达式的值
      result = eval(expression.get(), {"__builtins__":None}, vars(math))
      # 设置expression为结果
      expression.set(str(result))
    except:
      # 设置expression为"错误"
      expression.set("错误")
  # 如果文本是"退出"，则退出程序
  elif text == "退出":
    window.destroy()
  # 如果文本是"清空"，则清空文本框
  elif text == "清空":
    expression.set("")
  # 否则，将文本追加到文本框中
  else:
    expression.set(expression.get() + text)

# 创建一个列表，存储所有按钮上的文本
buttons = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "^", "/", "(", ")", "=", "清空", "退出"]

# 使用一个循环来创建所有按钮，并设置它们在窗口中的位置和大小
for i in range(len(buttons)):
  # 创建一个按钮对象，命名为button
  button = tk.Button(window, text=buttons[i])
  # 使用grid方法设置按钮在窗口中的位置和大小
  button.grid(row=i//4 + 1, column=i%4, sticky="nsew")
  # 绑定按钮的点击事件到button_click函数
  button.bind("<Button-1>", button_click)

# 让窗口自动调整大小
window.resizable(True, True)
# 进入窗口的主循环
window.mainloop()
# # 导入tkinter模块
# import tkinter as tk

# # 定义一个函数，用来计算字符串中的指数
# def power(s):
#   # 如果字符串中没有"^"符号，直接返回字符串
#   if "^" not in s:
#     return s
#   # 否则，找到"^"符号的位置
#   i = s.index("^")
#   # 计算"^"符号左边的数值
#   left = float(power(s[:i]))
#   # 计算"^"符号右边的数值
#   right = float(power(s[i+1:]))
#   # 返回左边的数值的右边的数值次方
#   return str(left ** right)

# # 定义一个函数，用来计算字符串中的括号
# def bracket(s):
#   # 如果字符串中没有"("或")"符号，直接返回字符串
#   if "(" not in s and ")" not in s:
#     return s
#   # 否则，找到最内层的括号的位置
#   i = s.rindex("(")
#   j = s.index(")", i)
#   # 计算括号内的表达式的值
#   inner = calculate(s[i+1:j])
#   # 返回括号外的字符串和括号内的值拼接起来的新字符串
#   return bracket(s[:i] + inner + s[j+1:])

# # 定义一个函数，用来计算字符串中的乘除
# def multiply_divide(s):
#   # 如果字符串中没有"*"或"/"符号，直接返回字符串
#   if "*" not in s and "/" not in s:
#     return s
#   # 否则，找到第一个"*"或"/"符号的位置
#   i = min(s.index("*") if "*" in s else len(s), s.index("/") if "/" in s else len(s))
#   # 计算"*"或"/"符号左边的数值
#   left = float(multiply_divide(s[:i]))
#   # 计算"*"或"/"符号右边的数值
#   right = float(multiply_divide(s[i+1:]))
#   # 如果是"*"符号，返回左边和右边的数值相乘
#   if s[i] == "*":
#     return str(left * right)
#   # 如果是"/"符号，返回左边和右边的数值相除
#   else:
#     return str(left / right)

# # 定义一个函数，用来计算字符串中的加减
# def add_subtract(s):
#   # 如果字符串中没有"+"或"-"符号，直接返回字符串
#   if "+" not in s and "-" not in s:
#     return s
#   # 否则，找到第一个"+"或"-"符号的位置（忽略开头的负号）
#   i = min(s.index("+") if "+" in s else len(s), s.index("-",1) if "-" in s[1:] else len(s))
#   # 计算"+"或"-"符号左边的数值
#   left = float(add_subtract(s[:i]))
#   # 计算"+"或"-"符号右边的数值
#   right = float(add_subtract(s[i+1:]))
#   # 如果是"+"符号，返回左边和右边的数值相加
#   if s[i] == "+":
#     return str(left + right)
#   # 如果是"-"符号，返回左边和右边的数值相减
#   else:
#     return str(left - right)
  
# def calculate(s):
#   # 去掉字符串中的空格
#   s = s.replace(" ", "")
#   # 计算字符串中的指数
#   s = power(s)
#   # 计算字符串中的括号
#   s = bracket(s)
#   # 计算字符串中的乘除
#   s = multiply_divide(s)
#   # 计算字符串中的加减
#   s = add_subtract(s)
#   # 返回最终的结果
#   return s

# # 创建一个窗口对象，命名为window
# window = tk.Tk()
# # 设置窗口的标题为"简单计算器"
# window.title("简单计算器")
# # 设置窗口的大小为300x200像素
# window.geometry("300x200")

# # 创建一个文本框对象，命名为entry
# entry = tk.Entry(window)
# # 设置文本框的位置和大小
# entry.place(x=10, y=10, width=280, height=30)

# # 定义一个函数，用来处理按钮的点击事件
# def button_click(event):
#   # 获取按钮上的文本
#   text = event.widget["text"]
#   # 如果文本是"="，则计算文本框中的算式，并显示结果
#   if text == "=":
#     try:
#       result = calculate(entry.get())
#       entry.delete(0, tk.END)
#       entry.insert(0, result)
#     except:
#       entry.delete(0, tk.END)
#       entry.insert(0, "错误")
#   # 如果文本是"退出"，则退出程序
#可以使用eval函数来直接计算一个字符串中的算式，而不需要自己定义各种函数。但是要注意，eval函数可能有安全风险，如果用户输入了一些恶意的代码，可能会造成损害。所以你可以使用一个安全的环境来运行eval函数，比如使用math模块中的变量和函数。
#可以使用tkinter中的grid方法来布局窗口中的组件，而不需要手动设置每个组件的位置和大小。这样可以让你的界面更加美观和灵活。
#可以使用tkinter中的StringVar类来绑定文本框和一个变量，这样可以方便地获取和设置文本框中的内容，而不需要使用entry.get()和entry.insert()等方法。