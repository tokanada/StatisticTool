def zScoreCal():
    #Normalize the distribution or whatever it means
    userInput = input("Enter the x-value: ")
    x = float(userInput)

    userInput = input("Enter the mean: ")
    mean = float(userInput)

    userInput = input("Enter the standard deviation: ")
    stanDev = float(userInput)

    temp = x - mean
    zScore = temp/stanDev

    print()
    print("=================")
    print("The Z-Score is: " + str(zScore))
    print("=================")
    print()

def areaUnderCurve():

    print("1: Area under the curve (help on how to find, table is provided on Hawkes)")
    print("2: Area between two points (area is inward from z1 and z2)")
    print("3: Area between two tails (area is outward from z1 and z2)")
    userInput = input("Enter: ")

    if userInput == str("1"):
        print()
        print("The cumulative normal curve tables we are using only give the area to the left of a given z-value, "
              "\nbut we can use the tables, along with the properties of the standard normal distribution, "
              "\nto find other areas as well. First, let's consider the area to the right of a given z-score. "
              "\nTo obtain this area, remember that the total area under the standard normal curve is 1. "
              "\nSo, if the table gives us the area to the left of z, then subtracting that area from 1 gives us the area "
              "\nto the right of z.")
        print()
    elif userInput == str("2"):
        areaBetweenTwoPoints()
    elif userInput == str("3"):
        areaTwoTail()

def areaBetweenTwoPoints():
    print("Typically z1 will be the negative value, and z2 will be the positive value")
    userInput = input("Enter the z1 value (typically the value on the left): ")
    z1 = float(userInput)

    userInput = input("Enter the z2 value (typically the value on the right): ")
    z2 = float(userInput)

    areaBetween = z2 - z1

    print()
    print("=================")
    print("The area between z1 and z2 is: " + str(areaBetween))
    print("=================")
    print()

def areaTwoTail():
    print("Are the z-values the same number, just positive and negative? (ie: -2 and 2): Y/N")
    tempInput = input("Enter: ")

    if tempInput.lower() == str("y"):
        userInput = input("Enter the z1 value: ")
        doubleZ = float(userInput) * 2

        print()
        print("=================")
        print("The combined area of z1 and z2 is: " + str(doubleZ))
        print("=================")
        print()
    elif tempInput.lower() == str("n"):
        userInput = input("Enter the z1 value: ")
        z1 = float(userInput)

        userInput = input("Enter the z2 value: ")
        z2 = float(userInput)

        areaTwoTailAns = z1 + z2

        print()
        print("=================")
        print("The combined area of z1 and z2 is: " + str(areaTwoTailAns))
        print("=================")
        print()

def spittinFactsP1():
    print()
    print("Find the Z-Score, then check the table."
          "\nIf the problem asks to for an answer that 'Differs by Less', it's asking for the area between."
          "\nIf it's asking for an answer that 'Differs by More', it's asking for the area of two tails combined.")
    print()

def spittinFactsP2():
    print("Are you searching for x?: Y/N")
    userInput = input("Enter: ")

    if userInput.lower() == str("n"):
        print()
        print("Take the given area and compare it to 0.5, if the given area"
              "\n is greater than 0.5 then the z-score will be positive."
              "\nIf it's less than, then the z-score will be negative.")
        print(
            "If the question is about percentiles, find the closest area in the table and use its z-score as the answer.")
        print(
            "If the question is looking for the z-score of the area between two points that are the same but with differing signs"
            "\n(ie: 2 and -2), take the total area given and subtract it from 1."
            "\nThen divide the result by 2. After that, go into the table and find 2 areas that are close to the result."
            "\nTake the z-score that is the halfway mark between the 2 z-scores of the 2 areas as your answer."
            "\n This is literally the same as two-tails")
        print()
    elif userInput.lower() == str("y"):
        xFinder()

def xFinder():
    x = 0
    tempInput = input("Enter in the z-score: ")
    z = float(tempInput)

    tempInput = input("Enter in the mean: ")
    mean = float(tempInput)

    tempInput = input("Enter in the standard deviation: ")
    sigma = float(tempInput)

    x = (z * sigma) + mean

    print()
    print("=================")
    print("The random variable (or x) is: " + str(x))
    print("=================")
    print()

def main():
    while (True):
        print("1: Unit 6.1: Normal Distribution (Normalize Z-Scores)")
        print("2: Unit 6.2: Finding the Area Under the Curve")
        print("3: Unit 6.3: Finding Probability Using a Normal Distribution")
        print("4: Unit 6.4: Finding Values of a Normally Distributed Random Variable (Also contains Percentiles)")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            zScoreCal()
        elif user_input == str(2):
            areaUnderCurve()
        elif user_input == str(3):
            spittinFactsP1()
        elif user_input == str(4):
            spittinFactsP2()
        else:
            break