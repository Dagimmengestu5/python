# Calculater 

# def format_name(f_name, l_name):
#     """input the first and last name then
#       you will see the title output"""
#     if f_name == "" or l_name == "":
#         return "you have no insert name"
#     f = f_name.title()
#     l = l_name.title()
#     return f"Resalt: {f} {l}"

# print(format_name(input("wha is your first name? "), input("wha is your last name? ") ))
    # Days in the month 
# def is_leap(yer):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
# def day_in_month(year, month):
#     month_days = [31,28,31,30,31,31,30]
#     if is_leap(year) and month == 2 :
#         return 29
#     return month_days [month -1]
# year = int(input("insert the year: "))
# month = int(input("insert the month: "))
# days = day_in_month(year, month)
# print(days)
import os
logo = '''

 _____________________
|  _________________  |
| | Dagi         0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
def add(n1,n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divided(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divided
}
def cal():
    print(logo)
    num1 = int(input("write the first number: "))

    for dagi in operation:
        print(dagi)
    should_continue = True
    while should_continue :
        operation_dagi = (input("Please pick an operation of the abave! "))
        num2 = int(input("write the second number: "))
        calculation_function = operation[operation_dagi]
        answer1 = calculation_function(num1,num2)
        print(f"{num1} {operation_dagi} {num2} = {answer1}")
        con = input(f"could you continue calculet with '{answer1}' Type 'y' exit 'n ' and back to new 'o' : ")
        if con == "y":
            num1 = answer1
        elif con == "o":
            os.system('cls' if os.name == 'nt' else 'clear')
            cal()
        elif con == "n":
            should_continue = False
            print("ok byy i'll see you later ")
        else:
            should_continue = False
            print("Rong key")

cal()
        #or do this 
# operation_dagi2 = (input("pick up another operation to continue: "))
# calculation_function = operation[operation_dagi2]
# num3 = int(input("write the second number: "))
# answer2 = calculation_function(answer1, num3)
# print(f"{answer1} {operation_dagi2} {num3} = {answer2}")