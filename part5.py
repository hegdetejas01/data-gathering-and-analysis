"""
Original file is located at
    https://colab.research.google.com/drive/18EWaqfDHdmNqndEQC_8qEJsO-OXvb8vR

"""

#### Exploratory Data Analysis ####

### Why EDA?
# It gives better understanding of the dataset

# 1. For Model Building
# 2. Analysis and Reporting
# 3. Validate Assumption          
# 4. Handling the Missing Data (either remove or add value for missing place)
# 5. Feature Engineering for Machine Learning
# 6. Detecting Outliers



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/train.csv")
df.columns = [i.lower() for i in df.columns]
df.head(2)



### Column Type/ Data Type
# 1. Numerical
# 2. Categorical
# 3. Mixed

# STEP1: Write them for every column of the DF

# Numerical - age, fare, passengerid
# Categorical - survived, pclass, sex, sibsp, parch, embarked
# Mixed - name, ticket, cabin



# Univariate Analysis :

    #     Univariate analysis focuses on analyzing each feature(column) in the dataset independently.

    #     How does univaiate analysis help ?
    #     1). **Distribution analysis**: The distribution of each feature is examined to identify its shape, central tendency, and dispersion.
    #     2). **Identifying potential issues**: Univariate analysis helps in identifying potential problems with the data such as outliers, skewness, and missing values


    #     The shape of a data distribution refers to its overall pattern or form as it is represented on a graph. Some common shapes of data distributions include:
    #         - **Normal Distribution**: A symmetrical and bell-shaped distribution where the mean, median, and mode are equal and the majority of the data falls in the middle of the distribution with gradually decreasing frequencies towards the tails.
    #         - **Skewed Distribution**: A distribution that is not symmetrical, with one tail being longer than the other. It can be either positively skewed (right-skewed) or negatively skewed (left-skewed).
    #         - **Bimodal Distribution**: A distribution with two peaks or modes.
    #         - **Uniform Distribution**: A distribution where all values have an equal chance of occurring.

    #     The shape of the data distribution is important in identifying the presence of outliers, skewness, and the type of statistical tests and models that can be used for further analysis.



    #     **Dispersion** is a statistical term used to describe the spread or variability of a set of data. It measures how far the values in a data set are spread out from the central tendency (mean, median, or mode) of the data.
    #     There are several measures of dispersion, including:
    #         - **Range**: The difference between the largest and smallest values in a data set.
    #         - **Variance**: The average of the squared deviations of each value from the mean of the data set.
    #         - **Standard Deviation**: The square root of the variance. It provides a measure of the spread of the data that is in the same units as the original data.
    #         - **Interquartile range (IQR)**: The range between the first quartile (25th percentile) and the third quartile (75th percentile) of the data.

    #     Dispersion helps to describe the spread of the data, which can help to identify the presence of outliers and skewness in the data.


    # Therefore, univariate analysis helps to know about shape(how it looks on graph), central tendency(mean, median, mode), dispersion(spread, std deviation, variance, min max, interquartile range)

### Steps of doing univariate analysis on numerical columns

# - **Descriptive Statistics**: Compute basic summary statistics for the column, such as mean, median, mode, standard deviation, range, and quartiles. These statistics give a general understanding of the distribution of the data and can help identify skewness or outliers.
# - **Visualizations**: Create visualizations to explore the distribution of the data. Some common visualizations for numerical data include histograms, box plots, and density plots. These visualizations provide a visual representation of the distribution of the data and can help identify skewness an outliers.
# - **Identifying Outliers**: Identify and examine any outliers in the data. Outliers can be identified using visualizations. It is important to determine whether the outliers are due to measurement errors, data entry errors, or legitimate differences in the data, and to decide whether to include or exclude them from the analysis.
# - **Skewness**: Check for skewness in the data and consider transforming the data or using robust statistical methods that are less sensitive to skewness, if necessary.
# - **Conclusion**: Summarize the findings of the EDA and make decisions about how to proceed with further analysis.



