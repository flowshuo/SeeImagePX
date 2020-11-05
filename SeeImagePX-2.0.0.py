import cv2
from tkinter import *
import tkinter.filedialog as tf
from PIL import Image, ImageTk
import webbrowser as web


def get_info_by_locate(x, y):
    try:
        g = gray[y, x]
        cb = color[y, x][0]
        cg = color[y, x][1]
        cr = color[y, x][2]
    except IndexError:
        print("")
    return g, cb, cg, cr


def fresh_info(x, y):
    try:
        xy = "%d,%d" % (x, y)
        g, cb, cg, cr = get_info_by_locate(x, y)
        bgr = "%d,%d,%d" % (cb, cg, cr)

        statusbar.delete(1.0, END)
        statusbar.insert('insert', ' 坐标：')
        statusbar.insert('insert', xy)
        statusbar.insert('insert', ' 灰度：')
        statusbar.insert('insert', g)
        statusbar.insert('insert', ' 色彩：')
        statusbar.insert('insert', bgr)
    except UnboundLocalError:
        print("")
        

def open_url():
    web.open('https://flowshuo.github.io/SeeImagePX/')


def open_image():
    file_dir = tf.askopenfilename()
    source_img = cv2.imread(file_dir)

    global color
    color = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
    global gray
    gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)

    rgb_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
    rgb_img = Image.fromarray(rgb_img)
    rgb_img = ImageTk.PhotoImage(rgb_img)

    ima_label.configure(image=rgb_img,width=0,height=0)
    ima_label.image = rgb_img
    ima_label.bind("<Motion>", mouse_move)


def mouse_move(event):
    fresh_info(event.x, event.y)


win = Tk()
win.title('图片框')

ima_label = Label(win,width=50,height=10)
ima_label.pack(side=TOP)

menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='打开', command=open_image)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='关于', menu=aboutmenu)
aboutmenu.add_command(label='项目网页', command=open_url)

win.config(menu=menubar)

statusbar = Text(win, bd=1, width=10, height=1)
statusbar.pack(side=BOTTOM, fill=X)

win.mainloop()
