# Planck's Constant (h) Does Not Set the Kilogram Scale In Isolation

## Abstract

A common misconception arises from the role of Planck's constant `h` in defining physical scales, particularly in the context of recent SI redefinitions. While `h` is used to define the kilogram in modern SI, this does not mean `h` *intrinsically* sets the kilogram's scale independent of other units. Based on the unit scaling framework, which views unit systems as arbitrary coordinate bases, we demonstrate that there are infinitely many unit systems where Planck's constant has the *same numerical value* as in SI, but where the base units of mass (kilogram), length (meter), and time (second) have entirely different physical sizes. This proves that `h` alone does not dictate the scale of mass or any other single base unit, but rather quantifies a specific relationship between multiple dimensions within a given system.

---

## 1. The Framework: Unit Systems as Coordinate Bases

Our understanding is grounded in the principle that a system of units (like SI) is a human-defined coordinate system for quantifying physical dimensions ([M], [L], [T], etc.). Each base unit (kg, m, s) sets the arbitrary scale along one axis of this dimensional space. Dimensionful physical constants are the scaling factors needed to translate between these arbitrary unit scales according to the universe's inherent proportionalities. There exist infinitely many valid coordinate bases (unit systems) that can describe the same physical reality.

---

## 2. Planck's Constant (h) as a Scaling Factor

Planck's constant `h` has dimensions of [Mass] x [Length]² / [Time] ([M L² T⁻¹]). It quantifies the proportionality between Energy and Frequency. Within any given unit system with base units of mass, length, and time, the numerical value of `h` is the number that results from measuring this proportionality using the scales of those specific base units.

Let's denote the physical sizes of the base units in a given system as $[kg]$, $[m]$, and $[s]$. The numerical value of `h` in this system is:

$$ h\_{\text{numerical}} = \frac{[\text{Physical Action Quantity}]}{[kg] [m]^2 [s]^{-1}} $$

Where `[Physical Action Quantity]` represents the constant, unit-independent physical 'amount' of action quantified by `h`. This is fixed by nature.

Let $h\_\text{SI}$ numerical be the numerical value of `h` in the SI system ($\approx 6.626 \times 10^{-34}$). This value is fixed by definition in modern SI, which effectively defines the SI kilogram relative to the SI meter and SI second using this constant value.

---

## 3. Demonstrating Infinite Systems with the Same h, Different Scales

We want to show that there are infinitely many sets of physical sizes for base units $([kg\_A], [m\_A], [s\_A])$ such that the numerical value of `h` in this new system ($h\_A$) is equal to $h\_\text{SI}$ numerical, even though $[kg\_A], [m\_A], [s\_A]$ are physically different from $[kg\_{\text{SI}}], [m\_{\text{SI}}], [s\_{\text{SI}}]$.

From the definition of the numerical value of `h`:

$$ h_* = \frac{[\text{Physical Action Quantity}]}{[kg\_A] [m\_A]^2 [s\_A]^{-1}} $$

We require $h\_A = h\_\text{SI}$ numerical. Therefore:

$$ \frac{[\text{Physical Action Quantity}]}{[kg\_A] [m\_A]^2 [s\_A]^{-1}} = h\_\text{SI} numerical $$

Rearranging the physical sizes:

$$ [kg\_A] [m\_A]^2 [s\_A]^{-1} = \frac{[\text{Physical Action Quantity}]}{h\_\text{SI} numerical} $$

The right side of this equation is a fixed physical quantity – the physical size corresponding to one unit of action in the system where `h` has the numerical value $h\_\text{SI}$ numerical}. Let's call this fixed physical size $A_0$:

$$ A\_0 = \frac{[\text{Physical Action Quantity}]}{h\_\text{SI} numerical} $$

So, we need to find physical sizes $[kg\_A], [m\_A], [s\_A]$ such that:

$$ [kg\_A] [m\_A]^2 [s\_A]^{-1} = A\_0 $$

Or, equivalently:

