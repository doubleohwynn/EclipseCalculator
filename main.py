import customtkinter as ctk
import os
import ctypes
import sys


ctk.set_appearance_mode("dark")


ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    "EclipseCalculator"
)


window = ctk.CTk()

window.title("Eclipse Calculator")
window.configure(fg_color="#000000")
window.resizable(False, False)
window.geometry("590x560")


# =====================
# APP ICON
# =====================

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))


icon_path = os.path.join(
    base_path,
    "eclipse.ico"
)


try:
    window.iconbitmap(icon_path)
except Exception:
    pass



history_visible = True


# Fonts

main_font = ("Arial", 24, "bold")
button_font = ("Arial", 22, "bold")



# Main container

main_frame = ctk.CTkFrame(
    window,
    fg_color="#000000"
)

main_frame.pack(
    expand=True,
    fill="both",
    padx=8,
    pady=15
)



# Calculator panel

calc_frame = ctk.CTkFrame(
    main_frame,
    corner_radius=25,
    fg_color="#000000",
    width=360,
    height=500
)

calc_frame.pack(side="left")

calc_frame.pack_propagate(False)



# History panel

history_frame = ctk.CTkFrame(
    main_frame,
    corner_radius=25,
    fg_color="#000000",
    width=220,
    height=500
)

history_frame.pack(side="right")

history_frame.pack_propagate(False)



def toggle_history():

    global history_visible

    if history_visible:

        history_frame.pack_forget()

        history_button.configure(
            text="Show History"
        )

        history_visible = False

        window.geometry("390x560")


    else:

        history_frame.pack(
            side="right"
        )

        history_button.configure(
            text="Hide History"
        )

        history_visible = True

        window.geometry("590x560")




history_button = ctk.CTkButton(
    calc_frame,
    text="Hide History",
    width=120,
    height=32,
    corner_radius=20,
    command=toggle_history,
    font=("Arial",14,"bold"),
    fg_color="#050505",
    border_width=1,
    border_color="#666666",
    hover_color="#151515"
)

history_button.pack(
    anchor="w",
    pady=5,
    padx=5
)



# Display

display = ctk.CTkEntry(
    calc_frame,
    width=320,
    height=70,
    font=main_font,
    corner_radius=20,
    fg_color="#111111",
    text_color="#ffffff",
    border_width=0
)

display.pack(
    pady=15
)



# History

history = ctk.CTkTextbox(
    history_frame,
    width=190,
    height=440,
    corner_radius=20,
    fg_color="#111111",
    font=("Arial",15,"bold"),
    border_width=0
)

history.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

history.configure(
    state="disabled"
)



def press(value):
    display.insert("end", value)



def clear():
    display.delete(0,"end")



def backspace():

    text = display.get()

    display.delete(0,"end")
    display.insert(0,text[:-1])



def add_history(text):

    history.configure(
        state="normal"
    )

    history.insert(
        "end",
        text
    )

    history.configure(
        state="disabled"
    )



def calculate():

    try:

        expression = display.get()

        expression = expression.replace("×","*")
        expression = expression.replace("÷","/")

        result = eval(expression)

        add_history(
            f"{display.get()} = {result}\n"
        )

        display.delete(
            0,
            "end"
        )

        display.insert(
            0,
            result
        )


    except:

        display.delete(
            0,
            "end"
        )

        display.insert(
            0,
            "Error"
        )





buttons = [

    ("C",clear),
    ("⌫",backspace),
    ("÷",lambda:press("÷")),
    ("×",lambda:press("×")),

    ("7",lambda:press("7")),
    ("8",lambda:press("8")),
    ("9",lambda:press("9")),
    ("-",lambda:press("-")),

    ("4",lambda:press("4")),
    ("5",lambda:press("5")),
    ("6",lambda:press("6")),
    ("+",lambda:press("+")),

    ("1",lambda:press("1")),
    ("2",lambda:press("2")),
    ("3",lambda:press("3")),
    ("=",calculate),

    ("0",lambda:press("0")),
    (".",lambda:press("."))

]



buttons_frame = ctk.CTkFrame(
    calc_frame,
    fg_color="#000000"
)

buttons_frame.pack()



row = 0
col = 0



for text, command in buttons:

    button = ctk.CTkButton(
        buttons_frame,
        text=text,
        command=command,
        width=70,
        height=55,
        corner_radius=30,
        font=button_font,
        fg_color="#000000",
        border_width=1,
        border_color="#666666",
        hover_color="#151515"
    )

    button.grid(
        row=row,
        column=col,
        padx=6,
        pady=6
    )

    col += 1

    if col == 4:

        col = 0
        row += 1



window.mainloop()