import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/titanic.csv', usecols=['Fare'])
print(df.shape)

df.plot(kind='kde')
plt.show()

samples = []
stds = []
for i in range(1000):
    x = df['Fare'].dropna().sample(30).values
    stds.append(x.std())
    samples.append(x.tolist())

samples = np.array(samples)
sampling_mean = samples.mean(axis=1)
sample_std = np.mean(stds)

# 95 percent confidence level and t-table
lower_limit = sampling_mean.mean() - 2.042 * sample_std / np.sqrt(30)
upper_limit = sampling_mean.mean() + 2.042 * sample_std / np.sqrt(30)

print("Range is {} - {}".format(lower_limit, upper_limit))

print("Population Mean = {}".format(df['Fare'].mean()))