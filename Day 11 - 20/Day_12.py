#########################  Scope  ###########################

# number_list = [str(d) for d in range(1, 101)]   # number list
# print(number_list)
from random import randint
logo = '''
  _   _                 _                  _____                      
 | \ | |               | |                / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ |/ _` | '_ ` _ \ / _ \\
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|_| |_| |_|\___|
                                                                     
 '''




   
print(logo)
print("Welcome the numbr Guessing")
print("I'm tinking of a number betwen 1 and 100. ")


number = randint(1, 100)
chose = input("chose difficalty Type 'easy' or 'hard': ").lower()
attempet = 10
h_attempet = 5
end_of_game = False
def easy():
    try:
        global end_of_game
        global attempet
        # print(f"the guess word is : {number}")
        
        guess = int(input("guess the number: "))
        if guess != number:
            attempet -= 1
            print(f"You have {attempet} attempts remaning to guess a number")
        if guess > number:
             print("high")
        if guess < number:
             print("low")
        if guess == number:
             end_of_game = True
             print(f"congra you are find the number the gussing number is [{number}]")

        if attempet == 0:
                end_of_game = True
                print(f"oohh i'm so sory the number is [{number}] Game Over")
    except ValueError:
            print("!!!oops you have not insert number please input the number !!!")
def hard():
    try:
        global end_of_game
        global h_attempet
        print(f" your guessing number is: {number} ")
        guess = int(input("guess the number: "))

        if guess != number:
            h_attempet -= 1
            print(f"You have {h_attempet} attempts remaning to guess a number")
        if guess > number:
            print("high")
        if guess < number:
            print("low")
        if guess == number:
            end_of_game = True
            print(f"congra you are find the number the gussing number is [{number}]")
        if h_attempet == 0:
                end_of_game = True
                print(f"oohh i'm so sory the number is [{number}] Game Over")
    except ValueError:
        print("!!!oops you have not insert number please input the number !!!")
while not end_of_game:

        if chose == "easy":
            easy()

        elif chose == "hard":
            hard()
        else:
            print("please Type 'easy' or 'hard' you are not select them: ")
            end_of_game = True