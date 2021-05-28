num = float(input("Enter the number m: "))
n = 1
if num <=0:
    print("You should enter a postive number!")
else:
    while n**2 <= num:
        n = n+1
    print("n =",n)