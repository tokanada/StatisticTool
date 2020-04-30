import numpy as np
from math import factorial

def classic_probability():
    number_outcomes = float(input("Enter Number of Outcomes that the expected event will occur: "))
    sample_outcomes = float(input("Enter Total Number of Outcomes: "))
    print()
    print("====================")
    print("P(E) =", number_outcomes / sample_outcomes)
    print("====================")
    print()


def compute_complement_rule():
    given = input("What is the probability you are given (decimal form): ")
    print()
    print("==========================")
    print("P(complement) =", 1 - given)


def compute_addition_rule():
    total = float(input("What is the total number of occurances? "))
    event_a = float(input("What is the number occurances for Event A: "))
    event_b = float(input("What is the number of occurences for Event B: "))
    event_ab = float(input("What is the number occurences for A & B: "))
    probability = (event_a/total) + (event_b/total) - (event_ab/total)
    print()
    print("============================")
    print("Probability(A or B) =", probability)
    print("============================")
    print()


def compute_multiplication_rule():
    data_list = []
    user_input = input("Do you know the probability already? (y/n/cancel): ")
    if user_input == 'y':
        while(True):
            user_input = input("Enter in probability (q to quit): ")
            if user_input == 'q':
                break
            data_list.append(float(user_input))
        print("Data List:", data_list)
    elif user_input == 'n':
        count = 1
        while (True):
            if count == 1:
                output = str(count) + "st "
            elif count == 2:
                output = str(count) + "nd "
            elif count == 3:
                output = str(count) + "rd "
            else:
                output = str(count) + "th "
            user_input = input("Enter in the maximum number of occurrences for the " + output + "event (q to stop): ")
            if user_input == 'q':
                break
            user_input2 = input("Enter in number of times the " + output + "event will occur: ")
            data_list.append(float(user_input2) / float(user_input))
            count += 1
        print("Data List:", data_list)
    else:
        return
    probability = np.prod(data_list)
    print()
    print("========================")
    print("Probability =", probability)
    print("========================")
    print()


def compute_conditional_rule():
    user_input = input("Do you know the probability already? (y/n/cancel): ")
    if user_input == 'y':
        combined = float(input("What is the probability of both events occuring: "))
        given = float(input("What is the probability of the given event: "))
    elif user_input == 'n':
        total = float(input("What is the maximum number of occurrences: "))
        combined_total = float(input("What is the number of occurrences for both events occuring: "))
        given_total = float(input("What is the number of occurrences for the given event: "))
        combined = combined_total / total
        given = given_total / total
    else:
        return
    probabilty = combined/given
    print()
    print("=====================")
    print("Conditional Probability =", probabilty)
    print("=====================")
    print()


def compute_fundamental():
    data_set = []
    while(True):
        user_input = input("Enter in possibilities one at a time (Enter q to stop): ")
        if user_input == 'q':
            break
        data_set.append(float(user_input))
    print("Dataset:",data_set)
    print()
    print("============================")
    print("Possible ways =", np.prod(data_set))
    print("============================")
    print()


def compute_fundamental_prob():
    data_set = []
    while (True):
        user_input = input("Enter in possibilities one at a time (Enter q to stop): ")
        if user_input == 'q':
            break
        data_set.append(float(user_input))
    print("Dataset:", data_set)
    user_input = float(input("Enter number of ways given event will occur: "))
    probability = user_input / np.prod(data_set)
    print()
    print("========================")
    print("Probability =", probability)
    print("========================")
    print()


def compute_factorial():
    factorialIntStorage = []
    multiFactorialAns = 1

    print("1: Standalone ex: 2!")
    print("2: Multiplication ex: 2! * 3!")
    print("3: Division ex: 2!/3!")
    print("4: Combination ex: 2!/(4-3)!")
    userInput = input("Enter: ")

    if userInput == str(1):
        standAloneInput = input("Enter the integer value: ")
        standAloneAns = factorial(float(standAloneInput))
        print()
        print(standAloneAns)
        print()
    elif userInput == str(2):
        token = True
        while(token):
            multiInput = input("Enter the integer value, or type 'q' to continue: ")
            if multiInput == str("q"):
                token = False
            else:
                factorialIntStorage.append(float(multiInput))
        for x in range(0, len(factorialIntStorage)):
            multiFactorialAns *= factorial(factorialIntStorage[x])
        print()
        print(multiFactorialAns)
        print()
    elif userInput == str(3):
        divisionInputTempX = input("Enter the numerator as an integer: ")
        divisionInputTempY = input("Enter the denominator as an integer: ")

        divisionFactorialAns = factorial(float(divisionInputTempX))/factorial(float(divisionInputTempY))

        print()
        print(divisionFactorialAns)
        print()
    elif userInput == str("4"):
        print("Simplify any parentheses before entering the integer values")

