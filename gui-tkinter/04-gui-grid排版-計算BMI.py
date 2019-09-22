# -*- coding: utf-8 -*-
"""
圖形使用者介面套件 tkinter
Grid 排版方式：使用「表格」方式安排元件位置，元件依行及列座標位置排版
計算 BMI 及判斷肥胖分級

@author: Ivy Wu 2019/9/22
"""

# 匯入 tkinter 套件
import tkinter as tk

# 自訂函式：計算 BMI
def CalBMI():
    h = float(enHeight.get())
    w = float(enWeight.get())
    BMI = w / h ** 2
    bmiString.set("BMI = %.2f" % BMI)
    if BMI < 18:
        rateString.set("分級 = 體重過輕")
    elif BMI < 24:
        rateString.set("分級 = 體重正常")
    elif BMI < 27:
        rateString.set("分級 = 體重過重")
    else:
        rateString.set("分級 = 體重肥胖")

        
# 自訂函式：重設所有輸入及顯示
def ClearData(): 
    enHeight.delete(0, tk.END)
    enWeight.delete(0, tk.END)
    bmiString.set("BMI = ")
    rateString.set("分級 = ")
    enHeight.focus()
    

# 建立視窗及設定外觀
root = tk.Tk()
root.title("計算BMI及分級-Grid排版")

# 共有 9 個元件要擺放，4 個標籤、2 個 Entry、3 個按鈕
lb1 = tk.Label(root, text="請輸入身高(公尺)：", height=2, font=('標楷體', 12))
lb2 = tk.Label(root, text="請輸入體重(公斤)：", height=2, font=('標楷體', 12))

# 宣告 BMI 及體重分級的字串變數
bmiString = tk.StringVar()
bmiString.set("BMI = ")
rateString = tk.StringVar()
rateString.set("分級為 ")
lbBMI = tk.Label(root, textvariable=bmiString, anchor="w", bg="lightyellow", \
                 width=25, height=2, font=('標楷體', 12))
lbRate = tk.Label(root, textvariable=rateString, anchor="w", bg="lightyellow", \
                  width=25, height=2, font=('標楷體', 12))

enHeight = tk.Entry(root, bg="gray80", width=15, font=('標楷體', 14))
enWeight = tk.Entry(root, bg="gray80", width=15, font=('標楷體', 14))

btnCal = tk.Button(root, text="計算", command=CalBMI, font=('標楷體', 14))
btnReset = tk.Button(root, text="重設", command=ClearData, font=('標楷體', 14))
btnQuit = tk.Button(root, text="關閉程式", command=root.destroy, font=('標楷體', 14))


# 使用 Grid 方式排版, row 設定列，column 設定行，由 0 開始設定
lb1.grid(row=0, column=0, padx=5, pady=5)
enHeight.grid(row=0, column=1, padx=5, pady=5)
lb2.grid(row=1, column=0, padx=5, pady=5)
enWeight.grid(row=1, column=1, padx=5, pady=5)
btnCal.grid(row=2, column=0, padx=5, pady=5)
btnReset.grid(row=2, column=1, padx=5, pady=5)

# 2 個欄位合併為一個
# rowspan 設定列合併，columnspaN 設定行合併，由 0 開始設定
# sticky 設定元件對齊方式：e 靠右、w 靠左、n 靠上、s 靠下
lbBMI.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky="w")
lbRate.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky="w")
btnQuit.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

# 啟動視窗
root.mainloop()