# Decoding Planck Units via Unit Scaling and G_n

## Abstract

Standard formulas for Planck units appear as complex combinations of fundamental constants \( \hbar \), \( c \), and \( G \). This document shows how, within the unit scaling framework, these complexities dissolve. By defining the "natural" gravitational constant \( G_n \), we demonstrate that the \( h \)-based Planck units (Length, Time, Mass, Temperature) emerge as simple expressions involving \( \sqrt{G_n} \) and the framework's core unit scaling factors \( c \), \( \text{Hz}_\text{kg} \), and \( \text{K}_\text{Hz} \). This reveals \( G_n \) as the fundamental scaling parameter for the Planck scale and clarifies the role of other constants as conversion bridges.

---

## 1. The Standard Gravitational Constant ($G_{SI}$)

The gravitational constant $G$ in SI units has a value and dimensions:

$$ G_{SI} \approx 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} $$

Its role in standard formulas often makes Planck units seem like arbitrary combinations of constants.

---

## 2. Introducing the Natural Gravitational Constant ($G_n$)

Within the unit scaling framework, $G_{SI}$ is related to a more fundamental, "natural" gravitational constant $G_n$. We define $G_{SI}$ as $G_n$ scaled by factors derived from other fundamental constants that relate SI units to natural units:

$$ G_{SI} = G_n \cdot \frac{c^3}{\text{Hz}_\text{kg}} $$

Here:
- \( G_n \) is the natural gravitational coupling constant. Based on dimensional analysis making quantities like \( \sqrt{G_n m_n / r_n} \) dimensionless, \( G_n \) has fundamental dimensions of \( [\text{Time}^2] \).
- \( c \) is the speed of light, the scaling factor bridging natural Length and Time units (and SI m and s).
- \( \text{Hz}_\text{kg} = h/c^2 \) is the scaling factor bridging SI Mass (kg) and natural Frequency/Mass/Energy units (Hz equivalent).

This definition means \( G_n = G_{SI} \cdot \frac{\text{Hz}_\text{kg}}{c^3} \). Calculating its value using SI constants gives \( G_n \approx 2.903 \times 10^{-87} \, \text{s}^2 \).

---

## 3. Other Core Unit Scaling Factors

We also use the following scaling factors from the framework:
- \( c \approx 2.998 \times 10^8 \, \text{m/s} \) (Length \( \leftrightarrow \) Time)
- \( \text{Hz}_\text{kg} = h/c^2 \approx 7.372 \times 10^{-51} \, \text{kg/Hz} \) (Mass \( \leftrightarrow \) Frequency/Energy)
- \( \text{K}_\text{Hz} = k_B/h \approx 2.084 \times 10^{10} \, \text{Hz/K} \) (Temperature \( \leftrightarrow \) Frequency)

Note that \( k_B = \text{K}_\text{Hz} \cdot h = \text{K}_\text{Hz} \cdot \text{Hz}_\text{kg} \cdot c^2 \).

---

## 4. Deriving the h-Based Planck Units

Using the natural constant \( G_n \) and the scaling factors, the \( h \)-based Planck units (where \( h=1 \), \( c=1 \), \( k=1 \), \( G=1 \) in their own natural system) simplify dramatically when expressed in SI units:

- **Planck Time ($t_P^h$):**
  The natural time scale is set directly by \( \sqrt{G_n} \).
  $$ t_P^h = \sqrt{G_n} $$
  (Dimensions: \( \sqrt{[\text{Time}^2]} = [\text{Time}] \). Value \( \sqrt{2.903 \times 10^{-87}} \approx 5.391 \times 10^{-44} \, \text{s} \))

- **Planck Length ($l_P^h$):**
  The natural length scale is the natural time scale scaled by \( c \).
  $$ l_P^h = \sqrt{G_n} \cdot c $$
  (Dimensions: \( [\text{Time}] \cdot [\text{Length}/\text{Time}] = [\text{Length}] \). Value \( 5.391 \times 10^{-44} \times 2.998 \times 10^8 \approx 1.616 \times 10^{-35} \, \text{m} \))

- **Planck Mass ($m_P^h$):**
  The natural mass scale is the inverse of the natural time scale, scaled by \( \text{Hz}_\text{kg} \) to get to kilograms.
  $$ m_P^h = \frac{1}{\sqrt{G_n}} \cdot \text{Hz}_\text{kg} $$
  (Dimensions: \( [\text{Time}]^{-1} \cdot [\text{Mass} \cdot \text{Time}] = [\text{Mass}] \). Value \( (5.391 \times 10^{-44})^{-1} \times 7.372 \times 10^{-51} \approx 1.850 \times 10^{-9} \, \text{kg} \))

- **Planck Temperature ($T_P^h$):**
  The natural temperature scale is related to the inverse of the natural time scale, scaled by \( 1/\text{K}_\text{Hz} \) to get to Kelvin.
  $$ T_P^h = \frac{1}{\sqrt{G_n}} \cdot \frac{1}{\text{K}_\text{Hz}} $$
  (Dimensions: \( [\text{Time}]^{-1} \cdot [\text{Temperature}/\text{Frequency}] = [\text{Time}]^{-1} \cdot [\text{Temperature} \cdot \text{Time}] = [\text{Temperature}] \). Value \( (5.391 \times 10^{-44})^{-1} \times (2.084 \times 10^{10})^{-1} \approx 3.550 \times 10^{32} \, \text{K} \))

These formulas precisely match the standard definitions of the \( h \)-based Planck units when \( G_n = G_{SI} \cdot \frac{Hz_{kg}}{c^3} \).

---

## 5. Key Insights

- **\( G_n \) is the Primary Scale:** The natural gravitational constant \( G_n \) is the fundamental unit of squared time \( (T_n)^2 \) from which the Planck scale naturally emerges. Its square root \( \sqrt{G_n} \) sets the base unit of time at the Planck scale in this framework.
- **Constants as Multipliers:** \( c \), \( \text{Hz}_\text{kg} \), and \( \text{K}_\text{Hz} \) are not just abstract constants; they are the necessary scaling factors to convert the base time scale \( \sqrt{G_n} \) into corresponding scales of length, mass, and temperature within our chosen (SI) unit system.
- **Simplicity Revealed:** The standard Planck unit formulas appear complex because they mix \( G_{SI} \) (a composite scalar) with \( \hbar \) (a composite scalar) and \( c \). By using \( G_n \) (a base scalar) and the other scaling factors, the structure becomes simple: Length is Time times \( c \), Mass is inverse Time scaled by \( \text{Hz}_\text{kg} \), Temperature is inverse Time scaled by \( 1/\text{K}_\text{Hz} \).
- **Dimensional Consistency:** The derivations show that the units cancel perfectly within the framework's definitions, resulting in the expected SI units for each Planck quantity.

---

## 6. Conclusion

The unit scaling framework, by defining a natural gravitational constant \( G_n \) with dimensions of \( [\text{Time}^2] \), simplifies the derivation and interpretation of Planck units. The \( h \)-based Planck length, time, mass, and temperature are revealed as direct products of \( \sqrt{G_n} \) (the fundamental time scale) and the core unit scaling factors \( c \), \( \text{Hz}_\text{kg} \), and \( \text{K}_\text{Hz} \). This demonstrates that the Planck scale is fundamentally set by \( G_n \), and the other constants merely act as conversion factors to express this scale across different dimensions (Length, Mass, Temperature) within our arbitrary SI unit system. This perspective demystifies Planck units and reinforces the framework's view of fundamental constants as the essential bridges between our units and the universe's inherent proportionalities.