# univariate analysis on age:
print(df['age'].describe())

# checking for missing value
print(df['age'].isnull().sum()) # 177 missing ages
print(df['age'].isnull().sum() / df.shape[0] * 100) # we don't have value of around 19 percent people

df['age'].plot(kind='hist', bins=20)

df['age'].plot(kind='kde')

df['age'].skew() # if this is around zero, the data is less skewed - normal distribution

df['age'].plot(kind='box')
# this gives idea about outliers

# checking outlier values
print(df[df['age'] > 65])

# here all the outlier values are normal



"""
Conclusion on AGE column
1. Age is normally(almost) distributed
2. 20 percent of values are missing
3. There are some outliers
"""





# Checking the Fare column
print(df['fare'].describe())

# visualisation
df['fare'].plot(kind='hist')

# not normally distributed

df['fare'].plot(kind='kde')

# this data is skewed

df['fare'].skew() # skew is 4.78 - highly positively skewed

df['fare'].plot(kind='box')

# studying outlies above 250

df[df['fare'] > 250]
# this analysis says that, the fare is not of individual person. It is for the entire people with the same ticket number
# eg: There are four entries for ticket: 19950, hence the fare 263 has been divided among all 4

df['fare'].isnull().sum()

"""
Conclusion on FARE column
1. Data is highly skewed ( high positive )
2. no missing values
3. Fare column actually contains the fare for the group and not for indivial passenger and hence,
4. We need to create a new column called as indiviual fare
"""







### Steps of doing Univariate Analysis on Categorical columns

# **Descriptive Statistics**: Compute the frequency distribution of the categories in the column. This will give a general understanding of the distribution of the categories and their relative frequencies.
# **Visualizations**: Create visualizations to explore the distribution of the categories. Some common visualizations for categorical data include count plots and pie charts. These visualizations provide a visual representation of the distribution of the categories and can help identify any patterns or anomalies in the data.
# **Missing Values**: Check for missing values in the data and decide how to handle them. Missing values can be imputed or excluded from the analysis, depending on the research question and the data set.
# **Conclusion**: Summarize the findings of the EDA and make decisions about how to proceed with further analysis.



# Considering Survived Column

df['survived'].value_counts()

df['survived'].value_counts().plot(kind='bar')

df['survived'].value_counts().plot(kind='pie', autopct="%0.2f%%")

df['survived'].isnull().sum()



"""
Conclusion on SURVIVED column
1. More than 50% i.e around 61 percent died
2. No missing data found
"""





df['pclass'].value_counts()

df['pclass'].value_counts().plot(kind='bar')

df['pclass'].value_counts().plot(kind='pie', autopct="%0.2f%%")

df['pclass'].isnull().sum()

"""
Conclusion on PCLASS column
1. It is surprising that more passengers travelled on 1st class compared to 2nd class
2. No missing data found
"""





df['sex'].value_counts()

df['sex'].value_counts().plot(kind='bar')

df['sex'].value_counts().plot(kind='pie', autopct="%0.2f%%")

df['sex'].isnull().sum()

"""
Conclusion on SEX column
1. Everything seems to be correct.
2. No missing data found
"""





#### Doing same for parch, sibsp
"""
Conclusion on PARCH and SIBSP
1. These two columns can be merged to form a new column called as family size by adding them
2. And create a new column, is_alone
"""





### Embark - from where the passenger boarded the train

df['embarked'].value_counts()

df['embarked'].value_counts().plot(kind='bar')

df['embarked'].value_counts().plot(kind='pie')

df['embarked'].isnull().sum()





##########
## MIXED columns - name, ticket, cabin
## This requies feature engineering
"""
Need to feature engineer them to get more insights
"""







### Steps of doing Bivariate Analysis

