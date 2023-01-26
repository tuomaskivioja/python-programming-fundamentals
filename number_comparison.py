

try:
    number = int(input("enter number "))
    if number > 0:
        print("positive!")
    elif number == 0:
        print("zero")
    else:
        print("negative")
except ValueError:
    print("error, must enter a number")

answer = input("are you hungr? ")

if answer == "yes":
    print("go eat food")
else:
    print("go do some work")

