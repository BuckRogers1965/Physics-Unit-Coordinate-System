# Demystifying the Rydberg Constant via Unit Scaling

## Overview  
In this paper, we explore the Rydberg constant \( R_\infty \) and demonstrate that its complex form in SI units arises from the way we define fundamental constants like the speed of light, Planck's constant, and the elementary charge. By examining the relationships between these constants, we show that the Rydberg constant simplifies to a natural form, ultimately revealing a deep connection between the fine-structure constant, electron mass, and a simple geometric scaling factor. Through this approach, we uncover how **unit scaling** and **dimensional analysis** offer a cleaner, more intuitive understanding of this fundamental quantity.


---

## Step 1. Starting Point: The SI Expression
The Rydberg constant in SI is traditionally written as:

\[
R_\infty = \frac{e^4 \cdot 2 \pi^2 \cdot m_e \cdot (10^{-7})^2}{(\text{Hz\_kg})^3 \cdot c^3}
\]

Where:
- \( e \) is the elementary charge
- \( m_e \) is the electron mass
- \( c \) is the speed of light
- \( h = \text{Hz\_kg} \cdot c^2 \)
- \( 10^{-7} \) comes from \( \mu_0 / 4\pi = 10^{-7} \ \text{N/A}^2 \), the Ampère force constant


---

## Step 2. Replace \( \varepsilon_0 \) using the identity:

\[ \varepsilon_0 = \frac{1}{\mu_0 c^2} \Rightarrow \varepsilon_0^2 = \frac{1}{\mu_0^2 c^4} \]

So we substitute:

\[
R_\infty = \frac{m_e e^4 \mu_0^2 c^4}{8 h^3 c} = \frac{m_e e^4 \mu_0^2 c^3}{8 h^3}
\]

---

## Step 3. Replace \( \mu_0 \) using the Ampère force constant:

\[ \frac{\mu_0}{4\pi} = 10^{-7} \Rightarrow \mu_0 = 4\pi \times 10^{-7} \]

So:

\[
\mu_0^2 = (4\pi)^2 \cdot 10^{-14} = 16\pi^2 \cdot 10^{-14}
\]

Substitute into the expression:

\[
R_\infty = \frac{m_e e^4 \cdot 16\pi^2 \cdot 10^{-14} \cdot c^3}{8 h^3} = \frac{2\pi^2 m_e e^4 c^3}{h^3} \cdot 10^{-14}
\]

---

## Step 4. Now express \( h \) as \( h = \text{Hz}_{kg} \cdot c^2 \):

Then \( h^3 = \text{Hz}_{kg}^3 \cdot c^6 \)

So:

\[
R_\infty = \frac{2 \pi^2 m_e e^4 c^3}{\text{Hz}_{kg}^3 c^6} \cdot 10^{-14} = \frac{2 \pi^2 m_e e^4}{\text{Hz}_{kg}^3 c^3} \cdot 10^{-14}
\]

---

## 5. Insert \( \text{amp\_force} = \mu_0 / 4\pi = 10^{-7} \)

We begin by recognizing that the Ampère force constant can be expressed as:

\[
\text{amp\_force} = \frac{\mu_0}{4\pi} = 10^{-7}
\]

Substituting this into the expression for \( R_\infty \):

\[
R_\infty = \frac{2 \pi^2 m_e (e^2 \cdot \text{amp\_force})^2}{\text{Hz}_{kg}^3 c^3}
\]

This simplifies to:

\[
R_\infty = 2 \pi^2 m_e \cdot \frac{(e^2 \cdot 10^{-7})^2}{\text{Hz}_{kg}^3 c^3}
\]

Thus, we obtain the intermediate form:

\[
R_\infty = \frac{2 \pi^2 m_e e^4}{\text{Hz}_{kg}^3 c^3} \cdot 10^{-14}
\]

---

## Step 6: Recognize \( \alpha \)'s Relation to Ampère Force

