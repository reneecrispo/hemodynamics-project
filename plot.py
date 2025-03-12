import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("history.txt")

t = data[:, 0]
pMeanIn, pMeanOut1, pMeanOut2 = data[:, 1], data[:, 2], data[:, 3]
fluxIn, fluxOut1, fluxOut2 = data[:, 4], data[:, 5], data[:, 6]

plt.figure(figsize = (10, 5))

plt.subplot(1, 2, 1)
plt.plot(t, pMeanIn, label = "P_in")
plt.plot(t, pMeanOut1, label = "P_out1")
plt.plot(t, pMeanOut2, label = "P_out2")
plt.xlabel("Time")
plt.ylabel("Avergae pressure")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t, fluxIn, label = "Flux_in")
plt.plot(t, fluxOut1, label = "Flux_out1")
plt.plot(t, fluxOut2, label = "Flux_out2")
plt.xlabel("Time")
plt.ylabel("Flux")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('history.png', dpi = 300)

