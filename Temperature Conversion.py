fCelsius = 0
fFahrenheight = 0

fTemp = float (input("Enter Temperature"))
sChoice = input ("Fahrenheight ( F) or Celsius (C):").upper()
#.upper() forces string to be upper case response

if sChoice != "F" and sChoice != "C":
    exit("Enter F or C" )

if sChoice == "F":
    if fTemp > 212 :
        exit("Temp can not be greater than 212")

    fCelsius = (5.0/9) * (fTemp - 32)
    print(f"The  celsius Equivalent is: {fCelsius:,.1f}")

if sChoice == "C":
    if fTemp > 100:
        exit("Temp can not be greater than 100")
    fFahrenheight = ((9.0/ 5.0) * fTemp) + 32

    print(f"The Fahrenheit is equivalent is: {fFahrenheight:,.1f}")


