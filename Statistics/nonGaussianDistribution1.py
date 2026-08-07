import matplotlib.pyplot as plt
import numpy as np


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