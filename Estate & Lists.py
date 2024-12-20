
# Number 1 - set up

#fSalesPrice = getFloatInput ("Enter property sales value:")

def getFloatInput(sPrompt):
   fNumber = 0
   while fNumber <= 0 :
      try:
         fNumber = float(input(sPrompt))
      except ValueError:
         print("Input must a numeric value")
   return fNumber

def getMedian(listOfNumbers):
    fMedian = 0
    listOfNumbers.sort()
    if len(listOfNumbers) % 2 == 0:
        fMedian = (listOfNumbers[len(listOfNumbers)//2 - 1] + listOfNumbers[len(listOfNumbers)//2]) / 2
    else:
        fMedian = listOfNumbers[len(listOfNumbers)//2]
    return fMedian

def main ():
    listofnumbers = []
    while True:
        fNumber =getFloatInput (" Enter property sales value:")
        listofnumbers.append(fNumber)
        sChoice =input ("Enter another value Y or N: ")
        if sChoice == "N":
                break
    listofnumbers.sort()
    iCount = 1
    for property in listofnumbers:
        print(f"Property {iCount}: $ {property:,.2f}")
        iCount += 1
    #min, max, total average
    print(f"{'Min:':10s} $ {min(listofnumbers):,.2f}")
    print(f"{'Max:':10s} $ {max(listofnumbers):,.2f}")
    print(f"Total:{sum(listofnumbers)}")
    print(f"Average:{sum(listofnumbers)/len(listofnumbers)}")
    print(f"Comission: {sum(listofnumbers)*.03}")
    print(f"Median: {getMedian(listofnumbers)}")
main ()


