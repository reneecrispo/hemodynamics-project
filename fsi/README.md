# Explicit Coupling and Added Mass in FSI

## Problem
The problem consists of solving the incompressible Navier-Stokes equations in  tube where the top is governed by an elastic model.

More info about the problem setting and its numerical analysis can be found in `report.pdf`.

## Files
- `main.edp`: core script, where the schemes and boundary conditions must be specified.
- `fsi-IMP.edp`, `fsi-DN.edp`, `fsi-RN.edp`: implementations of the problem using different schemes.
- `plot_xp.py`: Python code used to post process the resulting data. 
- `data`: Directory storing output files, such as the vertical displacement $\eta$.
- `figures`: Directory storing output figures.

## How to run
To execute the main script, run the following command in the terminal:
```
FreeFem++ main.edp -v 0
```
The program will prompt you to select the scheme and automatically call the corresponding script. If, instead, you want to run a specific implementation directly, simply replace `main.edp` with the name of the desired file, for instance: 
```
FreeFem++ <file_name>.edp -v 0
```