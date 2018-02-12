import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.wm_title('Tabbed Layout')

menuBar = tk.Menu(win)
win.config(menu=menuBar)


def _quit():
    win.quit()
    win.destroy()
    exit()


fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label='File')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=_quit)
helpMenu = tk.Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About')
menuBar.add_cascade(menu=fileMenu, label='File')
menuBar.add_cascade(menu=helpMenu, label='Help')

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

scrW = 30
scrH = 3
scr = scrolledtext.ScrolledText(monty, width=scrW, height=scrH, wrap=tk.WORD)
scr.grid(column=0, row=2, columnspan=3, sticky='WE')

cheVars = [tk.IntVar() for i in range(3)]
cheText = ['Disabled', 'Unchecked', 'Checked']
cheState = [['disabled', 'selected'], ['!disabled', '!selected'], ['!disabled', 'selected']]
for col in range(3):
    temp = ttk.Checkbutton(monty2, variable=cheVars[col], text=cheText[col])
    temp.grid(column=col, row=3, sticky='W')
    temp.state(cheState[col])

radVar = tk.IntVar()
radVar.set(99)
colors = ['Blue', 'Gold', 'Red']


def radCall():
    radnum = radVar.get()
    monty2.configure(text=colors[radnum])


for col in range(3):
    temp = ttk.Radiobutton(monty2, variable=radVar, text=colors[col], value=col, command=radCall)
    temp.grid(column=col, row=4, sticky='W')

win.mainloop()
