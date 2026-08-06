import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

df = pd.read_csv("datasets/titanic.csv")

sns.kdeplot(df['Age'])
plt.title("Age Column Graph (not normal but can be considered as normal)")
plt.show() # not normal but can be considered as normal

print(df['Age'].mean())
print(df['Age'].std())

# Therefore, the Age column has a mean of 29.69 and std of 14.52
# Convert this to Standardised Normal Variate

x = (df['Age'] - df['Age'].mean())/df['Age'].std()

sns.kdeplot(x)
plt.title("Standardised Normal Variate (mean appox 0, std appox 1)")
plt.show()

print(x.mean()) # close to 0
print(x.std()) # close to 1


### Finding Skewness ###
print(df['Age'].skew()) # very close to 0 and hence can be considered as normal


### Outlier Detection
max_ = df['Age'].mean() + 3*df['Age'].std()
min_ = df['Age'].mean() - 3*df['Age'].std()

outlier_1 = df[df['Age'] > max_]
outlier_2 = df[df['Age'] < min_]
print(df.shape)
print(outlier_1.shape)
print(outlier_2.shape)



### QQ Plot ###

df = sns.load_dataset('iris')
print(df.head(2))

sns.kdeplot(df['sepal_length'])
plt.title("Looks like Normal distribution")
plt.show()

temp = sorted(df['sepal_length'].tolist())
y_quant = []
for i in range(1,101):
    y_quant.append(np.percentile(temp, i))

samples = np.random.normal(loc=0, scale=1, size=1000)
x_quant = []
for i in range(1,101):
    x_quant.append(np.percentile(samples, i))

sns.scatterplot(x=x_quant, y=y_quant)
plt.title("Looks like a straight line")
plt.show()



fig = sm.qqplot(df['sepal_length'], line='45', fit=True)
plt.title("Using Inbuilt Function")
plt.show()