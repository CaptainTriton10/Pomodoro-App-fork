import math
import tkinter as tk

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
timer = None


# ---------------------------- UI SETUP ------------------------------- #

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pomodoro")
        self.config(padx=100, pady=100, bg=YELLOW)

        self.timer_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
        self.timer_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_image = tk.PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_image)

        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = tk.Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                                      command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = tk.Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                                      command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.check_marks = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
        self.check_marks.grid(column=1, row=3)

    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer(self):
        global reps
        self.after_cancel(timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.timer_label.config(text="Timer")
        self.check_marks.config(text="")
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer(self):
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 2 == 0:
            self.count_down(short_break_sec)
            self.timer_label.config(text="Break", fg=PINK)
        elif reps % 8 == 0:
            self.count_down(long_break_sec)
            self.timer_label.config(text="Break", fg=RED)
        else:
            self.count_down(work_sec)
            self.timer_label.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(self, count):
        global timer
        count_min = math.floor(count / 60)
        if count_min == 0:
            count_min = "00"

        count_sec = count % 60

        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            timer = self.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            marks = ""
            sessions = math.floor(reps / 2)
            for _ in range(sessions):
                marks += "✔"
            self.check_marks.config(text=marks)


window = Window()
window.mainloop()
