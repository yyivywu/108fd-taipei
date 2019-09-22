# -*- coding: utf-8 -*-
"""
圖形使用者介面套件 tkinter
Checkbutton 核取方塊

@author: Ivy Wu 2019/9/22
"""

import tkinter as tk

# 建立視窗及設定外觀
root = tk.Tk()
root.title('Checkbutton 多選鈕')

lb1 = tk.Label(root, bg='yellow', width=20, height=2, text='empty', font=('標楷體', 14))
lb1.pack()

# 自訂函式：核取方塊被選或不選時
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        lb1.config(text='我只愛 Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        lb1.config(text='我只愛 C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        lb1.config(text='我都不愛')
    else:
        lb1.config(text='我都愛')

# 宣告核取方塊使用的變數名稱
var1 = tk.IntVar()
var2 = tk.IntVar()

# 建立 2 個核取方塊
c1 = tk.Checkbutton(root, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection, font=('標楷體', 14))
c2 = tk.Checkbutton(root, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection, font=('標楷體', 14))
c1.pack()
c2.pack()


root.mainloop()