def classic_probability():
    number_outcomes = float(input("Enter Number of Outcomes that the expected event will occur: "))
    sample_outcomes = float(input("Enter Total Number of Outcomes: "))
    print()
    print("====================")
    print("P(E) =", number_outcomes / sample_outcomes)
    print("====================")
    print()


def main():
    while (True):
        print("1: Unit 4.1 Classic Probability Formula")
        print("2: Unit 1.2: Data Classification")
        print("3: Unit 1.3: The Process of a Statistical Study")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            classic_probability()
        elif user_input == str(2):
            pass
        elif user_input == str(3):
            pass
        else:
            break