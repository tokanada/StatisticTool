import numpy as np
from scipy import stats

from unit_eight import about_tdistribution, compute_point_estimate_proportion


def print_hypothesis_conclusion(outcome, type):
    if outcome:
        print()
        print("====================")
        print(f"{type}")
        print("Accept the Null Hypothesis")
        print("Claim is refuted")
        print("====================")
        print()
    else:
        print()
        print("====================")
        print(f"{type}")
        print("Reject the Null Hypothesis")
        print("Claim is Supported")
        print("====================")
        print()

def check_pvalue(p, significance):
    print()
    print("**************")
    print(f"P-Value = {p}")
    print("**************")
    print()
    if p < significance:
        print_hypothesis_conclusion(False, "P-Value Test")
        return False
    else:
        print_hypothesis_conclusion(True, "P-Value Test")
        return True

def check_pvalue_proportion(p, significance):
    print()
    print("**************")
    print(f"P-Value = {p}")
    print("**************")
    print()
    if p <= significance:
        print_hypothesis_conclusion(False, "P-Value Test")
        return False
    else:
        print_hypothesis_conclusion(True, "P-Value Test")
        return True

def compute_level_significance():
    c = float(input("Enter Confidence Level (as decimal): "))
    a = 1 - c
    print()
    print("**********")
    print("Level of Significance =",a)
    print("**********")
    print()
    return a

def test_proportion_values(p, n):
    np = n * p
    np2 = n * (1 - p)
    return np, np2 > 5

def about_hypothesis():
    print()
    print("===============================")
    print("H1: Null Hypothesis")
    print("Assume Null Hypothesis to be true")
    print("Ha: Alternative Hypothesis")
    print("Test the Alternative Hypothesis")
    print("===============================")
    print("Example:")
    print("Claim by manager of candy plant: Mean weight of chocolate bars is less than correct weight")
    print("Correct weight is µ(mean) = 4")
    print("Alternative Hypothesis: Ha: µ < 4 ")
    print("Null Hypothesis (the negation): H0: µ ≥ 4")
    print("===============================")
    print("The two available terms are µ and p")
    print("Use the keypad on Hawkes Learning")
    print()


def about_test_statistic():
    print()
    print("===============================")
    print("Test Statistic is the value used to make a decision about the null hypothesis")
    print("Derived from the sample statistic")
    print("===============================")
    print("Refer to example in About the Null and Alternative Hypothesis")
    print("What would determine if the null hypothesis is correct or wrong")
    print("Would a weight of 3.01 disprove it? Would 3.9?")
    print("===============================")
    print("If the Test Statistic is 'statistically significant' then it can accept or reject the null hypothesis")
    print("Use a confidence interval to determine if it is significant")
    print("a (level of significance) = 1 - c (confidence level)")
    print("===============================")
    print("If the null hypothesis is rejected, then the claim is true")
    print("===============================")


def about_testing_errors():
    print()
    print("==============================")
    print("Type I Error| Rejecting a TRUE null hypothesis")
    print("Type II Error| Accepting a FALSE null hypothesis")
    print("==============================")
    print("α = probability of a Type I error")
    print("β = probability of a Type II error")
    print("==============================")
    print()


def compute_test_statistic_mean_sigma():
    sample_mean = float(input("Enter Sample Mean (x): "))
    pop_mean = float(input("Enter the Claimed Mean (µ)"))
    pop_std = float(input("Enter the Population Standard Deviation (σ)"))
    n = float(input("Enter sample size (n): "))
    z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))
    print()
    print("=====================")
    print("Test Statistic (z) =", z)
    print("=====================")
    print()
    return z


def about_rejection_regions():
    print()
    print("===============================")
    print("Rejection Regions: Used to determine if the test statistic is statistically significant")
    print("===============================")
    print("Criteria:")
    print("1. The Type of Hypothesis Test")
    print("2. The Level of Significance")
    print("===============================")
    print("Types of tests")
    print("Alternative Hypothesis: < Value || Type of test: Left-Tailed Test || Reject if z ≤ −z(a).")
    print("Alternative Hypothesis: > Value || Type of test: Right-Tailed Test || Reject if z ≥ z(a)")
    print("Alternative Hypothesis: ≠ Value || Type of test: Two-Tailed Test || Reject if |z| ≥ z(a/2)")
    print("===============================")
    print()

