from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    # Calculate minutes and seconds based off of total seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Select canvas then the attribute of canvas that we want to change
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label for Pomodoro timer
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# Create a canvas roughly the size of the tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Read a file and get a hold of image
tomato_img = PhotoImage(file="tomato.png")
# Create image centered on canvas with x,y coords being halved
canvas.create_image(100, 112, image=tomato_img)
# Create countdown text on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
# Add the canvas into grid
canvas.grid(column=1, row=1)

# Start and Rest Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Progress Checkmarks
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
