import tkinter as tk
from tkinter.ttk import *
import database.dbconfig as db
import database.Bike as Bike
import database.Order as Order
import database.Report as Report
import database.User as User

class WinGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__win()

        self.tk_frame_left = self.__tk_frame_left(self)

        self.tk_button_MainButton = self.__tk_button_MainButton(self.tk_frame_left)
        self.tk_button_ReportButton = self.__tk_button_ReportButton(self.tk_frame_left)
        self.tk_button_DetailButton = self.__tk_button_DetailButton(self.tk_frame_left)
        self.tk_button_InfoButton = self.__tk_button_InfoButton(self.tk_frame_left)

        self.tk_frame_right = self.__tk_frame_right(self)
        self.tk_select_box_type = self.__tk_select_box_type(self.tk_frame_right)
        self.tk_input_search = self.__tk_input_search(self.tk_frame_right)
        self.tk_label_icon = self.__tk_label_icon(self.tk_frame_right)

        self.tk_frame_mapBox = self.__tk_frame_mapBox(self.tk_frame_right)
        self.tk_scale_slide = self.__tk_scale_slide(self.tk_frame_mapBox)

        self.tk_frame_reports_container = self.__tk_frame_reports_container(self.tk_frame_right)
        self.tk_frame_detailed = self.__tk_frame_detailed(self.tk_frame_right)
        self.tk_frame_info = self.__tk_frame_info(self.tk_frame_right)
        self.show_map_page()  # 默认显示地图页面

    def __win(self):
        operator_info = db.query_data(User.getUserInfo(3))
        self.title("Operator: "+operator_info[0]['user_name'])
        width = 783
        height = 322
        style = Style()
        style.configure("My.TFrame", borderwidth=2, relief="solid", foreground="black")
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def configure_frame_border(self, frame):
        frame.configure(style="My.TFrame")
    def __scrollbar_show(self, bar, widget):
        bar.lift(widget)
    def __scrollbar_hide(self, bar, widget):
        bar.lower(widget)
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    def vbar(self,ele, x, y, w, h, parent):
        sw = 15 # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar,ele)
    def __tk_frame_left(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=106, height=295)
        self.configure_frame_border(frame)
        return frame
    def __tk_button_MainButton(self, parent):
        btn = Button(parent, text="Map", takefocus=False, command=self.show_map_page)
        btn.place(x=10, y=20, width=80, height=48)
        return btn
    def __tk_button_ReportButton(self, parent):
        btn = Button(parent, text="Reports", takefocus=False, command=self.show_reports_page)
        btn.place(x=10, y=90, width=80, height=48)
        return btn
    def __tk_button_DetailButton(self, parent):
        btn = Button(parent, text="Details", takefocus=False, )
        btn.place(x=10, y=160, width=80, height=48)
        return btn
    def __tk_button_InfoButton(self, parent):
        btn = Button(parent, text="Info", takefocus=False, )
        btn.place(x=10, y=230, width=80, height=48)
        return btn
    def __tk_frame_right(self, parent):
        frame = Frame(parent)
        frame.place(x=130, y=10, width=638, height=295)
        self.configure_frame_border(frame)
        return frame
    def __tk_select_box_type(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("Types", "Python", "Tkinter Helper")
        cb.place(x=476, y=10, width=154, height=32)
        return cb
    def __tk_input_search(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=90, y=10, width=150, height=30)
        return ipt
    def __tk_label_icon(self, parent):
        label = Label(parent, text="Search: ", anchor="center", )
        label.place(x=20, y=10, width=50, height=30)
        return label

    def __tk_frame_mapBox(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=50, width=607, height=233)  # 修改位置
        self.configure_frame_border(frame)
        return frame

    def __tk_frame_detailed(self,parent):
        frame = Frame(parent)
        frame.place(x=10, y=50, width=607, height=233)
        self.configure_frame_border(frame)
        return frame

    def __tk_frame_info(self,parent):
        frame = Frame(parent)
        frame.place(x=10, y=50, width=607, height=233)
        self.configure_frame_border(frame)
        return frame

    def __tk_frame_reports_container(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=50, width=607, height=233)
        self.configure_frame_border(frame)
        return frame

    def __tk_scale_slide(self, parent):
        scale = Scale(parent)
        scale.place(relx=0.02, rely=0.95, anchor=tk.SW, width=150, height=30)
        return scale
    # def report_lists(self, parent, user_name, comment, date, frame_index):
    #     frame = Frame(parent)
    #     frame.place(relx=0.05, rely=frame_index * 0.12, width=0.9, height=0.1)
    #     frame.configure(style="My.TFrame")
    #
    #     label_user = Label(frame, text=user_name, anchor="center")
    #     label_user.place(relx=0.05, rely=0.1, width=0.2, height=0.8)
    #
    #     text_comment = tk.Text(frame)
    #     text_comment.place(relx=0.3, rely=0.1, width=0.5, height=0.8)
    #     text_comment.insert("1.0", comment)
    #     self.vbar(text_comment, 0.3, 0.1, 0.5, 0.8, frame)
    #
    #     label_date = Label(frame, text=date, anchor="center")
    #     label_date.place(relx=0.85, rely=0.1, width=0.15, height=0.8)
    #
    #     button_deal = Button(frame, text="Check", takefocus=False)
    #     button_deal.place(relx=0.95, rely=0.1, width=0.05, height=0.8)
    #
    #     return frame 使用相对布局的

    def report_lists(self, parent, user_name, comment, date, frame_index):
        frame = Frame(parent)
        frame.place(x=5, y=10 + frame_index * 60, width=600, height=50)
        frame.configure(style="My.TFrame")

        label_user = Label(frame, text=user_name, anchor="center")
        label_user.place(x=10, y=10, width=100, height=30)

        text_comment = tk.Text(frame)
        text_comment.place(x=120, y=10, width=300, height=30)
        text_comment.insert("1.0", comment)
        self.vbar(text_comment, 120, 10, 300, 30, frame)

        label_date = Label(frame, text=date, anchor="center")
        label_date.place(x=430, y=10, width=100, height=30)

        button_deal = Button(frame, text="Check", takefocus=False)
        button_deal.place(x=540, y=10, width=50, height=30)

        return frame

    def show_reports_page(self):
        # 隐藏地图控件
        self.tk_frame_mapBox.place_forget()
        self.tk_frame_detailed.place_forget()
        self.tk_frame_info.place_forget()
        # 显示报告控件

        # 获取用户报告数据，这里需要从数据库中获取数据
        report_data = [
            {"user_name": "User1", "comment": "Report 1 comment", "date": "06/09/2023"},
            {"user_name": "User2", "comment": "Report 2 comment", "date": "06/10/2023"},
            {"user_name": "User3", "comment": "Report 3 comment", "date": "06/10/2023"},
            {"user_name": "User4", "comment": "Report 4 comment", "date": "06/10/2023"},
            {"user_name": "User5", "comment": "Report 5 comment", "date": "06/10/2023"},
            {"user_name": "User6", "comment": "Report 6 comment", "date": "06/10/2023"},
            {"user_name": "User7", "comment": "Report 7 comment", "date": "06/10/2023"},

            # 添加更多报告数据
        ]

        # 清除之前的报告框架
        for widget in self.tk_frame_reports_container.winfo_children():
            widget.destroy()

        # 创建并显示用户报告框架
        for index, data in enumerate(report_data):
            self.report_lists(
                self.tk_frame_reports_container,
                data["user_name"],
                data["comment"],
                data["date"],
                index
            )

        style = Style()
        style.configure("Yellow.TFrame", background="yellow")  # 定义一个名为Yellow.TFrame的样式
        self.tk_frame_reports_container.configure(style="Yellow.TFrame")

        self.tk_frame_reports_container.place(x=10, y=50, width=607, height=233)

    def show_map_page(self):
        # 隐藏报告控件
        self.tk_frame_reports_container.place_forget()
        self.tk_frame_detailed.place_forget()
        self.tk_frame_info.place_forget()

        # 显示地图控件
        self.tk_frame_mapBox.place(x=10, y=50, width=607, height=233)

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Win()
    win.mainloop()