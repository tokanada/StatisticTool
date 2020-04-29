def unit11():
    print()
    print()
    print("Unit 1.1")
    print(
        "Statistics: The science of gathering, describing, and analyzing data or the actual numerical descriptions of sample data")
    print("Population: All persons or things about which one is trying to make an inference or decision")
    print("Variables: Values that change among members of the population")
    print("Data: Information gathered about a specific variable")
    print("Census: Data gathered from every member")
    print("Parameter: The numerical description of a particular population characteristic")
    print("Sample: A subset of the population")
    print("Sample statistic: A number that describes a characteristic of a sample")
    print()
    print()
    print(
        "Population: Whole Group | Group we want to know about | Characteristics are called parameters | Parameters are generally unknown | Parameters are fixed")
    print(
        "Sample: Part of Group | Group we do know about | Characteristics are called statistics | Statistics are always known | Statistics change with sample")
    print()
    print()
    print(
        "Descriptive statistics: First Branch | Gathers, sorts, summarizes and generally describes the data that have been collected")
    print("Inferential statistics: Second Branch | The interpretation of the information collected")
    print()
    print()

    return

def unit12():
    print()
    print()
    print("Unit 1.2")
    print("Qualitative data: Descriptions")
    print("Quantitative data: Counts, measurements")
    print()
    print()
    print("Continuous Data: can be any value in a given range of numbers | Measurements")
    print("Discrete Data: can take on only particular values in a range | Counts")
    print()
    print()
    print("Levels of Measurement:")
    print("Nominal Level of Measurement: Data is qualitative | Categorizing | No calculations")
    print("Ordinal Level: Data is qualitative | Data can be arranged in meaningful order | Mathematical calculation do not occur")
    print("Interval Level: Data is quantitative | Data can be ordered and differences are meaningful | The zero point does not mean an absence | Example: Temperature on the Fahrenheit and Celcius scale")
    print("Ratio Level: Data is quantitative | Like Interval but with meaningful zero point | Example: Money or temperature on Kelvin scale")
    print()
    print()

def unit13():
    print()
    print()
    print("Unit 1.3")
    print("Observational Studies: Gather data through observing data that already exist")
    print("Experiment: To determine if one thing causes another to happen")
    print()
    print()
    print("Observational: Representative Sample: A sample that has the same relevant characteristics as the population and does not favor one group from the population over another")
    print("Observational: Cross-sectional Study: Data collected at a single point in time")
    print("Observational: Longitudinal Study: Data collected following a group over a period of time")
    print("Observational: Meta-analysis: Study conducted based on information gathered from previous studies, not a sample. One variable per several studies")
    print("Observational: Case study: Like a meta-analysis but looks at multiple variables that affect a single event")
    print()
    print()
    print("Experiments: Researchers apply a 'treatment' to a group of people, 'subjects or participants,' and measure the response")
    print("Experiments: Response Variable: Variable that responds to the treatment")
    print("Experiments: Explanatory Variable: Variable that causes the change in the response variable")
    print("Experiments: Treatment group: The group of subjects which the treatment is applied")
    print("Experiments: Control group: The group that does not receive treatment")
    print("Experiments: Confounding Variables: Factors other than the treatment that cause an effect on the groups")
    print("Experiments: Placebo: Self induced results not caused by the treatment")
    print()
    print()
    print("Sampling Methods:")
    print("Random Sample: People selected at random")
    print("Simple Random Sampling: Every sample from the population has an equal chance of selection")
    print()
    print("Stratified Sampling: Members of the population are divided into two or more subgroup (strata) that share similar characteristics. Random Sample is drawn per each strata")
    print("Also called quota sampling")
    print()
    print("Cluster Sampling: Population is divided into groups (clusters). Clusters are randomly selected")
    print()
    print("Systematic Sampling: Every nth member of the population is selected")
    print()
    print("Convenience sampling: The most convienent method for the researcher")
    print()
    print()

def main():
    while (True):
        print("1: Unit 1.1: Getting Started")
        print("2: Unit 1.2: Data Classification")
        print("3: Unit 1.3: The Process of a Statistical Study")
        print("Other: Return")
        user_input = input("Enter a selection: ")

        if user_input == str(1):
            unit11()
        elif user_input == str(2):
            unit12()
        elif user_input == str(3):
            unit13()
        else:
            break
