import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox
import GUI.tooltip as tt


class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.wm_title('Tabbed Layout')
        # 设定图标
        self.win.iconbitmap(r'F:/GTA San Andreas/game.ico')

    # =====定义按钮回调函数
    def _callBack(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' + self.number.get())
        self.action.configure(state='disabled')

    def _spin(self):
        value = self.spin.get()
        # scr.insert(tk.INSERT, value + '\n')
        print(value)

    def _radCall(self):
        self.radnum = self.radVar.get()
        self.monty2.configure(text=self.colors[self.radnum])

    # =========定义退出按钮的回调函数
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    # =========定义菜单about选项的回调函数(弹出信息、警告或错误窗口)
    def _msgBox(self):
        self.type = ''
        if self.type == 'info':
            mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2018.')
        elif self.type == 'warning':
            mBox.showwarning('Python Message Warning Box',
                             'A Python GUI created using tkinter:\nWaring: There might be a bug in this code.')
        elif self.type == 'error':
            mBox.showerror('Python Message Error Box',
                           'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
        else:
            mBox.askyesno('Python Message Dual Choice Box', 'Are you sure you really wish to do this ?')

    def createWidgets(self):
        # 创建菜单栏
        self.menuBar = tk.Menu(self.win)
        # 主窗口关联菜单栏
        self.win.config(menu=self.menuBar)
        # ======创建菜单
        fileMenu = tk.Menu(self.menuBar, tearoff=0)
        # ======添加菜单选项
        fileMenu.add_command(label='File')
        fileMenu.add_separator()
        # =====添加菜单选项并关联回调函数
        fileMenu.add_command(label='Exit', command=self._quit)
        helpMenu = tk.Menu(self.menuBar, tearoff=0)
        helpMenu.add_command(label='About', command=self._msgBox)
        # =====以添加层叠的方式添加菜单
        self.menuBar.add_cascade(label='File', menu=fileMenu)
        self.menuBar.add_cascade(label='Help', menu=helpMenu)

        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab1')
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab2')
        tabControl.pack(expand=1, fill='both')

        self.monty = ttk.Labelframe(tab1, text='self.monty Python')
        self.monty.grid(column=0, row=0, padx=8, pady=4)
        self.monty2 = ttk.Labelframe(tab2, text='The Snake')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)

        ttk.Label(self.monty, text='Enter a name:').grid(column=0, row=0)
        ttk.Label(self.monty, text='Choose a number:').grid(column=1, row=0)

        self.name = tk.StringVar()
        self.nameEnter = ttk.Entry(self.monty, textvariable=self.name)
        self.nameEnter.grid(column=0, row=1)
        self.nameEnter.focus()

        self.number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.monty, textvariable=self.number, state='readonly')
        self.numberChosen.grid(column=1, row=1)
        self.numberChosen['value'] = [1, 2, 3, 4, 5]
        self.numberChosen.current(0)

        # ====创建按钮组件并关联回调函数
        self.action = ttk.Button(self.monty, text='Click Me', command=self._callBack)
        self.action.grid(column=2, row=1)

        self.spin = tk.Spinbox(self.monty, from_=1, to=10, width=5, bd=5, command=self._spin)
        self.spin.grid(column=0, row=2)
        # 指定一组特定值以供选择,改变外观
        self.spin2 = tk.Spinbox(self.monty, values=(1, 2, 4, 42, 100), width=5, bd=5, relief=tk.GROOVE,
                                command=self._spin)
        self.spin2.grid(column=1, row=2)
        # ===给组建添加提示
        tt.createToolTip(self.spin2, 'This is a spin widget')

        self.scrW = 30
        self.scrH = 3
        self.scr = scrolledtext.ScrolledText(self.monty, width=self.scrW, height=self.scrH, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, columnspan=3, sticky='WE')

        self.cheVars = [tk.BooleanVar() for i in range(3)]
        self.cheText = ['Disabled', 'Unchecked', 'Checked']
        self.cheState = [['disabled', 'selected'], ['!disabled', '!selected'], ['!disabled', 'selected']]
        for col in range(3):
            temp = ttk.Checkbutton(self.monty2, variable=self.cheVars[col], text=self.cheText[col])
            temp.grid(column=col, row=4, sticky='W')
            temp.state(self.cheState[col])

        self.radVar = tk.IntVar()
        self.radVar.set(99)
        self.colors = ['Blue', 'Gold', 'Red']

        for col in range(3):
            ttk.Radiobutton(self.monty2, variable=self.radVar, text=self.colors[col], value=col,
                            command=self._radCall).grid(column=col, row=5, sticky='W')


oop = OOP()
oop.createWidgets()
oop.win.mainloop()
