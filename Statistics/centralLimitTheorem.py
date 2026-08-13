import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ### Central Limit Theorem - uniform distribution

# num_samples = 10000
# sample_size = 300
# distribution_range = (0, 1)

# # Generate samples from a uniform distribution
# samples = np.random.uniform(distribution_range[0], distribution_range[1], (num_samples, sample_size))

# # Calculate the sample means
# sample_means = np.mean(samples, axis=1)

# # Plot the histogram of the sample means
# plt.hist(sample_means, bins=30, density=True, edgecolor='black')
# plt.title('Histogram of Sample Means (Poputaion:Uniform, SampleMean:Noraml)')
# plt.xlabel('Sample Mean')
# plt.ylabel('Density')
# plt.show()


# ### Central Limit Theorem - exponential distribution

# num_samples = 10000
# sample_size = 300
# lambda_param = 2

# # Generate samples from a uniform distribution
# samples = np.random.exponential(scale=1/lambda_param, size=(num_samples, sample_size))

# # Calculate the sample means
# sample_means = np.mean(samples, axis=1)

# # Plot the histogram of the sample means
# plt.hist(sample_means, bins=30, density=True, edgecolor='black')
# plt.title('Histogram of Sample Means (Poputaion:Exponential, SampleMean:Noraml)')
# plt.xlabel('Sample Mean')
# plt.ylabel('Density')
# plt.show()




### CLT ON TITANIC DATASET
df = pd.read_csv("datasets/titanic.csv").sample(891)
df.columns = [i.lower() for i in df.columns]

print(df.head(2))
print(df.shape)

print(df.columns)
df['fare'].plot(kind='kde')
plt.show()

sample_size = 50
times = 1000

samples = []
for i in range(times):
    samples.append(df['fare'].dropna().sample(50).values.tolist())

samples = np.array(samples)
print(samples.shape)
print(samples)

sampling_means = samples.mean(axis=1)
sns.kdeplot(sampling_means) # should give normal distribution
plt.show()

mean_ = sampling_means.mean()
print(mean_)
std_ = sampling_means.std()/np.sqrt(sample_size)

lowerLimit = mean_ - (std_*2)
upperLimit = mean_ + (std_*2)

print("Range is {} - {}".format(lowerLimit, upperLimit))

print("Population Mean = {}".format(df['fare'].mean()))