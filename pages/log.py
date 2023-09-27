from tkinter import *
from ttkbootstrap import *
from pytkUI.locale_zh_cn import zh_cn_initialize
from pytkUI.widgets import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        zh_cn_initialize()
        self.__win()
        self.ext_icon_big_logo = self.__ext_icon_big_logo(self)
        self.tk_label_center_login = self.__tk_label_center_login(self)
        self.tk_input_username = self.__tk_input_username(self)
        self.tk_input_password = self.__tk_input_password(self)
        self.ext_icon_userlogo = self.__ext_icon_userlogo(self)
        self.ext_icon_key = self.__ext_icon_key(self)
        self.tk_label_username = self.__tk_label_username(self)
        self.tk_label_password = self.__tk_label_password(self)
        self.tk_button_login = self.__tk_button_login(self)
        self.tk_button_register = self.__tk_button_register(self)

    def __win(self):
        self.title("My Window")
        width = 342
        height = 445
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, bar, widget):
        self.__scrollbar_hide(bar, widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))

    def __scrollbar_show(self, bar, widget):
        bar.lift(widget)

    def __scrollbar_hide(self, bar, widget):
        bar.lower(widget)

    def vbar(self, ele, x, y, w, h, parent):
        sw = 15
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar, ele)

    def __ext_icon_big_logo(self, parent):
        icon = Icon(parent, icon_name="file-person", size=132, color="#000000")
        icon.place(x=100, y=20, width=147, height=147)
        return icon

    def __tk_label_center_login(self, parent):
        label = Label(parent, text="User Login", anchor="center", bootstyle="default", font=('Helvetica',18))
        label.place(x=100, y=170, width=148, height=39)
        return label

    def __tk_input_username(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=134, y=230, width=190, height=42)
        return ipt

    def __tk_input_password(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(x=133, y=287, width=190, height=42)
        return ipt

    def __ext_icon_userlogo(self, parent):
        icon = Icon(parent, icon_name="envelope", size=48, color="#000000")
        icon.place(x=81, y=225, width=53, height=53)
        return icon

    def __ext_icon_key(self, parent):
        icon = Icon(parent, icon_name="key-fill", size=41, color="#000000")
        icon.place(x=86, y=287, width=46, height=46)
        return icon

    def __tk_label_username(self, parent):
        label = Label(parent, text="Username", anchor="center", bootstyle="primary", font=('Helvetica',11))
        label.place(x=7, y=225, width=78, height=49)
        return label

    def __tk_label_password(self, parent):
        label = Label(parent, text="Password", anchor="center", bootstyle="primary", font=('Helvetica',11))
        label.place(x=7, y=285, width=78, height=49)
        return label

    def __tk_button_login(self, parent):
        btn = Button(parent, text="Login", takefocus=False, bootstyle="default")
        btn.place(x=30, y=370, width=112, height=41)
        return btn

    def __tk_button_register(self, parent):
        btn = Button(parent, text="Register", takefocus=False, bootstyle="default")
        btn.place(x=200, y=370, width=112, height=41)
        return btn

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Win()
    win.mainloop()