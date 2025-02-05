# Smooth Movement with Accelerated Motion and Air Resistance

Implementation of physic model of smooth movement using acceleration, with an upper bound caused by air resistance.

## Equation
```math
F_o = F - (F_f + F_{ar})
```
where:
- \( F_o \) is the output force,
- \( F \) is the initial force,
- \( F_f \) is the friction force,
- \( F_{ar} \) is the additional resistance force.

---

The equation for acceleration output is:

```math
m a_o = m a - \mu_i m g - k v^2
```

which can be rewritten as:

```math
a_o = a - \mu_i g - \frac{k v^2}{m}
```

Since \( k \) is an air resistance constant for the object, we can absorb \( m \) into \( k \) and simplify:

```math
a_o = a - \mu_i g - k v^2
```

where:
- \( a_o \) is the output acceleration,
- \( a \) is the initial acceleration,
- \( \mu_i \) is a coefficient related to friction,
- \( g \) is gravitational acceleration,
- \( k \) is the modified air resistance constant,
- \( v \) is velocity.

## Repository content
 - Graphs showing the relationship between acceleration, velocity, and distance traveled,
 - Pygame demo of movable object.