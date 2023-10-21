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

# Connect to the SQLite database
conn = sqlite3.connect('../database.db')
cursor = conn.cursor()
# Define a function to generate the report and display graphs
def generate_report_and_graphs():
    # Retrieve user input (start_date and end_date) from GUI elements
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Query the database for vehicle activities within the defined time period
    query = """
        SELECT city, COUNT(*) FROM "order" 
        GROUP BY city
    """
    #WHERE start_date >= ? AND end_date <= ?
    cursor.execute(query)
    results = cursor.fetchall()

    # Display the results in the text box
    report_text.delete(1.0, tk.END)  # Clear previous report
    for row in results:
        report_text.insert(tk.END, f"City: {row[0]}, Count: {row[1]}\n")

    # Generate and display graphs
    display_bar_chart()
    display_pie_chart()
    display_line_chart()
    display_scatter_plot()
    display_histogram()

# Define functions to create different types of graphs
def display_bar_chart():
    cursor.execute("SELECT city, COUNT(*) FROM report GROUP BY city")
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    counts = [row[1] for row in results]

    fig, ax = plt.subplots()
    ax.bar(cities, counts)

    ax.set_xlabel('Cities')
    ax.set_ylabel('Count')
    ax.set_title('Report Counts by City')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def display_pie_chart():
    cursor.execute("SELECT city, COUNT(*) FROM report GROUP BY city")
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    counts = [row[1] for row in results]

    fig, ax = plt.subplots()
    ax.pie(counts, labels=cities, autopct='%1.1f%%', startangle=90)

    ax.axis('equal')
    ax.set_title('Report Distribution by City')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def display_line_chart():
    x_values = list(range(1, 11))
    y_values = [random.randint(1, 10) for _ in range(10)]

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o')

    ax.set_xlabel('X Values')
    ax.set_ylabel('Y Values')
    ax.set_title('Line Chart Example')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def display_scatter_plot():
    x_values = [random.randint(1, 10) for _ in range(10)]
    y_values = [random.randint(1, 10) for _ in range(10)]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, color='b', marker='o')

    ax.set_xlabel('X Values')
    ax.set_ylabel('Y Values')
    ax.set_title('Scatter Plot Example')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def display_histogram():
    data = [random.randint(1, 10) for _ in range(100)]

    fig, ax = plt.subplots()
    ax.hist(data, bins=10, color='b', alpha=0.7)

    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram Example')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main window
root = tk.Tk()
root.title("Vehicle Activity Report Generator")

# Create and configure the GUI elements
label_start_date = ttk.Label(root, text="Start Date (YYYY-MM-DD):")
label_start_date.grid(column=0, row=0, padx=10, pady=10)

start_date_entry = ttk.Entry(root)
start_date_entry.grid(column=1, row=0, padx=10, pady=10)

label_end_date = ttk.Label(root, text="End Date (YYYY-MM-DD):")
label_end_date.grid(column=0, row=1, padx=10, pady=10)

end_date_entry = ttk.Entry(root)
end_date_entry.grid(column=1, row=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Report and Display Graphs", command=generate_report_and_graphs)
generate_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

report_text = tk.Text(root, height=10, width=50)
report_text.grid(columnspan=2, row=3, padx=10, pady=10)

# Create a frame to hold the graphs
graph_frame = ttk.Frame(root)
graph_frame.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
