# Schwarzschild Radius Simplification via Modular Unit Scaling

This document demonstrates how applying the Modular Unit Scaling Framework simplifies the standard formula for the Schwarzschild radius, revealing that its perceived complexity in SI units arises from unit scaling artifacts rather than the fundamental physical relationship itself. We will show how, in a unit system aligned with natural scales (like Planck units), the formula reduces to a simple numerical proportionality.

---

## 1. Standard Schwarzschild Radius Formula (SI Units)

The standard formula for the Schwarzschild radius ($r_S$), the radius of the event horizon for a non-rotating, uncharged black hole of mass $M$, is given in SI units by:

$$
r_S = \frac{2 G_{SI} M_{SI}}{c^2}
$$

Where:
*   $r_S$ is the Schwarzschild radius in meters.
*   $G_{SI}$ is the gravitational constant in $\text{m}^3 \text{kg}^{-1} \text{s}^{-2}$.
*   $M_{SI}$ is the mass of the object in kilograms.
*   $c$ is the speed of light in $\text{m/s}$.

---

## 2. Applying Framework Definitions

Within the Modular Unit Scaling Framework, we redefine the SI constants and quantities in terms of more fundamental, 'natural' components and unit scaling factors:

*   **Gravitational Constant:** $G_{SI}$ is expressed using the natural gravitational constant $G_n$ (with dimensions of $\text{[Time}^2]$) and the scaling factors $c$ and $\text{Hz}\_\text{kg}$:

$$
G_{SI} = G_n \cdot \frac{c^3}{\text{Hz}\_\text{kg}} \quad \Bigl[\mathrm{m^3 \cdot kg^{-1} \cdot s^{-2}}\Bigr]
$$

    (Note: $\text{Hz}\_\text{kg} = h/c^2$ is the scaling factor bridging mass (kg) and frequency (Hz), effectively $\text{kg/Hz}$).

*   **Mass:** $M_{SI}$ (mass in kg) can be expressed as an equivalent frequency ($f_M$) scaled by $\text{Hz}\_\text{kg}$:

$$
M_{SI} = f_M \cdot \text{Hz}\_\text{kg} \quad \Bigl[\mathrm{kg}\Bigr]
$$

    ($f_M$ represents the mass $M$ in units of Hz-equivalent mass).

---

## 3. Substitute and Simplify (Still in SI Context)

Substitute these definitions into the standard Schwarzschild radius formula:

$$
r_S = \frac{2 \cdot \left(G_n \cdot \frac{c^3}{\text{Hz}\_\text{kg}}\right) \cdot (f_M \cdot \text{Hz}\_\text{kg})}{c^2}
$$

Simplify the expression:

$$
r_S = \frac{2 \cdot G_n \cdot c^3 \cdot f_M \cdot \text{Hz}\_\text{kg}}{c^2 \cdot \text{Hz}\_\text{kg}}
$$

Cancel the $\text{Hz}\_\text{kg}$ terms and simplify the powers of $c$:

$$
r_S = 2 \cdot G_n \cdot c \cdot f_M
$$

This intermediate result shows the Schwarzschild radius (still in meters) related to the natural gravitational constant ($G_n$ in s²), the speed of light ($c$ in m/s), and the mass expressed as a frequency ($f_M$ in Hz). The units $s^2 \cdot (m/s) \cdot s^{-1}$ correctly yield meters.

---

## 4. Expressing in Planck Units

Now, let's express the Schwarzschild radius and the mass using their numerical values in Planck units.

*   Let $r_{S, PU}$ be the numerical value of the Schwarzschild radius when measured in Planck Lengths ($l_P$). The physical radius is $r_S = r_{S, PU} \cdot l_P$.
*   Let $M_{PU}$ be the numerical value of the mass when measured in Planck Masses ($m_P$). The physical mass is $M = M_{PU} \cdot m_P$.

