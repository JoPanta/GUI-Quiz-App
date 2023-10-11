from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.question_label = Label(text="Questions Go Here", bg='White', font=("Arial", 20, "italic"), height=14, width=30)
        self.question_label.grid(row=1, column=0, columnspan=2)



        self.window.mainloop()

