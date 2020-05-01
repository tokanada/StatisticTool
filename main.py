from unit_one import main as main1
from unit_two import main as main2
from unit_three import main as main3
from unit_four import main as main4
from unit_five import main as main5
from unit_six import main as main6
from unit_seven import main as main7
from unit_eight import main as main8
from unit_ten import main as main10


while(True):
    print()
    print("1: Unit 1: Statistic Definitions")
    print("2: Unit 2: Graphs and Distributions")
    print("3: Unit 3: Mean, Median, Mode, Standard Deviation, Chebyshev, Graph Distribution, Z-score, Percentiles.")
    print("4: Unit 4: Probability & Factorials & C & P")
    print("5: Unit 5: Binomial Distribution & Discrete Random Variables & Expected Values")
    print("6: Unit 6: Normal Distribution")
    print("7: Unit 7: Central Limit Theorem")
    print("8: Unit 8: Population Means & Proportions")
    print("10: Unit 10: Hypothesis Testing for Population Means")
    print("12: Unit 12: Correlation & Linear Regression")
    print("Anything else: Quit")
    user_input = input("Select A Unit: ")

    if user_input == str(1):
        main1()
    elif user_input == str(2):
        main2()
    elif user_input == str(3):
        main3()
    elif user_input == str(4):
        main4()
    elif user_input == str(5):
        main5()
    elif user_input == str(6):
        main6()
    elif user_input == str(7):
        main7()
    elif user_input == str(8):
        main8()
    elif user_input == str(10):
        main10()
    elif user_input == str(12):
        print("Unit 12")
    else:
        print("Goodbye o7")
        break