import numpy as np

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


def main():
    while (True):
        print("1: Unit 4.1 Classic Probability Formula")
        print("2: Unit 4.2: Addition Rules for Probability")
        print("3: Unit 4.2: Complement Rule")
        print("4: Unit 4.3: Multiplication Rules for Probability")
        print("5: Unit 4.3: Multiplication Rules for Dependent Events (Conditional probability)")
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
        else:
            break