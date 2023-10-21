import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH, DISABLED, messagebox
from tkinter.ttk import *
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
import db.Report as Report
import db.User as User

class Userpage(tk.Tk):
    def __init__(self,user_id):
        super().__init__()
        self.__win()

        self.user_id = user_id
        self.now_type = 1
        self.title(self.get_title_name(user_id))
        self.filter = "All"

        self.tk_frame_left = self.__tk_frame_left(self)

        self.tk_button_MainButton = self.__tk_button_MainButton(self.tk_frame_left)
        self.tk_button_ReportButton = self.__tk_button_ReportButton(self.tk_frame_left)
        self.tk_button_OrdersButton = self.__tk_button_OrdersButton(self.tk_frame_left)
        self.tk_button_InfoButton = self.__tk_button_InfoButton(self.tk_frame_left)

        self.tk_frame_right = self.__tk_frame_right(self)
        self.tk_select_box_type = self.__tk_select_box_type(self.tk_frame_right)
        self.tk_label_icon = self.__tk_label_icon(self.tk_frame_right)

        self.tk_frame_mapBox = self.__tk_frame_mapBox(self.tk_frame_right)
        self.tk_scale_slide = self.__tk_scale_slide(self.tk_frame_mapBox)

        self.tk_canvas_reports_container = self.__tk_canvas_reports_container(self.tk_frame_right)
        self.tk_canvas_detailed = self.__tk_canvas_detailed(self.tk_frame_right)
        self.tk_frame_info = self.__tk_frame_info(self.tk_frame_right)
        self.show_map_page()  # default showing map pages

    def get_title_name(self,user_id):
        operator_info = db.query_data(User.getUserInfo(self.user_id))
        return "User: " + operator_info[0]['user_name']

    def __win(self):
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
        btn = Button(parent, text="My Reports", takefocus=False, command=self.show_reports_page)
        btn.place(x=10, y=90, width=80, height=48)
        return btn
    def __tk_button_OrdersButton(self, parent):
        btn = Button(parent, text="Orders", takefocus=False, command=self.show_orders_page)
        btn.place(x=10, y=160, width=80, height=48)
        return btn
    def __tk_button_InfoButton(self, parent):
        btn = Button(parent, text="Info", takefocus=False, command=self.show_info_page)
        btn.place(x=10, y=230, width=80, height=48)
        return btn
    def __tk_frame_right(self, parent):
        frame = Frame(parent)
        frame.place(x=130, y=10, width=638, height=295)
        self.configure_frame_border(frame)
        return frame
    def __tk_select_box_type(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("All", "Bike", "Car")
        cb.set("All")
        cb.place(x=476, y=10, width=154, height=32)
        cb.bind("<<ComboboxSelected>>", self.on_combobox_select)
        return cb
    def __tk_label_icon(self, parent):
        label = Label(parent, text="Map", anchor="center", )
        label.place(x=20, y=10, width=50, height=30)
        return label
    def __tk_frame_mapBox(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=50, width=607, height=233) # this is the containor of map
        self.configure_frame_border(frame)
        return frame
    def __tk_canvas_detailed(self,parent):
        canvas = tk.Canvas(parent)
        canvas.place(x=10, y=50, width=607, height=233)  # this is the containor of reports, IMPORTANT!! IT IS CANVAS!!
        return canvas
    def __tk_frame_info(self,parent):
        frame = Frame(parent)
        frame.place(x=10, y=50, width=607, height=233)
        self.configure_frame_border(frame)
        return frame
    def __tk_canvas_reports_container(self, parent):
        canvas = tk.Canvas(parent)
        canvas.place(x=10, y=50, width=607, height=233) # this is the containor of reports, IMPORTANT!! IT IS CANVAS!!
        return canvas
    def __tk_scale_slide(self, parent):
        scale = Scale(parent,from_=1, to=4, orient="horizontal")
        scale.place(relx=0.02, rely=0.95, anchor=tk.SW, width=150, height=30)
        return scale


    def report_lists(self, parent, user_name, comment, date, frame_index,order_id):  # this method is to show lots of small frame in a canvas
        frame = Frame(parent)                                               # You can copy it to other place you want
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_user = Label(frame, text=user_name, anchor="center")
        label_user.place(x=5, y=10, width=100, height=30)

        text_comment = tk.Text(frame)
        text_comment.place(x=100, y=10, width=300, height=30)
        text_comment.insert("1.0", comment)
        text_comment.config(state=DISABLED)  # 设置Text小部件为只读
        self.vbar(text_comment, 120, 10, 300, 30, frame)

        label_date = Label(frame, text=date, anchor="center")
        label_date.place(x=400, y=10, width=100, height=30)

        button_deal = Button(frame, text="Check", takefocus=False, command=lambda id=order_id: self.open_detail_page(id))
        button_deal.place(x=500, y=10, width=50, height=30)

        return frame

    def bike_lists(self, parent, frame_index,id, bike_id, start_date, end_date, cost):
        frame = Frame(parent)
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_id = Label(frame, text=id, anchor="center")
        label_id.place(x=5, y=10, width=30, height=30)

        label_type = Label(frame, text=bike_id, anchor="center")
        label_type.place(x=35, y=10, width=70, height=30)

        label_city = Label(frame, text=start_date, anchor="center")
        label_city.place(x=110, y=10, width=80, height=30)

        label_battery = Label(frame, text=end_date, anchor="center")
        label_battery.place(x=230, y=10, width=80, height=30)

        label_date = Label(frame, text=cost, anchor="center")
        label_date.place(x=310, y=10, width=100, height=30)

        # button_check = Button(frame, text="Detail", takefocus=False)
        # button_check.place(x=495, y=10, width=60, height=30)

        return frame

    def show_reports_page(self):
        # disappear the map frame
        self.tk_frame_mapBox.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 2
        self.tk_select_box_type['values'] = ("All", "Unfinished","Done")

        # then show the report canvas,
        # TODO this is test data, real one should be taken by DB
        report_data = db.query_data(Report.getReportByUserId(self.user_id))
        user_name = db.query_data(User.getUserInfo(self.user_id))[0]['user_name']
        print("Displaying reports for User " + user_name + " with ID: " + str(self.user_id))

        for report in report_data:
            report['user_name'] = user_name
            report['comment'] = report_data[0]['message']

        # report_data = [
        #     {"user_name": "User1", "comment": "Report 1 comment", "date": "06/09/2023","order_id": 1},
        #     {"user_name": "User2", "comment": "Report 2 comment", "date": "06/10/2023","order_id": 2},
        #     {"user_name": "User3", "comment": "Report 3 comment", "date": "06/10/2023","order_id": 3},
        #     {"user_name": "User4", "comment": "Report 4 comment", "date": "06/10/2023","order_id": 4},
        #     {"user_name": "User5", "comment": "Report 5 comment", "date": "06/10/2023","order_id": 5},
        #     {"user_name": "User6", "comment": "Report 6 comment", "date": "06/10/2023","order_id": 6},
        #     {"user_name": "User7", "comment": "Report 7 comment", "date": "06/10/2023","order_id": 7},
        # ]


        canvas_height = len(report_data) * 70
        for widget in self.tk_canvas_reports_container.winfo_children():
            widget.destroy() #before show the lists, destroy the remain one first

        self.tk_canvas_reports_container.configure(height=canvas_height,scrollregion=(0, 0, 607, canvas_height))
        self.tk_canvas_reports_container.place(x=10, y=50, width=607, height=233)
        vbar = Scrollbar(self.tk_canvas_reports_container, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)  #create a vbar for canvas first

        frame = Frame(self.tk_canvas_reports_container,width=580,height=canvas_height)
        self.configure_frame_border(frame)
        frame.pack()        # then create a frame inside this canvas
        frame.bind("<Configure>", lambda e: self.tk_canvas_reports_container.configure(
            scrollregion=self.tk_canvas_reports_container.bbox("all")))  # connect the vbar with this frame

        self.tk_canvas_reports_container.create_window((0, 0), window=frame, anchor="nw") # connect the frame with canvas
        self.tk_canvas_reports_container.configure(yscrollcommand=vbar.set)
        vbar.configure(command=self.tk_canvas_reports_container.yview) #apply the vbar

        for index, data in enumerate(report_data):
            self.report_lists(
                frame,
                data["user_name"],
                data["comment"],
                data["date"],
                index,
                data['order_id']
            )                   # put your list inside the frame, NOT THE CANVAS!

    def show_map_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 1

        self.tk_frame_mapBox.place(x=10, y=50, width=607, height=233)

    def show_orders_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_frame_mapBox.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 3
        self.tk_select_box_type['values'] = ("All", "Bike", "Car")

        deal_report_data = db.query_data(Order.getUserOrder(self.user_id))
        print(deal_report_data)
        # deal_report_data = [
        #     {"bike_id": 1,"city":"Glasgow","bike_type":"Bike","battery":95.5,"status":"Using"},
        #     {"bike_id": 2, "city": "Glasgow", "bike_type":"Bike","battery": 15.5, "status": "Unused"},
        #     {"bike_id": 3, "city": "Glasgow", "bike_type": "Car", "battery": 1.5, "status": "Broken"},
        #     {"bike_id": 4, "city": "Glasgow", "bike_type": "Car", "battery": 52.8, "status": "Using"},
        #     {"bike_id": 5, "city": "Glasgow", "bike_type": "Car", "battery": 100.0, "status": "Unused"},
        # ]
        if(self.filter!="All"):
            report_data = [item for item in deal_report_data if item["bike_type"] == self.filter]
        else:
            report_data = deal_report_data## TODO: in fact this is sql's duty

        canvas_height = len(report_data) * 70
        for widget in self.tk_canvas_detailed.winfo_children():
            widget.destroy()

        self.tk_canvas_detailed.configure(height=canvas_height, scrollregion=(0, 0, 607, canvas_height))
        self.tk_canvas_detailed.place(x=10, y=50, width=607, height=233)
        vbar = Scrollbar(self.tk_canvas_detailed, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)  # create a vbar for canvas first

        frame = Frame(self.tk_canvas_detailed, width=580, height=canvas_height)
        self.configure_frame_border(frame)
        frame.pack()  # then create a frame inside this canvas
        frame.bind("<Configure>", lambda e: self.tk_canvas_detailed.configure(
            scrollregion=self.tk_canvas_detailed.bbox("all")))  # connect the vbar with this frame

        self.tk_canvas_detailed.create_window((0, 0), window=frame,
                                                       anchor="nw")  # connect the frame with canvas
        self.tk_canvas_detailed.configure(yscrollcommand=vbar.set)
        vbar.configure(command=self.tk_canvas_detailed.yview)  # apply the vbar

        self.bike_lists(
                frame,
                0,
                "ID",
                "Bike ID",
                "Start date",
                "End Date",
                "Cost"
            )

        for index, data in enumerate(report_data):
            print(index)
            self.bike_lists(
                frame,
                index+1,
                data["id"],
                data["bike_id"],
                data["start_date"],
                data["end_date"],
                data["cost"]
            )  # put your list inside the frame, NOT THE CANVAS!


    def show_info_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_mapBox.place_forget()
        self.now_type = 4

        self.tk_frame_info.place(x=10, y=50, width=607, height=233)

    def open_detail_page(self, order_id):
        from opertor_report_info import ReportPage
        detail_page = ReportPage(order_id)
        detail_page.mainloop()

    def on_combobox_select(self, event):
        selected_value = self.tk_select_box_type.get()
        if(self.now_type==3):
            if selected_value == "All":
                self.filter = "All"
            elif selected_value == "Bike":
                self.filter = "Bike"
            elif selected_value == "Car":
                self.filter = "Car"
            self.show_orders_page()
        elif(self.now_type==2):
            if selected_value == "All":
                self.filter = "All"
            elif selected_value == "Unfinished":
                self.filter = "Unfinished"
            elif selected_value == "Done":
                self.filter = "Done"

if __name__ == "__main__":
    win = Userpage(1)  # you should transfer the user_id to me(with login)
    win.mainloop()