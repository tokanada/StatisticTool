import math
import numpy as np
import statistics as stat

def compute_mode(numbers):
    counts = {}
    maxcount = 0
    list = []
    for number in numbers:
        if number not in counts:
            counts[number] = 0
        counts[number] += 1
        if counts[number] > maxcount:
            maxcount = counts[number]
    if maxcount > 1:
        for number, count in counts.items():
            if count == maxcount:
                list.append([number, count])

    return list

def compute_mean_from_list():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))
    return np.mean(data_list)

def compute_stddev_from_list():
    user_input = input("Enter s for sample stddev, Enter p for population stddev: ")
    if user_input == 's':
        data_list = []
        while (True):
            user_input = input("Enter in data, q to stop: ")
            if user_input.lower() == 'q':
                break
            data_list.append(float(user_input))
        print("Data List:", str(data_list))
        return stat.stdev(data_list)
    elif user_input == 'p':
        data_list = []
        while (True):
            user_input = input("Enter in data, q to stop: ")
            if user_input.lower() == 'q':
                break
            data_list.append(float(user_input))
        print("Data List:", str(data_list))
        return stat.pstdev(data_list)

def unit31():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))
    mean = np.mean(data_list)
    median = np.median(data_list)
    mode = compute_mode(data_list)
    range = max(data_list) - min(data_list)
    print()
    print("========================")
    print("Mean:",mean)
    print("Median:",median)
    print("Mode:", mode)
    print("Range:", range)
    print("========================")
    print()


def unit31_definition():
    print()
    print("==============================")
    print("Mode is always located at the peak of a distribution")
    print("Median is the line that divides the area of the distribution in half")
    print("Mean is the line furthest from the skew of the graph. Ex: Skewed to the right -> Mean is the line closest to the right")
    print("==============================")
    print()

def compute_weighted_mean():
    data_list = []
    weighted_list = []
    while (True):
        user_input = input("Enter in data value (numbers only): ")
        data_list.append(float(user_input))
        user_input = input("Enter in data weight, q to stop: ")
        if user_input.lower() == 'q':
            break
        weighted_list.append(float(user_input))
    print()
    print("=========================")
    print(np.average(data_list, weights=weighted_list))
    print("=========================")
    print()

def compute_sample_std():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))
    stddev = stat.stdev(data_list)
    variance = stat.variance(data_list)
    range = max(data_list) - min(data_list)
    print()
    print("===================")
    print("Sample Std. Deviation:",stddev)
    print("Sample Variance:",variance)
    print("Range:", range)
    print("===================")
    print()

def compute_population_std():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))
    stddev = stat.pstdev(data_list)
    variance = stat.pvariance(data_list)
    range = max(data_list) - min(data_list)
    print()
    print("===================")
    print("Pop. Std. Deviation:", stddev)
    print("Pop Variance:", variance)
    print("Range:", range)
    print("===================")
    print()

def chebyshev_calculator():
    data_list = []
    user_input = input("Enter in lower value: ")
    data_list.append(float(user_input))
    user_input = input("Enter in upper value: ")
    data_list.append(float(user_input))
    user_input = input("Enter in std. deviation: ")
    data_list.append(float(user_input))
    user_input = input("Enter in mean: ")
    data_list.append(float(user_input))
    print("Data List:", str(data_list))
    stdev_below = (data_list[0] - data_list[3])/data_list[2]
    stdev_above = (data_list[1] - data_list[3])/data_list[2]
    percentage_below = 1 - (1/stdev_below**2)
    percentage_above = 1 - (1/stdev_above**2)
    print()
    print("====================")
    print("K below=",stdev_below)
    print("K above=",stdev_above)
    print("Percentage below (decimal form) =", percentage_below)
    print("Percentage above (decimal form) =", percentage_above)
    print("====================")
    print()

def empirical_rule_definition():
    print()
    print()
    print("=================Empirical Rule=================")
    print("*For bell-shaped data*")
    print("Approximately 68% of the data values lie within ONE standard deviation of the mean")
    print("Approximately 95% of the data values lie within TWO standard deviations of the mean")
    print("Approximately 99.7% of the data values lie within THREE standard deviations of the mean")
    print("================================================")
    print()
    print()

def compute_coefficient_of_variation():
    pop_stddev = input("Enter in standard deviation(Enter ? to calculate from list) : ")
    if pop_stddev == "?":
        pop_stddev = compute_stddev_from_list()
    else:
        pop_stddev = float(pop_stddev)
    pop_mean = input("Enter in mean (Enter ? to calculate from list): ")
    if pop_mean == '?':
        pop_mean = compute_mean_from_list()
    else:
        pop_mean = float(pop_mean)
    print()
    print("========================")
    print("Coefficient of variation =", (pop_stddev / pop_mean) * 100)
    print("========================")
    print()

def grouped_mean(mid, freq, n):
    sum = 0
    freqSum = 0
    for i in range(0,n):
        sum = sum + mid[i] * freq[i]
        freqSum = freqSum + freq[i]

    return sum / freqSum

