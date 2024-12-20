import math

def getFloatInput(sPrompt):
   fNumber = 0
   while fNumber <= 0 :
      try:
         fNumber = float(input(sPrompt))
      except ValueError:
         print("Input must a numeric value")
   return fNumber
def  getgallonsofpaint(SquareFeet, FeetPerGallon):

    fResult = SquareFeet/ FeetPerGallon
    fResult = math.ceil(fResult)

    return fResult
def GetLaborHours (Laborhourspergallon, totalgallons):
    fResult = Laborhourspergallon * totalgallons
    return fResult
def getlaborcost(laborhourspergallon, paintinglaborchargeperhour):
    fResult = paintinglaborchargeperhour * laborhourspergallon
    return fResult

def getpaintcost(iGallons, Paintprice):
    fResult = Paintprice * iGallons
    return fResult
def getsalestax(sState):
    fTaxRate = 0

    if sState == "CT":
        fTaxRate = .06
    elif sState == "MA":
        fTaxRate = .0625
    elif sState == "ME":
        fTaxRate = .085
    elif sState == "NH":
        fTaxRate = .0
    elif sState == "RI":
        fTaxRate = .07
    elif sState == "VT":
        fTaxRate = .06
    else:
        fTaxRate = 0

    return fTaxRate

def showcostestimate(iGallons,laborhours, paintcharge, laborCharge, tax, totalcost ):
    print(f"Gallons of paint: {iGallons}")
    print(f"Labor Hours: {laborhours}")
    print(f"Paint charge: {paintcharge:,.2f}")
    print(f"Labor Charge: {laborCharge:,.2f}")
    print(f"Tax amount: $ {tax:,.2f}")
    print(f"Total cost: $ {totalcost:,.2f}")

def main():

    fSquareFeet = getFloatInput("Enter a square feet: ")
    fPaintPrice =getFloatInput("Enter a paint price: ")
    fFeetPerGallon = getFloatInput("Enter a feet per gallon: ")
    fLaborhourspergallons = getFloatInput("Enter a labor hours per gallon: ")
    fPainting_Labor_charge_per_hour = getFloatInput("Painting Labor charge per hour: ")

    sState = input("Enter State: ")
    sName = input("Enter Last Name: ")

    iGallons = getgallonsofpaint(fSquareFeet, fFeetPerGallon)


    fLaborHours = GetLaborHours (fLaborhourspergallons, iGallons)


    flaborcost = getlaborcost( fLaborhourspergallons, fPainting_Labor_charge_per_hour) * iGallons


    fPaintcost = getpaintcost(iGallons,fPaintPrice)


    fTaxRate = getsalestax(sState)


    fTaxAmount = (fPaintcost + flaborcost ) * fTaxRate


    fTotal = fPaintcost + flaborcost + fTaxAmount


    showcostestimate(iGallons, fLaborHours, fPaintcost, flaborcost, fTaxAmount, fTotal)


    with open(f"{sName}_PaintJobOutput.txt","w") as file:

        file.write(f"Customer Name: {sName}\n")

        file.write(f"Gallons of paint:{str(iGallons)}\n")
        file.write(f"Labor Hours: {str(fLaborHours)}\n")

        sPaintcost = str(f"{fPaintcost:,.2f}")
        file.write(f"Paint Cost: $ {sPaintcost}\n")

        sLaborcost = str(f"{flaborcost:,.2f}")
        file.write(f"Labor Cost: $ {sLaborcost}\n")

        sTaxAmount = str(f"{fTaxAmount:,.2f}")
        file.write(f"Tax Amount: $ {sTaxAmount}\n")

        sTotal = str(f"{fTotal:,.2f}")
        file.write(f"Total: $ {sTotal}\n")

    print(f"File {sName}_PaintJobOutput.txt was created.")


       # file.write(f"Paint charge:$ {str(f"{fPaintCost:,.2f"}")}")


main ()





