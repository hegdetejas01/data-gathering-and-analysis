from scipy.stats import norm
import seaborn as sns
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from sklearn.neighbors import KernelDensity

x = 100000

# expriement of rolling a die once : approx= 1/6
l = []
for i in range(x):
    l.append(random.randint(1,6))

s = (pd.Series(l).value_counts()/x).sort_index()
print(s)

s.plot(kind='bar')
plt.show()


# tossing a coin once : approx = 1/2
l = []
for i in range(x):
    l.append(random.randint(1,2))

s = (pd.Series(l).value_counts()/x).sort_index()
print(s)

s.plot(kind='bar')
plt.show()


# sum of result of dies when thrown twice
# approx values:
    # 7 : 6/36            -> high probability
    # 10 : 3/36

l = []
for i in range(x):
    a = random.randint(1,6)
    b = random.randint(1,6)
    l.append(a+b)
    
s = (pd.Series(l).value_counts()/x).sort_index()
print(s)

s.plot(kind='bar')
plt.show()


# Cumulative Dritribution function if a single die is rolled
# cmf (x=4) : 4/6 = 0.66
# cmf (x=5) : 5/6 = 0.83
l = []
for i in range(x):
    l.append(random.randint(1,6))

s = (pd.Series(l).value_counts()/x).sort_index()
print(s)

np.cumsum(s).plot(kind='bar')
plt.show()



### Probablity Density Function ###
sample = normal(loc=50, scale=5, size=10000)
print(sample)

plt.hist(sample, bins=25)
plt.show() # says that whether the data may be of normal or not

sample_mean = sample.mean()
sample_std = sample.std()

dist = norm(sample_mean, sample_std)
print(dist)

values = np.linspace(sample.min(), sample.max(), 1000)
prob_den = [dist.pdf(x) for x in values]

plt.hist(sample, bins=20, density=True)
plt.plot(values, prob_den)
plt.show()


sns.displot(sample)
plt.show()



# KDE
sample1 = normal(loc=20, scale=5, size=3000)
sample2 = normal(loc=40, scale=5, size=7000)
sample = np.hstack((sample1, sample2))

plt.hist(sample, bins = 50)
plt.show()

model = KernelDensity(bandwidth=20, kernel='gaussian') # change this bandwidth and check
sample = sample.reshape((len(sample), 1))
model.fit(sample)


values = np.linspace(sample.min(), sample.max(), 1000)
values = values.reshape((len(values), 1))
prob = model.score_samples(values)
prob = np.exp(prob)

plt.hist(sample, bins= 50, density=True)
plt.plot(values[:], prob)
plt.show()