import tkinter as tk
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
timer_tf = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():

    window.after_cancel(timer_tf)
    canvas.itemconfig(timer_text, text = "00:00")
    timer.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        count_down(long)
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg=PINK)
        count_down(short)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    m = math.floor(count/60)
    s = count % 60
    if s < 10:
        s = f"0{s}"   # making sure all seconds have two digits
    count_mod = f"{m}:{s}"
    canvas.itemconfig(timer_text, text=count_mod)
    if count > 0:
        global timer_tf
        timer_tf = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(rep/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title = "Pomodoro"
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font= (FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)

timer = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer.grid(column=1,row=0)

start = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0,row=2)

reset = tk.Button(text="Reset",  command=reset_timer, highlightthickness=0)
reset.grid(column=2,row=2)

checkmarks = tk.Label(text="✓", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
