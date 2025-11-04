# Extended Physics Informed Neural Network for Hyperbolic Two-Phase Flow in Porous Media 

## Abstract
The accurate solution of nonlinear hyperbolic partial differential equations (PDEs) remains a central challenge in computational science due to the presence of steep gradients, discontinuities, and multiscale structures that make conventional discretization-based solvers computationally demanding. Physics-Informed Neural Networks (PINNs) embed the governing equations into the learning process, enabling mesh-free solution of PDEs, yet they often struggle to capture steep gradients, discontinuities, and complex nonlinear wave interactions. To address these limitations, this study employs the Extended Physics-Informed Neural Network (XPINN) framework to solve the nonlinear Buckley-Leverett equation with a nonconvex flux function, which models immiscible two-phase flow in porous media. The computational domain is dynamically decomposed in space and time into evolving pre-shock and post-shock regions, allowing localized subnetworks to efficiently learn distinct flow behaviors. Coupling between subnetworks is achieved through the Rankine-Hugoniot jump condition, which enforces physically consistent flux continuity across the moving shock interface. Numerical experiments demonstrate that the proposed XPINN approach accurately captures discontinuous saturation fronts and compound wave interactions without requiring artificial diffusion or entropy corrections. Compared to standard PINNs, the XPINN framework achieves superior stability, faster convergence, and enhanced resolution of nonlinear wave dynamics using smaller, domain-specific models with fewer trainable parameters, establishing it as an effective and scalable tool for solving challenging hyperbolic PDEs in multiphase flow problems. The code of this work is available on

### Authors:
- Saif Ur Rehman
- Wajid Yousuf

Cite as:



