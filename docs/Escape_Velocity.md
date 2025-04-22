# Escape Velocity: A Universal Dimensionless Ratio Scaled by Light Speed

## Abstract

The standard formula for escape velocity hides a fundamental, dimensionless ratio within its structure. By applying the unit scaling framework and expressing physical quantities in terms of their natural forms encoded within SI constants, we show how the escape velocity is simply this universal dimensionless ratio scaled by the speed of light.

---

## 1. The Standard Formula and the Goal

The familiar formula for escape velocity is given in SI units as:
\[
v_e = \sqrt{\frac{2\,G_{\rm SI}\,M_{\rm SI}}{r_{\rm SI}}}
\]
Our goal is to reveal that this formula is equivalent to a dimensionless universal speed ratio ($\beta$) multiplied by the speed of light ($c$).

---

## 2. Express Quantities in Scaled Natural Units

Using the relationships from our unit scaling framework:
-   Mass \(M_{\rm SI}\) in SI (kg) relates to its natural value \(m_n\) (Hz) via our constant \(Hz_{\rm kg}\):
    \[
    M_{\rm SI} = m_n \;\times\; Hz_{\rm kg} \quad \Bigl[ \mathrm{kg} \Bigr]
    \]
-   Newton's Constant \(G_{\rm SI}\) in SI (\(\mathrm{m^3\,kg^{-1}\,s^{-2}}\)) relates to its natural value \(G_n\) (\(\mathrm{s^2}\)) via \(c\) and \(Hz_{\rm kg}\):
    \[
    G_{\rm SI} = G_n \;\times\; \frac{c^3}{Hz_{\rm kg}} \quad \Bigl[\mathrm{m^3\,kg^{-1}\,s^{-2}}\Bigr]
    \]
-   Radius \(r_{\rm SI}\) in SI (m) relates to its natural length/time value \(r_n\) (s) via \(c\):
    \[
    r_{\rm SI} = r_n \;\times\; c \quad \Bigl[\mathrm{m}\Bigr]
    \]

---

## 3. Substitute and Simplify

Substitute these scaled forms into the standard escape velocity formula:
\[
v_e = \sqrt{\frac{2\,\left(G_n \frac{c^3}{Hz_{\rm kg}}\right)\,\left(m_n\,Hz_{\rm kg}\right)}{r_n\,c}}
\]
Simplify the terms under the square root:
\[
v_e = \sqrt{\frac{2 \cdot G_n \cdot \frac{c^3}{Hz_{\rm kg}} \cdot m_n \cdot Hz_{\rm kg}}{r_n \cdot c}}
\]
Cancel \(Hz_{\rm kg}\) in the numerator and denominator:
\[
v_e = \sqrt{\frac{2 \cdot G_n \cdot c^3 \cdot m_n}{r_n \cdot c}}
\]
Simplify the \(c\) terms (\(c^3/c = c^2\)):
\[
v_e = \sqrt{\frac{2 \cdot G_n \cdot c^2 \cdot m_n}{r_n}}
\]

---

## 4. Identify the Dimensionless Ratio and the Scaling Factor

Take \(c^2\) out of the square root:
\[
v_e = \sqrt{\frac{2 \cdot G_n \cdot m_n}{r_n}} \;\times\; c
\]
The term \(\sqrt{\frac{2\,G_n\,m_n}{r_n}}\) has units \(\sqrt{\mathrm{s^2 \cdot Hz / s}} = \sqrt{\mathrm{s^2 \cdot s^{-1} / s}} = \sqrt{\mathrm{1}}\), making it **dimensionless**. Let's call this universal dimensionless ratio \(\beta\):
\[
\beta = \sqrt{\frac{2\,G_n\,m_n}{r_n}}
\]
The equation then becomes:
\[
v_e = \beta \;\times\; c
\]

---

## 5. Interpretation

-   \(\beta\) is the **universal dimensionless escape velocity**. It represents the escape speed as a fraction of the speed of light. This value is inherent to the physical system (mass and radius) and is independent of any unit system.
-   \(c\) is the **Layer 3 unit scaling factor** for velocity. Its value in a specific unit system (like \(\approx 3 \times 10^8\) m/s in SI) converts the dimensionless ratio \(\beta\) into a velocity value measured in the arbitrary units of that system (m/s).

The standard escape velocity formula in SI works because \(G_{\rm SI}\), \(M_{\rm SI}\), and \(r_{\rm SI}\) carry the necessary scaling factors to implicitly calculate this universal dimensionless ratio \(\beta\), and the \(c\) outside the radical (hidden within the constants in the original form) performs the final conversion to SI velocity units.

## Conclusion

Escape velocity is fundamentally a universal, dimensionless ratio \(\beta\). Our calculation in SI units is simply determining this ratio and then scaling it by the value of the speed of light \(c\) in meters per second to express the result in SI velocity units. This highlights how the standard formula's appearance is shaped by unit scaling, obscuring the underlying simple dimensionless relationship.