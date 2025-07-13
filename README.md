# UMT-Symbolic-Kepler-Solver

Open-source implementation of the Unified Mathematical Taxonomy (UMT) symbolic and hyperbolic Kepler solvers, with ready-to-use datasets and benchmarks.

## Description

This repository provides a comprehensive symbolic and hyperbolic solver based on the Unified Mathematical Taxonomy (UMT) framework. The solvers are designed to solve Kepler’s Equation for both **elliptical and hyperbolic** orbits, using deterministic, projection-based methods.  
**No iterative tuning required. Plug-and-play.**  
All code, data, and benchmarks are fully transparent and reproducible.

### Key Features
- **UMT-based approach:** Symbolic solutions for elliptical and hyperbolic orbits.
- **Datasets:** Planets, moons, comets, and interstellar objects (from JPL, MPC, Horizons).
- **Benchmarks:** Validated against classic methods (Newton-Raphson) and JPL/MPC datasets.
- **High precision:** Suitable for astronomy, planetary science, and interstellar applications.

---

## Plug-and-Play Quick Start

Here’s how to use the solver directly on real data:

```python
from umt_solver import umt_elliptical, umt_hyperbolic

# Example 1: Mars (Elliptical)
M = 4.92948505  # mean anomaly [radians]
e = 0.093295    # eccentricity (e < 1)
E = umt_elliptical(M, e)
print(f"Eccentric anomaly (Mars): {E:.6f}")

# Example 2: Borisov (Hyperbolic Comet)
M = 6.825e-07     # mean anomaly [radians]
e = 1.0014143     # eccentricity (e > 1)
H = umt_hyperbolic(M, e)
print(f"Hyperbolic anomaly (Borisov): {H:.6f}")
Sample Results
Output for Mars (JPL Horizons, Jan 2024):

Mean Anomaly (rad)	Eccentricity	Eccentric Anomaly	Residual
4.929485	0.093295	4.836912	0.00e+00

Output for Borisov (C/2021 L3, Jan 2024):

Mean Anomaly (rad)	Eccentricity	Hyperbolic Anomaly	Residual
6.825e-07	1.001414	0.000483	~1.8e-21

Residual is the difference between the input mean anomaly and the value computed by inverting the solver.
For all tested objects, results match published JPL/MPC solutions to high precision.

Validation Benchmarks
Elliptical (Planets/Saturn): Residual < 1e-10 (identical to JPL Horizons output)

Hyperbolic (Borisov/Oumuamua): Residual < 1e-18 (within floating-point limits)

Batch tested on planets, hyperbolic comets, and interstellar objects.

Transparency: All steps shown in the Jupyter notebook (UMT_Solver_Benchmark.ipynb).

Datasets Included
Planets & Moons: JPL Horizons database

Interstellar: 1I/Oumuamua, 2I/Borisov, 3I/ATLAS

Comets/Asteroids: Recent and classic (MPC, Find_Orb)

See /data/ folder for details.

How to Cite
If you use this repository, algorithm, or datasets, please cite:

Abs187187. (2025). UMT-Symbolic-Kepler-Solver (Version 1.0) [Computer software]. Zenodo.
https://github.com/Abs187187/UMT-Symbolic-Kepler-Solver

License
This repository is licensed under the MIT License. See LICENSE for more information.

Questions or Contributions?
Open an issue or submit a pull request!