From the framework ($h$-based Planck units):
*   $G_n = t_P^2$, $c = l_P/t_P$, $m_P = \text{Hz}\_\text{kg}/t_P$.
*   The mass $M_{SI}$ relates to $M_{PU}$ by $M_{SI} = M_{PU} \cdot m_P$.
*   The frequency equivalent of mass $f_M = M_{SI} / \text{Hz}\_\text{kg} = (M_{PU} \cdot m_P) / \text{Hz}\_\text{kg}$.

Substitute $G_n = t_P^2$, $c = l_P/t_P$, and $f_M = (M_{PU} \cdot m_P) / \text{Hz}\_\text{kg}$ into the intermediate formula $r_S = 2 \cdot G_n \cdot c \cdot f_M$:

$$
r_S = 2 \cdot (t_P^2) \cdot \left(\frac{l_P}{t_P}\right) \cdot \left(\frac{M_{PU} \cdot m_P}{\text{Hz}\_\text{kg}}\right)
$$

$$
r_S = 2 \cdot t_P \cdot l_P \cdot \frac{M_{PU} \cdot m_P}{\text{Hz}\_\text{kg}}
$$

Now, substitute $\text{Hz}\_\text{kg} = m_P \cdot t_P$:

$$
r_S = 2 \cdot t_P \cdot l_P \cdot \frac{M_{PU} \cdot m_P}{(m_P \cdot t_P)}
$$

The terms $t_P$ and $m_P$ cancel out:

$$
r_S = 2 \cdot l_P \cdot M_{PU}
$$

Finally, recognize that $r_S = r_{S, PU} \cdot l_P$ where $r_{S, PU}$ is the numerical value of the radius in Planck Lengths:

$$
r_{S, PU} \cdot l_P = 2 \cdot M_{PU} \cdot l_P
$$

Cancel $l_P$ from both sides:

$$
r_{S, PU} = 2 \cdot M_{PU}
$$

---

## 5. Implications of the Simplification

This final result, $r_{S, PU} = 2 \cdot M_{PU}$, is profoundly significant when contrasted with the original SI formula $r_S = \frac{2 G_{SI} M_{SI}}{c^2}$.

*   **Constants as Unit Scaling Artifacts:** The fundamental constants $G_{SI}$ and $c$ (specifically the combination $G_{SI}/c^2$) have completely vanished from the relationship when the quantities are expressed in Planck units. This is because $G_{SI}/c^2$ is precisely the unit scaling factor needed to convert mass (in kg) into a length (in meters) in a way that respects the underlying gravitational proportionality, while also incorporating the conversion between meter and second time units ($c$). In Planck units, where the unit definitions ($l_P, m_P$) are inherently tied to these fundamental proportionalities (via $G_n, c, \text{Hz}\_\text{kg}$), this conversion factor is implicitly 'baked into' the units themselves, and the constants' numerical values effectively become 1.

*   **Underlying Simplicity:** The relationship between the gravitational radius of an object and its mass, stripped of unit scaling, is an incredibly simple proportionality: the radius (in natural length units) is just twice the mass (in natural mass units). The perceived complexity of the SI formula is an artifact of measuring these quantities using units (meters, kilograms) that are scaled arbitrarily relative to each other and to the natural scales set by $G_n, c,$ and $\text{Hz}\_\text{kg}$.

*   **The Planck Scale as a Natural Basis:** This simplification demonstrates that the Planck unit system ($l_P, m_P$) provides a natural basis for describing these fundamental gravitational relationships. It is the coordinate system where the constants that mediate dimensional conversions in other systems (like SI) take unit value, thus revealing the simplest form of the law. The "Planck scale" is significant not as a boundary to a different reality, but as the scale where the mathematical description of reality becomes simplest due to the alignment of the measurement basis with nature's inherent proportionalities.

In conclusion, the transformation of the Schwarzschild radius formula from a seemingly complex expression involving $G_{SI}$ and $c$ to a simple numerical factor of 2 in Planck units is a powerful illustration that fundamental constants, in their SI values, are primarily unit scaling artifacts that facilitate conversion between our chosen measurement basis and the universe's underlying, simpler dimensional proportionalities. The complexity lies in our measurement system, not in the fundamental physics of spacetime curvature related to mass.