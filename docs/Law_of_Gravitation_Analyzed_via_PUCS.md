# Newton's Law of Gravitation Analyzed via PUCS

## Abstract

The standard formulation of Newton's Law of Gravitation in SI units features the gravitational constant \( G \). Within the Physics Unit Coordinate System (PUCS) framework, we reveal that the complex numerical value and dimensions of \( G \) in SI are not fundamental Layer 1 properties, but rather composite Layer 3 scaling factors. We demonstrate how substituting the PUCS-defined components of \( G \), mass (\( m \)), and radius (\( r \)) into the formula \( $F = G m\_1 m\_2 / r^2$ \) breaks down the force calculation into its fundamental gravitational time scaling and the necessary unit scaling factors to convert to SI units. This analysis clarifies the role of \( G \) as a crucial multi-dimensional unit scaling constant.

---

## 1. Standard Formula in SI Units

Newton's Law of Gravitation in standard SI units is:

$$
F = G\_{\rm SI} \frac{m\_{1, \rm SI} m\_{2, \rm SI}}{r\_{\rm SI}^2}
$$

Where \( $G\_{\rm SI}$ \) is the gravitational constant in SI, \( $m\_{\rm SI}$ \) are masses in kilograms, \( $r\_{\rm SI}$ \) is the distance in meters, and \( F \) is the force in Newtons.

---

## 2. PUCS Definitions for SI Quantities

Within the PUCS framework, SI quantities are expressed in terms of their natural counterparts and the unit scaling factors \( c \), \( $\text{Hz}\_\text{kg}$ \), and \( $G\_n$ \) (represented by \( $t\_{Ph} = \sqrt{G\_n}$ \)):

-   Gravitational Constant \( $G\_{\rm SI}$ \) (units \( $\mathrm{m^3\,kg^{-1}\,s^{-2}}$ \)):

$$
G\_{\rm SI} = G\_n \cdot \frac{c^3}{\text{Hz}\_\text{kg}} = (t\_{Ph})^2 \cdot \frac{c^3}{\text{Hz}\_\text{kg}}
$$

\( $G\_n$ \) (or \( ($t\_{Ph})^2$ \)) represents the fundamental gravitational time-squared constant (units \( $\mathrm{s^2}$ \)).
    \( $c^3 / \text{Hz}\_\text{kg}$ \) are the scaling factors bridging natural units to SI dimensions.

-   Mass $\( m\_{\rm SI} \) (units \( \mathrm{kg} \))$:
    In the Energy/Mass/Frequency equivalence, mass can be represented by frequency scaled by \( $\text{Hz}\_\text{kg}$ \):

$$
m\_{\rm SI} = f\_m \cdot \text{Hz}\_\text{kg}
$$

\( $f\_m$ \) is the mass expressed as an equivalent frequency (units \( $\mathrm{Hz}$ \) or \( $\mathrm{s^{-1}}$ \)).
\( $\text{Hz}\_\text{kg}$ \) is the mass-per-frequency scaling factor (units \( $\mathrm{kg\,s}$ \)).

-   Radius \( $r\_{\rm SI}$ \) (units \( $\mathrm{m}$ \)):
    In the Length/Time equivalence, length can be represented by time scaled by \( c \):
This is true because in natural units of mass, it is mathematically the identical value of frequency because f ~ m in this universe.

$$
r\_{\rm SI} = r\_t \cdot c
$$

\( $r\_t$ \) is the radius expressed as an equivalent time (units \( $\mathrm{s}$ \)).
\( c \) is the length-per-time scaling factor (units \( $\mathrm{m/s}$ \)).
This is true because in natural units of length, it is mathematically the identical value of time because length ~ time in this universe.

---

## 3. Substituting into Newton's Law

Substitute these PUCS definitions into the formula \( $F = G\_{\rm SI} \frac{m\_{1, \rm SI} m\_{2, \rm SI}}{r\_{\rm SI}^2}$ \):

$$
F = \left( (t\_{Ph})^2 \frac{c^3}{\text{Hz}\_\text{kg}} \right) \frac{(f\_{m1} \text{Hz}\_\text{kg}) (f\_{m2} \text{Hz}\_\text{kg})}{(r\_t c)^2}
$$

$$
F = (t\_{Ph})^2 \frac{c^3}{\text{Hz}\_\text{kg}} \frac{f\_{m1} f\_{m2} (\text{Hz}\_\text{kg})^2}{r\_t^2 c^2}
$$

Simplify the terms:

$$
F = (t\_{Ph})^2 \frac{c^3 (\text{Hz}\_\text{kg})^2 f\_{m1} f\_{m2}}{ \text{Hz}\_\text{kg} r\_t^2 c^2}
$$

Cancel terms (\( $c^3/c^2 = c$ \), \( $(\text{Hz}\_\text{kg})^2 / \text{Hz}\_\text{kg} = \text{Hz}\_\text{kg}$ \)):