def compute_zcritical_region():
    while (True):
        confidence_level = float(input("Enter confidence level or level of significance (c or a)(as decimal): "))
        about_rejection_regions()
        user_input = input("Two or One-Tailed? (2 or 1): ")
        if user_input == '2' or user_input.lower() == 'two':
            if confidence_level == .90 or confidence_level == .1:
                print()
                print("======================")
                print("±Z(a/2) = ±1.645")
                print("======================")
                print()
                return 1.645, confidence_level
            elif confidence_level == .95 or confidence_level == .05:
                print()
                print("======================")
                print("±Z(a/2) = ±1.96")
                print("======================")
                print()
                return 1.96, confidence_level
            elif confidence_level == .98 or confidence_level ==.02:
                print()
                print("======================")
                print("±Z(a/2) = ±2.33")
                print("======================")
                print()
                return 2.33, confidence_level
            elif confidence_level == .99 or confidence_level == .01:
                print()
                print("======================")
                print("±Z(a/2) = ±2.575")
                print("======================")
                print()
                return 2.575, confidence_level
            else:
                print()
                print("======================")
                print("Not a valid Confidence Value, Please Try Again")
                print("======================")
                print()
        elif user_input == '1' or user_input == 'one':
            if confidence_level == .90 or confidence_level == .1:
                print()
                print("======================")
                print("Z(a) = 1.28")
                print("======================")
                print()
                return 1.28, confidence_level
            elif confidence_level == .95 or confidence_level == .05:
                print()
                print("======================")
                print("Z(a) = 1.645")
                print("======================")
                print()
                return 1.645, confidence_level
            elif confidence_level == .98 or confidence_level == .02:
                print()
                print("======================")
                print("Z(a) = 2.05")
                print("======================")
                print()
                return 2.05, confidence_level
            elif confidence_level == .99 or confidence_level == .01:
                print()
                print("======================")
                print("Z(a) = 2.33")
                print("======================")
                print()
                return 2.33, confidence_level
            else:
                print()
                print("======================")
                print("Not a valid Confidence Value, Please Try Again")
                print("======================")
                print()

def compute_test_statistic_mean_nosigma():
    sample_mean = float(input("Enter Sample Mean (x): "))
    pop_mean = float(input("Enter the Claimed Mean (µ)"))
    sample_std = float(input("Enter the Sample Standard Deviation (σ)"))
    n = float(input("Enter sample size (n): "))
    t = (sample_mean - pop_mean) / (sample_std / np.sqrt(n))
    print()
    print("=====================")
    print("Test Statistic (t) =", t)
    print("=====================")
    print()
    return round(t,3)

def compute_test_statistic_proportion():
    user_input = input("Do you know the sample proportion (p)? (y/n): ")
    if user_input == 'y':
        sp_proportion = float(input("Enter sample proportion (decimal): "))
    else:
        sp_proportion = compute_point_estimate_proportion()
    user_input = input("Do you know the claimed proportion)? (y/n): ")
    if user_input == 'y':
        pop_proportion = float(input("Enter claimed proportion (decimal): "))
    else:
        pop_proportion = compute_point_estimate_proportion()
    n = int(input("Enter sample size (n): "))
    pass_test = test_proportion_values(pop_proportion, n)
    if not pass_test:
        print()
        print("XXXXXXXXXXXXX")
        print("Proportion Conditions not met")
        print("XXXXXXXXXXXXX")
        print()
        return None
    z = (sp_proportion - pop_proportion) / np.sqrt((pop_proportion * (1 - pop_proportion))/ n)
    print()
    print("=====================")
    print("Test Statistic (z) = ", z)
    print("=====================")
    print()
    return z

