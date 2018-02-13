import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox


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

menuBar = tk.Menu(win)
win.config(menu=menuBar)


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


def _quit():
    win.quit()
    win.destroy()
    exit()


fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label='File')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=_quit)
helpMenu = tk.Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=_msgBox)
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


def callBack():
    action.configure(text='Hello ' + name.get() + ' ' + number.get())
    action.configure(state='disabled')


action = ttk.Button(monty, text='Click Me', command=callBack)
action.grid(column=2, row=1)


def _spin():
    value = spin.get()
    scr.insert(tk.INSERT, value + '\n')


spin = tk.Spinbox(monty, from_=1, to=10, width=5, bd=5, command=_spin)
spin.grid(column=0, row=2)
# 指定一组特定值以供选择,改变外观
spin2 = tk.Spinbox(monty, values=(2, 4, 42, 100), width=5, bd=5, relief=tk.GROOVE, command=_spin)
spin2.grid(column=1, row=2)
createToolTip(spin2, 'This is a spin widget.')

scrW = 30
scrH = 3
scr = scrolledtext.ScrolledText(monty, width=scrW, height=scrH, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3, sticky='WE')

cheVars = [tk.IntVar() for i in range(3)]
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
