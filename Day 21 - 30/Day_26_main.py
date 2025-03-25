############# generate word depand on your input

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {row.letter:row.code for(index, row) in data.iterrows()}

def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetics_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("sorry, only input the letter")
        generate()
generate()