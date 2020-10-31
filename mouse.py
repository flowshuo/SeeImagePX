import tkinter
from tkinter import ttk


def xFunc1(event):
    print(f"鼠标左键滑动坐标是:x={event.x},y={event.y}")


win = tkinter.Tk()
win.title("Kahn Software v1")  # #窗口标题
win.geometry("600x500+200+20")  # #窗口位置500后面是字母x
'''
鼠标移动事件
<B1-Motion>   鼠标左键滑动
<B2-Motion>   鼠标滚轮移动
<B3-Motion>   鼠标右键滑动
'''
xLabel = tkinter.Label(win, text="KAHN Hello world")
xLabel.pack()
xLabel.bind("<Motion>", xFunc1)

win.mainloop()  # #窗口持久化