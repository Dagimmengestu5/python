##################### Encript and decript
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caeser(start_text, shift_amount, chiper_direction):
    end_text = ""
    if chiper_direction == "decode":
        shift_amount *= -1
    for ch in start_text:
        if ch in alphabet:
            position = alphabet.index(ch)
            new_position = position + shift_amount 
            end_text += alphabet[new_position]
        else :
            end_text += ch
    print(f"here's the {chiper_direction}d resalt: {end_text}")
#8
direction = input("Type 'decode' to decript Type ' encode' to encript \n")
text = input("Type your massage: \n")
shift = int(input("Type the shift number \n"))

shift = shift % 26
caeser(start_text = text, shift_amount = shift, chiper_direction = direction)
print(caeser)
