from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, quiz_score):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {quiz_score} ", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     font=("Arial", 20, "italic"),
                                                     text="question_text",
                                                     fill=THEME_COLOR)

        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false, highlightthickness=0)
        self.false_button.grid(row=2, column=1)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def