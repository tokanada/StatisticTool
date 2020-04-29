def class_boundary_calculator(lower_limit, upper_limit):
    return float((lower_limit + upper_limit) / 2)

def relative_frequency_calculator(frequency_list):
    total_frequency = sum(frequency_list)
    relative_frequency_list = []
    for frequency in frequency_list:
        relative_frequency_list.append(frequency / total_frequency)
    return relative_frequency_list

def cumulative_frequency_calculator(frequency_list):
    cumulative_frequency_list = []
    count = 0
    for frequency in frequency_list:
        count += frequency
        cumulative_frequency_list.append(count)
    return cumulative_frequency_list

def frequency_distribution_maker():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    print("Data List:", str(data_list))

    class_number = float(input("What is the amount of classes: "))
    max_value = max(data_list)
    min_value = min(data_list)
    class_width = (max_value - min_value) / class_number
    print("Class Width:", class_width)
    user_input = input("Change class width? Enter your own, or n to cancel: ")
    if user_input.lower() != 'n':
        class_width = float(user_input)
    user_input = input("Starting point will be " + str(min_value) + ". Enter new value to change, or n to cancel: ")
    if user_input.lower() != 'n':
        min_value = float(user_input)
    subtract_value = 0
    while(True):
        user_input = input("What is the place value significance? (Aka, does the data end in the ones, tenths, hundredths, etc.): ")
        if user_input.lower() == "ones" or user_input.lower() == "one":
            subtract_value = 1
            break
        elif user_input.lower() == "hundredth" or user_input.lower() == "hundredths":
            subtract_value = 0.01
            break
        elif user_input.lower() == "tenth" or user_input.lower() == "tenths":
            subtract_value = 0.1
            break
        elif user_input.lower() == "thousandth" or user_input.lower() == "thousandths":
            subtract_value = 0.001
            break
        else:
            print("Error: Not a valid response. Please try again")
    class_list = []
    for i in range(0, int(class_number)):
        end_range = min_value + class_width - subtract_value
        temp_list = [min_value, end_range]
        class_list.append(temp_list)
        min_value += class_width
    print("=============================")
    print("Class List:", class_list)
    frequency_list = []
    midpoint_list = []
    boundaries = []
    end_value = class_list[0][0] - subtract_value
    for ranges in class_list:
        start_value = ranges[0]
        boundaries.append(class_boundary_calculator(start_value, end_value))
        end_value = ranges[1]
        midpoint_list.append(class_boundary_calculator(start_value, end_value))
        count = 0
        for value in data_list:
            if value >= start_value and value <= end_value:
                count += 1
        frequency_list.append(count)

    print("Frequency:", frequency_list)
    print("Midpoint:", midpoint_list)
    print("Boundaries:", boundaries)
    print("Relative Frequency:", relative_frequency_calculator(frequency_list))
    print("Cumulative Frequency:", cumulative_frequency_calculator(frequency_list))
    print("=============================")
    print()

def unit21():
    print()
    print()
    print("Unit 2.1")
    while(True):
        print("1: Frequency Distribution Maker")
        print("2: Class Boundary Calculator")
        print("3: Class Midpoint Calculator")
        print("4: Relative Frequency Calculator")
        print("5: Cumulative Frequency Calculator")
        print("Other: Exit")
        user_input = input("Select an option: ")
        if user_input == str(1):
            frequency_distribution_maker()
        elif user_input == str(2):

            temp_input = input("Are you searching for the upperbound or the lowerbound?: ")

            if temp_input.lower() == str("lowerbound"):
                lower_limit = float(input("Enter Upperbound of Previous Class: "))
                upper_limit = float(input("Enter Lowerbound of Given Class: "))
                print("=================")
                print("Class Boundary:", str(class_boundary_calculator(lower_limit, upper_limit)))
                print("=================")
                print()
            elif temp_input.lower() == str("upperbound"):
                lower_limit = float(input("Enter Upperbound of Given Class: "))
                upper_limit = float(input("Enter Lowerbound of Next Class: "))
                print("=================")
                print("Class Boundary:", str(class_boundary_calculator(lower_limit, upper_limit)))
                print("=================")
                print()

        elif user_input == str(3):
            lower_limit = float(input("Enter Lower Limit: "))
            upper_limit = float(input("Enter Upper Limit: "))
            print("=================")
            print("Midpoint:", str(class_boundary_calculator(lower_limit, upper_limit)))
            print("=================")
            print()
        elif user_input == str(4):
            data_list = []
            while (True):
                user_input = input("Enter in frequencies, q to stop: ")
                if user_input.lower() == 'q':
                    break
                data_list.append(int(user_input))
            print("Relative Frequency:", relative_frequency_calculator(data_list))
            print()
            print()
        elif user_input == str(5):
            data_list = []
            while (True):
                user_input = input("Enter in frequencies, q to stop: ")
                if user_input.lower() == 'q':
                    break
                data_list.append(int(user_input))
            print("Cumulative Frequency:", cumulative_frequency_calculator(data_list))
            print()
            print()
        else:
            break

def unit22():
    data_list = []
    while (True):
        user_input = input("Enter in data, q to stop: ")
        if user_input.lower() == 'q':
            break
        data_list.append(float(user_input))
    data_list.sort()
    print("==============")
    print("Sorted List:", str(data_list))
    print("==============")
    print()

def main():
    while (True):
        print("1: Unit 2.1 & 2.2: Frequency Distributions")
        print("2: Unit 2.2: Sorter for Stem & Leaf Plot")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            unit21()
        elif user_input == str(2):
            unit22()
        else:
            break