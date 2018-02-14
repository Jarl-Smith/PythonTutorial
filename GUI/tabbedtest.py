import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox

#========定义组件提示类=========
class ToolTip():
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT, background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#======创建鼠标停留组件事件需要绑定的回调函数
def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


win = tk.Tk()
win.wm_title('Tabbed Layout')
# 设定图标
win.iconbitmap(r'F:/GTA San Andreas/game.ico')
# 创建菜单栏
menuBar = tk.Menu(win)
# 主窗口关联菜单栏
win.config(menu=menuBar)

#=========定义菜单about选项的回调函数(弹出信息、警告或错误窗口)
def _msgBox():
    type = ''
    if type == 'info':
        mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2018.')
    elif type == 'warning':
        mBox.showwarning('Python Message Warning Box',
                         'A Python GUI created using tkinter:\nWaring: There might be a bug in this code.')
    elif type == 'error':
        mBox.showerror('Python Message Error Box',
                       'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
    else:
        answer = mBox.askyesno('Python Message Dual Choice Box', 'Are you sure you really wish to do this ?')
        print(answer)

#=========定义退出按钮的回调函数
def _quit():
    win.quit()
    win.destroy()
    exit()

#======创建菜单
fileMenu = tk.Menu(menuBar, tearoff=0)
#======添加菜单选项
fileMenu.add_command(label='File')
fileMenu.add_separator()
#=====添加菜单选项并关联回调函数
fileMenu.add_command(label='Exit', command=_quit)
helpMenu = tk.Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=_msgBox)
#=====以添加层叠的方式添加菜单
menuBar.add_cascade(label='File', menu=fileMenu)
menuBar.add_cascade(label='Help', menu=helpMenu)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab2')
tabControl.pack(expand=1, fill='both')

monty = ttk.Labelframe(tab1, text='Monty Python')
monty.grid(column=0, row=0, padx=8, pady=4)
monty2 = ttk.Labelframe(tab2, text='The Snake')
monty2.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(monty, text='Enter a name:').grid(column=0, row=0)
ttk.Label(monty, text='Choose a number:').grid(column=1, row=0)

name = tk.StringVar()
nameEnter = ttk.Entry(monty, textvariable=name)
nameEnter.grid(column=0, row=1)
nameEnter.focus()

number = tk.StringVar()
numberChosen = ttk.Combobox(monty, textvariable=number, state='readonly')
numberChosen.grid(column=1, row=1)
numberChosen['value'] = [1, 2, 3, 4, 5]
numberChosen.current(0)

#=====定义按钮回调函数
def callBack():
    action.configure(text='Hello ' + name.get() + ' ' + number.get())
    action.configure(state='disabled')

#====创建按钮组件并关联回调函数
action = ttk.Button(monty, text='Click Me', command=callBack)
action.grid(column=2, row=1)


def _spin():
    value = spin.get()
    # scr.insert(tk.INSERT, value + '\n')
    print(value)


spin = tk.Spinbox(monty, from_=1, to=10, width=5, bd=5, command=_spin)
spin.grid(column=0, row=2)
# 指定一组特定值以供选择,改变外观
spin2 = tk.Spinbox(monty, values=(1, 2, 4, 42, 100), width=5, bd=5, relief=tk.GROOVE, command=_spin)
spin2.grid(column=1, row=2)
#===给组建添加提示
createToolTip(spin2, 'This is a spin widget.')

scrW = 30
scrH = 3
scr = scrolledtext.ScrolledText(monty, width=scrW, height=scrH, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3, sticky='WE')

cheVars = [tk.BooleanVar() for i in range(3)]
cheText = ['Disabled', 'Unchecked', 'Checked']
cheState = [['disabled', 'selected'], ['!disabled', '!selected'], ['!disabled', 'selected']]
for col in range(3):
    temp = ttk.Checkbutton(monty2, variable=cheVars[col], text=cheText[col])
    temp.grid(column=col, row=4, sticky='W')
    temp.state(cheState[col])

radVar = tk.IntVar()
radVar.set(99)
colors = ['Blue', 'Gold', 'Red']


def radCall():
    radnum = radVar.get()
    monty2.configure(text=colors[radnum])


for col in range(3):
    temp = ttk.Radiobutton(monty2, variable=radVar, text=colors[col], value=col, command=radCall)
    temp.grid(column=col, row=5, sticky='W')

win.mainloop()
