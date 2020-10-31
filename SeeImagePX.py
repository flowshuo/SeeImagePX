import cv2
from tkinter import *
import tkinter.filedialog as tf
from PIL import Image, ImageTk


#解决了基本的界面整合
#残留问题1：没有排版
#残留问题2：图片label仍然存在超界问题（可能是自带边框的缘故，能捕获的坐标比图片大）
#残留问题3：路径框不显示
#残留问题4：没有做第二次打开图片的处理


def get_info_by_locate(x, y):
    g = gray[y, x]
    cb = color[y, x][0]
    cg = color[y, x][1]
    cr = color[y, x][2]
    return g, cb, cg, cr


def fresh_info(x, y):
    xy = "%d,%d" % (x, y)
    g, cb, cg, cr = get_info_by_locate(x, y)
    bgr = "%d,%d,%d" % (cb, cg, cr)

    t1.delete(1.0, END)
    t1.insert('insert', xy)
    t2.delete(1.0, END)
    t2.insert('insert', g)
    t3.delete(1.0, END)
    t3.insert('insert', bgr)


def open_image():
    file_dir = tf.askopenfilename()
    ima_ety.delete(1, END)
    ima_ety.insert(0, file_dir)
    if file_dir != '':
        source_img = cv2.imread(file_dir)

        global color
        color = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
        global gray
        gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)

        rgb_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
        rgb_img = Image.fromarray(rgb_img)
        rgb_img = ImageTk.PhotoImage(rgb_img)
        ima_label = Label(win)
        ima_label.configure(image=rgb_img)
        ima_label.image = rgb_img
        ima_label.grid(column=0, row=2)
        ima_label.bind("<Motion>", mouse_move)


def mouse_move(event):
    print(f"X:{event.x},Y:{event.y}")
    fresh_info(event.x, event.y)


win = Tk()
win.title('图片框')
ima_ety = Entry(win, textvariable=StringVar(), borderwidth=1, state=DISABLED)
ima_ety.grid(column=0, row=0)
ima_bt = Button(win, text='选择', command=open_image)
ima_bt.grid(column=1, row=0)

t1 = Text(win, width=10, height=1)
t1.grid(column=0, row=1)
t2 = Text(win, width=10, height=1)
t2.grid(column=1, row=1)
t3 = Text(win, width=10, height=1)
t3.grid(column=2, row=1)

win.mainloop()
