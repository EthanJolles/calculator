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


def number_button_input(number):
    ent_number.insert(-1, number)


# set up window
window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)

# term entry frame
frm_entry = tk.Frame(master=window)
ent_number = tk.Entry(master=frm_entry, width=5)
lbl_calculator = tk.Label(master=frm_entry, text="Calculator")
lbl_answer = tk.Label(master=frm_entry, text="answer-placeholder")

# Layout the Entry and Label in frm_entry
# using the .grid() geometry manager
ent_number.grid(row=1, column=0, sticky="w")
lbl_calculator.grid(row=0, column=1, sticky="n", padx=10)
lbl_answer.grid(row=1, column=2, sticky="e")

# buttons
btn_submit = tk.Button(master=frm_entry, text="=", width=2, height=1, bg="black", fg="white", command=return_answer)
btn_three = tk.Button(master=window, text="3", width=2, height=1, bg="black", fg="white",
                      command=number_button_input("3"))
btn_one = tk.Button(master=window, text="1", width=2, height=1, bg="black", fg="white",
                    command=number_button_input("1"))
btn_two = tk.Button(master=window, text="2", width=2, height=1, bg="black", fg="white",
                    command=number_button_input("2"))

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_submit.grid(row=1, column=1, padx=10)
btn_one.grid(row=2, column=0)
btn_two.grid(row=2, column=1)
btn_three.grid(row=2, column=2)

window.mainloop()