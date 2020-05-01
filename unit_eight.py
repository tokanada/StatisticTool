import numpy as np


def compute_point_estimate():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))
    sum = sum(data_list)
    point = sum / len(data_list)
    print()
    print("=====================")
    print("Point Estimate =", point)
    print("=====================")
    print()

def about_population_mean_standard_normal():
    print()
    print("=============================")
    print("Conditions that need to be met:")
    print("1. Simple Random Sample is used")
    print("2. Population Standard Deviation is known")
    print("3. Sample size is at least 30 (n>=30) or population distribution is normal")
    print("=============================")
    print("Z(a/2) stands for critical z-values. These mark the boundaries for the area under the middle of the standard normal curve")
    print("For example, let -Z(a/2) be -1.96 and let Z(a/2) be 1.96")
    print("The area under the normal curve between -Z and Z will be called 'c'")
    print("'c' in this case equals 0.95 (This will be the confidence level) ")
    print("The areas not in 'c' but are still under the curve is called 'a'")
    print("'a' is split into 2 sections (2 tails) and are referred to as a/2 individually")
    print("Hence why Z has the (a/2) on it")
    print("Now since 'c' is the confidence level. You now know that when\nconfidence level is 0.95, the z-critical score is 1.96")
    print("=============================")
    print()

def compute_zcritical():
    while(True):
        confidence_level = float(input("Enter confidence level (as decimal): "))
        if confidence_level == .80:
            print()
            print("======================")
            print("Z(a/2) = 1.28")
            print("======================")
            print()
            return 1.28
        elif confidence_level == .85:
            print()
            print("======================")
            print("Z(a/2) = 1.44")
            print("======================")
            print()
            return 1.44
        elif confidence_level == .90:
            print()
            print("======================")
            print("Z(a/2) = 1.645")
            print("======================")
            print()
            return 1.645
        elif confidence_level == .95:
            print()
            print("======================")
            print("Z(a/2) == 1.96")
            print("======================")
            print()
            return 1.96
        elif confidence_level == .98:
            print()
            print("======================")
            print("Z(a/2) == 2.33")
            print("======================")
            print()
            return 2.33
        elif confidence_level == .99:
            print()
            print("======================")
            print("Z(a/2) == 2.575")
            print("======================")
            print()
            return 2.575
        else:
            print()
            print("======================")
            print("Not a valid Confidence Value, Please Try Again")
            print("======================")
            print()

def compute_margin_error():
    user_input = input("Do you know the z-critical score (z(a/2))? (y/n): ")
    if user_input == 'y':
        z = float(input("Enter z critical score (z(a/2)): "))
    if user_input == 'n':
        z = compute_zcritical()
    user_input = input("Do you know the sample standard deviation (σx)? (y/n): ")
    if user_input == 'y':
        user_input = float(input("Enter sample stddev: "))
        e = z * user_input
    elif user_input == 'n':
        pop_std = float(input("Enter population stddev (σ): "))
        n = float(input("Enter sample size (n): "))
        e = z * (pop_std/np.sqrt(n))
    print()
    print("====================")
    print("Margin of Error (E) =", e)
    print("====================")
    print()
    return e

def about_confidence_interval():
    print()
    print("=============================")
    print("When comparing confidence intervals, take into account whether")
    print("the intervals of different methods overlap.")
    print("If they do, then you can have the assurance that the")
    print("methods have the same confidence level")
    print("Keep in mind about the upper and lower bounds, but do not make")
    print("assumptions with them")
    print("=============================")
    print()


def compute_minimum_sample():
    user_input = input("Do you know the z-critical score (z(a/2))? (y/n): ")
    if user_input == 'y':
        z = float(input("Enter Z-critical (z(a/2)): "))
    elif user_input == 'n':
        z = compute_zcritical()
    user_input = input("Do you know the margin of error (How many units from mean)? (y/n): ")
    if user_input == 'y':
        e = float(input("Enter margin of error (E): "))
    elif user_input == 'n':
        e = compute_margin_error()
    pop_std = float(input("Enter population standard deviation: "))
    min_size = ((z * pop_std)/e)**2
    print()
    print("=====================")
    print("Minimum Sample Size (n) =", min_size)
    print("=====================")
    print()
    return min_size


def about_tdistribution():
    print()
    print("========================")
    print("Properties of t-Distribution")
    print("1. A t-distribution curve is symmetric and bell-shaped. Centered around 0")
    print("2. A t-distribution curve is completely defined by its number of degrees of freedom (df)")
    print("3. Total area under t-distribution curve = 1")
    print("4. The x-axis is a horizontal asymptote for a t-distribution curve")
    print("========================")
    print("You use the 'Critical Values of t' table for this unit")
    print("Left Tail: Area to the left of 't'. The value from the table will be negated (-)")
    print("Right Tail: Area to the right of 't'. The value from the table is used directly")
    print("Two Tails: Area to the right & left of 't'. The value from two tails table is used")
    print("If you are given a problem that gives you the area inbetween the curve. Find its complement")
    print("========================")
    print("df = n - 1")
    print()

