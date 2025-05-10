
"""

# Write your code here


"""
# Q2:- Write a program that will convert celsius value to fahrenheit."""

# Write your code here
celsius = float(input("Enter The Celsius: "))
fahrenheit = (celsius*(9/5))+32
print(f"{celsius} Celsius is {fahrenheit} Fahrenheit  ")


"""### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

num1 = int(input("Enter Num1 :"))
num2 = int(input("Enter Num2 :"))
print("Num1 Before :",num1)
print("Num2 Before :",num2)
magic_box = num1
num1 = num2
num2 = magic_box
print("After swapping:")
print("num1 :", num1)
print("num2 :", num2)




# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

# Write your code here
x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))
x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))
distance = ((((x2-x1)**2 )+((y2-y1)**2 ))**(1/2))
print("Euclidean distance between the two points is:", distance)

"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""

# Write your code here
principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest is:", simple_interest)


"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2

"""

heads = int(input("heads -> "))
legs = int(input("legs -> "))

dogs = (legs - 2 * heads) // 2
chickens = heads - dogs

if dogs >= 0 and chickens >= 0 and (2 * chickens + 4 * dogs == legs):
    print("dogs ->", dogs)
    print("chicken ->", chickens)
else:
    print("Invalid input!")

"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

# Write your code here

n = int(input("Enter the value of n: "))
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i * i
print("Sum of squares of first", n, "natural numbers is:", sum_of_squares)

"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

# Write your code here
first_term = int(input("Enter the first term:"))
second_term = int(input("Enter the second term:"))
terms =int(input("Enter the length of series:"))
d= second_term-first_term
last_term = (first_term) +((terms-1)*(second_term-first_term))
print(last_term)

"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# Write your code here
num1_numerator = int(input("Enter the numerator for first term:"))
num1_denominator = int(input("Enter the denominator for first term:"))
num1 = num1_numerator/num1_denominator
num2_numerator = int(input("Enter the numerator for second term:"))
num2_denominator = int(input("Enter the denominator for second term:"))
num2 = num2_numerator/num2_denominator
print(num1+num2)


"""### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

# Write your code here
height_tank = int(input("Enter the Height of tank : "))
Width_tank = int(input("Enter the Width of tank : "))
Breadth_tank = int(input("Enter the Breadth of tank : "))
height_glass =int(input("Enter the Height of glass : "))
r_glass = int(input("Enter the radius of tank : "))
vol_tank = height_tank*Width_tank*Breadth_tank
vol_glass = ((3.14)*r_glass*r_glass*height_glass)
total_glasses = vol_tank//vol_glass
print("The total number of glasses filled from milk container will be ",total_glasses)