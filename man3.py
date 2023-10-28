import tkinter as tk
from tkinter import ttk
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
import db.Report as Report
import db.User as User

#Establish Database connection
openconn = sqlite3.connect('db/database.db')
dbc = openconn.cursor()

#Creating Data_Visualisation Graphs 

#Graph 1: Customer Distribution over cities of Scotland 

def disp_bar_chart():

    

    for w in gframe.winfo_children():
        w.destroy()

    dbc.execute("SELECT city, COUNT(*) FROM user where user_type = 'User' GROUP BY city")
    retrived_detail = dbc.fetchall()

    cities = [row[0] for row in retrived_detail]
    counts = [row[1] for row in retrived_detail]

    fig_plot, x_data = plt.subplots(figsize=(5, 4))
    x_data.bar(cities, counts)

    x_data.set_xlabel('Scotland Cities')
    x_data.set_ylabel('Number of Users')
    x_data.set_title('Distribution of our users over scotland')

    canvas = FigureCanvasTkAgg(fig_plot, master=gframe)
    canvas.draw()
    canvas.get_tk_widget().pack()

#Graph 2: bike types vs cities distribution 

def disp_gbar_chart():
    for w2 in gframe.winfo_children():
        w2.destroy()

    dbc.execute("""
        SELECT city, bike_type, COUNT(*) 
        FROM Bike 
        GROUP BY city, bike_type
    """)
    res2 = dbc.fetchall()

    city_details = set(row[0] for row in res2)
    bike_typs = set(row[1] for row in res2)

    data = {city: {bike_type: 0 for bike_type in bike_typs} for city in city_details}

    for row in res2:
        city, bike_type, count = row
        data[city][bike_type] = count

    #Data for graph building
    city_labels = list(city_details)
    bike_type_labels = list(bike_typs)
    counts = [[data[city][bike_type] for bike_type in bike_type_labels] for city in city_labels]

    #x range definition
    x = range(len(city_labels))

    #width definition 
    width = 0.2  

    #grouped bar chart creation 
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    for i, bike_type in enumerate(bike_type_labels):
        ax2.bar([pos + i*width for pos in x], [count[i] for count in counts], width, label=f'{bike_type} Bikes')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax2.set_xlabel('Cities')
    ax2.set_ylabel('Count')
    ax2.set_title('Most used vehicle types with respect to cities')
    ax2.set_xticks([pos + width for pos in x])
    ax2.set_xticklabels(city_labels)
    ax2.legend()

    canvas = FigureCanvasTkAgg(fig2, master=gframe)
    canvas.draw()
    canvas.get_tk_widget().pack()


#Graph3 :Income generated over cities 
def revenue_pie_chart():

    for w3 in gframe.winfo_children():
        w3.destroy()


    dbc.execute("""
        SELECT city, SUM(cost) 
        FROM "order" 
        GROUP BY city
    """)
    res3 = dbc.fetchall()

    # Extract city names and corresponding revenues
    cities3 = [row[0] for row in res3]
    revenues3 = [row[1] for row in res3]


    max_revenue_index = revenues3.index(max(revenues3))

    labels = [f"{city}" if i == max_revenue_index else city for i, city in enumerate(cities3)]

    #Pie Chart creation 
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    ax3.pie(revenues3, labels=labels, autopct='%1.1f%%', startangle=90)

    ax3.axis('equal')
    ax3.set_title('Revenue Distribution over Scotland')

    # Embed the pie chart in the Tkinter window
    canvas = FigureCanvasTkAgg(fig3, master=gframe)
    canvas.draw()
    canvas.get_tk_widget().pack()

