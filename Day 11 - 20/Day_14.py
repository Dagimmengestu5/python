######### compare
# import random
# import os

# data = [
#     {"name": "Cristiano Ronaldo", "team": "Football", "followers": "500M", "age": 39, "nationality": "Portuguese", "profession": "Athlete"},
#     {"name": "Lionel Messi", "team": "Football", "followers": "300M", "age": 36, "nationality": "Argentinian", "profession": "Athlete"},
#     {"name": "LeBron James", "team": "Basketball", "followers": "200M", "age": 39, "nationality": "American", "profession": "Athlete"},
#     {"name": "Dwayne Johnson", "team": "Entertainment", "followers": "250M", "age": 51, "nationality": "American", "profession": "Actor, Wrestler"},
#     {"name": "Virat Kohli", "team": "Cricket", "followers": "150M", "age": 35, "nationality": "Indian", "profession": "Athlete"},
#     {"name": "Elon Musk", "team": "Technology", "followers": "180M", "age": 52, "nationality": "American", "profession": "Entrepreneur"},
#     {"name": "Jeff Bezos", "team": "Business", "followers": "100M", "age": 60, "nationality": "American", "profession": "Entrepreneur"},
#     {"name": "Michael Jordan", "team": "Basketball", "followers": "90M", "age": 61, "nationality": "American", "profession": "Athlete, Entrepreneur"},
#     {"name": "Tom Cruise", "team": "Hollywood", "followers": "50M", "age": 61, "nationality": "American", "profession": "Actor"},
#     {"name": "Robert Downey Jr.", "team": "Hollywood", "followers": "75M", "age": 58, "nationality": "American", "profession": "Actor"},
#     {"name": "Bill Gates", "team": "Technology", "followers": "130M", "age": 68, "nationality": "American", "profession": "Entrepreneur, Philanthropist"},
#     {"name": "Kylian Mbappé", "team": "Football", "followers": "100M", "age": 25, "nationality": "French", "profession": "Athlete"},
#     {"name": "Taylor Swift", "team": "Music", "followers": "400M", "age": 34, "nationality": "American", "profession": "Singer"},
#     {"name": "Drake", "team": "Music", "followers": "120M", "age": 37, "nationality": "Canadian", "profession": "Singer"},
#     {"name": "Usain Bolt", "team": "Athletics", "followers": "80M", "age": 37, "nationality": "Jamaican", "profession": "Athlete"},
#     {"name": "Roger Federer", "team": "Tennis", "followers": "110M", "age": 42, "nationality": "Swiss", "profession": "Athlete"},
#     {"name": "Novak Djokovic", "team": "Tennis", "followers": "95M", "age": 36, "nationality": "Serbian", "profession": "Athlete"},
#     {"name": "Mark Zuckerberg", "team": "Technology", "followers": "120M", "age": 40, "nationality": "American", "profession": "Entrepreneur"},
#     {"name": "Jackie Chan", "team": "Hollywood", "followers": "80M", "age": 69, "nationality": "Chinese", "profession": "Actor, Martial Artist"},
# ]
# score = 0
# compare_a = random.choice(data)
# compare_b = random.choice(data)

# end_of_game = False
# def account_file(compare):
#     account_n = compare["name"]
#     account_t = compare["team"]
#     account_a = compare["age"]
#     account_nat = compare["nationality"]
#     account_p = compare["profession"]
#     return f"{account_n}, a {account_t}, in {account_a} years old , frome {account_nat}, is a {account_p}"

# account_f_a = compare_a["followers"]
# account_f_b = compare_b["followers"]

# def chack_anser(guess, A, B):
 
#     if A > B:
#         return guess == "A"
#     else:
#         return guess == "B"
    

# # print(compare)

# while not end_of_game:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(account_f_a)
#     print(account_f_b)
#     compare_a = compare_b
#     compare_b = random.choice(data)
#     if compare_a == compare_b:
#         compare_b = random.choice(data)
   
#     print(f"Choice A: {account_file(compare_a)}")
#     print(f"Choice B: {account_file(compare_b)}")
#     guess = input("which of the more fallower in instagram 'A' or 'B': ").upper()
   
#     is_corect = chack_anser(guess, account_f_a, account_f_b)
#     if is_corect:
#         score += 1
#         print(f"you are right Curent score: {score}")
#     else :
#         print(f"sory that wes wrong total score is: {score}")
#         end_of_game =True


import random
import os
#
# vs = '''
#
#  .----------------.  .----------------.
# | .--------------. || .--------------. |
# | | ____   ____  | || |    _______   | |
# | ||_  _| |_  _| | || |   /  ___  |  | |
# | |  \ \   / /   | || |  |  (__ \_|  | |
# | |   \ \ / /    | || |   '.___`-.   | |
# | |    \ ' /     | || |  |`\____) |  | |
# | |     \_/      | || |  |_______.'  | |
# | |              | || |              | |
# | '--------------' || '--------------' |
#  '----------------'  '----------------'
# '''
# logo = '''
#
#
#  _     _       _
# | |   (_)     | |
# | |__  _  __ _| |__   ___ _ __
# | '_ \| |/ _` | '_ \ / _ \ '__|
# | | | | | (_| | | | |  __/ |
# |_| |_|_|\__, |_| |_|\___|_|
#           __/ |
#          |___/
#  _
# | |
# | | _____      _____ _ __
# | |/ _ \ \ /\ / / _ \ '__|
# | | (_) \ V  V /  __/ |
# |_|\___/ \_/\_/ \___|_|
#
#
# '''


