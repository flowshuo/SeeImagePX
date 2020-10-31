import cv2
from tkinter import *
import tkinter.filedialog as TF

def get_info_by_locate(color,gray,x,y):
    g = gray[y, x]
    cb = color[y, x][0]
    cg = color[y, x][1]
    cr = color[y, x][2]
    return g, cb, cg, cr

file = TF.askopenfilename()
img = cv2.imread(file)

win = Tk()
win.title('图片框')
win.geometry('300x200')
color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
        g, cb, cg, cr = get_info_by_locate(color, gray, x, y)
        try:
            t1.delete(1.0,END)
            t1.insert('insert', xy)
            # Label(win, text='灰度值', width=10, height=5).grid(column = 0,row = 1)
            t2.delete(1.0,END)
            t2.insert('insert', g)
            t2.insert('insert', ',')
            t2.insert('insert', cb)
            t2.insert('insert', ',')
            t2.insert('insert', cg)
            t2.insert('insert', ',')
            t2.insert('insert', cr)
            cv2.imshow("image", img)
            # print(x, y)
        except:
            return None


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
win.mainloop()
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