def check_hypothesis_pass():
    test_type = input("Do you know Population Stddev σ and Population Mean μ? (y/n): ")
    if test_type == 'y':
        about_hypothesis()
        alt_hypothesis = input("What is the Alternative Hypothesis? (Ex, u <= 26.5 or u != 26.5): ")
        null_hypothesis = input("What is the Null Hypothesis? (Ex, u > 26.5): ")
        print()
        print("*****************")
        print(f"H0: {null_hypothesis}\nHa: {alt_hypothesis}")
        print("*****************")
        print()
        if "<" in alt_hypothesis or "<=" in alt_hypothesis:
            tail = 'left'
        elif ">" in alt_hypothesis or ">=" in alt_hypothesis:
            tail = 'right'
        elif "!=" in alt_hypothesis:
            tail = 'two'
        else:
            tail = ""
        zcritical, confidence = compute_zcritical_region()
        if confidence > .1:
            confidence = 1 - confidence
        print("Confidence Level:",confidence)
        z = compute_test_statistic_mean_sigma()
        p_value = stats.norm.sf(abs(z))
        while(True):
            if len(tail) < 3:
                about_rejection_regions()
                tail = input("Based on the alternative hypothesis, which tail should this program test? (left, right, two): ")
            if tail == 'left':
                check_pvalue(p_value, confidence)
                if z <= -zcritical:
                    print_hypothesis_conclusion(False, "Rejection Region Test")
                    return False
                else:
                    print_hypothesis_conclusion(True, "Rejection Region Test")
                    return True
            elif tail == 'right':
                check_pvalue(p_value, confidence)
                if z >= zcritical:
                    print_hypothesis_conclusion(False, "Rejection Region Test")
                    return False
                else:
                    print_hypothesis_conclusion(True, "Rejection Region Test")
                    return True
            elif tail == 'two':
                p_value *= 2
                check_pvalue(p_value, confidence)
                if abs(z) >= zcritical:
                    print_hypothesis_conclusion(False, "Rejection Region Test")
                    return False
                else:
                    print_hypothesis_conclusion(True, "Rejection Region Test")
                    return True
            else:
                print("Incorrect option, please try again")
    test_type = input("Do you know the Sample Stddev and the Population Mean? (y/n): ")
    if test_type == 'y':
        about_hypothesis()
        alt_hypothesis = input("What is the Alternative Hypothesis? (Ex, u <= 26.5 or u != 26.5): ")
        null_hypothesis = input("What is the Null Hypothesis? (Ex, u > 26.5): ")
        print()
        print("*****************")
        print(f"H0: {null_hypothesis}\nHa: {alt_hypothesis}")
        print("*****************")
        print()
        if "<" in alt_hypothesis or "<=" in alt_hypothesis:
            tail = 'left'
        elif ">" in alt_hypothesis or ">=" in alt_hypothesis:
            tail = 'right'
        elif "!=" in alt_hypothesis:
            tail = 'two'
        else:
            tail = ""
        a = float(input("What is the Level of Significance? (a = c - 1): "))
        t = compute_test_statistic_mean_nosigma()
        n = int(input("What is the sample size (n): "))
        df = n - 1
        while (True):
            about_tdistribution()
            if len(tail) < 3:
                about_rejection_regions()
                tail = input(
                    "Based on the alternative hypothesis, which tail should this program test? (left, right, two): ")
            if tail == 'left':
                print("This is a left-tail problem, so t will be negative")
                print(f"Find the value with a = {a} and df = {df}")
                print()
                rejection_region = float(input("Enter the critical t-score value: "))
                if rejection_region > 0:
                    rejection_region *= -1
                if t <= rejection_region:
                    print_hypothesis_conclusion(False, "Rejection Region Test")
                    return False
                else:
                    print_hypothesis_conclusion(True, "Rejection Region Test")
                    return True
            elif tail == 'right':
                print("This is a right-tail problem, so t will be positive")
                print(f"Find the value with a = {a} and df = {df}")
                print()
                rejection_region = float(input("Enter the critical t-score value: "))
                if t >= rejection_region:
                    print_hypothesis_conclusion(False, "Rejection Region Test")
                    return False
                else:
                    print_hypothesis_conclusion(True, "Rejection Region Test")
                    return True
            elif tail == 'two':
                print("This is a two-tail problem, so use the two tail table")
                print(f"Find the value with a = {a} and df = {df}")
                print()
                rejection_region = float(input("Enter the critical t-score value: "))
                if abs(t) >= rejection_region:
                    print_hypothesis_conclusion(False, "Rejection Region Test")
                    return False
                else:
                    print_hypothesis_conclusion(True, "Rejection Region Test")
                    return True
            else:
                print("Incorrect option, please try again")
    test_type = input("Do you know the proportion of the population (percentages)? (y/n): ")
    if test_type == 'y':
        about_hypothesis()
        alt_hypothesis = input("What is the Alternative Hypothesis? (Ex, u <= 26.5 or u != 26.5): ")
        null_hypothesis = input("What is the Null Hypothesis? (Ex, u > 26.5): ")
        print()
        print("*****************")
        print(f"H0: {null_hypothesis}\nHa: {alt_hypothesis}")
        print("*****************")
        print()
        if "<" in alt_hypothesis or "<=" in alt_hypothesis:
            tail = 'left'
        elif ">" in alt_hypothesis or ">=" in alt_hypothesis:
            tail = 'right'
        elif "!=" in alt_hypothesis:
            tail = 'two'
        else:
            tail = ""
        a = float(input("What is the Level of Significance? (a = c - 1): "))
        z = compute_test_statistic_proportion()
        p_value = stats.norm.sf(abs(z))
        if z == None:
            return
        while (True):
            if len(tail) < 3:
                about_rejection_regions()
                tail = input(
                    "Based on the alternative hypothesis, which tail should this program test? (left, right, two): ")
            if tail == 'left' or tail == 'right':
                return check_pvalue_proportion(p_value, a)
            elif tail == 'two':
                p_value *= 2
                return check_pvalue_proportion(p_value, a)
            else:
                print("Incorrect option, please try again")
    else:
        print("Well I don't know what you want then")

