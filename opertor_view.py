import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH, DISABLED, messagebox
from tkinter.ttk import *
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
import db.Report as Report
import db.User as User

class Opertor(tk.Tk):
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
        self.tk_button_DetailButton = self.__tk_button_DetailButton(self.tk_frame_left)
        self.tk_button_InfoButton = self.__tk_button_InfoButton(self.tk_frame_left)

        self.tk_frame_right = self.__tk_frame_right(self)
        self.tk_select_box_type = self.__tk_select_box_type(self.tk_frame_right)
        self.tk_input_search = self.__tk_input_search(self.tk_frame_right)
        self.tk_label_icon = self.__tk_label_icon(self.tk_frame_right)

        self.tk_frame_mapBox = self.__tk_frame_mapBox(self.tk_frame_right)
        self.tk_scale_slide = self.__tk_scale_slide(self.tk_frame_mapBox)

        self.tk_canvas_reports_container = self.__tk_canvas_reports_container(self.tk_frame_right)
        self.tk_canvas_detailed = self.__tk_canvas_detailed(self.tk_frame_right)
        self.tk_frame_info = self.__tk_frame_info(self.tk_frame_right)
        self.show_map_page()  # default showing map pages

    def get_title_name(self,user_id):
        operator_info = db.query_data(User.getUserInfo(self.user_id))
        return "Operator: " + operator_info[0]['user_name']

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
        btn = Button(parent, text="Reports", takefocus=False, command=self.show_reports_page)
        btn.place(x=10, y=90, width=80, height=48)
        return btn
    def __tk_button_DetailButton(self, parent):
        btn = Button(parent, text="Details", takefocus=False, command=self.show_detail_page)
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


    def report_lists(self, parent, user_name, comment, date, frame_index, order_id, report_id):  # this method is to show lots of small frame in a canvas
        frame = Frame(parent)                                               # You can copy it to other place you want
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_user = Label(frame, text=user_name, anchor="center")
        label_user.place(x=5, y=10, width=100, height=30)

        text_comment = tk.Text(frame)
        text_comment.place(x=100, y=10, width=250, height=30)
        text_comment.insert("1.0", comment)
        text_comment.config(state=DISABLED)  # 设置Text小部件为只读
        self.vbar(text_comment, 120, 10, 300, 30, frame)

        date_part = date.split()[0]
        label_date = Label(frame, text=date_part, anchor="center")
        label_date.place(x=360, y=10, width=100, height=30)

        button_deal = Button(frame, text="Check", takefocus=False, command=lambda id=order_id, report=report_id: self.open_detail_page(id,report))
        button_deal.place(x=500, y=10, width=50, height=30)

        return frame

    def bike_lists(self, parent, frame_index,bike_id, bike_type, city, battery,status):
        user_id_dict = db.query_data(Bike.getUserByBikeId(bike_id))
        user_id = user_id_dict[0]['is_use']
        frame = Frame(parent)
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_id = Label(frame, text=bike_id, anchor="center")
        label_id.place(x=5, y=10, width=20, height=30)

        label_type = Label(frame, text=bike_type, anchor="center")
        label_type.place(x=25, y=10, width=30, height=30)

        label_city = Label(frame, text=city, anchor="center")
        label_city.place(x=60, y=10, width=80, height=30)

        label_battery = Label(frame, text=str(battery)+'%', anchor="center")
        label_battery.place(x=150, y=10, width=67, height=30)

        label_date = Label(frame, text=status, anchor="center")
        label_date.place(x=210, y=10, width=100, height=30)

        button_charge = Button(frame, text="Charge", takefocus=False, command=lambda id=bike_id, comment=label_battery, status_label=label_date: self.charge(id, comment, status_label))
        button_charge.place(x=355, y=10, width=60, height=30)

        button_fix = Button(frame, text="Fix", takefocus=False,command=lambda id=bike_id: self.fix(id, label_date))
        button_fix.place(x=425, y=10, width=60, height=30)

        button_check = Button(frame, text="Detail", takefocus=False,command=lambda user=user_id,bike=bike_id:self.open_bike_page(user,bike))
        button_check.place(x=495, y=10, width=60, height=30)

        return frame

    def show_reports_page(self):
        # disappear the map frame
        self.tk_frame_mapBox.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 2
        self.tk_select_box_type['values'] = ("All", "Unfinished","Done")

        if(self.filter=="All"):
            report_data=db.query_data(Report.getAllReport())
        else:
            report_data = db.query_data(Report.getReportByStatus(self.filter))

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
                self.get_username(data['user_id']),
                data["message"],
                data["date"],
                index,
                data['order_id'],
                data['id']
            )                   # put your list inside the frame, NOT THE CANVAS!

    def show_map_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 1

        self.tk_frame_mapBox.place(x=10, y=50, width=607, height=233)

    def show_detail_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_frame_mapBox.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 3
        self.tk_select_box_type['values'] = ("All", "Bike", "Car")

        if(self.filter=="All"):
            deal_report_data=db.query_data(Bike.getAllBike())
        else:
            deal_report_data = db.query_data(Bike.getBikeByTypes(self.filter))

        canvas_height = len(deal_report_data) * 70
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

        for index, data in enumerate(deal_report_data):
            self.bike_lists(
                frame,
                index,
                data["id"],
                data["bike_type"],
                data["city"],
                data["battery"],
                self.show_status_of_bike(data['is_use'],data['is_broken'])
            )  # put your list inside the frame, NOT THE CANVAS!


    def show_info_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_mapBox.place_forget()
        self.now_type = 4

        self.tk_frame_info.place(x=10, y=50, width=607, height=233)

    def charge(self, bike_id, battery_label, status_label):
        battery = float((battery_label["text"])[:-1])
        if status_label["text"] == "Using":
            messagebox.showinfo("Info", "Is been using now!")
        else:
            if battery == 100:
                messagebox.showinfo("Info", "Already full!")
            else:
                battery_label.config(text="100.0%")
                db.insert_or_delete_data(Bike.changeBattery(bike_id))
                messagebox.showinfo("Info", "Completed")

    def fix(self, bike_id, status_label):
        status = status_label["text"]
        if status == "Using":
            messagebox.showinfo("Info", "Is been using now!")
        elif status == "Broken":
            messagebox.showinfo("Info", "Complete!")
            db.insert_or_delete_data(Bike.fix(bike_id))
            status_label.config(text="Unused")
        elif status == "Unused":
            messagebox.showinfo("Info", "It's OK now")

    def open_detail_page(self, order_id,report_id):
        from opertor_report_info import ReportPage
        detail_page = ReportPage(order_id,report_id,self.user_id)
        detail_page.mainloop()

    def open_bike_page(self, user_id,bike_id):
        from bike_info import BikePage
        detail_page = BikePage(user_id,bike_id)
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
            self.show_detail_page()
        elif(self.now_type==2):
            if selected_value == "All":
                self.filter = "All"
            elif selected_value == "Unfinished":
                self.filter = "Unfinished"
            elif selected_value == "Done":
                self.filter = "Done"
            self.show_reports_page()

    def show_status_of_bike(self,is_use,is_broken):
        if is_broken==1:
            return "Broken"
        else:
            if is_use==-1:
                return "Unused"
            else:
                return "Using"

    def get_username(self,user_id):
        user = db.query_data(User.getUserInfo(user_id))
        return user[0]['user_name']

class Opertor_view(Opertor):
    def __init__(self):
        super().__init__(self.user_id)
        self.__event_bind()

    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Opertor(3)  # you should transfer the user_id to me(with login)
    win.mainloop()