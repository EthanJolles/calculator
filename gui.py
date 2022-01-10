import tkinter as tk

# Define GUI window
def make_calculator():
    window = tk.Tk()
    header = tk.Label(text="Calculator")
    text_box = tk.Entry()

    header.pack()
    text_box.pack()

    window.mainloop()
