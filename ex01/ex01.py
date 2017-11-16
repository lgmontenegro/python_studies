name = input("What's your name?")
age = int(input("what's your age?"))
number = int(input("Choose a randon number:"))
hundred_year = (100-age)+2017
print(number*"{}, you'll be a 100 at {}\n".format(name, hundred_year))