def compute_combinations(n, r):
    return (factorial(n)) / (factorial(r) * factorial(n - r))


def compute_permutations(n, r):
    return (factorial(n)) / (factorial(n - r))

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def compute_special_permutations_word(n):
    k_values = [n.count(i) for i in set(n)]
    print(k_values)
    n = len(n)
    print(n)
    return k_values, n

def compute_special_permutations():
    print()
    print("****************************************")
    print("Special Permutations involve objects that are identical. The number of distinguishable permutations of k1-kp objects are all alike, is given by:")
    print("(n!)/(k1! *k2! *...* kp!)")
    print("Where k1 + k2 + ... + kp = n")
    print("Example: How many arrangement of letters in TENNESSEE | T=1 (k1=1), E=4 (k2=4), etc.")
    print("****************************************")
    print()
    n = input("Enter n value(Length) or word to be rearrranged: ")
    data_list = []
    if not is_integer(n):
        data_list, n = compute_special_permutations_word(n.lower())
    else:
        count = 1
        while(True):
            user_input = input("Enter in k" + str(count) + " value (q to stop): ")
            count += 1
            if user_input == 'q':
                break
            data_list.append(float(user_input))
        print("K values =", data_list)
    bottom_value = 1
    for k in data_list:
        bottom_value *= factorial(k)
    permutation = factorial(n) / bottom_value
    print()
    print("====================================")
    print("Special Permutation =", permutation)
    print("====================================")
    print()

def main():
    while (True):
        print("1: Unit 4.1 Classic Probability Formula")
        print("2: Unit 4.2: Addition Rules for Probability")
        print("3: Unit 4.2: Complement Rule")
        print("4: Unit 4.3: Multiplication Rules for Probability")
        print("5: Unit 4.3: Multiplication Rules for Dependent Events (Conditional probability)")
        print("6: Unit 4.3: Fundamental Counting Principle")
        print("7: Unit 4.3: Fundamental Counting Principle to calculate Probability")
        print("8: Unit 4.4: Factorial Calculator")
        print("9: Unit 4.4: Combinations Calculator (Order doesn't matter)")
        print("10: Unit 4.4: Permutations Calculator (Order matters)")
        print("11: Unit 4.4: nPr/nCr Probability Calculator")
        print("12: Unit 4.4: Special Permutations")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            classic_probability()
        elif user_input == str(2):
            compute_addition_rule()
        elif user_input == str(3):
            compute_complement_rule()
        elif user_input == str(4):
            compute_multiplication_rule()
        elif user_input == str(5):
            compute_conditional_rule()
        elif user_input == str(6):
            compute_fundamental()
        elif user_input == str(7):
            compute_fundamental_prob()
        elif user_input == str(8):
            compute_factorial()
        elif user_input == str(9):
            n = float(input("Enter in n value (Group size)(nCr): "))
            r = float(input("Enter in r value (Number being arranged)(nCr): "))
            combination = compute_combinations(n, r)
            print()
            print("=============================")
            print(f"{n}C{r} = {combination}")
            print("=============================")
            print()
        elif user_input == str(10):
            n = float(input("Enter in n value (Group Size)(nPr): "))
            r = float(input("Enter in r value (Number being arranged)(nPr): "))
            permuation = compute_permutations(n, r)
            print()
            print("=============================")
            print(f"{n}P{r} = {permuation}")
            print("=============================")
            print()
        elif user_input == str(11):
            user_input = input("Enter 'c' for combination | Enter 'p' for permutation: ")
            if user_input == 'c':
                user_input = input("Do you know the combination? y/n: ")
                if user_input == 'y':
                    bottom_value = float(input("What is the combination: "))

                else:
                    n = float(input("Enter in n value (group size)(nCr): "))
                    r = float(input("Enter in r value (number being arranged)(nCr): "))
                    bottom_value = compute_combinations(n, r)
            elif user_input == 'p':
                user_input = input("Do you know the permutation? y/n: ")
                if user_input == 'y':
                    bottom_value = float(input("What is the permutation: "))
                else:
                    n = float(input("Enter in n value (group size)(nPr): "))
                    r = float(input("Enter in r value (number being arranged)(nPr): "))
                    bottom_value = compute_permutations(n, r)
            else:
                print("Invalid Entry")
                return
            outcomes = float(input("What is the number of outcomes for the given event: "))
            probability = outcomes / bottom_value
            print()
            print("========================")
            print("Probability =", probability)
            print("========================")
            print()
        elif user_input == str(12):
            compute_special_permutations()
        else:
            break