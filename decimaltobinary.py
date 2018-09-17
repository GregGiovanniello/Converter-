""" 
program: decimaltobinary.py
converts a decimal iteger to a string of bits.
"""
decimal = int(input("Enter a decimal iteger: "))
if decimal == 0:
	print(0)
else: 
	print("Quotent remainder binary")
	bstring = ""
	while decimal > 0:
		remainder = decimal % 2
		decimal = decimal // 2
		bstring = str(remainder) + bstring
	print("%5d%8d%12s" % (decimal, remainder, bstring))