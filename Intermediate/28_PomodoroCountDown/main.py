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
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it's the 8th repetition
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # If it's the 2nd/4th/6th repetition
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th repetition
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # Calculate minutes and seconds based off of total seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Display two digits once count goes below 10. Ex. 09..08..07
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Select canvas then the attribute of canvas that we want to change
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


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
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
