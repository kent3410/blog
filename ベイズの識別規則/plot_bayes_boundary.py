# ベイズの識別境界の図示

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = np.linspace(-10,10,10000)

p_c1 = []
p_c2 = []
for i in n:
    p_c1.append(norm.pdf(x = i, loc = -1, scale = 1))
    p_c2.append(norm.pdf(x = i, loc = 1, scale = 1))
    

plt.scatter(n, p_c1)
plt.scatter(n, p_c2)
plt.show()


