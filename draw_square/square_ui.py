import tkinter as tk
from tkinter import ttk
import random

def square(num, canvas, middle_color):
    canvas.delete("all")  # Clear previous drawings
    colors = ["red", "green", "blue", "orange", "purple", "pink"]
    
    cell_size = min(30, 400 // num)  # Adjust cell size based on canvas and square size
    start_x = (400 - num * cell_size) // 2
    start_y = (400 - num * cell_size) // 2

    for i in range(num):
        for j in range(num):
            x = start_x + j * cell_size
            y = start_y + i * cell_size
            
            if i == 0 or i == num-1 or j == 0 or j == num-1:
                color = random.choice(colors)
                canvas.create_text(x + cell_size/2, y + cell_size/2, text="*", fill=color, font=("Arial", cell_size))
            elif 0 < i < num-1 and 0 < j < num-1:
                canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=middle_color, outline="")

def draw_square():
    size = int(size_entry.get())
    middle_color = color_var.get()
    square(size, canvas, middle_color)

# Create main window
root = tk.Tk()
root.title("Colored Square Generator")

# Create and pack widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

size_label = ttk.Label(frame, text="Enter square size:")
size_label.grid(row=0, column=0, sticky=tk.W, pady=5)

size_entry = ttk.Entry(frame, width=10)
size_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
size_entry.insert(0, "5")  # Default value

color_label = ttk.Label(frame, text="Middle color:")
color_label.grid(row=1, column=0, sticky=tk.W, pady=5)

color_var = tk.StringVar(value="light blue")
color_choices = ["light blue", "light green", "light yellow", "light pink"]
color_menu = ttk.Combobox(frame, textvariable=color_var, values=color_choices, state="readonly", width=15)
color_menu.grid(row=1, column=1, sticky=tk.W, pady=5)

draw_button = ttk.Button(frame, text="Draw Square", command=draw_square)
draw_button.grid(row=2, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()