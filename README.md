# Extended Physics-Informed Neural Network (XPINN) for Hyperbolic Two-Phase Flow

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
└── README.md
```


## Requirements
pip install numpy matplotlib tensorflow jupyter

## How to Run
git clone https://github.com/saifkhanengr/XPINN-for-Buckley-Leverett.git

cd XPINN-for-Buckley-Leverett

jupyter notebook

Open:
XPINN_for_Buckley_Leverett.ipynb

Run all cells.

## Reproducibility
All results can be reproduced using this repository by running the notebook without modification.

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
For academic and research use.
