
deposit = 0
interest_rate_percentage = 0
number_of_months = 0
goal = 0

while deposit <= 0:
    deposit = int(input("Enter your deposit: "))
    if deposit <= 0:
       print("Invalid deposit- Can not be negative or zero - Let's try again")

while interest_rate_percentage <=0 :
    interest_rate_percentage = float (input("Enter your interest rate:"))/100/12
    if interest_rate_percentage <= 0:
        print("Invalid interest rate- Can not be negative or zero - Let's try again")

while True:
    number_of_months = int(input("Enter Months"))
    if number_of_months > 0:
        break
    else:
        print("Invalid number of months- Can not be negative or zero - Let's try again")

while goal < 0:
    goal = int(input("Enter your goal:"))
    if goal < 0:
        print("Invalid goal- Can not be negative - Let's try again")

#goal = deposit * (1 + interest_rate_percentage/100)* number_of_months)
#print (goal)
print(interest_rate_percentage)
for number_of_months in range(1,number_of_months+1):
    Interest_rate_amount = deposit * interest_rate_percentage
    deposit += Interest_rate_amount
    print(f"Month {number_of_months} account balance is:$ {deposit:,.2f}")

while deposit  < goal :
    Interest_rate_amount = deposit * interest_rate_percentage
    deposit += Interest_rate_amount
    number_of_months += 1
print(f"It will take {number_of_months} to reach the goal of {goal}")









