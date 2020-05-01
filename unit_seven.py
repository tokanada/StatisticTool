import numpy as np

def about_clt():
    print()
    print("==========================")
    print("CENTRAL LIMIT THEOREM")
    print("For any given population with mean, µ, and stddev, σ:")
    print("A sampling distribution of samples means will have these characteristics")
    print("If sample size, n, is at least 30 or the population is normally distribution")
    print("1: The mean of the sample equals the mean of the population")
    print("2: The stddev of the sample, σx, equals the stddev of the population, σ, divided by the sq. root of the sample size, n")
    print("         σx = (σ)/(√n)")
    print("3. The shape of the sample distribution will always be a normal distribution")
    print("==========================")
    print()


def compute_sample_stddev():
    n = float(input("Enter sample size (n): "))
    stddev = float(input("Enter population stddev: "))
    stddev = stddev / (np.sqrt(n))
    print()
    print("===========================")
    print(f"Sample Std. Deviation: {stddev}")
    print("===========================")
    print()
    return stddev

def compute_zscore_sample_mean():
    sample_mean = float(input("Enter sample mean (x): "))
    pop_mean = float(input("Enter population mean (µ): "))
    stddev = float(input("Enter population stddev (σ): "))
    n = float(input("Enter sample size (n): "))
    zscore = (sample_mean - pop_mean) / (stddev/np.sqrt(n))
    print()
    print("=======================")
    print(f"Z-Score: {zscore}")
    print("=======================")
    print()
    return zscore


def compute_proportion():
    x = float(input("Enter number of individuals: "))
    n = float(input("Enter sample/population size: "))
    p = x / n
    print()
    print("========================")
    print(f"p = {p}")
    print("========================")
    print()
    return p


def compute_proportion_mean():
    p = float(input("Enter proportion (p): "))
    print()
    print("================")
    print("Sample Mean =", p)
    print("================")
    print()


def compute_proportion_stddev():
    p = float(input("Enter proportion (p): "))
    n = float(input("Enter sample size (n): "))
    stddev = np.sqrt((p * (1 - p))/n)
    print()
    print("====================")
    print("Stddev =", stddev)
    print("====================")
    print()


def compute_proportion_zscore():
    sample_prop = float(input("Enter sample proportion: "))
    pop_prop = float(input("Enter population proportion: "))
    n = float(input("Enter sample size (n): "))
    zscore = (sample_prop - pop_prop) / np.sqrt((pop_prop * (1 - pop_prop))/n)
    print()
    print("=========================")
    print("Z-Score =", zscore)
    print("=========================")
    print()
    return zscore

def main():
    while (True):
        print()
        print("1: Unit 7.1: About the Central Limit Theorem")
        print("2: Unit 7.1: Find stddev of sample distribution")
        print("3: Unit 7.2: Finding Z-Score from sample mean (Normal Table)")
        print("4: Unit 7.3: Find Proportion (P)")
        print("5: Unit 7.3: Find Sample Mean from proportion")
        print("6: Unit 7.3: Find Sample stddev from proportion")
        print("7: Unit 7.3: Find Z-Score from proportion (Normal Table")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            about_clt()
        elif user_input == str(2):
            compute_sample_stddev()
        elif user_input == str(3):
            compute_zscore_sample_mean()
        elif user_input == str(4):
            compute_proportion()
        elif user_input == str(5):
            compute_proportion_mean()
        elif user_input == str(6):
            compute_proportion_stddev()
        elif user_input == str(7):
            compute_proportion_zscore()
        else:
            print()
            break