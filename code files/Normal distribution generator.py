import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

#mu, sigma = 0.002499139, 0.012555068 # omega_z mean and standard deviation
mu, sigma = 0.0000994836, 0.000478052 # theta_z mean and standard deviation
sample = np.random.normal(mu, sigma, 1000)
sample_array = np.random.normal(mu, sigma, size=(599,20))

count, bins, ignored = plt.hist(sample, 100, density=1)

params = {'figure.figsize': (8, 5),
          'xtick.labelsize': 10, 
          'ytick.labelsize' : 10}
plt.rcParams.update(params)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()
print("mu =", abs(np.mean(sample)))
print("sigma =", abs(np.std(sample, ddof=1)))

#x = pd.DataFrame(sample_array)
#x.to_excel(excel_writer = "normdist_theta_z.xlsx")