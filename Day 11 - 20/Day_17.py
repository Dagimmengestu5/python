################################ True or false quastion

import random

# from multiprocessing.resource_tracker import ensure_running
#
# question_data = [
# {"text": "A slug's blood is green.", "answer": "true"},
# {"text": "The loudest animal is the African Elephant.", "answer": "false"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "true"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "true"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "true"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "false"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "true"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "false"},
# {"text": "Google was originally called 'Backrub'.", "answer": "true"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "true"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "false"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "true"}
# ]
# import random
# print("welcome to test.")
# dagi = dict(question_data)
# chose = random.choice(question_data)
# chose2 = random.choice(question_data)
# chose3 = random.choice(question_data)
# chose4 = random.choice(question_data)
# end_of_game = True
# score = 0
#
#
# def Q1():
#     global chose
#     global score
#     global end_of_game
#     q1 = input(f"Q.1: {chose["text"]}").lower()
#     if q1 == chose["answer"]:
#         score += 1
#         print("correct")
#         print(f"your score is {score}")
#         end_of_game = True
#     else:
#         print("wrong")
#         user_continue = input("would you continue the game 'y' or 'n'")
#         if user_continue == "y":
#             chose = random.choice(question_data)
#             score += 0
#         else:
#             print(f"your final score is {score}")
#             end_of_game = False
# def Q2():
#             global chose2
#             global score
#             global end_of_game
#             q2 = input(f"Q.2: {chose2["text"]}").lower()
#             if q2 == chose2["answer"]:
#                 score += 1
#                 print("correct")
#                 print(f"your score is {score}")
#                 end_of_game = True
#             else:
#                 print("wrong")
#                 user_continue = input("would you continue the game 'y' or 'n'")
#                 if user_continue == "y":
#                     chose2 = random.choice(question_data)
#                     score += 0
#                 else:
#                     print(f"your final score is {score}")
#                     end_of_game = False
#
# def Q3():
#     global chose3
#     global score
#     global end_of_game
#
#     q3 = input(f"Q.3: {chose3["text"]}").lower()
#     if q3 == chose3["answer"]:
#         score += 1
#         print("correct")
#         print(f"your score is {score}")
#         end_of_game = True
#     else:
#         print("wrong")
#         user_continue = input("would you continue the game 'y' or 'n'")
#         if user_continue == "y":
#             chose3 = random.choice(question_data)
#             score += 0
#         else:
#             print(f"your final score is {score}")
#             end_of_game = False
# def Q4():
#     global chose4
#     global score
#     global end_of_game
#
#     q4 = input(f"Q.4: {chose4["text"]}").lower()
#     if q4 == chose4["answer"]:
#         score += 1
#         print("correct")
#         print(f"your total score is {score}/4")
#         end_of_game = False
#     else:
#         print("wrong")
#         user_continue = input("would you continue the game 'y' or 'n'")
#         if user_continue == "y":
#             score += 0
#             Q4()
#
#         else:
#             print(f"your final score is {score}")
#             end_of_game = False
# while end_of_game:
#     print("welcome to test.")
#     print("True or False? ")
#     Q1()
#     Q2()
#     Q3()
#     Q4()
#
#


question_data = [
    {"text": "A slug's blood is green.", "answer": "true"},
    {"text": "The loudest animal is the African Elephant.", "answer": "false"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "true"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "true"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
     "       you are free to take it home to eat.", "answer": "true"},
    {"text": "In London, UK, if you happen to die in the House of "
             "Parliament, you are entitled to a state funeral.", "answer": "false"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "true"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "false"},
    {"text": "Google was originally called 'Backrub'.", "answer": "true"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "true"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "false"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "true"}
]

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
        current_question = self.question_list[self.quastion_number]
        self.quastion_number += 1
        user_answer = input(f"Q.{self.quastion_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
quastion_bank = []
for quastion in question_data:
    quastion_text = quastion["text"]
    quastion_answer = quastion["answer"]
    new_quastion = Quastion(quastion_text, quastion_answer)
    quastion_bank.append(new_quastion)
quize = Quizbrain(quastion_bank)
while quize.still_has_question():
    quize.next_question()
    print(f"Your current score is: {quize.score}/{quize.quastion_number}")

