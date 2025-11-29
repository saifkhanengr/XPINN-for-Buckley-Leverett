# Extended Physics Informed Neural Network for Hyperbolic Two-Phase Flow in Porous Media 

## Abstract
The accurate solution of nonlinear hyperbolic partial differential equations (PDEs) remains challenging due to steep gradients, discontinuities, and multiscale structures that make conventional solvers computationally demanding. Physics-Informed Neural Networks (PINNs) embed the governing equations into the learning process, enabling mesh-free solution of PDEs, yet they often struggle to capture steep gradients, discontinuities, and complex nonlinear wave interactions. To address these limitations, we employ the Extended Physics-Informed Neural Network (XPINN) framework to solve the nonlinear Buckley-Leverett equation with a nonconvex flux, modeling immiscible two-phase flow in porous media. The computational domain is dynamically decomposed in space and time into evolving pre-shock and post-shock subdomains, allowing localized subnetworks to efficiently learn distinct flow behaviors, with coupling enforced via the Rankine-Hugoniot jump condition to ensure physically consistent flux continuity. We compare XPINN with standard PINNs and its variants, including PINN with artificial viscosity, PINN with Welge construction, and PINN with the Oleinik entropy condition, and across all cases, XPINN consistently outperforms the other methods, accurately resolving sharp fronts and capturing the correct physical behavior. Importantly, XPINN achieves this using the simpler Adam optimizer, whereas some PINN variants require more complex or higher-order strategies such as L-BFGS to reach comparable accuracy, demonstrating that XPINN is a robust and scalable approach for challenging hyperbolic PDEs without artificial diffusion or entropy corrections.

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
