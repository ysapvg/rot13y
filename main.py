# My first Python program
# A simple ROT13 encoder that I will try to update periodically

text = input("Tell me : ")


def rot13y(text):
    for character in text:
        char_code = ord(character)
        shifted_code = (char_code - 97) + 13
        alphabet_position = shifted_code % 26
        new_code = alphabet_position + 97
        encoded_character = chr(new_code)
        print(encoded_character, end="")

rot13y(text)
