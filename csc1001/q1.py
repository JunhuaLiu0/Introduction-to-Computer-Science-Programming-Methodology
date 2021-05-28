final_value = float(input("Enter final account value:"))
rate = float(input("Enter the annual interest rate:"))
year = float(input("Enter the number of years:"))
initial_value = final_value/(1+rate/100)**year
print("The initial value is:", initial_value)