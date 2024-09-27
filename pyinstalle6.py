import os
import shutil
import subprocess
from tkinter import Tk, Toplevel, filedialog, messagebox, ttk, Text, Scrollbar
import tkinter

def run_pyinstaller(script_path, icon_path, one_file, output_dir, console_mode=True):
    command = ['pyinstaller']

    if one_file:
        command.append('-F')
    else:
        command.append('-D')

    if icon_path and os.path.exists(icon_path):
        command.extend(['-i', icon_path])

    if console_mode:
        command.append('-c')

    if output_dir and os.path.isdir(output_dir):
        command.extend(['--distpath', output_dir])

    with subprocess.Popen(command + [script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as process:
        debug_window = Toplevel(root)
        debug_window.title("Debug 输出")
        debug_text = Text(debug_window, wrap='word', width=80, height=20)
        scrollbar = Scrollbar(debug_window, orient="vertical", command=debug_text.yview)
        debug_text.configure(yscrollcommand=scrollbar.set)

        debug_text.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')

        while True:
            line = process.stdout.readline().strip()
            if not line:
                break
            debug_text.insert('end', line + '\n')
            debug_text.see('end')

        process.wait()

        if process.returncode == 0:
            build_dir = os.path.join(os.getcwd(), 'build')
            spec_file = f"{os.path.splitext(os.path.basename(script_path))[0]}.spec"

            if messagebox.askyesno("询问", "是否将build文件夹和.spec文件一并放入输出目录？"):
                if os.path.exists(build_dir):
                    shutil.move(build_dir, output_dir)
                if os.path.exists(spec_file):
                    shutil.move(spec_file, output_dir)

            messagebox.showinfo("消息", "打包成功")
        else:
            messagebox.showerror("错误", "打包过程中发生错误")

def select_script():
    script_path = filedialog.askopenfilename(title="选择Python脚本文件", filetypes=[('Python files', '*.py')])
    script_entry.delete(0, 'end')
    script_entry.insert(0, script_path)

def select_icon():
    icon_path = filedialog.askopenfilename(title="选择图标文件", filetypes=[('ICO files', '*.ico')])
    icon_entry.delete(0, 'end')
    icon_entry.insert(0, icon_path)

def select_output_dir():
    directory = filedialog.askdirectory(title="选择输出目录")
    output_entry.delete(0, 'end')
    output_entry.insert(0, directory)

def copy_and_run_pyinstaller(script_path, icon_path, one_file, output_dir):
    script_basename = os.path.basename(script_path)
    output_script_path = os.path.join(output_dir, script_basename)

    # 拷贝Python脚本到输出目录
    shutil.copyfile(script_path, output_script_path)

    run_pyinstaller(output_script_path, icon_path, one_file, output_dir)

def on_compile_click(script_path, icon_path, one_file_var, output_dir):
    if not script_path.endswith('.py'):
        messagebox.showerror("错误", "请选择一个有效的Python脚本文件")
        return

    # 检查并创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    copy_and_run_pyinstaller(script_path, icon_path, one_file_var.get(), output_dir)

# 主程序入口
if __name__ == "__main__":
    root = Tk()
    root.title("PyInstaller GUI Packager")

    script_label = ttk.Label(root, text="Python脚本路径:")
    script_label.grid(row=0, column=0, padx=5, pady=5)
    
    script_entry = ttk.Entry(root, width=60)
    script_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    ttk.Button(root, text="选择脚本", command=select_script).grid(row=0, column=3, padx=5, pady=5)

    icon_label = ttk.Label(root, text="图标路径:")
    icon_label.grid(row=1, column=0, padx=5, pady=5)
    
    icon_entry = ttk.Entry(root, width=60)
    icon_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
    ttk.Button(root, text="选择图标", command=select_icon).grid(row=1, column=3, padx=5, pady=5)

    one_file_option = tkinter.BooleanVar()
    one_file_checkbutton = ttk.Checkbutton(root, text="打包为单个文件", variable=one_file_option)
    one_file_checkbutton.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

    output_label = ttk.Label(root, text="输出目录:")
    output_label.grid(row=3, column=0, padx=5, pady=5)
    
    output_entry = ttk.Entry(root, width=60)
    output_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
    ttk.Button(root, text="选择目录", command=select_output_dir).grid(row=3, column=3, padx=5, pady=5)

    compile_button = ttk.Button(root, text="开始打包", command=lambda: on_compile_click(script_entry.get(), icon_entry.get(), one_file_option, output_entry.get()))
    compile_button.grid(row=4, column=0, columnspan=4, pady=10)

    root.mainloop()