$$
F = (t\_{Ph})^2 \cdot c \cdot \text{Hz}\_\text{kg} \cdot \frac{f\_{m1} f\_{m2}}{r\_t^2}
$$

We can now scale the frequency to planck time unit scales. $f_m * t_{Ph}  = m_{planck}$

$$
F = c \cdot \text{Hz}\_\text{kg} \cdot \frac{m\_{planck1} m\_{planck2}}{r\_t^2}
$$

This just leaves kg m/ s^2 units. The proportion is now matching the universe's scale and the newton's scale to align the proportion to the value of the Newton in this formula.  

Let's remove that last little bit of SI unit scaling in the denominator.  We know $r_t = r_planck t_{Ph}$. 


$$
F = c \cdot \text{Hz}\_\text{kg} \cdot \frac{m\_{planck1} m\_{planck2}}{r\_{planck}^2 \cdot t_{Ph}^2}
$$

And we can pull that out to the scaling term.

$$
F = \frac {c \cdot \text{Hz}\_\text{kg}}{t_{Ph}^2} \cdot \frac{m\_{planck1} m\_{planck2}}{r\_{planck}^2}
$$

And we can divide through by that scaling term to get a dimensionless formula. The natural gravity law formula, back to how Newton formulated it.

$$
F_planck = \frac{m\_{planck1} m\_{planck2}}{r\_{planck}^2}
$$

By reversing these steps, scaling the Force to an SI Newton, scaling the planck length and mass terms to their SI scaling and simplifying we restore the original formula, showing that it was just unit scaling all along.



---

## 4. Analysis of the Resulting Formula and Units

The final form of the formula is dimensionless, it has no units.  This is exactly how Newton used it his entire life. 

---

## 5. Key Insights: The Role of \( $G\_{\rm SI}$ \) as a Unit Scaler

This decomposition reveals exactly what the complex value of \( $G\_{\rm SI}$ \) in the standard formula is doing:

-   \( $G\_{\rm SI}$ \) is not an isolated, fundamental property of reality in the way that \( $G\_\text{planck}$ \), \( c \) (Length-Time scaler), or \( $\text{Hz}\_\text{kg}$ \) (Mass-Frequency scaler) are within the PUCS framework.
-   Instead, \( $G\_{\rm SI}$ \) serves as a necessary **composite unit scaling factor** for the SI system. Its numerical value \( $\approx 6.674 \times 10^{-11}$ \) is precisely the product of the numerical value of \( $G\_\text{planck}$ \) (1 in its natural dimensionless unit) and the scaling factors \( G\_n \), \( $c^3$ \), and \( $1/\text{Hz}\_\text{kg}$ \) needed to reconcile the arbitrary scales of the SI meter, kilogram, and second with the fundamental gravitational proportionality governed by \( $G\_\text{planck}$ \).
-   The standard formula \( $F = G\_{\rm SI} m\_{1, \rm SI} m\_{2, \rm SI} / r\_{\rm SI}^2$ \) works because \( $G\_{\rm SI}$ \) includes the scaling \( $c^3/\text{Hz}\_\text{kg}$ \) which, when multiplied by \( $m\_{1, \rm SI} m\_{2, \rm SI} / r\_{\rm SI}^2$ \) (which contains SI units \( $\mathrm{kg^2/m^2}$ \)), correctly transforms the units and scales to yield a force in Newtons, while implicitly reflecting the underlying relationship driven by \( $(t\_{Ph})^2$ \) and the proportionalities expressed as frequencies and times.

In essence, \( $G\_{\rm SI}$ \) is the specific numerical bridge required to make gravity calculations consistent when using SI units. Its complex form embodies the transformations needed to align SI's arbitrary scales with the universe's fundamental gravitational constant \( $G\_\text{planck}$ = 1 \). The formula, when broken down, shows the gravitational time unit scaling \( $(t\_{Ph})^2$ \), scaled by \( $c^3 / \text{Hz}\_\text{kg}$ \) to fit the SI s, kg, and m base units, acting on the masses (as frequencies) and radius (as time).

This analysis highlights how the perceived complexity of \( G \) in SI is a result of its role as a multi-axis of measurement unit scaling constant, necessary because SI units are arbitrarily scaled relative to the natural proportionalities and the fundamental gravitational scale of a dimensionless 1.

---

## 6. Conclusion

Applying the PUCS framework to Newton's Law reveals that the gravitational constant \( G \) in SI units is a complex composite scaling factor \( $(t\_{Ph})^2 \cdot c^3 / \text{Hz}\_\text{kg}$ \). This factor is essential for converting mass and distance values measured in arbitrary SI base units into a force value consistent with the fundamental gravitational time coupling constant \( $G\_n$ \). This perspective demystifies \( G \) by showing its numerical value is a consequence of unit definitions rather than a standalone Layer 1 mystery, and clarifies how our choice of measurement system shapes the appearance of fundamental laws.