$$ [kg\_A] [m\_A]^2 = A_0 \cdot [s\_A] $$

This is a single equation relating the physical sizes of the three base units in the new system. We have three variables $([kg\_A], [m\_A], [s\_A])$ and only one constraint equation.

**How to find infinite solutions:**

1.  Choose a physical size for the new second, $[s\_A]$, that is different from $[s\_{\text{SI}}]$.
2.  Choose a physical size for the new meter, $[m\_A]$, that is different from $[m\_{\text{SI}}]$.
3.  The physical size of the new kilogram, $[kg_*]$, is then uniquely determined by the equation:
    $$ [kg\_A] = \frac{A\_0 \cdot [s\_A]}{[m\_A]^2} $$

As long as we choose $[s\_A]$ and $[m\_A]$ differently from their SI values, and in such a way that the resulting $[kg\_A]$ is also different from $[kg\_{\text{SI}}]$ (which is almost always the case unless we accidentally pick the exact SI scaling), we have found a new unit system where the numerical value of `h` is the same, but all three base unit scales are different.

Since we can choose $[s\_A]$ and $[m\_A]$ from a continuous range of values (any positive physical duration for $[s\_A]$, any positive physical length for $[m\_A]$), there are infinitely many such combinations.

**Example:**

Imagine $A_0 = 1$ SI kg⋅m²/s.
We need $[kg\_A][m\_A]^2/[s\_A] = 1$ SI kg⋅m²/s.

*   **SI System:** $[kg]=1$ kg, $[m]=1$ m, $[s]=1$ s. $1 \cdot 1^2 / 1 = 1$. (Numerical $h$ depends on how many $A\_0$ units are in physical h).
*   **New System 1:** Let $s\_A = 2$ s, $m\_A = 0.5$ m. Then $kg\_A(0.5)^2/(2) = A\_0$. $kg_A(0.25)/2 = A\_0$. $kg\_A = 8 \cdot A\_0$. The new kilogram is 8 times heavier than the size corresponding to $A_0$. If $A\_0$ corresponds to $1/h\_{SI}$ of the physical action quantity, then $kg\_A = 8 / h_{SI} \times \text{Phys Action}$. This new system has a meter that's half the SI meter, a second that's double the SI second, and a kilogram that's 8 times some reference mass scale derived from $h$. In this system, the numerical value of $h$ is still $h\_{SI}$, but the base units are different.
*   **New System 2:** Let $s\_B = 0.1$ s, $m\_B = 10$ m. Then $kg\_B(10)^2/(0.1) = B\_0$. $kg\_B(100)/(0.1) = B\_0$. $[kg\_B] = 0.001 \cdot B\_0$. The new kilogram is 1/1000th the size corresponding to $B\_0$. This system has a meter 10x the SI meter, a second 1/10th the SI second, and a much smaller kilogram. In this system, the numerical value of $h$ is still $h\_{SI}$.

In both System 1 and System 2, the numerical value of $h$ is the same, but the physical sizes of the kilogram, meter, and second are drastically different from each other and from the SI units. Since we can pick $s\_A$ and $m\_A$ arbitrarily (within physical limits), there's an infinite continuum of such systems.

---

## 4. Conclusion

The argument demonstrates that Planck's constant `h`, despite its use in the modern SI definition of the kilogram, does not uniquely dictate the physical scale of the kilogram or any single base unit. The numerical value of `h` in a unit system quantifies a fixed proportionality between specific combinations of mass, length, and time scales $([kg] [m]^2 [s]^{-1})$. Because there are three base units involved and only one constraint equation from `h`, there remains an infinite freedom to choose the scales of two units and have the third determined, or choose scales for all three as long as they satisfy the relationship. This proves conclusively that `h` alone does not set the scale of the kilogram; rather, its value is a consequence of the chosen scales of mass, length, and time within a specific unit system. This reinforces the view of unit systems as flexible coordinate bases, not fundamentally rigid structures imposed by individual constants.