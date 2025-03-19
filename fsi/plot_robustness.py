import numpy as np
import matplotlib.pyplot as plt
import os
import re

data_files_length = ["data/plot_exp1_L4.gp", "data/plot_exp1.gp", "data/plot_exp1_L10.gp", "data/plot_exp1_L20.gp"]
data_files_rho = ["data/plot_exp1.gp", "data/plot_exp1_rhof0.05.gp", "data/plot_exp1_rhof0.005.gp" ,"data/plot_exp1_rhos2.gp", "data/plot_exp1_rhos50.gp"]

def load_data(files):
    data = []
    for file in files:
        data.append(np.loadtxt(file))
    return data

data_length = load_data(data_files_length)
data_rho = load_data(data_files_rho)

plt.figure(figsize = (10, 5))

plt.subplot(1, 2, 1)
count = 0
for file, data in zip(data_files_length, data_length):
    xc, displacement = data[:, 0], data[:, 1]
    match = re.search(r'L(\d+)', os.path.basename(file))
    L = float(match.group(1)) if match else 6
    plt.plot(xc, displacement, label=f"length= {L}")
plt.xlabel("xc")
plt.ylabel("Displacement")
plt.title("Varying Length")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
for file, data in zip(data_files_rho, data):
    xc, displacement = data[:, 0], data[:, 1]
    
    # Extract rhof and rhos values using regex
    basename = os.path.basename(file)
    rhof_match = re.search(r'rhof(\d+\.\d+)', basename)
    rhos_match = re.search(r'rhos(\d+)', basename)
    
    rhof_value = float(rhof_match.group(1)) if rhof_match else 1.0 
    rhos_value = float(rhos_match.group(1)) if rhos_match else 1.1 
    
    plt.plot(xc, displacement, label=f"rhof = {rhof_value}, rhos = {rhos_value}")

plt.xlabel("xc")
plt.ylabel("Displacement")
plt.title("Varying Density Values")
plt.legend()
plt.grid()

plt.tight_layout()

plt.savefig('figures/plot_rob.png', dpi = 300)