def about_pvalue():
    print()
    print("==========================")
    print("A p-value is the probability of obtaining a sample statistic as extreme or\n"
          "more extreme than the one observed in the data, when the null hypothesis, H0,\n"
          "is assumed to be true")
    print("==========================")
    print("Find p-value by finding the test statistic")
    print("Left Tailed: P(z ≤ test statistic")
    print("Right Tailed: P(z ≥ test statistic")
    print("Two Tailed: P(|z| ≥ test statistic")
    print("Use the Standard Normal to find the Z-values")
    print("For two tails, multiply the z-value by 2")
    print("==========================")
    print("If p ≤ level of significance: reject null")
    print("If p > level of significance: accept null")
    print("==========================")
    print()


def compute_pvalue():
    u_input = input("Population mean or Population Proportion? (mean, proportion): ")
    if u_input.lower() == 'mean':
        z = compute_test_statistic_mean_sigma()
    elif u_input.lower() == 'proportion':
        z = compute_test_statistic_proportion()
    p = stats.norm.sf(abs(z))
    u_input = input("Single or Two-Tails? (1, 2)")
    if u_input == '2':
        p *= 2
    print()
    print("++++++++++")
    print("P Value =", p)
    print("++++++++++")
    print()
    return p






def main():
    while (True):
        print()
        print("\033[1m1: Unit 10: Test Validity of Claim\033[0m")
        print("2: Unit 10.1: About the Null and Alternative Hypothesis")
        print("3: Unit 10.1: About the Test Statistic")
        print("4: Unit 10.1: About Types of Errors in Hypothesis testing")
        print("5: Unit 10.2: About Rejection Regions")
        print("6: Unit 10.2: Find Test Statistic for Population Mean (sigma known)")
        print("7: Unit 10.2: Find Z critical score for rejection regions (Z(a) & Z(a/2))")
        print("8: Unit 10.2: About p-Values")
        print("9: Unit 10.2: Find P-Value")
        print("10: Unit 10.3: Find Test Statistic for Population Mean (sigma unknown)")
        print("11: Unit 10.4: Find Test Statistic for Proportion")
        print("12: Unit 10.4: Find Proportion")
        print("Other: Return")
        user_input = input("Enter a selection: ")
        if user_input == str(1):
            check_hypothesis_pass()
        elif user_input == str(2):
            about_hypothesis()
        elif user_input == str(3):
            about_test_statistic()
        elif user_input == str(4):
            about_testing_errors()
        elif user_input == str(5):
            about_rejection_regions()
        elif user_input == str(6):
            compute_test_statistic_mean_sigma()
        elif user_input == str(7):
            compute_zcritical_region()
        elif user_input == str(8):
            about_pvalue()
        elif user_input == str(9):
            compute_pvalue()
        elif user_input == str(10):
            compute_test_statistic_mean_nosigma()
        elif user_input == str(11):
            compute_test_statistic_proportion()
        elif user_input == str(12):
            compute_point_estimate_proportion()
        else:
            print()
            break