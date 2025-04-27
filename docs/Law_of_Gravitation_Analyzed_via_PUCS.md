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

Within the PUCS framework, SI quantities are expressed in terms of their natural counterparts and the unit scaling factors \( c \), \( $\text{Hz}\_\text{kg}$ \), and \( $G\_n$ \) (represented by \( $t\_P^h = \sqrt{G\_n}$ \)):

-   Gravitational Constant \( $G\_{\rm SI}$ \) (units \( $\mathrm{m^3\,kg^{-1}\,s^{-2}}$ \)):

$$
G\_{\rm SI} = G\_n \cdot \frac{c^3}{\text{Hz}\_\text{kg}} = (t\_P^h)^2 \cdot \frac{c^3}{\text{Hz}\_\text{kg}}
$$

\( $G\_n$ \) (or \( ($t\_P^h)^2$ \)) represents the fundamental gravitational time-squared constant (units \( $\mathrm{s^2}$ \)).
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
F = \left( (t\_P^h)^2 \frac{c^3}{\text{Hz}\_\text{kg}} \right) \frac{(f\_{m1} \text{Hz}\_\text{kg}) (f\_{m2} \text{Hz}\_\text{kg})}{(r\_t c)^2}
$$

$$
F = (t\_P^h)^2 \frac{c^3}{\text{Hz}\_\text{kg}} \frac{f\_{m1} f\_{m2} (\text{Hz}\_\text{kg})^2}{r\_t^2 c^2}
$$

Simplify the terms:

$$
F = (t\_P^h)^2 \frac{c^3 (\text{Hz}\_\text{kg})^2 f\_{m1} f\_{m2}}{ \text{Hz}\_\text{kg} r\_t^2 c^2}
$$

Cancel terms (\( $c^3/c^2 = c$ \), \( $(\text{Hz}\_\text{kg})^2 / \text{Hz}\_\text{kg} = \text{Hz}\_\text{kg}$ \)):

$$
F = (t\_P^h)^2 \cdot c \cdot \text{Hz}\_\text{kg} \cdot \frac{f\_{m1} f\_{m2}}{r\_t^2}
$$

---

## 4. Analysis of the Resulting Formula and Units

The formula \( $F = (t\_P^h)^2 \cdot (c \cdot \text{Hz}\_\text{kg}) \cdot \frac{f\_{m1} f\_{m2}}{r\_t^2}$ \) breaks down the force into components whose units and roles are clearer:

-   \( $(t\_P^h)^2$ \): This represents the fundamental gravitational scale, the time-squared constant \( $G\_n$ \). It provides the necessary \( \mathrm{s^2} \) dimension and the fundamental numerical value of the gravitational coupling (1 in its natural units). Units: \( \mathrm{s^2} \).
-   \( $c \cdot \text{Hz}\_\text{kg}$ \): This is a composite unit scaling factor. Units: \( $(\mathrm{m/s}) \cdot (\mathrm{kg/Hz}) = (\mathrm{m/s}) \cdot (\mathrm{kg \cdot s}) = \mathrm{m \cdot kg}$ \). This factor brings in the specific scales of the SI meter and kilogram to the force calculation.
-   \( $f\_{m1} f\_{m2}$ \): The product of the masses expressed as frequencies. Units: \( $\mathrm{Hz^2}$ \) or \( $\mathrm{s^{-2}}$ \).
-   \( $r\_t^2$ \): The square of the radius expressed as time. Units: \( $\mathrm{s^2}$ \).

Putting the units together:

Units of $F = \( (\mathrm{s^2}) \cdot (\mathrm{m \cdot kg}) \cdot \frac{(\mathrm{s^{-2}})}{(\mathrm{s^2})} = \mathrm{s^2} \cdot \mathrm{m \cdot kg} \cdot \mathrm{s^{-2}} \cdot \mathrm{s^{-2}} = \mathrm{m \cdot kg \cdot s^{-2}} \)$

These are the units of a Newton, the standard SI unit for Force.

The unit cancellation reveals the roles: the \( $\mathrm{s^2}$ \) from \( ($t\_P^h)^2$ \) and \( $r\_t^2$ \) cancel dimensionally, leaving the \( $\mathrm{m \cdot kg}$ \) from the \( $c \cdot \text{Hz}\_\text{kg}$ \) scaling factor multiplied by the \( $\mathrm{s^{-2}}$ \) from the squared frequencies \( $f\_{m1} f\_{m2}$ \).

---

## 5. Key Insights: The Role of \( $G\_{\rm SI}$ \) as a Unit Scaler

This decomposition reveals exactly what the complex value of \( $G\_{\rm SI}$ \) in the standard formula is doing:

-   \( $G\_{\rm SI}$ \) is not an isolated, fundamental property of reality in the way that \( $G\_\text{planck}$ \), \( c \) (Length-Time scaler), or \( $\text{Hz}\_\text{kg}$ \) (Mass-Frequency scaler) are within the PUCS framework.
-   Instead, \( $G\_{\rm SI}$ \) serves as a necessary **composite unit scaling factor** for the SI system. Its numerical value \( $\approx 6.674 \times 10^{-11}$ \) is precisely the product of the numerical value of \( G\_\text{planck} \) (1 in its natural dimensionless unit) and the scaling factors \( G\_n \), \( $c^3$ \), and \( $1/\text{Hz}\_\text{kg}$ \) needed to reconcile the arbitrary scales of the SI meter, kilogram, and second with the fundamental gravitational proportionality governed by \( G\_n \).
-   The standard formula \( $F = G\_{\rm SI} m\_{1, \rm SI} m\_{2, \rm SI} / r\_{\rm SI}^2$ \) works because \( $G\_{\rm SI}$ \) includes the scaling \( $c^3/\text{Hz}\_\text{kg}$ \) which, when multiplied by \( $m\_{1, \rm SI} m\_{2, \rm SI} / r\_{\rm SI}^2$ \) (which contains SI units \( $\mathrm{kg^2/m^2}$ \)), correctly transforms the units and scales to yield a force in Newtons, while implicitly reflecting the underlying relationship driven by \( $(t\_P^h)^2$ \) and the proportionalities expressed as frequencies and times.

In essence, \( $G\_{\rm SI}$ \) is the specific numerical bridge required to make gravity calculations consistent when using SI units. Its complex form embodies the transformations needed to align SI's arbitrary scales with the universe's fundamental gravitational constant \( $G\_\text{planck}$ = 1 \). The formula, when broken down, shows the gravitational time unit scaling \( $(t\_P^h)^2$ \), scaled by \( $c^3 / \text{Hz}\_\text{kg}$ \) to fit the SI s, kg, and m base units, acting on the masses (as frequencies) and radius (as time).

This analysis highlights how the perceived complexity of \( G \) in SI is a result of its role as a multi-axis of measurement unit scaling constant, necessary because SI units are arbitrarily scaled relative to the natural proportionalities and the fundamental gravitational scale of a dimensionless 1.

---

## 6. Conclusion

Applying the PUCS framework to Newton's Law reveals that the gravitational constant \( G \) in SI units is a complex composite scaling factor \( $(t\_P^h)^2 \cdot c^3 / \text{Hz}\_\text{kg}$ \). This factor is essential for converting mass and distance values measured in arbitrary SI base units into a force value consistent with the fundamental gravitational time coupling constant \( $G\_n$ \). This perspective demystifies \( G \) by showing its numerical value is a consequence of unit definitions rather than a standalone Layer 1 mystery, and clarifies how our choice of measurement system shapes the appearance of fundamental laws.