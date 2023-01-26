import math

def square_area(side1, side2):
    area = side1 * side2
    return area

def triangle_area(height, bottom):
    area = (height * bottom) / 2
    return f"The area of the triangle is {area}"

def circle_area(radius):
    return math.pi * (radius ** 2)

def main():

    shape = input("Whhich shape's area would you like to calculate? ")

    area = 0

    if shape == "circle":
        radius = int(input("What is the radius? "))
        area = circle_area(radius)
    elif shape == "square" or shape =="rectangle":
        x = int(input("What is the length of the first side? "))
        y = int(input("What is the length of the second side? "))
        area = square_area(x, y)
    elif shape == "triangle":
        x = int(input("What is the length of the height? "))
        y = int(input("What is the length of the bottom? "))
        area = triangle_area(x, y)
    else:
        print("error, invalid shape name")
        return 1
    
    print(f"The area is {area}")

    return 0


main()