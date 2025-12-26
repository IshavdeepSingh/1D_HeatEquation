# 1D Heat Equation Simulation (Finite Difference Method)

This project numerically simulates **heat diffusion along a one-dimensional rod** using the **explicit finite-difference method**. The simulation models how temperature evolves in time due to thermal conduction, given fixed boundary temperatures.

---

## What this project does

- Models a **1D rod** with fixed temperatures at both ends
- Solves the **1D heat equation**:
  
  \[
  \frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
  \]

- Uses **finite differences** to discretize space and time
- Enforces a **numerical stability condition** for the explicit scheme
- Visualizes temperature evolution using a color map
- Prints the average temperature as the system evolves toward equilibrium

---

## Physical model

### Governing equation
The heat equation describes how temperature \(u(x,t)\) diffuses through a material:

- \(u(x,t)\): temperature
- \(\alpha\): thermal diffusivity (material property)

In this simulation:
- \(\alpha = 110 \ \text{mm}^2/\text{s}\)
- The rod length is 50 mm
- Heat flows only along one spatial dimension

---

## Numerical method

### Spatial discretization
The rod is divided into a finite number of nodes:

- Number of nodes: `nodes = 10`
- Spatial step:
  \[
  \Delta x = \frac{\text{length}}{\text{nodes}}
  \]

### Time discretization
Time is advanced in small steps \(\Delta t\), chosen to satisfy the **stability condition** for the explicit finite-difference scheme:

\[
\Delta t \le \frac{1}{2} \frac{\Delta x^2}{\alpha}
\]

In the code:
```python
dt = 0.5 * dx**2 / a
