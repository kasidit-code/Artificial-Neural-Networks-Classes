import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math

ff = pd.read_csv(r'Model train\forestfires.csv')
a, b = ff.ISI, ff.temp

#print(ff)
X = np.linspace(0,57,50)
Y = -1/144*(X-14)**2+33.3
plt.plot(X, Y,'-')
plt.plot(a, b, 'o')
plt.ylabel("Temperature")
plt.xlabel("Initial Spreading Index")
plt.show()