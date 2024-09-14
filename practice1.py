import math

# Question 1: Calculate the square root of the sum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_of_numbers = num1 + num2
square_root = math.sqrt(sum_of_numbers)

print("The square root of the sum of", num1, "and", num2, "is:", square_root)

# Question 2: Calculate the circumference and area of a circle
radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("The circumference of the circle is:", circumference)
print("The area of the circle is:", area)

# Question 3: Calculate the trigonometric functions of an angle
angle_degrees = float(input("Enter the angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sine = math.sin(angle_radians)
cosine = math.cos(angle_radians)
tangent = math.tan(angle_radians)

print("The sine of", angle_degrees, "degrees is:", sine)
print("The cosine of", angle_degrees, "degrees is:", cosine)
print("The tangent of", angle_degrees, "degrees is:", tangent)