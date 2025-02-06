# Smooth Movement with Accelerated Motion and Air Resistance

Implementation of physics model of smooth movement using acceleration, with an upper bound caused by air resistance.

## Equation
```math
F_o = F - (F_f + F_{ar})
```
- $F_o$ is the output force,
- $F$ is the applied force,
- $F_f$ is the friction force,
- $F_{ar}$ is the additional resistance force.


The equation for acceleration output is:

```math
m a_o = m a - \mu m g - k v^2
```

which can be rewritten as:

```math
a_o = a - \mu g - \frac{k v^2}{m}
```

Since $k$ is an air resistance constant for the object, we can absorb $m$ into $k$ and simplify:

```math
a_o = a - \mu g - k v^2
```
Thus giving the final form of equation.


where:  
- $a_o$ is the output acceleration,
- $a$ is the applied force acceleration,
- $\mu$ is a coefficient friction,
- $g$ is gravitational acceleration,
- $k$ is the modified air resistance constant,
- $v$ is velocity.


## Repository content
 - Graphs showing the relationship between acceleration, velocity, and distance traveled,
 - Pygame demo of movable object.

## Demo keybinds
Use ```wsad``` for movement, hold ```b``` faster movement (sprint). 
## How to run

Prefered python version Python 3.12.3 or newer.

Install  required dependencies and libraries

```bash
pip install -r requirements.txt 
```

To run the demo use

```bash
python3 main.py
```