# - Select 2 cols
# - Understand type of relationship
#     1. **Numerical - Numerical**
#         a. You can plot graphs like scatterplot(regression plots), 2D histplot, 2D KDEplots
#         b. Check correlation coefficent to check linear relationship

#     2. **Numerical - Categorical** - create visualizations that compare the distribution of the numerical data across different categories of the categorical data.<br>
#         a. You can plot graphs like barplot, boxplot, kdeplot violinplot even scatterplots

#     3. **Categorical - Categorical**
#         a. You can create cross-tabulations or contingency tables that show the distribution of values in one categorical column, grouped by the values in the other categorical column.<br>
#         b. You can plots like heatmap, stacked barplots, treemaps

# - Write your conclusions



### Select the main column(s) and do bivariate analysis of them with all other columns

# 1. Survived - Pclass : categorical - categorical

pd.crosstab(df['survived'],df['pclass']) # this is contingency table

pd.crosstab(df['survived'],df['pclass'] , normalize = 'columns')

# pclass 3 was the most dangerous class and pclass 1 was more safe

sns.heatmap(pd.crosstab(df['survived'],df['pclass'] , normalize = 'columns') * 100)



# 2. Survived - Sex : categorical - categorical
pd.crosstab(df['survived'],df['sex'] , normalize = 'columns') * 100

# female had more chances of survival



# 3. Survived - Emabarked : categorical - categorical
pd.crosstab(df['survived'],df['embarked'] , normalize = 'columns') * 100

## more people boarded from C survived compared to Q and S - therefore, C passengers were more female or they were more pclass 1 passengers

pd.crosstab(df['sex'],df['embarked'] , normalize = 'columns') * 100
# therefore the above prediction of survival of C is not because of Ses

pd.crosstab(df['pclass'],df['embarked'] , normalize = 'columns') * 100
# This might be the reason that those boarded from C were more safe compared to Q and S





### 4 . Age - Survived : numerical - categorical
df[df['survived'] == 1]['age'].plot(kind='kde', label='Survived Versus Age')
df[df['survived'] == 0]['age'].plot(kind='kde', label='Dead Versus Age')

plt.legend()
plt.show()







######### FEATURE ENGINEERING #########

df1 = pd.read_csv('datasets/test.csv')
df1.columns = [i.lower() for i in df1.columns]

df = pd.concat([df,df1])

# Working on fare column

df['ticket'].value_counts()

df[df['ticket'] == 'CA. 2343']

df['individual_fare'] = df['fare'] / (df['sibsp'] + df['parch'] + 1)

df.head(2)





# Working on sibsp and parch
df['family_size'] = df['sibsp'] + 1 + df['parch']

df.head()



# Family type

def getFamilyType(num):
  if num == 1 : return "Alone"
  elif num > 1 and num < 5 : return "Small Family"
  elif num > 5 : return "Large Family"

df['family_type'] = df['family_size'].apply(getFamilyType)

df.sample(5)





# relation between family type and survived
# pd.crosstab(df['survived'], df['family_type'], normalize='columns') * 100





df['surname'] = df['name'].str.split(',').str.get(0)

df['title'] = df['name'].str.split(',').str.get(1).str.strip().str.split().str.get(0)

df.head(2)

df['title'].value_counts()



temp = df[df['title'].isin(['Mr.','Miss.','Mrs.','Master.'])]

# relation between survived and title
# pd.crosstab(temp['survived'], temp['title'], normalize='columns')*100







# cabin
df['cabin'].isnull().sum()

df['cabin'].isnull().sum() / df.shape[0] * 100 # 77 percent null value is present

df['cabin'].fillna('M', inplace=True)
# M is for missing

df['cabin'].value_counts()

df['deck'] = df['cabin'].str.get(0)

df['deck'].value_counts()

# pd.crosstab(df['deck'], df['pclass'])

# pd.crosstab(df['deck'], df['survived'])

# pd.crosstab(df['survived'], df['deck'])



sns.heatmap(df.corr(numeric_only = True))
sns.pairplot(df1)