from fractions import Fraction

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

    print("Expected Value: " + str(eValue))

def main():
    while (True):
        print("1: Unit 5.1: Discrete Random Variables (Expected Value)")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            expectedValue()
        # elif user_input == str(2):
        #     unit22()
        else:
            break