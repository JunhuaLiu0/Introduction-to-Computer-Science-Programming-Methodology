from math import sin
from math import cos
from math import tan

while True:
    robust_a = input("Please enter the start point of interval:")
    if robust_a.isdigit():
        break
while True:
    robust_b = input("Please enter the end point of interval:")
    if robust_b.isdigit():
        break
while True:
    robust_n = input("Please enter the number of intervals:")
    if robust_n.isdigit():
        break
a = int(robust_a)
b = int(robust_b)
n = int(robust_n)
triangle_function = str(input("Please choose the function: sin cos or tan: "))
sum = 0
while True:
    if triangle_function == "sin":
        for i in range(1, n + 1):
            sum += ((b - a) / n) * sin(a + (((b - a) / n) * (i - 0.5)))
        print("The numerical integration is", sum)
        break
    elif triangle_function == "cos":
        for i in range(1, n + 1):
            sum += ((b - a) / n) * cos(a + (((b - a) / n) * (i - 0.5)))
        print("The numerical integration is", sum)
        break
    elif triangle_function == "tan":
        for i in range(1, n + 1):
            sum += ((b - a) / n) * tan(a + (((b - a) / n) * (i - 0.5)))
        print("The numerical integration is", sum)
        break
    else:
        triangle_function = str(input("Please enter the valid function:"))

