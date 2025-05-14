Deriving Gravitational Redshift (z) in the PUCS Framework and Planck Ratios
--------------------------------------------------------------------------

The standard approximate formula for gravitational redshift (weak field) is:

$$
z = (G_{SI} * M_{SI}) / (r_{SI} * c_{SI}^2)
$$

Let's convert the SI quantities to their PUCS naturalized forms:

1.  **Substitute PUCS naturalized quantities:**
    *   $G_{SI} = t_P^2 * c_{SI}^3 / Hz_{kg}$  (where $t_P$ is non reduced Planck Time)
    *   $M_{SI} = M_n * Hz_{kg}$          (where $M_n$ is naturalized mass in Hz)
    *   $r_{SI} = r_n * c_{SI}$            (where $r_n$ is naturalized radius in seconds)
    *   $c_{SI}$ is speed of light in SI

Plugging these into the formula for z:

$$
z = [(t_P^2 * c_{SI}^3 / Hz_{kg}) * (M_n * Hz_{kg})] / [(r_n * c_{SI}) * c_{SI}^2]
$$

2.  **Simplify the expression by cancelling terms:**
    *   $Hz_{kg}$ in the numerator cancels with $Hz_{kg}$.
    *   $c_{SI}^3$ in the numerator (from $G_{SI}$'s conversion) cancels with $c_{SI} * c_{SI}^2 = c_{SI}^3$ in the denominator.

$$
z = (t_P^2 * M_n) / r_n
$$

3.  **Convert to dimensionless Planck ratios:**
    *   Define $M_{planck} = M_n * t_P$
        (This is $(M_{SI} / Hz_{kg}) * t_P = M_{SI} / (Hz_{kg} / t_P) = M_{SI} / m_P$)
    *   Define $r_{planck} = r_n / t_P$
        (This is $(r_{SI} / c_{SI}) / t_P = r_{SI} / (c_{SI} * t_P) = r_{SI} / l_P$)

Now, let's manipulate the equation $z = (t_P^2 * M_n) / r_n$ to introduce these ratios:

$$
z = (t_P * (M_n * t_P)) / r_n
$$

(Multiply numerator by $t_P$ and one $t_P$ from $t_P^2$ into $M_n$)

$$
z = M_{planck} / r_{planck}
$$

--------------------------------------------------------------------------
This derivation shows that the approximate gravitational redshift $z$ is directly given by the ratio of the gravitating mass (expressed in Planck mass units) to the emission radius (expressed in Planck length units). The SI constants $G_{SI}$ and $c_{SI}$ are absorbed during the conversion to these naturalized and then Planck-scaled quantities, revealing a very simple underlying dimensionless relationship.  This is always what that combination of constants were doing, was unit scaling the formula to dimensionless planck unit of measurement scale.



**Considering the Strong Field Case (Schwarzschild Metric):**

The exact formula for gravitational redshift from a non-rotating, uncharged spherical mass (Schwarzschild metric) for an emitter at radius `r` and observer at infinity is:

$1 + z = 1 / sqrt(1 - 2GM/(rc^2))$
$1 + z = 1 / sqrt(1 - v_e^2/c^2)$
$1 + z = 1 / sqrt(1 - β²)$

Now substitute $β² = 2 \cdot m_{planck} / r_{planck}$:

$$
1 + z = 1 / sqrt(1 - 2 \cdot  m_{planck} / r_{planck})
$$