#Graph4 :The relevance between the bike type and cities when it comes to vehicle damage 
def disp_broken_bikes_cities():

    for w4 in gframe.winfo_children():
        w4.destroy()
   
    dbc.execute("""
        SELECT city, bike_type, COUNT(*) 
        FROM Bike 
        WHERE is_broken = 1 
        GROUP BY city, bike_type
    """)
    res4 = dbc.fetchall()

    cities4 = set(row[0] for row in res4)
    bike_typs4 = set(row[1] for row in res4)

    data = {city: {bike_type: 0 for bike_type in bike_typs4} for city in cities4}

    for row in res4:
        city, bike_type, count = row
        data[city][bike_type] = count


    city_labels = list(cities4)
    bike_type_labels = list(bike_typs4)
    counts = [[data[city][bike_type] for bike_type in bike_type_labels] for city in city_labels]


    x = range(len(city_labels))


    width = 0.2  # Adjust as needed


    fig4, ax4 = plt.subplots(figsize=(5, 4))
    for i, bike_type in enumerate(bike_type_labels):
        ax4.bar([pos + i*width for pos in x], [count[i] for count in counts], width, label=f'{bike_type} Bikes')


    ax4.set_xlabel('Cities')
    ax4.set_ylabel('Count of Broken Bikes')
    ax4.set_title('Relevance between Broken Bike types and locations ')
    ax4.set_xticks([pos + width for pos in x])
    ax4.set_xticklabels(city_labels)
    ax4.legend()

    canvas = FigureCanvasTkAgg(fig4, master=gframe)
    canvas.draw()
    canvas.get_tk_widget().pack()

#Graph 5 : Number of orders placed by each user
def disp_orders_by_each():
    for w5 in gframe.winfo_children():
        w5.destroy()
   
    dbc.execute("""
        SELECT user_id, COUNT(*) as num_orders
        FROM "order"
        GROUP BY user_id;
    """)
    res5 = dbc.fetchall()
    act_user_id = [row[0] for row in res5]
    no_orders = [row[1] for row in res5]


    active_most = act_user_id[no_orders.index(max(no_orders))]

    fig5, ax5 = plt.subplots()
    ax5.bar(act_user_id, no_orders)
    ax5.set_xlabel('User ID')
    ax5.set_ylabel('Number of Orders')
    ax5.set_title('Most Active User')
    ax5.text(active_most, max(no_orders), f'Top Active User: {active_most}', ha='left', va='top')


    # Create a canvas and display the plot in the existing gframe
    canvas = FigureCanvasTkAgg(fig5, master=gframe)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Create the main window
win = tk.Tk()
win.title("Manager Report Dashboard")
win.geometry("1000x1000")

# Create and configure the GUI elements
#label_start_date = ttk.Label(win, text="Start Date (YYYY-MM-DD):")
#label_start_date.grid(column=0, row=0, padx=10, pady=10)

#start_date_entry = ttk.Entry(win)
#start_date_entry.grid(column=1, row=0, padx=10, pady=10)

#label_end_date = ttk.Label(win, text="End Date (YYYY-MM-DD):")
#label_end_date.grid(column=0, row=1, padx=10, pady=10)

#end_date_entry = ttk.Entry(win)
#end_date_entry.grid(column=1, row=1, padx=10, pady=10)

# Retrieve user input (start_date and end_date) from GUI elements
#sdate = start_date_entry.get()
#edate = end_date_entry.get()

b1 = ttk.Button(win, text="User dist over cities", command=disp_bar_chart)
b1.grid(column=0, row=2, padx=10, pady=10)

b2 = ttk.Button(win, text="Biketypes vs cities used", command=disp_gbar_chart)
b2.grid(column=1, row=2, padx=10, pady=10)

b3 = ttk.Button(win, text="Revenue from each city", command=revenue_pie_chart)
b3.grid(column=2, row=2, padx=10, pady=10)

b4 = ttk.Button(win, text="Broken bikes vs Cities", command=disp_broken_bikes_cities)
b4.grid(column=3, row=2, padx=10, pady=10)

b5 = ttk.Button(win, text="Most active users inference", command=disp_orders_by_each)
b5.grid(column=4, row=2, padx=10, pady=10)





#report_text = tk.Text(win, height=10, width=50)
#report_text.grid(columnspan=2, row=3, padx=10, pady=10)

# Create a frame to hold the graphs
gframe = ttk.Frame(win)
gframe.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
win.mainloop()
