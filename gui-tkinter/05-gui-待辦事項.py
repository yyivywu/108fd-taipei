# -*- coding: utf-8 -*-
"""
圖形使用者介面套件 tkinter
使用串列 list 建立及操作 待辦事項

@author: Ivy Wu 2019/9/22
"""

# 匯入 tkinter 套件
import tkinter as tk

# 自訂函式：待辦事項操作
def ItemWork():
    if choice.get() == 'add':
        todolist.append(enWork.get())
        txtWorks.delete(1.0, tk.END)   
        txtWorks.insert(tk.INSERT, todolist)
        rbAdd.deselect()
    elif choice.get() == 'insert':
        todolist.insert(int(enPos.get()), enWork.get())
        txtWorks.delete(1.0, tk.END)   
        txtWorks.insert(tk.INSERT, todolist)
        rbInsert.deselect()        
    elif choice.get() == 'remove':
        todolist.remove(enWork.get())
        txtWorks.delete(1.0, tk.END)   
        txtWorks.insert(tk.INSERT, todolist)
        rbRemove.deselect()
    else:
        todolist.pop(int(enPos.get()))
        txtWorks.delete(1.0, tk.END)   
        txtWorks.insert(tk.INSERT, todolist)
        rbPop.deselect()
        
    
# 自訂函式：重設所有輸入及顯示
def ClearData(): 
    enWork.delete(0, tk.END)
    enPos.delete(0, tk.END) 
    enWork.focus()

# 宣告待辦事項空串列
todolist = []

# 建立視窗及設定外觀
root = tk.Tk()
root.title("待辦事項-Grid排版")

# 8 個元件：2 個標籤、2 個 Entry、2 個按鈕、１ 個文字區塊、1 個選項按鈕
lb1 = tk.Label(root, text="待辦事項：", height=2, font=('標楷體', 12))
lb2 = tk.Label(root, text="串列位置：", height=2, font=('標楷體', 12))

enWork = tk.Entry(root, bg="gray80", width=15, font=('標楷體', 14))
enPos = tk.Entry(root, bg="gray80", width=15, font=('標楷體', 14))

btnReset = tk.Button(root, text="清除資料", command=ClearData, font=('標楷體', 14))
btnQuit = tk.Button(root, text="關閉程式", command=root.destroy, font=('標楷體', 14))

# 建立文字區塊 Text
txtWorks = tk.Text(root, width=40, height=6)
txtWorks.insert(tk.INSERT, "")
txtWorks.config(bg="yellow")

# 建立選項按鈕 Radiobutton
# 選項按鈕的 variable 參數指定相同變數名稱，即為同一組選項
choice = tk.StringVar()  # 設定資料型態為字串
rbAdd = tk.Radiobutton(root, text="新增", value='add', variable=choice, command=ItemWork)
rbInsert = tk.Radiobutton(root, text="插入", value='insert', variable=choice, command=ItemWork)
rbRemove = tk.Radiobutton(root, text="刪除元素", value='remove', variable=choice, command=ItemWork)
rbPop = tk.Radiobutton(root, text="刪除索引", value='pop', variable=choice, command=ItemWork)


# 使用 Grid 方式排版, row 設定列，column 設定行，由 0 開始設定
lb1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
enWork.grid(row=0, column=1, padx=5, pady=5, sticky="w")
lb2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
enPos.grid(row=1, column=1, padx=5, pady=5, sticky="w")
rbAdd.grid(row=2, column=0, padx=5, pady=5, sticky="w")
rbInsert.grid(row=2, column=1, padx=5, pady=5, sticky="w")
rbRemove.grid(row=3, column=0, padx=5, pady=5, sticky="w")
rbPop.grid(row=3, column=1, padx=5, pady=5, sticky="w")

txtWorks.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky="w")

btnReset.grid(row=5, column=0, padx=5, pady=5)
btnQuit.grid(row=5, column=1, padx=5, pady=5)

# 剛啟動時，游標停在最上面一個輸入元件中
enWork.focus()

# 啟動視窗
root.mainloop()