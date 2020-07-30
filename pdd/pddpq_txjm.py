from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("第一个程序")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "#DC143C"                                 #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高，这里不需要虚化屏蔽掉
        #标签
        self.init_data_label = Label(self.init_window_name, text="请复制登录后网站的cookie到文本框：")   #添加标签
        self.init_data_label.grid(row=0, column=0)                               #标签所在窗口的位置
        # self.result_data_label = Label(self.init_window_name, text="输出结果")
        # self.result_data_label.grid(row=0, column=12)
        # self.log_label = Label(self.init_window_name, text="日志")
        # self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)    #文本框所在的位置
        # self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        # self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        # self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        # self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮 # 调用内部方法  加()为直接调用  ,command=self.str_trans_to_md5
        self.str_trans_to_md5_button = Button(self.init_window_name, text="取数", bg="lightblue", width=10)#,command=self.str_trans_to_md5)
        self.str_trans_to_md5_button.grid(row=0, column=11)

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    init_window.mainloop()


gui_start()