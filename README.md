# Simulation of blood flow in a bifurcation

## Overview
The objective is to simulate blood flow in a simplified bifurcated vessel geometry using the Navier-Stokes equations in FreeFem++. 

## Problem
The problem consists of solving the incompressible Navier-Stokes equations in a domain representing a bifurcation. The blood can be modeled as an incompressible Newtonian fluid with density $\rho_f = 1$ and viscosity $\mu = 0.035$. 

The velocity $v$ and pressure $p$ fields are computed under given initial and boundary conditions: 
- On $\Gamma^\text{wall}$: no-slip condition; 
- On $\Gamma^\text{in}$: parabolic profile, periodic in time;
- On $\Gamma^\text{out}$: pressure boundary condition via resistance relation.

## Files
The folder contains: 
- `main.edp`: Core script, where the finite element spaces are specified.
- `bif-P2P1.edp`, `bif-P3P1dc.edp`, `bif-P2isoP1.edp`: Implementations of the problem using different finite element spaces.

## Installation
In order to be able to run the file, make sure to have [FreeFem++](https://doc.freefem.org/introduction/download.html) installed on your computer. 

To run any of the files, write
```
FreeFem++ <file_name>.edp -v 0
```