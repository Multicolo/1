from tkinter import *
from PIL import Image, ImageTk

# 初始化名单列表和被打钩名字列表
name_list = ['小明', '小红', '小张', '小李']
checked_name_list = []

# 初始化Tkinter窗口
root = Tk()
root.title("名单打钩")
root.geometry("600x400")

# 定义打钩事件处理函数
def handle_check(name):
    if name in checked_name_list:
        checked_name_list.remove(name)
        # 更新打钩图标
        var_dict[name].set(unchecked_icon)
    else:
        checked_name_list.append(name)
        # 更新打钩图标
        var_dict[name].set(checked_icon)

# 加载打钩和未打钩图标
checked_image = Image.open("checked.png")
checked_image = checked_image.resize((30, 30))
checked_icon = ImageTk.PhotoImage(checked_image)

unchecked_image = Image.open("unchecked.png")
unchecked_image = unchecked_image.resize((30, 30))
unchecked_icon = ImageTk.PhotoImage(unchecked_image)

var_dict = {} # 存储每个名字对应的图标变量

# 创建名字列表的Label和CheckBox控件
for i, name in enumerate(name_list):
    var_dict[name] = BooleanVar()
    cb = Checkbutton(root, text=name, variable=var_dict[name], command=lambda name=name: handle_check(name))
    cb.grid(row=i, column=0)

    # 设置默认状态
    var_dict[name].set(unchecked_icon)

# 创建确认按钮
btn = Button(root, text="确认")
btn.grid(row=len(name_list), column=0)

# 点击确认按钮后打印勾选的名字数量
def print_checked_names():
    print("共勾选了 {} 个名字：".format(len(checked_name_list)))
    for name in checked_name_list:
        print(name)

# 绑定确认按钮的点击事件
btn.config(command=print_checked_names)

root.mainloop()
