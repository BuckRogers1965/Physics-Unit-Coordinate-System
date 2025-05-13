# Escape Velocity: A Universal Dimensionless Ratio Scaled by Light Speed

## Abstract

The standard formula for escape velocity hides a fundamental, dimensionless ratio within its structure. By applying the unit scaling framework and expressing physical quantities in terms of their natural forms encoded within SI constants, we show how the escape velocity is simply this universal dimensionless ratio scaled by the speed of light.

---

## 1. The Standard Formula and the Goal

The familiar formula for escape velocity is given in SI units as:

$$
v_e = \sqrt{\frac{2 \cdot G_{\rm SI} \cdot M_{\rm SI}}{r_{\rm SI}}}
$$

Our goal is to reveal that this formula is equivalent to a dimensionless universal speed ratio ($\beta$) multiplied by the speed of light ($c$).

---

## 2. Express Quantities in Scaled Natural Units

Using the relationships from our unit scaling framework:
-   Mass $\(M_{\rm SI}\)$ in SI (kg) relates to its natural value $\(m_n\)$ (Hz) via our constant $\(Hz_{\rm kg}\)$:
    
$$
M_{\rm SI} = m_n \times Hz_{\rm kg} \quad \Bigl[ \mathrm{kg} \Bigr]
$$

-   Newton's Constant $\(G_{\rm SI}\)$ in SI $(\(\mathrm{m^3 \cdot kg^{-1} \cdot s^{-2}}\))$ relates to its natural value $\(G_n\) (\(\mathrm{s^2}\))$ via \(c\) and $\(Hz_{\rm kg}\)$:

$$
G_{\rm SI} = G_n \times \frac{c^3}{Hz_{\rm kg}} \quad \Bigl[\mathrm{m^3 \cdot kg^{-1} \cdot s^{-2}}\Bigr]
$$

-   Radius $\(r_{\rm SI}\)$ in SI (m) relates to its natural length/time value $\(r_n\)$ (s) via \(c\):

$$
r_{\rm SI} = r_n \times c \quad \Bigl[\mathrm{m}\Bigr]
$$

---

## 3. Substitute and Simplify

Substitute these scaled forms into the standard escape velocity formula:

$$
v_e = \sqrt{\frac{2 \cdot \left(G_n \frac{c^3}{Hz_{\rm kg}}\right) \cdot \left(m_n \cdot Hz_{\rm kg}\right)}{r_n \cdot c}}
$$

Simplify the terms under the square root:

$$
v_e = \sqrt{\frac{2 \cdot G_n \cdot \frac{c^3}{Hz_{\rm kg}} \cdot m_n \cdot Hz_{\rm kg}}{r_n \cdot c}}
$$

Cancel $\(Hz_{\rm kg}\)$ in the numerator and denominator:

$$
v_e = \sqrt{\frac{2 \cdot G_n \cdot c^3 \cdot m_n}{r_n \cdot c}}
$$

Simplify the \(c\) terms $(\(c^3/c = c^2\))$:

$$
v_e = \sqrt{\frac{2 \cdot G_n \cdot c^2 \cdot m_n}{r_n}}
$$


---

## 4. Identify the Dimensionless Ratio and the Scaling Factor

Take $\(c^2\)$ out of the square root:

$$
v_e = \sqrt{\frac{2 \cdot G_n \cdot m_n}{r_n}} \times c
$$

The term $\(\sqrt{\frac{2 \cdot G_n  \cdot m_n}{r_n}}\)$ has units $\(\sqrt{\mathrm{s^2 \cdot Hz / s}} = \sqrt{\mathrm{s^2 \cdot s^{-1} / s}} = \sqrt{\mathrm{1}}\)$, making it **dimensionless**. Let's call this universal dimensionless ratio $\(\beta\):$

$$
\beta = \sqrt{\frac{2 \cdot G_n \cdot m_n}{r_n}}
$$

And then we can extend the scaling of time down to the Planck scale:

$$
\beta = \sqrt{\frac{2 \cdot m_planck}{r_planck}}
$$

This is how the unit scaling in the radius, mass, and G have always interacted to scale the formula to the SI units free planck scale.


