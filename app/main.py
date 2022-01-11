import tkinter as tk
import operations


def return_answer():
    """Convert value fed into the application into a split
    string and then feeds it into math(), outputs answer to lbl_answer
    """
    term_input = ent_number.get()
    string_term_input = str(term_input)
    split_term_input = string_term_input.split()
    lbl_answer["text"] = operations.math(float(split_term_input[0]), split_term_input[1], float(split_term_input[2]))
    print(f"{split_term_input} = {lbl_answer['text']}")


# set up window
window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)


# term entry frame
frm_entry = tk.Frame(master=window)
frm_entry.grid(row=0)

ent_number = tk.Entry(master=frm_entry, width=30)
ent_number.grid(row=1, column=0, pady=5, sticky=tk.E + tk.W)

# lbl_calculator = tk.Label(master=frm_entry, text="Calculator")
# lbl_calculator.grid(row=0, padx=10, sticky=tk.E + tk.W)


# grid of buttons frame
frm_buttons = tk.Frame(master=window)
frm_buttons.grid(row=1)

# row one
btn_seven = tk.Button(master=frm_buttons, text="7", width=8, height=1, bg="black", fg="white")
btn_seven.grid(row=2, column=0, padx=10)

btn_eight = tk.Button(master=frm_buttons, text="8", width=8, height=1, bg="black", fg="white")
btn_eight.grid(row=2, column=1)

btn_nine = tk.Button(master=frm_buttons, text="9", width=8, height=1, bg="black", fg="white")
btn_nine.grid(row=2, column=2)

# row two
btn_four = tk.Button(master=frm_buttons, text="4", width=8, height=1, bg="black", fg="white")
btn_four.grid(row=3, column=0)

btn_five = tk.Button(master=frm_buttons, text="5", width=8, height=1, bg="black", fg="white")
btn_five.grid(row=3, column=1)

btn_six = tk.Button(master=frm_buttons, text="6", width=8, height=1, bg="black", fg="white")
btn_six.grid(row=3, column=2)

# row three
btn_one = tk.Button(master=frm_buttons, text="1", width=8, height=1, bg="black", fg="white")
btn_one.grid(row=4, column=0)

btn_two = tk.Button(master=frm_buttons, text="2", width=8, height=1, bg="black", fg="white")
btn_two.grid(row=4, column=1)

btn_three = tk.Button(master=frm_buttons, text="3", width=8, height=1, bg="black", fg="white")
btn_three.grid(row=4, column=2)

# row four
btn_zero = tk.Button(master=frm_buttons, text="0", width=8, height=1, bg="black", fg="white")
btn_zero.grid(row=5, column=0)

btn_point = tk.Button(master=frm_buttons, text=".", width=8, height=1, bg="black", fg="white")
btn_point.grid(row=5, column=1)

btn_submit = tk.Button(master=frm_buttons, text="=", width=8, height=1, bg="black", fg="white", command=return_answer)
btn_submit.grid(row=5, column=2)


# results frame
frm_results = tk.Frame(master=window)
frm_results.grid(row=2)

lbl_answer = tk.Label(master=frm_results, text="answer goes here")
lbl_answer.grid(row=6)

window.mainloop()
