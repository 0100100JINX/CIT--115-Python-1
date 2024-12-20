print("We will be computing - Compound Interest. Wish us Luck")
PV= float(input("Enter the principal: "))
R = float(input("Enter the Interest Rate: ")) /100
M = float(input("Enter the time to per year is the interest compounded?: " ))
T = int(input("Enter the number of years: "))
FV = PV*(1+R/M)**(M*T)
print(f"At the end of {M} years, you will have {FV:,.2f}")

# WOW
