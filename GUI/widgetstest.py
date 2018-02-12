import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()

# 修改标题
win.wm_title("Hello World")

# 窗体设置为不可改变大小
win.resizable(width=False, height=False)

# 创建标签组件并设置布局位置(此处使用网格布局)
ttk.Label(win, text='Enter your name').grid(column=0, row=0)
ttk.Label(win, text='Chose a number').grid(column=1, row=0)


# 定义回调函数
def clickMe():
    action.configure(text="Hello " + nameEntry.get() + numberChosen.get())
    # 关闭按钮组件
    action.configure(state='disabled')


# 定义一个字符串变量，tkinter需要指定变量类型才能够使用
name = tk.StringVar()
# 创建文本框组件(组件关联的窗体，长度，文本变量)并设置网格布局位置
nameEntry = ttk.Entry(win, width=12, textvariable=name)
nameEntry.grid(column=0, row=1)
# 定义游标位置
nameEntry.focus()
# 创建按钮(按钮所关联的窗体，按钮文字，回调函数)
action = ttk.Button(win, text='Click Me', command=clickMe)
action.grid(column=2, row=1)

number = tk.StringVar()
# 创建下拉列表组件(该组件关联的窗体，长度，文本变量，状态为只读若不指定则可编辑)
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen.grid(column=1, row=1)
# 创建列表的内容
numberChosen['value'] = (1, 2, 3, 4, 5)
# 设定起始位置索引
numberChosen.current(0)

# 创建整型变量，勾选状态其值为1，非勾选状态其值为0
chVarDis = tk.IntVar()
# 创建checkbutton组件(关联窗体，提示文本，状态变量，组件状态)
check1 = ttk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
# 设置组件状态变量为关闭状态，勾选
check1.state(['disabled', 'selected'])
# sticky=tk.W表示该组件在网格中左对齐
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = ttk.Checkbutton(win, text='Unabled', variable=chVarUn)
# 设置组件状态变量为启动，非勾选
check2.state(['!disabled', '!selected'])
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = ttk.Checkbutton(win, text='Enabled', variable=chVarEn)
# 设置组件状态变量为启动，勾选
check3.state(['!disabled', 'selected'])
check3.grid(column=2, row=2, sticky=tk.W)

# 创建颜色列表
colors = ["Blue", "Red", "Gold"]


def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


# 创建整数变量
radVar = tk.IntVar()
# 此变量应在列表索引之外的值，否则的话在创建GUI时，被索引到的组件将被选中而并没有调用回调函数
radVar.set(99)

for col in range(len(colors)):
    # 创建radiobutton(关联窗体，提示文本，关联变量，本地变量，回调函数)
    curRad = ttk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=3, sticky=tk.W)

# 定义滚动文本框的宽度和高度
scroW = 30
scroH = 3
# 创建滚动文本框(关联窗体，宽度，高度，以单词为单位进行换行)
scr = scrolledtext.ScrolledText(win, width=scroW, height=scroH, wrap=tk.WORD)
# 指定该组件所在网格位置以及跨行个数
scr.grid(column=0, row=4, columnspan=3, sticky='WE')

# 创建标签框架(关联主窗口，标题)
labelsFrame = ttk.Labelframe(win, text='Labels in a Frame')
labelsFrame.grid(column=0, row=5, padx=20, pady=40)
# 在标签框架中创建标签并指定在标签框架中的网格位置
ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label2').grid(column=1, row=0)
ttk.Label(labelsFrame, text='Label3').grid(column=2, row=0)
# 为标签框架中的所有组件设置间距
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# 循环监听窗体事件
win.mainloop()

# 最终显示结果比较丑，因为网格布局中的一列宽度是动态的(该列所有组件的最大宽度)，同理一行也是这样