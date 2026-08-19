# My first Python program
# A simple ROT13 encoder that I will try to update periodically

text = input("Tell me : ")

def rot13y(text): # ROT13 function
    for character in text: # check each character from the text
        if character == " ": # don't process spaces
            print(" ", end="") 
        else:
            char_code = ord(character) # get the ASCII code of the character
            shifted_code = (char_code - 97) + 13 # shift the character by 13 positions
            alphabet_position = shifted_code % 26 # keep the position within the alphabet
            new_code = alphabet_position + 97 # convert the position back to ASCII
            encoded_character = chr(new_code) # convert the ASCII code back to a character
            print(encoded_character, end="") # print the encoded character


rot13y(text)