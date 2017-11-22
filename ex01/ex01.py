import time
year = int(time.strftime("%Y"))
name = input("What's your name?")
age = int(input("what's your age?"))
number = int(input("Choose a randon number:"))
if age >=100:
	hundred_year = year-(age-100)
	print(number*"{}, you did 100 at {}\n".format(name, hundred_year) )
else:
	hundred_year = (100-age)+year
	print(number*"{}, you'll be a 100 at {}\n".format(name, hundred_year) )
