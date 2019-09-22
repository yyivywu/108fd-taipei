# -*- coding: utf-8 -*-
"""
圖形使用者介面套件 tkinter
輸入姓名、身高、體重等基本資料

@author: Ivy Wu 2019/9/22
"""

# 匯入 tkinter 套件
import tkinter as tk

# 自訂函式 ShowData：顯示使用者輸入的資料
# 使用 get 方法讀取 Entry 元件的輸入文字
def ShowData():
    dataString.set("%s 你好！你的身高為 %s 公分，體重為 %s 公斤！" % (enName.get(), enHeight.get(), enWeight.get()))
    
# 建立視窗及設定外觀
root = tk.Tk()
root.title("基本資料輸入")
root.geometry("500x400")

# 標籤 Label：用於顯示提示文字
lb1 = tk.Label(root, text="請輸入姓名：")
lb2 = tk.Label(root, text="請輸入身高：")
lb3 = tk.Label(root, text="請輸入體重：")

# 宣告標籤 Label 顯示資料的字串變數
dataString = tk.StringVar()
dataString.set("顯示使用者輸入的基本資料")
lbShow = tk.Label(root, textvariable=dataString)

# 文字輸入 Entry：用於接收使用者輸入基本資料
enName = tk.Entry(root)
enHeight = tk.Entry(root)
enWeight = tk.Entry(root)

# 按鈕 Button：用於執行動作
btnShow = tk.Button(root, text="顯示基本資料", command=ShowData)
btnQuit = tk.Button(root, text="關閉程式", command=root.destroy)

# 在視窗中擺放各個元件
lb1.pack()
enName.pack()
lb2.pack()
enHeight.pack()
lb3.pack()
enWeight.pack()
btnShow.pack()
lbShow.pack()
btnQuit.pack()

# 呼叫視窗
root.mainloop()