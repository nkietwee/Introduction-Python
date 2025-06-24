"""
Prompt
	This script should contain a while loop that accepts user input, writes a response,
	and only stops when the user enters "STOP". and print `Exit`
	Output :
		I got that! Anything else? : I like ponies
		I got that! Anything else? : stop
		I got that! Anything else? : stop...
		I got that! Anything else? : STOP
		Exit
"""
while True:
	prompt = input("I got that! Anything else? : ")
	if prompt == "STOP":
		break
print("EXIT")