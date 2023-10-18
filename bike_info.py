
from tkinter import *
from tkinter.ttk import *
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
import db.Report as Report
import db.User as User
class BikePage(Tk):
    def __init__(self,open_user_id,bike_id):
        super().__init__()
        self.__win()
        self.open_user_id = open_user_id
        self.bike_id = bike_id
        self.title("BikeId: "+str(bike_id))
        self.bike_dict = db.query_data(Bike.getBikeById(bike_id))
        self.user = db.query_data(User.getUserInfo(open_user_id))

        self.tk_frame_frame_left = self.__tk_frame_frame_left(self)
        self.tk_label_Vechine = self.__tk_label_Vechine(self.tk_frame_frame_left)
        self.tk_label_status = self.__tk_label_status(self.tk_frame_frame_left)
        self.tk_label_battery = self.__tk_label_battery(self.tk_frame_frame_left)
        self.tk_text_bike_box = self.__tk_text_bike_box(self.tk_frame_frame_left)
        self.tk_text_status_box = self.__tk_text_status_box(self.tk_frame_frame_left)
        self.tk_text_battery_box = self.__tk_text_battery_box(self.tk_frame_frame_left)
        self.tk_label_min = self.__tk_label_min(self.tk_frame_frame_left)
        self.tk_text_min = self.__tk_text_min(self.tk_frame_frame_left)
        self.tk_frame_frame_right = self.__tk_frame_frame_right(self)
        self.tk_canvas_map = self.__tk_canvas_map(self.tk_frame_frame_right)
        self.tk_label_location = self.__tk_label_location(self.tk_frame_frame_right)
        self.tk_frame_button_different = self.__tk_frame_button_different(self)

    def __win(self):
        # 设置窗口大小、居中
        width = 484
        height = 289
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_frame_frame_left(self, parent):
        frame = Frame(parent, )
        frame.place(x=10, y=10, width=220, height=198)
        return frame

    def __tk_label_Vechine(self, parent):
        label = Label(parent, text="Vehicles:", anchor="center", )
        label.place(x=10, y=10, width=59, height=30)
        return label

    def __tk_label_status(self, parent):
        label = Label(parent, text="Status:", anchor="center", )
        label.place(x=10, y=60, width=59, height=30)
        return label

    def __tk_label_battery(self, parent):
        label = Label(parent, text="Battery:", anchor="center", )
        label.place(x=10, y=110, width=59, height=30)
        return label

    def __tk_text_bike_box(self, parent):
        text = Text(parent)
        text.insert("1.0",self.bike_dict[0]['bike_type'])
        text.place(x=78, y=10, width=136, height=31)
        return text

    def __tk_text_status_box(self, parent):
        text = Text(parent)
        status = self.show_status_of_bike(self.bike_dict[0]['is_use'],self.bike_dict[0]['is_broken'])
        text.insert("1.0", status)
        text.place(x=79, y=60, width=135, height=31)
        return text

    def __tk_text_battery_box(self, parent):
        text = Text(parent)
        text.insert("1.0", str(self.bike_dict[0]['battery'])+"%")
        text.place(x=79, y=110, width=135, height=31)
        return text

    def __tk_label_min(self, parent):
        label = Label(parent, text="Total(min):", anchor="center", )
        label.place(x=5, y=158, width=64, height=30)
        return label

    def __tk_text_min(self, parent):
        text = Text(parent)
        text.insert("1.0", self.bike_dict[0]['total_minutes'])
        text.place(x=77, y=158, width=135, height=31)
        return text

    def __tk_frame_frame_right(self, parent):
        frame = Frame(parent, )
        frame.place(x=250, y=10, width=220, height=268)
        return frame

    def __tk_canvas_map(self, parent):
        canvas = Canvas(parent)
        canvas.place(x=12, y=10, width=199, height=195)
        return canvas

    def __tk_label_location(self, parent):
        location = "longitude: {}, latitude: {}".format(self.bike_dict[0]['longitude'],self.bike_dict[0]['latitude'])
        label = Label(parent, text=location, anchor="center", )
        label.place(x=10, y=214, width=200, height=38)
        return label

    def __tk_frame_button_different(self, parent):
        frame = Frame(parent, )
        if self.user[0]['user_type'] == 'User':
            if self.bike_dict[0]['is_use'] == self.open_user_id:
                return_button = Button(frame, text="Return", command=self.return_bike)
                return_button.grid(row=0, column=0, padx=10)
            else:
                rent_button = Button(frame, text="Rent", command=self.rent_bike)
                rent_button.grid(row=0, column=0, padx=10)
            cancel_button = Button(frame, text="Cancel", command=self.cancel_bike)
            cancel_button.grid(row=0, column=1, padx=10)

        elif self.user[0]['user_type'] == 'Operator':
            charge_button = Button(frame, text="Charge", command=self.charge_bike, width=7)
            fix_button = Button(frame, text="Fix", command=self.fix_bike, width=7)
            move_button = Button(frame, text="Move", command=self.move_bike, width=7)
            charge_button.grid(row=0, column=0, padx=5)
            fix_button.grid(row=0, column=1, padx=5)
            move_button.grid(row=0, column=2, padx=5)

        elif self.user[0]['user_type'] == 'Manager':
            add_same_button = Button(frame, text="Add Same", command=self.add_same_bike)
            delete_button = Button(frame, text="Delete", command=self.delete_bike)
            add_same_button.grid(row=0, column=0, padx=10)
            delete_button.grid(row=0, column=1, padx=10)

        frame.place(x=11, y=223, width=218, height=54)
        return frame

    def show_status_of_bike(self,is_use,is_broken):
        if is_broken==1:
            return "Broken"
        else:
            if is_use==-1:
                return "Unused"
            else:
                user = db.query_data(User.getUserInfo(is_use))
                return "Used By "+user[0]['user_name']

    def rent_bike(self):
        # rent logic(User)
        pass

    def return_bike(self):
        # return logic(User)
        pass

    def cancel_bike(self):
        # cancel (User)
        pass

    def charge_bike(self):
        # charge (Operator)
        pass

    def fix_bike(self):
        # fix (Operator)
        pass

    def move_bike(self):
        # move (Operator)
        pass

    def add_same_bike(self):
        # add numerous new bikes with same type (Manager)
        pass

    def delete_bike(self):
        # delete this one (Manager)
        pass

class Win(BikePage):
    def __init__(self):
        super().__init__(self.open_user_id,self.bike_id)
        self.__event_bind()
    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = BikePage(1,1)
    win.mainloop()