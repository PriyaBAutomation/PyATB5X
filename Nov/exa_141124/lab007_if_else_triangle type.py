#Write a program that classifies a triangle based on its side lengths. Given three input values representing
# the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
s1 = input("Enter the length of the 1st side of the triangle: ")
s2 = input("Enter the length of the 2nd side of the triangle: ")
s3 = input("Enter the length of the 3rd side of the triangle: ")

if s1==s2==s3:
    print("The triangle is equilateral.")
elif s1 ==s2 or s2==s3 or s3 ==s1 :
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")
