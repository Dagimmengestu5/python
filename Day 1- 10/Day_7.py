# Hangman Game
import random
import os
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                  
'''

stage = ['''
 _______
|/      |
|       O
|      /|\\
|      / \\ 
|      
|
|______________''', '''
 _______
|/      |
|       O
|      /|\\ 
|      /  
|      
|
|______________''',

''' _______
|/      |
|       O
|      /|\\
|      
|       
|
|______________''', 
'''
 _______
|/      |
|       O
|      /| 
|      
|      
|
|______________''',
'''
 _______
|/      |
|       O
|       | 
|       
|      
|
|______________''', 
'''
 _______
|/      |
|       O
|       
|       
|      
|
|______________''',
]    
word_list = [ "ethiopia" , "kenya", "tanzanya", "jebuti"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"you guessed word is {chosen_word}")
life = 6
end_of_game = False
# to create the _ area 
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
    print(life)
    guess = input("Guess the word: ").lower()

    # To fill in the position of the letter area
    for possition in range(word_length):
        letter = chosen_word[possition]
        if letter == guess:
            display[possition] = letter
            pass
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        life -= 1
    if life == 0:
        print(f"game over the word was '{chosen_word}'")
        end_of_game = True
# dfsdgdfvbdfds
    if "_" not in display:
        end_of_game = True
        print("you Win")
