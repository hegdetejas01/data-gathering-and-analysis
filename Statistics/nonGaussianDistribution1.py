import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer

# Pareto Graph
alpha = 3
xm = 1

x = np.linspace(0.1, 10, 10000)
y = alpha * (xm**alpha) / (x**(alpha+1))

plt.plot(x,y)
plt.title("X versus Y graph")
plt.show()

x_log = np.log(x)
y_log = np.log(y)

plt.plot(x_log, y_log)
plt.title("Log(X) versus Log(Y) grpah (Confirms that the data is Pareto)")
plt.show()



### Transformation ###
df = pd.read_csv("datasets/titanic.csv", usecols=['Age','Fare','Survived'])
print(df.head(2))

df['Age'].fillna(df['Age'].mean(), inplace=True)

X = df.iloc[:,1:3]
Y = df.iloc[:,0]

sns.displot(X['Age'])
plt.show()

stats.probplot(X['Age'], dist='norm', plot=plt)
plt.show()

sns.displot(X['Fare']) # Fare is right skewed
plt.show()

stats.probplot(X['Fare'], dist='norm', plot=plt)
plt.show() 

fare_log = np.log(X['Fare'])
sns.displot(fare_log) # Fare is right skewed
plt.show()

stats.probplot(fare_log, dist='norm', plot=plt)
plt.show() 
