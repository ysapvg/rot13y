# My first Python program
# A simple ROT13 encoder that I will try to update periodically

text = input("Tell me : ")


def rot13y(text):
    for character in text:
        # Convert character to its Unicode number
        char_code = ord(character)

        # Convert the character code to a 0-25 alphabet position
        shifted_code = (char_code - 97) + 13

        # Keep the result within the 0-25 range
        alphabet_position = shifted_code % 26

        # Convert the alphabet position back to a Unicode number
        new_code = alphabet_position + 97

        # Convert the Unicode number back to a character
        encoded_character = chr(new_code)

        # Print the encoded character without creating a new line
        print(encoded_character, end="")


rot13y(text)