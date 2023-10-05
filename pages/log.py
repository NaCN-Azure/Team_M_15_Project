from tkinter import *
from tkinter.ttk import *

import requests
from PIL import ImageTk,Image
from io import BytesIO

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_icon_big = self.__tk_icon_big(self)
        self.tk_label_login = self.__tk_label_login(self)
        self.tk_input_input_username = self.__tk_input_input_username(self)
        self.tk_input_input_password = self.__tk_input_input_password(self)
        self.tk_label_label_username = self.__tk_label_label_username(self)
        self.tk_label_label_password = self.__tk_label_label_password(self)
        self.tk_button_button_login = self.__tk_button_button_login(self)
        self.tk_button_button_register = self.__tk_button_button_register(self)

    def __win(self):
        self.title("Bicycle")
        width = 341
        height = 422
        self.config(background='white')
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条

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

    def __tk_label_login(self, parent):
        label = Label(parent, text="User Login", anchor="center", )
        label.place(x=100, y=150, width=148, height=39)
        return label

    def __tk_input_input_username(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=130, y=210, width=190, height=42)
        return ipt

    def __tk_input_input_password(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=130, y=280, width=190, height=42)
        return ipt

    def __tk_label_label_username(self, parent):
        label = Label(parent, text="Username", anchor="center", )
        label.place(x=43, y=205, width=78, height=49)
        return label

    def __tk_label_label_password(self, parent):
        label = Label(parent, text="Password", anchor="center", )
        label.place(x=43, y=274, width=78, height=49)
        return label

    def __tk_button_button_login(self, parent):
        btn = Button(parent, text="Login", takefocus=False, )
        btn.place(x=30, y=350, width=112, height=41)
        return btn

    def __tk_button_button_register(self, parent):
        btn = Button(parent, text="Register", takefocus=False, )
        btn.place(x=190, y=350, width=112, height=41)
        return btn

    def __tk_icon_big(self, parent):
        web_image_icon = requests.get('https://static-00.iconduck.com/assets.00/person-icon-1901x2048-a9h70k71.png')
        temp = BytesIO(web_image_icon.content)
        image_open = Image.open(temp).resize((120, 120))
        # image_open = Image.open("..\images\login\login_big.png").resize((120,120))
        icon_big = ImageTk.PhotoImage(image_open)
        label = Label(parent, image=icon_big)
        label.image = icon_big
        label.place(x=110, y=30)
        return label

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Win()
    win.mainloop()
