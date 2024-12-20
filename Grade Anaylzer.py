
sName = input( "Please enter your name: ")
iTest1 = int(input("Please enter your Test 1: "))
iTest2 = int(input("Please enter your Test 2: "))
iTest3 = int(input("Please enter your Test 3: "))
iTest4 = int(input("Please enter your Test 4: "))

if iTest1 <= 0 or iTest2 <= 0 or iTest3 <=0 or iTest4 <= 0:
        exit()

sChoice = input ("Do you want to drop your lowest grade?: Y/N ")
if sChoice != "Y" and sChoice != "N":
    exit ("Error, Enter Y or N to Drop lowest grade: ")

iDivisionFactor = 4
iLowest = 0

if sChoice == "Y":

    iDivisionFactor = 3

    if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4 :
        iTest1 = iLowest
    elif iTest2 < iTest3 and iTest2 < iTest4:
        iTest2 = iLowest
    elif iTest3 < iTest4:
        iTest3 = iLowest
    else:
        iLowest = iTest4

fAverage = (iTest1 + iTest2 + iTest3 + iTest4 - iLowest) / iDivisionFactor

sGrade = ""
if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.00:
    sGrade = "A"
elif fAverage >= 90.00:
    sGrade = "A-"
elif fAverage >= 87.0:
 sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

print (f"{sName} test average is: {fAverage:.1f}")
print (f" Letter grade: {sGrade}")


