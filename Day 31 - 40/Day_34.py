import requests
import html
from tkinter import *

them_color = "#324567"
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quastion Game")
        self.window.config(padx=20, pady=20, bg=them_color)
        self.score = 0
        self.score_label = Label(text="Score: 0", bg=them_color, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some Question Text",
            fill=them_color,
            font=("Arial", 20, "italic")
        )
        true_image = PhotoImage(file="files/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
class Quastion:
    def __init__ (self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
class Quizbrain:
    def __init__(self, q_list):
        self.quastion_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
        return self.quastion_number < len(self.question_list)
    def next_question(self):
        self.current_question = self.question_list[self.quastion_number]
        self.quastion_number += 1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.quastion_number}: {q_text} (True/False): ")
        self.check_answer(user_answer, self.current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
quastion_bank = []
for quastion in question_data:
    quastion_text = quastion["question"]
    quastion_answer = quastion["correct_answer"]
    new_quastion = Quastion(quastion_text, quastion_answer)
    quastion_bank.append(new_quastion)
quize = Quizbrain(quastion_bank)
while quize.still_has_question():
    quize.next_question()
    print(f"Your current score is: {quize.score}/{quize.quastion_number}")

