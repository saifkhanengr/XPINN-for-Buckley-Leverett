# Extended Physics-Informed Neural Network for Hyperbolic Two-Phase Flow in Porous Media

## Overview
This repository provides the implementation of an Extended Physics-Informed Neural Network (XPINN) for solving the nonlinear Buckley–Leverett equation, which models immiscible two-phase flow in porous media.

The method is designed to overcome limitations of standard Physics-Informed Neural Networks (PINNs) in handling:
- Sharp fronts (shock waves)
- Strong nonlinearities
- Discontinuities in hyperbolic PDEs

## Problem Description
The Buckley–Leverett equation is a nonlinear hyperbolic partial differential equation that describes two-phase flow in porous media. Due to its nonconvex flux, the solution develops discontinuities (shocks), making it challenging for traditional numerical and machine learning methods.

## Method (XPINN)
The XPINN framework improves learning by:
- Decomposing the domain into pre-shock and post-shock regions
- Assigning separate neural networks to each subdomain
- Enforcing physical consistency via the Rankine–Hugoniot jump condition
- Allowing localized learning of different flow regimes

## Key Features
- Accurate resolution of shock fronts
- No artificial viscosity required
- No entropy correction needed
- Works with Adam optimizer only
- Better performance than standard PINN variants

## Repository Structure

```
XPINN-for-Buckley-Leverett/
├── XPINN_for_Buckley_Leverett.ipynb
├── run.py
├── requirements.txt
├── LICENSE
├── README.md
```

## Installation

Clone the repository:

git clone https://github.com/saifkhanengr/XPINN-for-Buckley-Leverett.git

cd XPINN-for-Buckley-Leverett 

Install dependencies:

pip install -r requirements.txt 

## How to Run

### Option 1 (Recommended - Automated)

python run.py

### Option 2 (Manual)

jupyter notebook

Then open:

XPINN_for_Buckley_Leverett.ipynb

and run all cells.

## Reproducibility
All results reported in the paper can be reproduced by running:

python run.py

No modification to the code is required.

## Expected Output
Running the code will reproduce:
- XPINN solution for the Buckley–Leverett problem
- Shock front behavior and saturation profiles
- Results corresponding to the figures (2 to 12) presented in the paper

## Computer Code Availability
The code developed for this study is publicly available:
https://github.com/saifkhanengr/XPINN-for-Buckley-Leverett

The repository includes:
- Full implementation of XPINN
- Training and evaluation workflow
- Instructions to reproduce results

### Authors:
- Saif Ur Rehman
- Wajid Yousuf

Cite as:

```bibtex
@article{SaifXPINN2025,
  title={Extended Physics Informed Neural Network for Hyperbolic Two-Phase Flow in Porous Media},
  author={Ur Rehman, Saif and Yousuf, Wajid},
  journal={arXiv preprint arXiv:2511.13734},
  year={2025}
}
```

## License
This project is licensed under the MIT License.

