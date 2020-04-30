from fractions import Fraction
import math

def expectedValue():
    xValue = []
    pOfX = []
    eValue = 0

    token = True

    while(token):
        userInput = input("Enter in a 'x' value or 'q' to exit: ")
        if userInput.lower() == str('q'):
            token = False
        else:
            xValue.append(float(userInput))

    if token == False:
        token = True

    while(token):
        userInput = input("Enter in a 'p(x)' value or 'q' to exit: ")
        if userInput.lower() == str('q'):
            token = False
        else:
            pOfX.append(Fraction(userInput))

    for x in range(0, len(xValue)):
        eValue += xValue[x] * pOfX[x]

    print()
    print("=================")
    print("Expected Value: " + str(eValue))
    print("=================")
    print()

def binomialDistribution():
    userInput = input("Enter the number of trials (n): ")
    n = float(userInput)

    userInput = input("Enter the number of successes (x): ")
    x = float(userInput)

    userInput = input("Enter the probability (as a decimal) of getting a success on any trial (p): ")
    p = float(userInput)

    tempN = math.factorial(n)
    tempX = math.factorial(x)
    tempDifference = math.factorial(n - x)

    binomialP1 = tempN/(tempX * tempDifference)
    binomialP2 = pow(p, x) * pow(1 - p, n - x)
    binomialSum = binomialP1 * binomialP2

    print()
    print("=================")
    print("Binomial Distribution is: " + str(binomialSum))
    print("=================")
    print()

def main():
    while (True):
        print("1: Unit 5.1: Discrete Random Variables (Expected Value)")
        print("2: Unit 5.2: Binomial Distribution")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            expectedValue()
        elif user_input == str(2):
            binomialDistribution()
        else:
            break