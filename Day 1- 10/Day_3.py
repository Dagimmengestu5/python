#Trasher land
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/_____/_____/[Created by Dagi]
*******************************************************************************''')
print("wellcome to the trasher land")
print("Your missen is to find the Trasher")
road = str(input("you're at a cross road. where do you went to go? type 'Left' or 'Right'\n" )).lower()


if road  ==  "left":
    island = input("you're came to a lack. their is an island in the middel of the lake. type 'wait' to wait to a boot or type 'swim' to swim acroes? \n  ").lower()
else:
    print("rong way Game over")
if island == "wait":
    doors = input("you arrived the island unarmed. There a house with 3 doors. one red one yellow and one blue. Which color do you chose?\n").lower()
else :
    print("you're eaten by the corocody Game over")
if doors == "yellow":
    print("Congragulation you are get the trasher You Win")
else:
    print("Game over you are rong choice")
