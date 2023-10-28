import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, BOTH, DISABLED, messagebox,simpledialog
from tkinter.ttk import *
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
from PIL import Image, ImageTk
import db.Report as Report
import db.User as User

class Userpage(tk.Tk):
    def __init__(self,user_id):
        super().__init__()
        self.__win()

        self.user_id = user_id
        self.now_type = 1
        self.title(self.get_title_name())
        self.filter = "All"
        self.city = self.get_city()

        self.panning = False
        self.default_map_x = 0
        self.default_map_y = 0
        self.last_x = 0
        self.last_y = 0
        self.bike_count = 0

        self.tk_frame_left = self.__tk_frame_left(self)

        self.tk_button_MainButton = self.__tk_button_MainButton(self.tk_frame_left)
        self.tk_button_ReportButton = self.__tk_button_ReportButton(self.tk_frame_left)
        self.tk_button_OrdersButton = self.__tk_button_OrdersButton(self.tk_frame_left)
        self.tk_button_InfoButton = self.__tk_button_InfoButton(self.tk_frame_left)

        self.tk_frame_right = self.__tk_frame_right(self)
        self.tk_select_box_type = self.__tk_select_box_type(self.tk_frame_right)

        self.tk_label_icon = self.__tk_label_icon(self.tk_frame_right)
        self.tk_label_wallet = self.__tk_label_wallet(self.tk_frame_right)
        self.tl_button_money = self.__tk_button_money(self.tk_frame_right)

        self.tk_canvas_mapBox = self.__tk_canvas_mapBox(self.tk_frame_right)

        self.tk_canvas_reports_container = self.__tk_canvas_reports_container(self.tk_frame_right)
        self.tk_canvas_detailed = self.__tk_canvas_detailed(self.tk_frame_right)
        self.tk_frame_info = self.__tk_frame_info(self.tk_frame_right)
        self.show_map_page()  # default showing map pages

    def get_title_name(self):
        operator_info = db.query_data(User.getUserInfo(self.user_id))
        return "User: " + operator_info[0]['user_name']
    def get_money(self):
        user = db.query_data(User.getUserInfo(self.user_id))
        return user[0]['wallet']
    def add_money(self):
        x = simpledialog.askinteger("Enter New X", "Enter the new X coordinate:")
        now = float(self.tk_label_wallet['text'])
        self.tk_label_wallet.configure(text=x+now)
        db.insert_or_delete_data(User.addMoney(self.user_id,x))
        return
    def get_city(self):
        operator_info = db.query_data(User.getUserInfo(self.user_id))
        return operator_info[0]['city']

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
        sw = 15
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
        label = Label(parent, text="Your wallet:", anchor="center", )
        label.place(x=20, y=10, width=100, height=30)
        return label

    def __tk_label_wallet(self,parent):
        label = Label(parent, text=self.get_money(), anchor="center", )
        label.place(x=120, y=10, width=100, height=30)
        return label
    def __tk_button_money(self,parent):
        btn = Button(parent, text="Add", takefocus=False, command=self.add_money)
        btn.place(x=250, y=10, width=50, height=30)
        return btn

    def __tk_canvas_mapBox(self, parent):
        canvas = tk.Canvas(parent)
        canvas.place(x=10, y=50, width=607, height=233)
        return canvas
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

    def show_map(self):
        self.map_image = Image.open(self.city+".jpg")  # Replace with your map image path
        self.map_width, self.map_height = self.map_image.size
        new_width = int(self.map_width)
        new_height = int(self.map_height)
        resized_image = self.map_image.resize((new_width, new_height))
        self.photo = ImageTk.PhotoImage(resized_image)
        # Clear the canvas and display the resized map
        self.tk_canvas_mapBox.delete("all")
        self.map_item = self.tk_canvas_mapBox.create_image(self.default_map_x, self.default_map_y, image=self.photo,
                                                           anchor="nw")  # TODO I will do with pos

        ids = []
        if (self.filter == "All"):
            data = db.query_data(Bike.getAllBike(self.city))
        else:
            data = db.query_data(Bike.getBikeByTypes(self.filter,self.city))
        for item in data:
            x = item['X'] + self.default_map_x
            y = item['Y'] + self.default_map_y
            id = item['id']
            ids.append(id)
            color = Bike.getColorForBike(item['bike_type'])
            if(item['is_use'])==self.user_id:
                color='green'
            self.add_marker(x, y, id, color)
        self.tk_canvas_mapBox.bind("<ButtonPress-1>", self.on_map_click)
        # id_list is used in the lambda function below,this red line may due to edit's error, does't matter
        self.tk_canvas_mapBox.bind("<B1-Motion>", lambda event, id_list=ids: self.on_map_drag(event, id_list))
        # Bind click events for markers
        self.bike_count = len(data)
        for i in ids:
            self.tk_canvas_mapBox.tag_bind('marker_%s' % i, '<ButtonPress-1>',
                                           lambda evt, id=i: self.open_bike_page(self.user_id, id))

    def on_map_click(self, event):
        self.panning = True
        self.last_x = event.x
        self.last_y = event.y

    def on_map_drag(self, event, id_list):
        if self.panning:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            self.last_x = event.x
            self.last_y = event.y

            # Calculate the current map position
            current_x, current_y = self.tk_canvas_mapBox.coords(self.map_item)
            new_x = current_x + dx
            new_y = current_y + dy
            self.default_map_x = new_x
            self.default_map_y = new_y

            # Calculate the boundaries
            min_x = 607 - self.map_width
            min_y = 233 - self.map_height

            # Ensure the new position is within bounds
            new_x = max(min_x, min(0, new_x))
            new_y = max(min_y, min(0, new_y))

            self.tk_canvas_mapBox.move(self.map_item, new_x - current_x, new_y - current_y)

            # Update marker positions
            for i in id_list:
                x1, y1, x2, y2 = self.tk_canvas_mapBox.coords('marker_%s' % i)  ##TODO

                self.tk_canvas_mapBox.coords('marker_%s' % i, x1 + new_x - current_x, y1 + new_y - current_y,
                                             x2 + new_x - current_x, y2 + new_y - current_y)

    def add_marker(self, x, y, id, color):
        # red
        self.tk_canvas_mapBox.coords('marker_%s' % id, x - 5, y - 5, x + 5, y + 5)
        self.tk_canvas_mapBox.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color, tag='marker_%s' % id)


    def report_lists(self, parent, user_name, comment, date, frame_index,order_id):  # this method is to show lots of small frame in a canvas
        frame = Frame(parent)                                               # You can copy it to other place you want
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_user = Label(frame, text=user_name, anchor="center")
        label_user.place(x=5, y=10, width=100, height=30)

        text_comment = tk.Text(frame)
        text_comment.place(x=100, y=10, width=200, height=30)
        text_comment.insert("1.0", comment)
        text_comment.config(state=DISABLED)
        self.vbar(text_comment, 120, 10, 200, 30, frame)

        date_part = date.split()[0]
        label_date = Label(frame, text=date_part, anchor="center")
        label_date.place(x=300, y=10, width=100, height=30)

        label_order = Label(frame, text="Order Id: "+str(order_id), anchor="center")
        label_order.place(x=400, y=10, width=100, height=30)

        return frame

    def bike_lists(self, parent, frame_index,id, bike_id, start_date, end_date, cost,order_id):
        frame = Frame(parent)
        frame.place(x=5, y=10 + frame_index * 60, width=570, height=50)
        frame.configure(style="My.TFrame")

        label_id = Label(frame, text=id, anchor="center")
        label_id.place(x=5, y=10, width=30, height=30)

        label_type = Label(frame, text=bike_id, anchor="center")
        label_type.place(x=35, y=10, width=70, height=30)

        start_date_part = start_date.split()[0]
        label_city = Label(frame, text=start_date_part, anchor="center")
        label_city.place(x=110, y=10, width=70, height=30)

        if(end_date!=None):
            end_date_part = end_date.split()[0]
        else:
            end_date_part = None
        label_battery = Label(frame, text=end_date_part, anchor="center")
        label_battery.place(x=220, y=10, width=70, height=30)

        label_date = Label(frame, text=cost, anchor="center")
        label_date.place(x=290, y=10, width=100, height=30)

        if(order_id!=-1 and end_date!=None):
            button_deal = Button(frame, text="Report", takefocus=False, command=lambda order=order_id, bike=bike_id: self.report_question(order_id,bike_id))
            button_deal.place(x=400, y=10, width=50, height=30)

        return frame

    def show_reports_page(self):
        # disappear the map frame
        self.tk_canvas_mapBox.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 2
        self.tk_select_box_type['values'] = ("All", "Unfinished","Done")

        if(self.filter=="All"):
            report_data = db.query_data(Report.getReportByUserId(self.user_id))
        else:
            report_data = db.query_data(Report.getReportByStatusAndUserId(self.filter,self.user_id))

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
                data["problem_type"],
                data["message"],
                data["date"],
                index,
                data['order_id']
            )                   # put your list inside the frame, NOT THE CANVAS!

    def show_map_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 1
        self.tk_select_box_type['values'] = ("All", "Bike", "Car")

        self.tk_canvas_mapBox.place(x=10, y=50, width=607, height=233)
        self.show_map()

    def show_orders_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_mapBox.place_forget()
        self.tk_frame_info.place_forget()
        self.now_type = 3
        self.tk_select_box_type['values'] = ("All")

        report_data = db.query_data(Order.getUserOrder(self.user_id))

        canvas_height = (len(report_data)+1) * 70
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
                "Cost",
                -1
            )

        for index, data in enumerate(report_data):
            self.bike_lists(
                frame,
                index+1,
                data["id"],
                data["bike_id"],
                data["start_date"],
                data["end_date"],
                data["cost"],
                data["id"]
            )  # put your list inside the frame, NOT THE CANVAS!

    def show_info_page(self):
        self.tk_canvas_reports_container.place_forget()
        self.tk_canvas_detailed.place_forget()
        self.tk_canvas_mapBox.place_forget()
        self.now_type = 4

        self.tk_frame_info.place(x=10, y=50, width=607, height=233)
        labels = ["UserName:", "Email:", "Phone:", "City:", "Wallet:"]
        keys=["user_name","email","phone","city","wallet"]
        user_info = db.query_data(User.getUserInfo(self.user_id))

        for i, label_text in enumerate(labels):
            label = tk.Label(self.tk_frame_info, text=label_text)
            label.place(x=120, y=8 + i * 30, width=100, height=30)

            text = tk.Text(self.tk_frame_info)
            text.insert("1.0", user_info[0][keys[i]])
            text.config(state=DISABLED)
            text.place(x=240, y=10 + i * 30, width=200, height=30)
            self.vbar(text, 240, 8 + i * 30, 200, 30, self.tk_frame_info)

        button_deal = Button(self.tk_frame_info, text="Logout", takefocus=False,command=self.logout)
        button_deal.place(x=280, y=180, width=50, height=30)

    def open_bike_page(self, user_id,bike_id):
        from bikeInfo import BikePage
        detail_page = BikePage(user_id,bike_id)
        detail_page.mainloop()

    def report_question(self,order, bike):
        from userReportInfo import NewReport
        newReport = NewReport(self.user_id,order,bike)
        newReport.mainloop()

    def on_combobox_select(self, event):
        selected_value = self.tk_select_box_type.get()
        if(self.now_type==3 or self.now_type==1):
            if selected_value == "All":
                self.filter = "All"
            elif selected_value == "Bike":
                self.filter = "Bike"
            elif selected_value == "Car":
                self.filter = "Car"
            if(self.now_type==3):
                self.show_orders_page()
            elif(self.now_type==1):
                self.show_map_page()
        elif(self.now_type==2):
            if selected_value == "All":
                self.filter = "All"
            elif selected_value == "Unfinished":
                self.filter = "Unfinished"
            elif selected_value == "Done":
                self.filter = "Done"
            self.show_reports_page()
    def logout(self):
        self.destroy()
        from log import Login
        x = Login()
        x.run()

if __name__ == "__main__":
    win = Userpage(1)  # you should transfer the user_id to me(with login)
    win.mainloop()