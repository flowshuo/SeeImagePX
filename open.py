import tkinter
import os
import cv2
from PIL import Image,ImageTk
from tkinter import filedialog

# global start 全局变量定义初始化开始
carmela_hight = 300
carmela_width = 300
Source_Img_Label = None
py_path=os.path.abspath(os.path.dirname(__file__))
#global end 全局变量定义初始化结束
#创建窗口对象
root = tkinter.Tk()
#窗口使用变量初始化开始
screen_Width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_Width//2
height = screen_height//2
root_win_par = '%dx%d+%d+%d'% (width, height, (screen_Width-width)/2, (screen_height-height)/2)
String_var = tkinter.StringVar()
String_var.set('尚未选择文件')
#窗口使用变量初始化结束
#按键绑定函数
def AskPicture():
    global Source_Img_Label
    #图片路径获取
    Picture_Path = filedialog.askopenfilename()
    #显示图片路径，在Img_Path_Text中
    String_var.set(Picture_Path)
    #读取图片参数，通过opencv
    Source_Img = cv2.imread(Picture_Path)
    #检测是否输入确实为图片
    if (Source_Img is None):
        String_var.set('文件选择错误')
        return
    #图片格式转化
    Rgb_Img = cv2.cvtColor(Source_Img,cv2.COLOR_BGR2RGB)
    Rgb_Img = Image.fromarray(Rgb_Img)
    #图片大小更改
    Source_Img_Height = Source_Img.shape[0]
    Source_Img_Width = Source_Img.shape[1]
    if carmela_hight > carmela_width:
        Rgb_Img = Rgb_Img.resize( (carmela_width , int((carmela_width/Source_Img_Width)*Source_Img_Height) ) ,Image.ANTIALIAS)
    else:
        Rgb_Img = Rgb_Img.resize( (int((carmela_hight/Source_Img_Height)*Source_Img_Width) , carmela_hight) ,Image.ANTIALIAS)
    #图片格式转化
    Rgb_Img = ImageTk.PhotoImage(Rgb_Img)

    #检测是否是第一次输入图片
    if(Source_Img_Label is None):#是的话创建图片显示Label
        Source_Img_Label = tkinter.Label(root,bg='red',image=Rgb_Img,width=carmela_width,height=carmela_hight)
        Source_Img_Label.image = Rgb_Img
        Source_Img_Label.place(x=10,y=40)
    else:#不是的话更改Label中的图片
        Source_Img_Label.configure(image=Rgb_Img)
        Source_Img_Label.image = Rgb_Img



#窗口大小及位置设置
root.geometry(root_win_par)
#设置窗口是否可变长、宽，True：可变，False：不可变
root.resizable(width=False, height=False)

root.title('图像显示')#窗口标题设置
#root.iconbitmap(py_path+'\\ico.ico')#窗口图标设置
#显示路径输入框初始化及放置(禁止写入)
Img_Path_Text = tkinter.Entry(root,textvariable=String_var,borderwidth=1,state=tkinter.DISABLED)
Img_Path_Text.place(x=10,y=10,width=width-20-40,height=20)
#路径选取按钮初始化设置
Img_Path_Button = tkinter.Button(root,text='选择',command=AskPicture)
Img_Path_Button.place(x=width-45,y=10,width=40,height=20)

#窗口主循环
root.mainloop()