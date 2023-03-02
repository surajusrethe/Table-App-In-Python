#Suraj Usrethe
#This Partical table App takes user input So that People Can Try Different Values As Per Their Need.

import tkinter as tk

# Define function to update total marks
def update_total(*args):
    english_total = 0
    hindi_total = 0
    for i in range(len(data)):
        if data[i][0].get() == 1:
            english_total += int(data[i][2].get())
            hindi_total += int(data[i][3].get())
    english_total_label.config(text=english_total)
    hindi_total_label.config(text=hindi_total)

# Create main window
root = tk.Tk()
root.title("Table with Checkboxes")

# Create border
border = tk.Frame(root, relief="groove", bd=2)
border.pack(padx=10, pady=10)

# Create header labels
tk.Label(border, text="Select").grid(row=0, column=0)
tk.Label(border, text="Name").grid(row=0, column=1)
tk.Label(border, text="English").grid(row=0, column=2)
tk.Label(border, text="Hindi").grid(row=0, column=3)

# Create data rows
data = []
for i in range(6):
    # Create checkbox
    checkbox_var = tk.IntVar()
    checkbox_var.trace("w", update_total)
    checkbox = tk.Checkbutton(border, variable=checkbox_var)
    checkbox.grid(row=i+1, column=0)
    # Create name label
    name_label = tk.Label(border, text="Name "+str(i+1))
    name_label.grid(row=i+1, column=1)
    # Create English entry
    english_entry = tk.Entry(border)
    english_entry.grid(row=i+1, column=2)
    # Create Hindi entry
    hindi_entry = tk.Entry(border)
    hindi_entry.grid(row=i+1, column=3)
    # Add data to list
    data.append((checkbox_var, name_label, english_entry, hindi_entry))

# Create labels to display total marks
tk.Label(border, text="Total").grid(row=len(data)+1, column=1)
english_total_label = tk.Label(border, text="0")
english_total_label.grid(row=len(data)+1, column=2)
hindi_total_label = tk.Label(border, text="0")
hindi_total_label.grid(row=len(data)+1, column=3)

# Add outline to border
border.update()
border_width = sum(border.pack_info()[key] for key in ("ipadx", "padx"))
border_height = sum(border.pack_info()[key] for key in ("ipady", "pady"))
canvas = tk.Canvas(root, width=border.winfo_width()+2*border_width, height=border.winfo_height()+2*border_height, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), outline="black", width=2)

# Start main loop
root.mainloop()