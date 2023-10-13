import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH
from tkinter.ttk import *
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
import db.Report as Report
import db.User as User

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

        self.tk_canvas_reports_container = self.__tk_canvas_reports_container(self.tk_frame_right)
        self.tk_frame_detailed = self.__tk_frame_detailed(self.tk_frame_right)
        self.tk_frame_info = self.__tk_frame_info(self.tk_frame_right)
        self.show_map_page()  # 默认显示地图页面

    def __win(self):
        operator_info = db.query_data(User.getUserInfo(3)) # TODO this is just a test of showing id
        print(operator_info)
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
        btn = Button(parent, text="Details", takefocus=False, command=self.show_detail_page)
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

    def __tk_canvas_reports_container(self, parent):
        canvas = tk.Canvas(parent)
        canvas.place(x=10, y=50, width=607, height=233)
        return canvas

    def __tk_scale_slide(self, parent):
        scale = Scale(parent)
        scale.place(relx=0.02, rely=0.95, anchor=tk.SW, width=150, height=30)
        return scale

    def report_lists(self, parent, user_name, comment, date, frame_index):
        frame = Frame(parent)
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_user = Label(frame, text=user_name, anchor="center")
        label_user.place(x=5, y=10, width=100, height=30)

        text_comment = tk.Text(frame)
        text_comment.place(x=100, y=10, width=300, height=30)
        text_comment.insert("1.0", comment)
        self.vbar(text_comment, 120, 10, 300, 30, frame)

        label_date = Label(frame, text=date, anchor="center")
        label_date.place(x=400, y=10, width=100, height=30)

        button_deal = Button(frame, text="Check", takefocus=False)
        button_deal.place(x=500, y=10, width=50, height=30)

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
        canvas_height = len(report_data) * 70
        for widget in self.tk_canvas_reports_container.winfo_children():
            widget.destroy()

        self.tk_canvas_reports_container.configure(height=canvas_height,scrollregion=(0, 0, 607, canvas_height))
        self.tk_canvas_reports_container.place(x=10, y=50, width=607, height=233)
        vbar = Scrollbar(self.tk_canvas_reports_container, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)

        frame = Frame(self.tk_canvas_reports_container,width=580,height=canvas_height)
        self.configure_frame_border(frame)
        frame.pack()

        frame.bind("<Configure>", lambda e: self.tk_canvas_reports_container.configure(
            scrollregion=self.tk_canvas_reports_container.bbox("all")))

        self.tk_canvas_reports_container.create_window((0, 0), window=frame, anchor="nw")
        self.tk_canvas_reports_container.configure(yscrollcommand=vbar.set)
        vbar.configure(command=self.tk_canvas_reports_container.yview)

        for index, data in enumerate(report_data):
            self.report_lists(
                frame,
                data["user_name"],
                data["comment"],
                data["date"],
                index
            )

    def show_map_page(self):
        # 隐藏报告控件
        self.tk_canvas_reports_container.place_forget()
        self.tk_frame_detailed.place_forget()
        self.tk_frame_info.place_forget()

        # 显示地图控件
        self.tk_frame_mapBox.place(x=10, y=50, width=607, height=233)

    def show_detail_page(self):
        # 隐藏报告控件
        self.tk_canvas_reports_container.place_forget()
        self.tk_frame_mapBox.place_forget()
        self.tk_frame_info.place_forget()

        # 显示地图控件
        self.tk_frame_detailed.place(x=10, y=50, width=607, height=233)

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Win()
    win.mainloop()
    db.get_connect().close()