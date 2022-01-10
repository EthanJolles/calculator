import tkinter as tk


# Define GUI window
def make_calculator():
    #Set up window
    window = tk.Tk()
    window.title("Calculator")
    window.resizable(width=False,height=False)

    #Term entry frame
    frm_entry = tk.Frame(master=window)
    ent_number = tk.Entry(master=frm_entry, width=10)


    btn_submit = tk.Button(
        text="Submit",
        width=2,
        height=1,
        bg="black",
        fg="white",
    )
    btn_submit.grid(
        row=3,
        column=0,
    )

    btn_submit.pack()
    ent_number.pack()
    window.mainloop()

