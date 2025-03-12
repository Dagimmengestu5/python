# GAME rock paper scissors
import random 

Rock = '''
    .-.______
 ----/ \ )___)
      (_/()___)
        ()____)
----\___()___)
                    '''
Paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       

'''
scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
  
  '''
game_image = [Rock, Paper, scissors]
man_chose = int(input("What do you chose? Type 0 for Rock Type 1 for Paper Type 2 for scissors: "))
print(f"user choise {game_image[man_chose]}")
computer_chose = random.randint(0, 2)
print(f"computer coise: {game_image[computer_chose]}")




if man_chose == 0 and computer_chose == 1:
    print("'ohh' Computer win")
elif man_chose == 1 and computer_chose == 2:
    print("'ohh' Computer win")
elif computer_chose > man_chose:
    print("'ohh' Computer win")
if man_chose > computer_chose:
     print("'yas' you Win")
elif computer_chose == 0 and man_chose == 2:
    print("'ohh' Computer win")
elif computer_chose == 2 and man_chose == 0:
    print("'yas' you Win")
    
elif computer_chose == man_chose:
    print("it's Drow")
else:
    print("you are chose wrong number")

