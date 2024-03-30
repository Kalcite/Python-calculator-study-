import tkinter as tk
from tkinter import messagebox
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplify_fraction():
    try:
        num = int(num_entry.get())
        den = int(den_entry.get())
        
        if den == 0:
            messagebox.showerror("错误", "分母不能为零")
            return
        
        gcd_value = gcd(num, den)
        simplified_num = num // gcd_value
        simplified_denom = den // gcd_value

        result_label.config(text=f"化简后的分数为：{simplified_num}/{simplified_denom}")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的整数")

root = tk.Tk()
root.title("分数化简器")

num_label = tk.Label(root, text="分子:")
num_label.grid(row=0, column=0)
num_entry = tk.Entry(root)
num_entry.grid(row=0, column=1)

den_label = tk.Label(root, text="分母:")
den_label.grid(row=1, column=0)
den_entry = tk.Entry(root)
den_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="化简", command=simplify_fraction)
calculate_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()


# def simplify_fraction(numerator, denominator):
#     # 找到最大公约数
#     gcd = math.gcd(numerator, denominator)
    
#     # 通过除以最大公约数来化简分数
#     simplified_numerator = numerator // gcd
#     simplified_denominator = denominator // gcd
    
#     return simplified_numerator, simplified_denominator

# import math

# # 测试函数
# numerator = 9
# denominator = 21
# simplified_num, simplified_denom = simplify_fraction(numerator, denominator)

# print(f"{numerator}/{denominator} 化简后为 {simplified_num}/{simplified_denom}")