import random

secret = random.randint(1,10)
guess = random.randint(1,10)

if(guess == secret):
	print("just right")
elif(guess < secret):
	print("too low")
else:
	print("too high")