import tkinter as tk

def button_click(item):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, str(current) + str(item))

def button_clear():
    entry_display.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry_display.get()))
        entry_display.delete(0, tk.END)
        entry_display.insert(0, result)
    except ZeroDivisionError:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Div by Zero Error")
    except Exception:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Error")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x420")
root.resizable(False, False)
root.configure(bg="#f0f0f0")


entry_display = tk.Entry(root, font=("Arial", 24), bg="#e8e8e8", fg="black", justify="right")
entry_display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

btn_font = ("Arial", 16, "bold")
btn_bg = "#ffffff"


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=btn_font, bg="#4CAF50", fg="black", command=button_equal, height=2, width=5)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=btn_font, bg="#f44336", fg="black", command=button_clear, height=2, width=5)
    elif text in ['/', '*', '-', '+']:
        btn = tk.Button(root, text=text, font=btn_font, bg="#ffeb3b", fg="black", command=lambda t=text: button_click(t), height=2, width=5)
    else:
        btn = tk.Button(root, text=text, font=btn_font, bg=btn_bg, fg="black", command=lambda t=text: button_click(t), height=2, width=5)
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()