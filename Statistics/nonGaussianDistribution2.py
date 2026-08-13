import numpy as np
import matplotlib.pyplot as plt

# Binomial

n = 10  # number of trials
p = 0.5  # probability of success
size = 1000  # number of samples to generate

binomial_dist = np.random.binomial(n, p, size)
print(binomial_dist)

plt.hist(binomial_dist,density=True)
plt.show()