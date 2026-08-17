# My first python program 
# It is just simple ROT13 encode but I'll try to update It periodically

text = input("tell me : ")

def rot13y(text):
	for character in text:
		cvt_u = ord(character)
		txt_s = (cvt_u - 97) + 13
		txt_l = txt_s % 26
		txt_b = txt_l + 97
		cvt_t = chr(txt_b)
		print(cvt_t, end="")

rot13y(text)
