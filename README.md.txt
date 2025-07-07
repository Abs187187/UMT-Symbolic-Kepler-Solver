# UMT Symbolic and Hyperbolic Kepler Solver

This repository provides open-source Python implementations of the Unified Mathematical Taxonomy (UMT) symbolic and hyperbolic solvers for Kepler's equation.

## Features
- **Elliptical and hyperbolic solver:** Supports both \( e < 1 \) and \( e > 1 \) cases.
- **Deterministic, non-iterative method:** Achieves high-precision solutions without numerical root-finding loops.
- **Transparent code:** Designed for open science, peer review, and extension.

## Usage

1. **Requirements:**  
   - Python 3.x  
   - numpy

2. **Example:**
   ```python
   import pandas as pd
   from umt_solver import umt_elliptical, umt_hyperbolic

   # Load example data
   df = pd.read_csv('example_data.csv')
   results = []
   for i, row in df.iterrows():
       M = row['Mean_Anomaly']
       e = row['Eccentricity']
       if e < 1:
           E = umt_elliptical(M, e)
           results.append(E)
       else:
           H = umt_hyperbolic(M, e)
           results.append(H)
   print(results)