data = [
    {"name": "Cristiano Ronaldo", "team": "Football", "followers": "500", "age": 39, "nationality": "Portuguese", "profession": "Athlete"},
    {"name": "Lionel Messi", "team": "Football", "followers": "300", "age": 36, "nationality": "Argentinian", "profession": "Athlete"},
    {"name": "LeBron James", "team": "Basketball", "followers": "200", "age": 39, "nationality": "American", "profession": "Athlete"},
    {"name": "Dwayne Johnson", "team": "Entertainment", "followers": "250", "age": 51, "nationality": "American", "profession": "Actor, Wrestler"},
    {"name": "Virat Kohli", "team": "Cricket", "followers": "150", "age": 35, "nationality": "Indian", "profession": "Athlete"},
    {"name": "Elon Musk", "team": "Technology", "followers": "180", "age": 52, "nationality": "American", "profession": "Entrepreneur"},
    {"name": "Jeff Bezos", "team": "Business", "followers": "100", "age": 60, "nationality": "American", "profession": "Entrepreneur"},
    {"name": "Michael Jordan", "team": "Basketball", "followers": "90", "age": 61, "nationality": "American", "profession": "Athlete, Entrepreneur"},
    {"name": "Tom Cruise", "team": "Hollywood", "followers": "50", "age": 61, "nationality": "American", "profession": "Actor"},
    {"name": "Robert Downey Jr.", "team": "Hollywood", "followers": "75", "age": 58, "nationality": "American", "profession": "Actor"},
    {"name": "Bill Gates", "team": "Technology", "followers": "130", "age": 68, "nationality": "American", "profession": "Entrepreneur, Philanthropist"},
    {"name": "Kylian Mbappé", "team": "Football", "followers": "110", "age": 25, "nationality": "French", "profession": "Athlete"},
    {"name": "Taylor Swift", "team": "Music", "followers": "400", "age": 34, "nationality": "American", "profession": "Singer"},
    {"name": "Drake", "team": "Music", "followers": "160", "age": 37, "nationality": "Canadian", "profession": "Singer"},
    {"name": "Usain Bolt", "team": "Athletics", "followers": "80", "age": 37, "nationality": "Jamaican", "profession": "Athlete"},
    {"name": "Roger Federer", "team": "Tennis", "followers": "120", "age": 42, "nationality": "Swiss", "profession": "Athlete"},
    {"name": "Novak Djokovic", "team": "Tennis", "followers": "95", "age": 36, "nationality": "Serbian", "profession": "Athlete"},
    {"name": "Mark Zuckerberg", "team": "Technology", "followers": "140", "age": 40, "nationality": "American", "profession": "Entrepreneur"},
    {"name": "Jackie Chan", "team": "Hollywood", "followers": "60", "age": 69, "nationality": "Chinese", "profession": "Actor, Martial Artist"},
]
score = 3
end_of_game = False
amount_b = random.choice(data)
def formate_data(amount):
    amount_n = amount["name"]
    amount_t = amount["team"]
    amount_a = amount["age"]
    amount_nat = amount["nationality"]
    amount_p = amount["profession"]
    return f"{amount_n}, is the {amount_t}, and {amount_a} yers old, is{amount_nat}, is {amount_p}"
def chake_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"
while not end_of_game:
    os.system('cls' if os.name == 'nt' else 'clear')
    # print(logo)
    print("welcome to the Upper Lower game")
    
    amount_a = amount_b
    amount_b = random.choice(data)
    while amount_a == amount_b:
        amount_b = random.choice(data)
    a_follower_count = amount_a["followers"]
    b_follower_count = amount_b["followers"]
    print (f"Choise A: {formate_data(amount_a)}")
    # print(a_follower_count) # example
    # print(vs)
    # print(b_follower_count) # exaple
    print (f"Choise B: {formate_data(amount_b)}")

    guess = input("which of the more fallower in instagram 'A' or 'B': ").lower()

    a_follower_count = amount_a["followers"]
    b_follower_count = amount_b["followers"]

    is_corect = chake_answer(guess, a_follower_count, b_follower_count)

    if is_corect:
        score += 1
        print(f"you  right the score is {score}")
    else:
        print(f"sory not your final score is {score}")
        end_of_game = True

    # if guess == "A":
    #     if A > B:
    #         score += 1
    #         print(f"your score is {score}")
    #     elif A < B:
    #         end_of_game = True
    #         print(f"ow sory the Choice A: followers are {A} so {A} not > {B}")
    # elif guess == "B":
    #     if B > A:
    #         score += 1
    #         print(f"your score is {score}")
    #     elif B < A:
    #         end_of_game = True
    #         print(f"ow sory the Choice B: followers are {B} so {B} not > {A}")





# if compare_a == compare_b:
#     compare_b = random.choice(data)
# for compare in set(compare_a.values()):
#     print(f"[{compare}]")

# print(compare_b.title())