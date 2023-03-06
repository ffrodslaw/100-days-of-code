import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = tk.Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,
                                                     text="Question goes here",
                                                     width=280,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        image_true = tk.PhotoImage(file="images/true.png")
        image_false = tk.PhotoImage(file="images/false.png")

        self.button_true = tk.Button(image=image_true, highlightthickness=0, command=self.press_true)
        self.button_false = tk.Button(image=image_false, highlightthickness=0, command=self.press_false)
        self.button_true.grid(column=0, row=2)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)