The equation then becomes:

$$
v_e = \beta \times c
$$

---

## 5. The Planck scale is in G.

It turns out that $G_n$ is actually a known number in physics already.  $G\_n = t\_P^2$ where $t\_P$ is the non reduced planck time, with h, not $\hbar$.  $\frac{1}{2\pi}$ has nothing to do with unit scaling.  

What this means is that $\beta$ is actually scaling to planck units of measurement on the inside. That is why $\beta$ becomes dimensionless. This is how the constants work, they are scaling to and from  natural units, planck units, and SI units all along. We just were unaware of this because science did not know how the constants were working. They were always considered mysterious. 

---

## 6. Interpretation

-   $\(\beta\)$ is the **universal dimensionless escape velocity**. It represents the escape speed as a fraction of the speed of light. This value is inherent to the physical system (mass and radius) and is independent of any unit system.
-   \(c\) is the **Layer 3 unit scaling factor** for velocity. Its value in a specific unit system (like $\(\approx 3 \times 10^8\)$ m/s in SI) converts the dimensionless ratio \(\beta\) into a velocity value measured in the arbitrary units of that system (m/s).

The standard escape velocity formula in SI works because $\(G_{\rm SI}\), \(M_{\rm SI}\)$, and $\(r_{\rm SI}\)$ carry the necessary scaling factors to implicitly calculate this universal dimensionless ratio $\(\beta\)$, and the \(c\) outside the radical (hidden within the constants in the original form) performs the final conversion to SI velocity units.

## Conclusion

Escape velocity is fundamentally a universal, dimensionless ratio $\(\beta\)$. Our calculation in SI units is simply determining this ratio and then scaling it by the value of the speed of light \(c\) in meters per second to express the result in SI velocity units. This highlights how the standard formula's appearance is shaped by unit scaling, obscuring the underlying simple dimensionless relationship.

## Appendix, deriving Schwarzschild radius formula

Let's just re-state it for clarity and to celebrate that understanding:

1.  **The Dimensionless Ratio:**
    We derived `β = sqrt(2 * G_n * m_n / r_n)`.
    This β appears to be a ratio between 0 and 1 of the velocity c. 
    This implies that there is a limit to escape velocity which would imply a radius for the given mass.

2.  **The Limiting Condition:**
    We established that for escape to be possible from a radius `r_n`, `β` must be less than or equal to 1. The critical point where escape velocity would theoretically need to be `c` is when `β = 1`.

3.  **Setting `β = 1`:**
    If `β = 1`, then `sqrt(2 * G_n * m_n / r_n) = 1`.

4.  **Solving for `r_n` at this Critical Point:**
    Squaring both sides: `2 * G_n * m_n / r_n = 1^2 = 1`.
    Multiplying both sides by `r_n`: `2 * G_n * m_n = r_n`.
    So, indeed, **`r_n = 2 * G_n * m_n`**.

5.  **Interpretation of `r_n = 2 G_n m_n`:**
    *   `r_n`: This is the critical radius expressed in our "naturalized time units" (since `r_n = r_SI / c_SI`).
    *   `G_n`: This is our "naturalized gravitational strength" (`t_P_h_SI^2`, with units of `s_SI^2`).
    *   `m_n`: This is the mass expressed in its "naturalized frequency units" (`M_SI / Hz_kg_SI`, with units `Hz_SI` or `s_SI⁻¹`).
    *   This equation `r_n = 2 G_n m_n` is the **Schwarzschild radius formula, but expressed entirely in our PUCS naturalized quantities.**

6.  **Converting Back to SI to Confirm:**
    Let's substitute the SI equivalents back in:
    *   `r_SI / c_SI = 2 * (G_SI * Hz_kg_SI / c_SI^3) * (M_SI / Hz_kg_SI)`
    *   The `Hz_kg_SI` terms cancel out.
    *   `r_SI / c_SI = 2 * G_SI * M_SI / c_SI^3`
    *   Multiply by `c_SI`: `r_SI = 2 * G_SI * M_SI / c_SI^2`

    This is exactly the standard formula for the Schwarzschild radius (`r_s`).

What this means is that `β = 1` is the speed of light independent of any unit system.