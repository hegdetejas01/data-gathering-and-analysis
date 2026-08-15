import pandas as pd
from scipy.stats import shapiro, t
import matplotlib.pyplot as plt
from scipy.stats import levene
import scipy.stats as stats
import numpy as np

### Single Sample t-Test

# Age of the df
# h0: mean age is 35
# h1: mean age is less than 35

# Given data
# population mean is 35
# sample size = 25 (we can't apply CLT)
# x-bar
# sample std

# Shapiro Wilk Test - Tells if the sample follows normal distribution or not
# It gives the p-value
# here if p-value < 0.05 -> not normal, if p-value > 0.05 -> Normal Distribution

# SEE THE KAGGLE NOTES : 
# https://www.kaggle.com/code/campusx/titanic-single-sample-t-test

def singleSampleTest():

    df = pd.read_csv('datasets/titanic.csv')
    df = df.sample(1309)
    print(df.head(2))
    pop = df['Age'].dropna()

    sample_age = pop.sample(25).values
    shapiro_age = shapiro(sample_age)
    print(shapiro_age)

    pop.plot(kind='kde')
    plt.show()

    pop_mean = 35
    t_statistic, p_value = stats.ttest_1samp(sample_age, pop_mean)
    print("t-statistic:", t_statistic)
    print("p-value:", p_value/2)

    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")




### Independent Two Sample t-Test ###

def independentTwoSampleTest_desktopAndMobileUsers():
    # Input the data as lists
    desktop_users = [12, 15, 18, 16, 20, 17, 14, 22, 19, 21, 23, 18, 25, 17, 16, 24, 20, 19, 22, 18, 15, 14, 23, 16, 12, 21, 19, 17, 20, 14]
    mobile_users = [10, 12, 14, 13, 16, 15, 11, 17, 14, 16, 18, 14, 20, 15, 14, 19, 16, 15, 17, 14, 12, 11, 18, 15, 10, 16, 15, 13, 16, 11]

    # Perform the Shapiro-Wilk test for both desktop and mobile users
    shapiro_desktop = shapiro(desktop_users)
    shapiro_mobile = shapiro(mobile_users)

    print("Shapiro-Wilk test for desktop users:", shapiro_desktop)
    print("Shapiro-Wilk test for mobile users:", shapiro_mobile)

    # If the p-value from Levene's test is greater than your chosen significance level (α = 0.05), you can assume equal variances
    #  If the p-value is less than or equal to the significance level, the assumption of equal variances is not met, 
    # and you should consider using Welch's t-test instead of the regular independent two-sample t-test.

    # Perform Levene's test
    levene_test = levene(desktop_users, mobile_users)
    print(levene_test)

    # For 2 sample test
    t_value = -5.25
    degreeOfFreedom = 30+30-2 # n1 + n2 - 2
    cdf_value = t.cdf(t_value, degreeOfFreedom)

    p_value = 2*cdf_value
    print("P-Value:", p_value)

    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")



### Another Example - Independent Two Sample t-Test ###

def independentTwoSampleTest_titanicSexAndAge():
    # H1: mean age of male = mean age of female
    # Ha: mean age of males >>> mean age of female
    # alpha = 0.05

    df = pd.read_csv("datasets/titanic.csv")
    df = df.sample(1309)
    print(df.head(2))

    male_age = df[df['Sex'] == 'male']['Age'].dropna()
    female_age = df[df['Sex'] == 'female']['Age'].dropna()

    sample_male = male_age.sample(25)
    sample_female = female_age.sample(25)

    shapiro_male = shapiro(sample_male)
    shapiro_female = shapiro(sample_female)
    print("Shapiro-Wilk test for desktop users:", shapiro_male)
    print("Shapiro-Wilk test for mobile users:", shapiro_female)

    levene_test = levene(sample_male, sample_female)
    print(levene_test)

    t_statistic, p_value = stats.ttest_ind(sample_male, sample_female)
    print("t-statistic:", t_statistic)
    print("p-value:", p_value/2)

    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")

    print(male_age.mean())
    print(female_age.mean())



### Paired Two Sample t-Test ###
def pairedTwoSampleTest():
    
    before = np.array([80, 92, 75, 68, 85, 78, 73, 90, 70, 88, 76, 84, 82, 77, 91])
    after = np.array([78, 93, 81, 67, 88, 76, 74, 91, 69, 88, 77, 81, 80, 79, 88])
    differences = after - before

    plt.hist(differences)
    plt.title("Histogram of Weight Differences")
    plt.xlabel("Weight Differences (kg)")
    plt.ylabel("Frequency")
    plt.show()

    shapiro_test = stats.shapiro(differences)
    print("Shapiro-Wilk test:", shapiro_test) # follows normal distribution

    mean_diff = np.mean(differences)
    std_diff = np.std(differences, ddof=1)

    n = len(differences)
    t_statistic = mean_diff / (std_diff / np.sqrt(n))
    degreeOfFreedom = n - 1

    alpha = 0.05
    p_value = stats.t.cdf(t_statistic, degreeOfFreedom)

    print(p_value)

    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")



singleSampleTest()
independentTwoSampleTest_desktopAndMobileUsers()
independentTwoSampleTest_titanicSexAndAge()
pairedTwoSampleTest()