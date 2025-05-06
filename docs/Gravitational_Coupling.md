# Gravitational Coupling: A Dimensionless Ratio Revealed by Unit Scaling

## Abstract

The dimensionless gravitational coupling for a particle of mass \(m\), typically expressed using standard constants, appears complex. By applying the Physics Unit Coordinate System (PUCS) framework, we decompose the involved SI constants into their fundamental unit scaling factors, demonstrating that the complexity cancels out. The resulting dimensionless ratio reveals the coupling as a simple product of fundamental natural scales, highlighting how SI unit scaling obscures this underlying structure.

---

## 1. Standard Dimensionless Gravitational Coupling

A common dimensionless quantity representing the gravitational coupling strength for a particle of mass \(m\) (e.g., the electron mass) is given by:

$$
A\_G = \frac{G \cdot m^2}{\hbar \cdot c}
$$

Where \(G\), \(m\), \(\$hbar$\), and \(c\) are their values in a given unit system (e.g., SI). This ratio is dimensionless:
[Units of G]: M⁻¹ L³ T⁻²
[Units of m]: M
[Units of hbar]: M L² T⁻¹
[Units of c]: L T⁻¹

[Units of \($A\_G$\)]: \( $\frac{\text{M⁻¹ L³ T⁻²} \cdot \text{M}^2}{\text{M L² T⁻¹} \cdot \text{L T⁻¹}} = \frac{\text{M L³ T⁻²}}{\text{M L³ T⁻²}} = 1 \) (Dimensionless)$

---

## 2. PUCS Definitions of SI Constants and Mass

Within the PUCS framework, we define the SI values of these quantities in terms of fundamental scaling factors:

*   **Gravitational Constant \($G\_{SI}$\):** Relates to the fundamental gravitational time-squared constant \($G\_n$\) (or \($t\_P^h\)^2$) and other scalers.

$$ G\_{SI} = G\_n \cdot \frac{c^3}{Hz\_\text{kg}} $$

    \($G\_n$\) (or \($t\_P^h\)^2$) has units \($s^2$\). \(c\) has units \(m/s\). \($Hz\_\text{kg}$\) has units \($kg \cdot s$\).

*   **Mass \($m\_{SI}$\):** Relates to the natural mass equivalent \($m\_n$\) (frequency) and the mass-frequency scaler.

$$ m\_{SI} = m\_n \cdot Hz\_\text{kg} $$

    \($m\_n$\) has units \(Hz\) or \($s^{-1}$\). \($Hz\_\text{kg}$\) has units \($kg \cdot s$\).

*   **Reduced Planck Constant \(\hbar\_{SI}\):** Relates to \(h\), which is a composite of \($Hz\_\text{kg}$\) and \($c^2$\).

$$ \hbar\_{SI} = \frac{h\_{SI}}{2\pi} = \frac{Hz\_\text{kg} \cdot c^2}{2\pi} $$

    \(2\pi\) is dimensionless.

*   **Speed of Light \($c\_{SI}$\):** A fundamental scaler for length-time.

$$ c\_{SI} = c $$

    \(c\) has units \(m/s\).

---

## 3. Substitute and Simplify within PUCS

Substitute the PUCS definitions for \(G\), \(m\), \($\hbar$\), and \(c\) (using their SI values) into the expression for \($A\_G$\):

$$
A\_G = \frac{\left(G\_n \cdot \frac{c^3}{Hz\_\text{kg}}\right) \cdot (m\_n \cdot Hz\_\text{kg})^2}{\left(\frac{Hz\_\text{kg} \cdot c^2}{2\pi}\right) \cdot c}
$$

Expand the squared term:

$$
A\_G = \frac{G\_n \cdot \frac{c^3}{Hz\_\text{kg}} \cdot m\_n^2 \cdot (Hz\_\text{kg})^2}{\frac{Hz\_\text{kg} \cdot c^3}{2\pi}}
$$

Rearrange the terms and use the property of dividing by a fraction:

$$
A\_G = G\_n \cdot \frac{c^3}{Hz\_\text{kg}} \cdot m\_n^2 \cdot (Hz\_\text{kg})^2 \cdot \frac{2\pi}{Hz\_\text{kg} \cdot c^3}
$$

Group terms:

$$
A\_G = G\_n \cdot m\_n^2 \cdot (Hz\_\text{kg}) \cdot \frac{c^3}{Hz\_\text{kg}} \cdot (Hz\_\text{kg}) \cdot \frac{2\pi}{c^3}
$$

$$
A\_G = G\_n \cdot m\_n^2 \cdot (Hz\_\text{kg})^2 \cdot c^3 \cdot \frac{2\pi}{Hz\_\text{kg}^2 \cdot c^3}
$$

Cancel the terms \($(Hz\_\text{kg})^2\)$ and \($c^3$\) in the numerator and denominator:

$$
A\_G = G\_n \cdot m\_n^2 \cdot 2\pi
$$

$$
A\_G = 2\pi \cdot G\_n \cdot m\_n^2
$$

---

## 4. Interpretation within PUCS

The derivation shows that the dimensionless gravitational coupling \($A\_G = \frac{G m^2}{\hbar c}$\) simplifies to \($2\pi \cdot G\_n \cdot m\_n^2$\) when the SI constants are broken down into their fundamental scaling factor components.

*   \($G\_n$\) is the fundamental gravitational time-squared constant (units \($s^2$\)).
*   \($m\_n$\) is the natural mass equivalent (frequency, units \($s^{-1}$\)).
*   \($m\_n^2$\) has units \($s^{-2}$\).

The product \($G\_n \cdot m\_n^2$\) has units \($s^2 \cdot s^{-2} = 1$\), confirming it is dimensionless.

*   **Unit Scaling Cancellation:** The factors \(c\) and \($Hz\_\text{kg}$\) (and \($2\pi$\) from \($\hbar$\)), which are components of the SI constants, **completely cancel out** in this derivation. This demonstrates that their presence in the standard formula $\frac{G m^2}{\hbar c}$ is due to their role as unit scaling factors embedded within \(G\), \(m\), \($\hbar$\), and \(c\) in the SI system. They are necessary to make the calculation work dimensionally and numerically in SI units, but they cancel when revealing the underlying natural relationship.

*   **Underlying Natural Relationship:** The dimensionless gravitational coupling is fundamentally the product of \($2\pi$\), the fundamental gravitational time constant squared (\($G\_n$\)), and the square of the natural mass equivalent (\($m\_n$\)).

---

## 5. Significance

This analysis demonstrates that the perceived complexity and interpretation of $\frac{G m^2}{\hbar c}$ (often seen as an interplay between gravity, quantum mechanics, and relativity due to the presence of \(G\), \($\hbar$\), and \(c\)) is partially an artifact of SI unit scaling. By breaking down the constants, we see that the factors \(c\) and \(h\) (or \($\hbar$\)), which might imply "relativity" and "quantum mechanics" are fundamentally defining this coupling, actually cancel out. The dimensionless ratio is ultimately determined by the fundamental gravitational time scale (\($G\_n$\)) and the fundamental mass scale (\($m\_n$\)), scaled by \($2\pi$\).

The mystery shifts from explaining why \(G\), \($\hbar$\), and \(c\) combine in this specific way to produce a number like \($1.75 \times 10^{-45}$\) (for the electron) to understanding why the fundamental gravitational time constant and the natural mass equivalent (frequency) have values such that their product, scaled by \($2\pi$\), equals this number. The complexity of unit scaling has been removed, revealing a simpler product of natural scales.