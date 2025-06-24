"""
Password prompt
   Keep asking the user for a password until they enter the correct one.
   Limit attempts to 3 and then lock them out.
   Given :
		password = PaSsWoRd
	Output :
		Attempt 1 of 3: Pass
		Invalid password. Attempts left: 2
		Attempt 2 of 3: PaSS
		Invalid password. Attempts left: 1
		Attempt 3 of 3: PaSs
		Access granted!

		Attempt 1 of 3: sd
		Invalid password. Attempts left: 2
		Attempt 2 of 3: sd
		Invalid password. Attempts left: 1
		Attempt 3 of 3: sss
		Invalid password. Attempts left: 0
"""

MAX_ATTEMPTS = 3
PASSWORD = "PaSs"
attempts = 0

while attempts < MAX_ATTEMPTS:
	entry = input(f"Attempt {attempts+1} of {MAX_ATTEMPTS}: ")
	if entry == PASSWORD:
		print("Access granted!")
		break
	else:
		attempts += 1
		remaining = MAX_ATTEMPTS - attempts
		print(f"Invalid password. Attempts left: {remaining}")
