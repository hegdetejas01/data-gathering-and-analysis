"""
Original file is located at
    https://colab.research.google.com/drive/1DelVbO61GGfCjjzKu4NYNLxHAwffB9m9

"""

import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')
df.head(2)

sns.kdeplot(df['sepal_length'])
sns.kdeplot(data=df, x='sepal_length', hue='species')
sns.kdeplot(data=df, x='sepal_width', hue='species')
sns.kdeplot(data=df, x='petal_length', hue='species')
sns.kdeplot(data=df, x='petal_width', hue='species')

sns.ecdfplot(data=df, x='petal_width', hue='species') # it is cdf plot

sns.kdeplot(data=df, x='petal_width', hue='species')

sns.ecdfplot(data=df, x='petal_width', hue='species') # it is cdf plot



titanic = pd.read_csv("/content/titanic.csv")
titanic.head(2)
sns.kdeplot(data=titanic, x='Survived')
sns.kdeplot(data=titanic, x='Age', hue='Survived')





# 2D Density plots
sns.jointplot(data=df, x="petal_length", y="sepal_length", kind='kde', fill=True, cbar=True)
sns.jointplot(data=df, x="sepal_width", y="sepal_length", kind='kde', fill=True, cbar=True)
sns.jointplot(data=df, x="sepal_width", y="petal_width", kind='kde', fill=True, cbar=True)