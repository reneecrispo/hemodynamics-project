import numpy as np
import matplotlib.pyplot as plt

# Define file paths
data_files_RN = ["data/plot_exp1_i0.gp", "data/plot_exp1_i1.gp", "data/plot_exp1_i2.gp", "data/plot_exp1_i3.gp"]
data_files_IMP = ["data/plot_imp_i0.gp", "data/plot_imp_i1.gp", "data/plot_imp_i2.gp", "data/plot_imp_i3.gp"]

# Function to load data
def load_data(files):
    return [np.loadtxt(file) for file in files]

# Load RN and IMP data
data_RN = load_data(data_files_RN)
data_IMP = load_data(data_files_IMP)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

# Plot data
for i in range(4):
    ax = axes[i]
    xc_RN, displacement_RN = data_RN[i][:, 0], data_RN[i][:, 1]
    xc_IMP, displacement_IMP = data_IMP[i][:, 0], data_IMP[i][:, 1]
    
    ax.plot(xc_RN, displacement_RN, label="RN")
    ax.plot(xc_IMP, displacement_IMP, label="IMP")
    
    ax.set_xlabel("xc")
    ax.set_ylabel("Displacement")
    ax.set_title(f"i = {i}")
    ax.legend()
    ax.grid()

# Adjust layout and save
plt.tight_layout()
plt.savefig('figures/plot_exp.png', dpi=300)