def compute_tcritical():
    c = float(input("Enter area under curve (level of confidence) as a decimal: "))
    n = float(input("Enter sample size (n): "))
    df = n - 1
    a = (1 - c) /2
    a = round(a,3)
    print()
    print("**************")
    print(f"t(a/2) = t{a}")
    print(f"Now find t{a} and df = {df} in the One Tail Table")
    print("**************")
    print()

def compute_margin_error_nosig():
    compute_tcritical()
    t = float(input("Enter the t(a/2) (critical value): "))
    s = float(input("Enter the sample standard deviation (s): "))
    n = float(input("Enter the sample size (n): "))
    e = t * (s/np.sqrt(n))
    print()
    print("========================")
    print("Margin of Error (E) =", e)
    print("========================")
    print()
    return e


def compute_margin_error_proportion():
    user_input = input("Do you know the Point Estimate (proportion)? (y/n): ")
    if user_input == 'y':
        p = float(input("Enter Point Estimate: "))
    elif user_input == 'n':
        p = compute_point_estimate_proportion()
    user_input = input("Do you know the Z-Critical? (y/n): ")
    if user_input == 'y':
        z = float(input("Enter Z-critical (Z(a/2)): "))
    elif user_input == 'n':
        z = compute_zcritical()
    n = float(input("Enter Sample Size (n): "))
    margin = z * np.sqrt((p * (1 - p)) / n)
    print()
    print("===================")
    print(f"Margin of Error (E) = {margin}")
    print("===================")
    print()
    return margin


def compute_confidence_interval():
    user_input = input("Do you know the margin of error (E)? (y/n) ")
    if user_input == 'y':
        margin = float(input("Enter margin of error (E): "))
    elif user_input == 'n':
        user_input = input("Calculate from Proportion? (y/n)")
        if user_input == 'y':
            margin = compute_margin_error_proportion()
        elif user_input == 'n':
            user_input = input("Do you know sigma (pop. stddev)? (y/n): ")
            if user_input == 'y':
                margin = compute_margin_error()
            elif user_input == 'n':
                margin = compute_margin_error_nosig()
    sample_mean = float(input("What is the Point Estimate (p for proportion | sample mean for mean): "))
    lower = sample_mean - margin
    upper = sample_mean + margin
    print()
    print("====================")
    print("Lower:", lower)
    print("Upper:", upper)
    print("====================")
    print()
    return [lower, upper]


def compute_point_estimate_proportion():
    x = float(input("Enter given group size: "))
    n = float(input("Enter sample size (n): "))
    p = x / n
    print()
    print("==============")
    print(f"p = {p}")
    print("==============")
    print()
    return p


def compute_minimum_sample_proportion():
    user_input = input("Do you know the population proportion (p)? (y/n): ")
    if user_input == 'y':
        p = float(input("Enter Population proportion (p): "))
    elif user_input == 'n':
        p = compute_point_estimate_proportion()
    user_input = input("Do you know the Z-critical (Z(a/2))? (y/n): ")
    if user_input == 'y':
        z = float(input("Enter Z-critical (Z(a/2)): "))
    elif user_input == 'n':
        z = compute_zcritical()
    user_input = input("Do you know the Margin of Error (E)? (y/n): ")
    if user_input == 'y':
        e = float(input("Enter Margin of Error (E)(decimal form): "))
    elif user_input == 'n':
        e = compute_margin_error_proportion()
    n = p * (1 - p) * (z/e)**2
    print()
    print("==============")
    print(f"Minimum Sample size (n) = {n}")
    print("==============")
    print()
    return n


def main():
    while (True):
        print()
        print("1: Unit 8.1: About Using Standard Normal Distribution to Estimate Population Mean")
        print("2: Unit 8.1: Finding point estimate (mean)")
        print("3: Unit 8.1: Find E (Margin of Error) with sigma known")
        print("\033[1m4: Unit 8: Find Confidence Interval with Margin of Error\033[0m")
        print("5: Unit 8.1: Find Z critical score (Z(a/2))")
        print("6: Unit 8.1: Interpreting a Confidence interval")
        print("\033[1m7: Unit 8.1: Find Minimum Sample Size for Estimating a Population Mean\033[0m")
        print("8: Unit 8.2: About t-Distribution")
        print("9: Unit 8.3: Find t-critical value (t(a/2))")
        print("10: Unit 8.3: Find E (Margin of Error) with sigma unknown")
        print("11: Unit 8.4: Find Point Estimate (proportion)")
        print("12: Unit 8.4: Find E (Margin of Error) with Proportions")
        print("\033[1m13: Unit 8.4: Find Minimum Sample for Estimating a Population Proportion\033[0m")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            about_population_mean_standard_normal()
        elif user_input == str(2):
            compute_point_estimate()
        elif user_input == str(3):
            compute_margin_error()
        elif user_input == str(4):
            compute_confidence_interval()
        elif user_input == str(5):
            compute_zcritical()
        elif user_input == str(6):
            about_confidence_interval()
        elif user_input == str(7):
            compute_minimum_sample()
        elif user_input == str(8):
            about_tdistribution()
        elif user_input == str(9):
            compute_tcritical()
        elif user_input == str(10):
            compute_margin_error_nosig()
        elif user_input == str(11):
            compute_point_estimate_proportion()
        elif user_input == str(12):
            compute_margin_error_proportion()
        elif user_input == str(13):
            compute_minimum_sample_proportion()
        else:
            print()
            break