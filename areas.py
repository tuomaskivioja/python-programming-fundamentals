# To access pi, we can import a library called math - we will cover libraries in depth ina  future video - if you found this from Google, well done!
# If not, you could have also simply defined an estimate value, for example: PI = 3.14 and used that.
import math

def square_area(side1, side2):
    area = side1 * side2
    return area

def triangle_area(height, bottom):
    area = (height * bottom) / 2
    return f"The area of the triangle is {area}"

def circle_area(radius):
    # From the documentation of the math library we can find how to access the value of pi as below. Alternatively you could have defined an approximate value yourself (see comment on line 2)
    return math.pi * (radius ** 2)


# We define a "main" function - this is a convention to indicate what is the "main part" of your program
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
        # Returning a value exits us out of the program and ensures we don't run line 38 in the error case - returning a value of 1 is customary when we are indicating that something "went wrong"
        return 1
    
    print(f"The area is {area}")

    # Returning a value of 0 is customary in programming to indicate that "everything went right" (contrast this to the case above where we returned 1)
    return 0

# at the end of the file we run the main() function
main()