import cv2
import numpy as np
from tkinter import *

# 图片路径
img = cv2.imread('0.jpg')
a = []
b = []
win = Tk()
win.title('zuobiao')
win.geometry('300x200')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Label(win, text='二维坐标', width=10, height=5).grid(column=0, row=0)
Label(win, text='灰度值', width=10, height=5).grid(column=0, row=1)

t1 = Text(win, width=10, height=3)
t1.grid(column = 1,row = 0)
t2 = Text(win, width=10, height=3)
t2.grid(column = 1,row=1)
def on_EVENT_LBUTTONDOWN(event, x, y,param,er):
    if event == cv2.EVENT_MOUSEMOVE:
        xy = "%d,%d" % (x, y)
        g = gray[y,x]
        a.append(x)
        b.append(y)

        t1.delete(1.0,END)
        t1.insert('insert', xy)
        # Label(win, text='灰度值', width=10, height=5).grid(column = 0,row = 1)
        t2.delete(1.0,END)
        t2.insert('insert',g)
        win.mainloop()
        #cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        #cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
         #           1.0, (0, 0, 0), thickness=1)

        cv2.imshow("image", img)
        #print(x, y)


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)
#print(a[0], b[0])
cv2.destroyAllWindows()

'''
位置参数说明：

图片
要添加的文字
文字添加到图片上的位置
字体的类型
字体大小
字体颜色
字体粗细
'''