Next, we recognize the connection between the fine-structure constant \( \alpha \) and the Ampère force constant. From previous derivations, we have:

\[
\alpha = 2\pi \cdot \text{amp\_force}_\text{natural} = 2\pi \cdot 0.0011614097323
\]

Thus, we can express \( 10^{-7} \) as:

\[
10^{-7} = \frac{\alpha}{2\pi}
\]

Squaring both sides:

\[
(10^{-7})^2 = \left(\frac{\alpha}{2\pi}\right)^2 = \frac{\alpha^2}{4\pi^2}
\]

This allows us to rewrite the expression for \( R_\infty \) in terms of \( \alpha^2 \).

---

## Step 7: Plug In \( \alpha \) into \( R_\infty \)
Now substitute this into the simplified \( R_\infty \):

\[
R_\infty = 2 \pi^2 \cdot \left(\frac{\alpha^2}{4\pi^2}\right) \cdot m_e
\]

The \( \pi^2 \) terms cancel:

\[
R_\infty = \frac{\alpha^2}{2} \cdot m_e
\]

---

## Final Form in Natural Units
Thus, in natural units where \( h = c = e = 1 \):

\[
R_\infty = \frac{\alpha^2}{2} \cdot m_e
\]

This final equation highlights a deep geometric truth:
> The Rydberg constant is not mysterious; it emerges as the product of a **pure dimensionless interaction strength squared** and the **mass of the electron**, scaled by a simple geometric factor.


## Simplified Formula for the Rydberg Constant

We begin with the simplified expression for the Rydberg constant \( R_\infty \) in natural units, based on the fine-structure constant \( \alpha \), the electron mass \( m_e \), and the scaling factor \( kg_{Hz} \):

\[
R_\infty = \frac{\alpha^2}{2} \cdot m_e \cdot \frac{kg_{Hz}}{c}
\]

### Unit Analysis

To ensure that the simplified formula is dimensionally consistent, we perform a unit analysis:

1. **\( \alpha^2 \)** is dimensionless.
2. **\( m_e \)** has units of mass, or \( \text{kg} \).
3. **\( kg_{Hz} \)** has units of \( \frac{\text{Hz}}{\text{kg}} \), which can be expressed as \( \frac{1}{\text{kg} \cdot \text{s}} \) (since \( \text{Hz} = \text{s}^{-1} \)).
4. **\( c \)**, the speed of light, has units of \( \text{m} \cdot \text{s}^{-1} \).

Thus, the units of the simplified expression for \( R_\infty \) are:

\[
\text{Units of } R_\infty = \left(\frac{\text{dimensionless}}{2}\right) \cdot \text{kg} \cdot \frac{1}{\text{kg} \cdot \text{s}} \cdot \frac{1}{\text{m} \cdot \text{s}^{-1}}
\]

Upon simplifying:

- The **\( \text{kg} \)** terms cancel out.
- The **\( \text{s} \)** terms from \( kg_{Hz} \) and \( c \) cancel out.
- We are left with the units of:

\[
\frac{1}{\text{m}}
\]

This is the correct unit for the Rydberg constant, \( R_\infty \), which is typically given in units of inverse meters (\( \text{m}^{-1} \)).

### Conclusion

The simplified formula for the Rydberg constant:

\[
R_\infty = \frac{\alpha^2}{2} \cdot m_e \cdot \frac{kg_{Hz}}{c}
\]

is dimensionally consistent and produces the correct units of \( \text{m}^{-1} \), confirming its validity as a simplified expression for the Rydberg constant.

---

## Conclusion
This derivation resolves the apparent complexity of \( R_\infty \) by showing that all the nested constants simply represent scaling artifacts of the SI unit system. When we transition to a natural unit system, the Rydberg constant becomes an elegantly simple expression of atomic geometry:

\[
R_\infty \sim \alpha^2 \cdot m_e
\]

The remaining mystery is not \( R_\infty \), but **why** \( \alpha \) and \( m_e \) take the specific values they do.

---