def grouped_sd(lower, upper, freq, n):
    mid=[[0] for i in range(0,n)]
    sum = 0
    freqSum = 0
    sd = 0
    for i in range(0,n):
        mid[i] = (lower[i] + upper[i]) / 2
        sum = sum + freq[i] * mid[i] * mid[i]
        freqSum = freqSum + freq[i]

    sd = math.sqrt((sum - freqSum * grouped_mean(mid, freq, n) * grouped_mean(mid, freq, n)) / (freqSum - 1))
    return sd

def compute_grouped_stddev_variance():
    lower = []
    upper = []
    freq = []
    while(True):
        user_input = input("Enter in lower limit (one at a time), enter q when finished: ")
        if user_input == 'q':
            break
        lower.append(float(user_input))
    print()
    while(True):
        user_input = input("Enter in upper limit (one at a time), enter q when finished: ")
        if user_input == 'q':
            break
        upper.append(float(user_input))
    print()
    while(True):
        user_input = input("Enter in frequency, enter q when finished: ")
        if user_input == 'q':
            break
        freq.append(int(user_input))
    n = len(lower)
    sd = grouped_sd(lower, upper, freq, n)
    print()
    print("====================")
    print("Grouped Std. Deviation:", sd)
    print("Grouped Variance:", sd**2)
    print("====================")
    print()

def compute_empirical_rule():
    print("Please note that this only does basic calculations. Won't work for complex questions")
    upper = float(input("Enter in upper bound: "))
    mean = float(input("Enter mean: "))
    stddev = float(input("Enter std. deviation: "))
    stdev_above = int((upper - mean) / stddev)
    if stdev_above == 0:
        print()
        print("====================")
        print("Percentage: 0%")
        print("====================")
        print()
    elif stdev_above == 1:
        print()
        print("====================")
        print("Percentage: 68%")
        print("====================")
        print()
    elif stdev_above == 2:
        print()
        print("====================")
        print("Percentage: 95%")
        print("====================")
        print()
    elif stdev_above == 3:
        print()
        print("====================")
        print("Percentage: 99.7%")
        print("====================")
        print()

def compute_location_percentile():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))
    print()
    percentile = int(input("Enter percentile to locate: "))
    print()
    print("=================")
    print("Location =", np.percentile(data_list, percentile))
    print("=================")
    print()

def compute_z_score():
    observed_value = float(input("Enter observed value (x): "))
    mean = input("Enter mean (Enter ? to calculate from list: ")
    if mean == '?':
        mean = compute_mean_from_list()
    else:
        mean = float(mean)
    stddev = input("Enter stddev (Enter ? to calculate from list: ")
    if stddev == '?':
        stddev = compute_stddev_from_list()
    else:
        stddev = float(stddev)

    print()
    print("===================")
    print("Z-Score =", (observed_value - mean) / stddev)
    print("===================")
    print()


def compute_total_from_percentile():
    partial = int(input("Enter Partial Sample Size (Ex: 'Twenty-four of the families in the sampled turned on the television for 20 hours or less for the week'): "))
    percentile = int(input("What is the percentile: "))
    print()
    print("======================")
    print("Total Number: ", (100/percentile) * partial)
    print("======================")
    print()

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def compute_five_number_summary():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    data_list.sort()
    print("Data List:", str(data_list))
    print()
    first = min(data_list)
    fifth = max(data_list)

    print(data_list[:len(data_list) // 2])
    second = np.median(data_list[:len(data_list) // 2])
    third = np.median(data_list)
    print(data_list[len(data_list) //2:])
    fourth = np.median(data_list[len(data_list) //2 if len(data_list)%2 == 0
                                 else ((len(data_list)//2)+1):])

    print()
    print("=======================")
    print(f"Answer: {first},{second},{third},{fourth},{fifth}")
    print("=======================")
    print()


def main():
    while (True):
        print("1: Mean, Median, Mode, Range")
        print("2: Weighted Mean")
        print("3: Determining Mean, Median, and Mode From a Graph")
        print("4: Determine sample std. deviation, variance, and range")
        print("5: Determine population std. deviation, variance, and range")
        print("6: Chebyshev's Theorem Calculator")
        print("7: Info on Empirical Rule & Calculator")
        print("8: Coefficient of Variation Calculator (Finding the size of variation)")
        print("9: Determine stddev and variance of grouped data")
        print("10: Determine location of the X percentile")
        print("11: Calculate Z Score")
        print("12: Calculate total sample size in percentile sample")
        print("13: Calculate five-number summary")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            unit31()
        elif user_input == str(2):
            compute_weighted_mean()
        elif user_input == str(3):
            unit31_definition()
        elif user_input == str(4):
            compute_sample_std()
        elif user_input == str(5):
            compute_population_std()
        elif user_input == str(6):
            chebyshev_calculator()
        elif user_input == str(7):
            empirical_rule_definition()
            compute_empirical_rule()
        elif user_input == str(8):
            compute_coefficient_of_variation()
        elif user_input == str(9):
            compute_grouped_stddev_variance()
        elif user_input == str(10):
            compute_location_percentile()
        elif user_input == str(11):
            compute_z_score()
        elif user_input == str(12):
            compute_total_from_percentile()
        elif user_input == str(13):
            compute_five_number_summary()
        else:
            break