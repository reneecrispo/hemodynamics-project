import numpy as np
import matplotlib.pyplot as plt
import os

data_files = ["data/history-P2P1.txt"]
              # "data/history-P3P1dc.txt"
              # "data/history-P2isoP1.txt"
              # "data/history-P1P1.txt"

for data_file in data_files:
    data = np.loadtxt(data_file)
    t = data[:, 0]
    pMeanIn, pMeanOut1, pMeanOut2 = data[:, 1], data[:, 2], data[:, 3]
    fluxIn, fluxOut1, fluxOut2 = data[:, 4], data[:, 5], data[:, 6]

    plt.figure(figsize = (10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(t, pMeanIn, label = "P in")
    plt.plot(t, pMeanOut1, label = "P out1")
    plt.plot(t, pMeanOut2, label = "P out2")
    plt.xlabel("Time")
    plt.ylabel("Average pressure")
    plt.legend()
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.plot(t, fluxIn, label = "Flux in")
    plt.plot(t, fluxOut1, label = "Flux out1")
    plt.plot(t, fluxOut2, label = "Flux out2")
    plt.plot(t, fluxIn + fluxOut1 + fluxOut2, label = "Sum")
    plt.xlabel("Time")
    plt.ylabel("Flux")
    plt.legend()
    plt.grid()
    
    plt.tight_layout()
    name = "figures/" + os.path.basename(data_file) + ".png"
    plt.savefig(name, dpi = 300)