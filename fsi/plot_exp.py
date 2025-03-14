import numpy as np
import matplotlib.pyplot as plt

data_files_RN = ["data/plot_exp1_i0.gp", "data/plot_exp1_i1.gp", "data/plot_exp1_i2.gp", "data/plot_exp1_i3.gp"]
data_files_IMP = ["data/plot_imp_i0.gp", "data/plot_imp_i1.gp", "data/plot_imp_i2.gp", "data/plot_imp_i3.gp"]

def load_data(files):
    data = []
    for file in files:
        data.append(np.loadtxt(file))
    return data

data_RN = load_data(data_files_RN)
data_IMP = load_data(data_files_IMP)

plt.figure(figsize = (10, 5))

plt.subplot(1, 2, 1)
count = 0
for data in data_RN:
    xc, displacement = data[:, 0], data[:, 1]
    plt.plot(xc, displacement, label=f"i = {count}")
    count += 1
plt.xlabel("xc")
plt.ylabel("Displacement")
plt.title("RN Data")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
count = 0
for data in data_IMP:
    xc, displacement = data[:, 0], data[:, 1]
    plt.plot(xc, displacement, label=f"i = {count}")
plt.xlabel("xc")
plt.ylabel("Displacement")
plt.title("IMP Data")
plt.legend()
plt.grid()

plt.tight_layout()

plt.savefig('figures/plot_exp.png', dpi = 300)