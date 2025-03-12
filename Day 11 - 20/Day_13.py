################## Debugger 

# from random import randint
# answer = randint(1, 101)
# print(answer)

# year = int(input("ehat is your yerar of birth? "))

# if year > 1980 and year < 1994:
#         print("you are good batch ")
# elif year > 1994:
#         print("you are eligable modern")

# age = int(input("what is your age? "))
# if age > 18:
#     print(f"you can feive to age {age}")
# else:
#     print("oww sory")
# page = 0
# word_on_page = 0
# page = int(input("insert your page: "))
# word_on_page = int(input("insert your word on page: "))
# total_word = page * word_on_page
# print(f"you page is {page}")
# print(f"your word on page is {word_on_page}")
# print(total_word)

def add_list(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)
add_list([0,1,2,3,4,5,10])   