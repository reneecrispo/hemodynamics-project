# Simulation of blood flow in a bifurcation

## Overview
The objective is to simulate blood flow in a simplified bifurcated vessel geometry in 2D solving the Navier-Stokes equations in FreeFem++. 

## Problem
The problem consists of solving the incompressible Navier-Stokes equations in a domain representing a bifurcation. The blood can be modeled as an incompressible Newtonian fluid with density $\rho_f = 1$ and viscosity $\mu = 0.035$. 

The velocity $v$ and pressure $p$ fields are computed under given initial and boundary conditions: 
- On $\Gamma^\text{wall}$: no-slip condition; 
- On $\Gamma^\text{in}$: parabolic profile, periodic in time;
- On $\Gamma^\text{out}$: pressure boundary condition via resistance relation.

More info about the problem setting and its numerical analysis can be found in `report.pdf`.

## Files
- `main.edp`: core script, where the finite element spaces must be specified.
- `bif-P2P1.edp`, `bif-P3P1dc.edp`, `bif-P2isoP1.edp`: implementations of the problem using different finite element spaces.
-  `bif-P2P1-alt.edp`: implementation of the problem using an alternative semi-discretisation on the boundary.
- `plot.py`: Python code used to post process the resulting data. 
- `data`: Directory storing output files, such as flux through boundaries and average pressure.
- `figures`: Directory storing output files, such as flux through boundaries and average pressure.

## How to run
To execute the main script, run the following command in the terminal:
```
FreeFem++ main.edp -v 0
```
The program will prompt you to select the finite element spaces and automatically call the corresponding script. If, instead, you want to run a specific implementation directly, simply replace `main.edp` with the name of the desired file, for instance: 
```
FreeFem++ <file_name>.edp -v 0
```