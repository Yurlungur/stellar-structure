# Stellar Structure Toy

Author: [Jonah Miller](jonah.maxwell.miller@gmail.com)

This is a simple program showing how to solve for the density and
pressure of the interior of a star using the Forward Euler method.

## Purpose

This code is intended as a teaching school for the interested
programming or physics student.

## The system

We use the stellar structure equations:

*(dM/dr) = 4 pi r^2 rho*

and

*(dP/dr) = - G M rho/r^2*

where *M* is the mass contained in a spherical shell of radius *r*,
*P* is the pressure at a given radius, and the mass density is gien by

*rho = rho(P)*

where *rho(P)* is the *equation of state.* We use a simple
*polytropic* equation of state

*rho(P) = (P/K)^(n/(n+1))*

for some *K* and *polytropic index* *n*.

## Procedure

At the center of the star, *M=0* (there is no mass contained in the
shell of radius zero) and the pressure is some fixed constant. We use
the stellar structure equations to iterate outwards and we stop when
*P=0*. This signifies that we've reached the outer edge of the star.

Therefore, a given pressure in the center of the star produces a
different mass and a different radius of the star.

## To run

Simply clone the repository and run

```bash
python2 structure.py
```

This should produce a pdf plot. You can play with the constants at the
top of the program to change the polytropic index, the initial
pressure, or the radial distance for the forward Euler step.
