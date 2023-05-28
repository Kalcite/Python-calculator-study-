# import math

# def combination(n, r):
#     """
#     计算组合数 C(n, r)
#     """
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# def permutation(n, r):
#     """
#     计算排列数 A(n, r)
#     """
#     return math.factorial(n) // math.factorial(n - r)

# # 测试代码
# print(combination(5, 2)) # 输出 10
# print(permutation(5, 2)) # 输出 20
import math
import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("组合数和排列数计算器")

        # 创建输入框和标签
        self.n_label = tk.Label(master, text="n=")
        self.n_label.grid(row=0, column=0)
        self.n_entry = tk.Entry(master)
        self.n_entry.grid(row=0, column=1)
        self.r_label = tk.Label(master, text="r=")
        self.r_label.grid(row=1, column=0)
        self.r_entry = tk.Entry(master)
        self.r_entry.grid(row=1, column=1)

        # 创建计算结果标签
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=1)

        # 创建按钮
        self.combination_button = tk.Button(
            master, text="计算组合数", command=self.calculate_combination)
        self.combination_button.grid(row=3, column=0)
        self.permutation_button = tk.Button(
            master, text="计算排列数", command=self.calculate_permutation)
        self.permutation_button.grid(row=3, column=1)

    def calculate_combination(self):
        try:
            n = int(self.n_entry.get())
            r = int(self.r_entry.get())
            result = math.comb(n, r)
            self.result_label.config(text=f"C({n}, {r}) = {result}")
        except ValueError:
            self.result_label.config(text="请输入一个整数")

    def calculate_permutation(self):
        try:
            n = int(self.n_entry.get())
            r = int(self.r_entry.get())
            result = math.perm(n, r)
            self.result_label.config(text=f"A({n}, {r}) = {result}")
        except ValueError:
            self.result_label.config(text="请输入一个整数")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

