# --- Define Constants GROUPED within the main dictionary ---
grouped_constants = {
    "Core Scaling Constants": {
        "speed_of_light_c": {
            "value": 299792458,
            "units": [("m", 1), ("s", -1)],  # Base unit scaling: meters per second
            "symbol": "c",
            "pronunciation": "See",
            "date": "1676",
            "name": "Ole Rømer",  # Credited for the initial measurement
            "origin": "The speed of light was first inferred from astronomical observations and later defined precisely in terms of the meter and second.",
            "formula": "λ * ν",  # Relates to wavelength (λ) and frequency (ν)
            "comment": "The speed of light is the fastest speed at which information and matter can travel in vacuum.",
            "application": [
                "Special relativity: Defines the limit of speed in spacetime.",
                "Quantum mechanics: Appears in equations for energy and momentum.",
                "Electromagnetism: Directly relates electric and magnetic fields."
            ],
            "reference": "Defined by CODATA 2018",
            "dimensionless_form": "c = 1 in natural units",
            "visualization": "No graphical representation provided here but often visualized as the slope of a light cone in spacetime diagrams."
        },
        "planck_constant_h": {
            "value": 6.62607015e-34,
            "units": [("J", 1), ("s", 1)],
            #"units": [("kg", 1), ("m", 2), ("s", -1)],
            "symbol": "h",
            "formula": "Hz_kg c**2",
            "pronunciation": "Planck constant",
            "date": "1900",
            "name": "Max Planck",
            "origin": "Introduced by Max Planck as part of quantum theory to explain blackbody radiation.",
            "comment": "Essential in quantum mechanics, relating energy and frequency.",
            "reference": "Defined by CODATA 2018."
        },
        "Hz_kg": {
            "value": 7.37249732381e-51,
            "units": [("kg", 1), ("Hz", -1)],
            "symbol": "Hz_kg",
            "formula": "h / c**2",
            "pronunciation": "Hz to kg unit conversion",
            "date": "1900",
            "name": "Max Planck",
            "origin": "Introduced by Max Planck as part of quantum theory to explain blackbody radiation.",
            "comment": "Essential in quantum mechanics, relating energy and frequency.",
            "reference": "Defined by CODATA 2018."
        },
        "boltzmann_constant_k": {
            "value": 1.380649e-23,
            "units": [("kg", 1), ("m", 2), ("s", -2), ("K", -1)],
            "symbol": "k",
            "formula": "K_Hz Hz_kg c**2",
            "pronunciation": "Boltz-mann constant",
            "date": "1871",
            "name": "Ludwig Boltzmann",
            "origin": "Defines the relationship between temperature and energy in statistical mechanics.",
            "comment": "Used to convert temperature into units of energy.",
            "reference": "Defined by CODATA 2018."
        },
        "K_Hz": {
            "value": 2.083661912333e+10,
            "units": [("Hz", 1), ("K", -1)],
            "symbol": "K_Hz",
            "formula": "k / (Hz_kg c**2)",
            "pronunciation": "Boltz-mann constant",
            "date": "1871",
            "name": "Ludwig Boltzmann",
            "origin": "Defines the relationship between temperature and energy in statistical mechanics.",
            "comment": "Used to convert temperature into units of energy.",
            "reference": "Defined by CODATA 2018."
        },
        "molar_gas_constant_R": {
            "value": 8.314462618,
            "units": [("kg", 1), ("m", 2), ("s", -2), ("mol", -1), ("K", -1)],
            "symbol": "R",
            "formula": "Na * K_Hz * Hz_kg * c**2",
            "pronunciation": "Molar gas constant",
            "date": "1873",
            "name": "Dmitri Mendeleev (concept)",
            "origin": "Relates energy per mole to temperature in gas laws.",
            "comment": "Universal constant in thermodynamics and gas laws.",
            "reference": "Defined by CODATA 2018."
        },
        "klitzing_constant_Rk": {
            "value": 25812.80745,
            "units": [("kg", 1), ("m", 2), ("s", -1), ("C", -2)], 
            "symbol": "R_K",
            "formula": "h / e**2",
            "pronunciation": "Klitz-ing constant",
            "date": "1980",
            "name": "Klaus von Klitzing",
            "origin": "Derived from the quantum Hall effect, linking resistance to quantum mechanics.",
            "comment": "Key to metrology and quantum electronics.",
            "reference": "Defined by CODATA 2018."
        },
        "magnetic_flux_quantum_Phi0": {
            "value": 2.067833848e-15,
            "units": [("kg", 1), ("m", 2), ("s", -1), ("C", -1)],
            "symbol": "Φ₀",
            "formula": "h/(2 * e)",
            "pronunciation": "Magnetic flux quantum",
            "date": "1961",
            "name": "Brian Josephson",
            "origin": "Represents the quantization of magnetic flux in superconductors.",
            "comment": "Central to superconductivity and quantum phenomena.",
            "reference": "Defined by CODATA 2018."
        },
        "faraday_constant_F": {
            "value": 96485.33212,
            "units": [("mol", -1), ("C", 1)],
            "symbol": "F",
            "formula": "Na * e",
            "pronunciation": "Far-a-day constant",
            "date": "1834",
            "name": "Michael Faraday",
            "origin": "Defines the total electric charge in one mole of electrons.",
            "comment": "Widely used in electrochemistry and electronics.",
            "reference": "Defined by CODATA 2018."
        },
        "josephson_constant_KJ": {
            "value": 483597.8484e9,
            "units": [("kg", -1), ("m", -2), ("s", 1), ("C", 1)],
            "symbol": "K_J",
            "formula": "2 * e / h",
            "pronunciation": "Jo-seph-son constant",
            "date": "1962",
            "name": "Brian Josephson",
            "origin": "Derived from the Josephson effect, linking voltage to frequency in quantum tunneling.",
            "comment": "Crucial in quantum metrology.",
            "reference": "Defined by CODATA 2018."
        },
        "conductance_quantum_G0": {
            "value": 7.748091729e-5,
            "units": [("kg", -1), ("m", -2), ("s", 1), ("C", 2)],
            "symbol": "G₀",
            "formula": "2 e**2 / h",
            "pronunciation": "Con-duct-ance quantum",
            "date": "1988",
            "name": "Contributed by multiple researchers",
            "origin": "Represents the quantized unit of conductance in nanostructures.",
            "comment": "Key to understanding conductance at quantum scales.",
            "reference": "Defined by CODATA 2018."
        },
        "first radiation constant": { 
            "value": 3.741771852e-16,
            "units": [("kg", 1), ("m", 4), ("s", -3), ("pi", 1)],
            "symbol": "c_1",
            "formula": "2 * pi * h * c**2",
            "pronunciation": "First radiation constant",
            "date": "1900",
            "name": "Max Planck",
            "origin": "Derived as part of Planck's blackbody radiation law, relating energy to temperature and area.",
            "comment": "Key to understanding blackbody radiation.",
            "reference": "Defined by CODATA 2018."
        },
        "first radiation constant sr": { 
            "value": 1.191042972e-16,
            "units": [("kg", 1), ("m", 4), ("s", -3)],
            "symbol": "c_1L",
            "formula": "2 * Hz_kg * c**4",
            "pronunciation": "First radiation constant per steradian",
            "date": "1900",
            "name": "Max Planck",
            "origin": "Adjusted form of the first radiation constant to account for steradian measures in blackbody radiation.",
            "comment": "Extends blackbody radiation analysis into angular measurements.",
            "reference": "Defined by CODATA 2018."
        },
        "second_radiation_constant_c2": {
            "value": 1.4387768776e-02,
            "units": [("m", 1), ("K", 1)],
            "symbol": "c_2",
            "formula": "c / K_Hz",
            "pronunciation": "Second radiation constant",
            "date": "1900",
            "name": "Max Planck",
            "origin": "Appears in Planck's law, relating temperature to the peak wavelength of blackbody radiation.",
            "comment": "Essential for thermodynamic and astrophysical calculations.",
            "reference": "Defined by CODATA 2018."
        }
    },
    "Units of Measure": {
        "1 kg": {
            "value": 1,
            "units": [("kg", 1)],
            "symbol": "1 kg",
            "pronunciation": "One kilogram",
            "date": "1889",
            "name": "International Bureau of Weights and Measures",
            "origin": "The kilogram was originally defined by the mass of the international prototype of the kilogram.",
            "comment": "The standard SI unit of mass.",
            "reference": "Updated definition based on Planck constant in 2019."
        },
        "1 meter": {
            "value": 1,
            "units": [("m", 1)],
            "symbol": "1 m",
            "pronunciation": "One meter",
            "date": "1793",
            "name": "French Academy of Sciences",
            "origin": "Originally defined as one ten-millionth of the distance from the equator to the North Pole along a meridian through Paris.",
            "comment": "The standard SI unit of length.",
            "reference": "Revised definition based on the speed of light in 1983."
        },
        "1 second": {
            "value": 1,
            "units": [("s", 1)],
            "symbol": "1 s",
            "pronunciation": "One second",
            "date": "~2000 BCE",
            "name": "Ancient Babylonians",
            "origin": "Initially developed by the Babylonians as part of a sexagesimal system, dividing the day into 24 hours, each hour into 60 minutes, and each minute into 60 seconds.",
            "comment": "The standard SI unit of time, now defined by atomic clocks based on cesium-133 transitions.",
            "reference": "Modern definition adopted in 1967 by the International System of Units (SI)."
        },
        "1 Hz": {
            "value": 1,
            "units": [("s", -1)],
            "symbol": "Hz",
            "pronunciation": "One Hertz",
            "date": "~2000 BCE",
            "name": "Ancient Babylonians",
            "origin": "The inverse second.",
            "comment": "The standard SI unit of frequency, now defined by atomic clocks based on cesium-133 transitions.",
            "reference": "Modern definition adopted in 1967 by the International System of Units (SI)."
        },
        "Amp force": {
            "value": 1e-7,
            "units": [("kg", 1), ("m", 1), ("s", -2), ("A", -2)],
            "symbol": "A",
            "pronunciation": "amp force",
            "comment": "in natural units where e = squart(alpha), amp_force = α/2π where e=1, amp_force = α/2π",
        },
        "Amp force scaled in alpha": {
            "value": 1e-7,
            "units": [("kg", 1), ("m", 1), ("s", -2), ("A_old", -2)],
            "symbol": "A",
            "pronunciation": "amp force",
            "comment": "in natural units where e = squart(alpha), amp_force = α/2π where e=1, amp_force = α/2π",
        },
        "1 N": {
            "value": 1, 
            "units": [("N", 1)],
            #"units": [("kg", 1), ("m", 1), ("s", -2)],
            "symbol": "N",
            "pronunciation": "One Newton",
        },
        "1 J": {
            "value": 1, 
            "units": [("J", 1)],
            #"units": [("kg", 1), ("m", 2), ("s", -2)],
            "symbol": "J",
            "pronunciation": "One Jewel",
        },
        "elementary_charge_e": {
            "value": 1.602176634e-19,
            "units": [("C", 1)],
            #"units": [("A", 1), ("s", -1)],
            "symbol": "e",
            "pronunciation": "Element-ary charge",
            "date": "1897",
            "name": "J.J. Thomson",
            "origin": "First measured in cathode ray experiments as the charge of an electron.",
            "comment": "natural units it is sqrt (alpha) - Fundamental to electromagnetism and quantum mechanics.",
            "reference": "Defined by CODATA 2018."
        },
        "avogadro_constant_Na": {
            "value": 6.02214076e+23,
            "units": [("mol", -1)],
            "symbol": "Na",
            "pronunciation": "Ah-vo-gah-dro constant",
            "date": "1811",
            "name": "Amedeo Avogadro",
            "origin": "Establishes the number of atoms or molecules in one mole of a substance.",
            "comment": "Links the macroscopic and microscopic worlds in chemistry and physics.",
            "reference": "Defined by CODATA 2018."
        },
    },
    "Masses": {
        "electron_mass_me": {
            "value": 9.1093837015e-31,
            "units": [("kg", 1)],
            "symbol": "me",
            "pronunciation": "Electron mass",
            "date": "1897",
            "name": "J.J. Thomson",
            "origin": "Measured as part of the discovery of the electron during cathode ray experiments.",
            "comment": "Fundamental to atomic and quantum physics.",
            "reference": "Defined by CODATA 2018."
        },
        "pion_charged_mass_pi_pm": {
            "value": 2.4880679e-28,  # CODATA 2022 (from MeV/c^2 for pi+/-)
            "units": [("kg", 1)],
            "symbol": "m_{π^±}",
            "pronunciation": "Charged pion mass",
            "date": "1947",
            "name": "Cecil Powell",
            "origin": "Measured during cosmic ray studies and experiments involving pions.",
            "comment": "Critical to studying meson interactions and weak force.",
            "reference": "CODATA 2022 values."
        },
        "pion_neutral_mass_pi0": {
            "value": 2.4061802e-28,  # CODATA 2022 (from MeV/c^2 for pi0)
            "units": [("kg", 1)],
            "symbol": "m_{π^0}",
            "pronunciation": "Neutral pion mass",
            "date": "1950",
            "name": "Wolfgang Panofsky",
            "origin": "First observed during particle decay experiments.",
            "comment": "Key to understanding meson properties in particle physics.",
            "reference": "CODATA 2022 values."
        },
        "muon_mass_mu": {
            "value": 1.883531627e-28,  # CODATA 2018 (from MeV/c^2)
            "units": [("kg", 1)],
            "symbol": "m_μ",
            "pronunciation": "Muon mass",
            "date": "1936",
            "name": "Carl D. Anderson",
            "origin": "Measured during cosmic ray experiments.",
            "comment": "Important for understanding lepton properties and weak force interactions.",
            "reference": "Defined by CODATA 2018."
        },
        "tau_mass_tau": {
            "value": 3.16747e-27,  # CODATA 2018 (from MeV/c^2, uncertainty larger)
            "units": [("kg", 1)],
            "symbol": "m_τ",
            "pronunciation": "Tau mass",
            "date": "1975",
            "name": "Martin Perl",
            "origin": "Identified in high-energy particle collisions.",
            "comment": "Central to the study of heavier leptons.",
            "reference": "Defined by CODATA 2018."
        },
        "lambda_baryon_mass_Lambda0": {
            "value": 1.988380e-27,  # CODATA 2022 (from MeV/c^2 for Lambda0)
            "units": [("kg", 1)],
            "symbol": "m_{Λ^0}",
            "pronunciation": "Lambda baryon mass",
            "date": "1950",
            "name": "Valentine Telegdi",
            "origin": "Measured during particle scattering experiments.",
            "comment": "Important in studying baryon interactions.",
            "reference": "CODATA 2022 values."
        },
        "proton_mass_mp": {
            "value": 1.67262192369e-27,
            "units": [("kg", 1)],
            "symbol": "mp",
            "pronunciation": "Proton mass",
            "date": "1911",
            "name": "Ernest Rutherford",
            "origin": "Measured during experiments identifying atomic nuclei.",
            "comment": "Fundamental to nuclear and atomic physics.",
            "reference": "Defined by CODATA 2018."
        },
        "neutron_mass_mn": {
            "value": 1.67492749804e-27,
            "units": [("kg", 1)],
            "symbol": "mn",
            "pronunciation": "Neutron mass",
            "date": "1932",
            "name": "James Chadwick",
            "origin": "Measured during experiments identifying the neutron.",
            "comment": "Critical to nuclear physics and particle interactions.",
            "reference": "Defined by CODATA 2018."
        },
        "atomic_mass_unit_u": {
            "value": 1.66053906660e-27,
            "units": [("kg", 1)],
            "symbol": "u",
            "pronunciation": "Atomic mass unit",
            "date": "1961",
            "name": "Defined by IUPAC",
            "origin": "Represents 1/12th the mass of a carbon-12 atom.",
            "comment": "Widely used in chemistry and atomic physics.",
            "reference": "Defined by CODATA 2018."
        },
        "Higgs_boson_mass_H": {
            "value": 2.23204e-25,  # PDG 2023 (from ~125.25 GeV/c^2)
            "units": [("kg", 1)],
            "symbol": "m_H",
            "pronunciation": "Higgs boson mass",
            "date": "2012",
            "name": "CMS and ATLAS collaborations",
            "origin": "Measured during experiments at the Large Hadron Collider (LHC).",
            "comment": "Fundamental to the standard model and field theory.",
            "reference": "Defined by Particle Data Group (PDG) 2023."
        },
        "Z_boson_mass_Z": {
            "value": 1.62557e-25,  # PDG 2023 (from 91.1876 GeV/c^2)
            "units": [("kg", 1)],
            "symbol": "m_Z",
            "pronunciation": "Z boson mass",
            "date": "1983",
            "name": "CERN collaborations",
            "origin": "Measured during experiments at CERN.",
            "comment": "Vital to electroweak unification in the standard model.",
            "reference": "Defined by Particle Data Group (PDG) 2023."
        },
        "W_boson_mass_W": {
            "value": 1.43269e-25,  # PDG 2023 (from 80.377 GeV/c^2)
            "units": [("kg", 1)],
            "symbol": "m_W",
            "pronunciation": "W boson mass",
            "date": "1983",
            "name": "CERN collaborations",
            "origin": "Measured during experiments at CERN.",
            "comment": "Key to studying weak force interactions.",
            "reference": "Defined by Particle Data Group (PDG) 2023."
        },
    },
    "Planck Units": {
        "planck_length_lP": {
            "value": 1.616255e-35,
            "units": [("m", 1)],
            "symbol": "l_P",
            "pronunciation": "Planck length",
            "date": "1899",
            "name": "Max Planck",
            "origin": "Derived from fundamental constants as the smallest possible length scale, where quantum gravity effects become significant.",
            "comment": "Represents the quantum scale in space dimensions.",
            "reference": "Defined by CODATA 2018."
        },
        "planck_time": {
            "value": 5.391247e-44,
            "units": [("s", 1)],
            "symbol": "t_P",
            "pronunciation": "Planck time",
            "date": "1899",
            "name": "Max Planck",
            "origin": "Represents the time it takes for light to travel one Planck length.",
            "comment": "Defines the quantum scale in time.",
            "reference": "Defined by CODATA 2018."
        },
        "planck_mass": {
            "value": 2.176434e-8,
            "units": [("kg", 1)],
            "symbol": "m_P",
            "formula": "sqrt(hc/(G* 2 *pi))",
            "pronunciation": "Planck mass",
            "date": "1899",
            "name": "Max Planck",
            "origin": "Represents the maximum mass before black hole formation due to quantum effects.",
            "comment": "Key in quantum gravity theories.",
            "reference": "Defined by CODATA 2018."
        },
        "planck_temperature": {
            "value": 1.416784e+32,
            "units": [("K", 1)],
            "symbol": "T_P",
            "pronunciation": "Planck temperature",
            "date": "1899",
            "name": "Max Planck",
            "origin": "Represents the highest possible temperature before quantum gravitational effects dominate.",
            "comment": "Associated with the energy of a Planck particle.",
            "reference": "Defined by CODATA 2018."
        }
    },

    "Stoney Units": {
        "stoney_length_lS": {
            "value": 1.38e-33,  # Approximation
            "units": [("m", 1)],
            "symbol": "l_S",
            "pronunciation": "Stoney length",
            "date": "1874",
            "name": "George Johnstone Stoney",
            "origin": "Derived from fundamental constants including the elementary charge and gravitational constant.",
            "comment": "Represents a fundamental length scale in Stoney units.",
            "reference": "Conceptual basis for natural unit systems."
        },
        "stoney_time_tS": {
            "value": 4.60e-43,  # Approximation
            "units": [("s", 1)],
            "symbol": "t_S",
            "pronunciation": "Stoney time",
            "date": "1874",
            "name": "George Johnstone Stoney",
            "origin": "Represents the time it takes for light to travel one Stoney length.",
            "comment": "Defines the quantum scale in Stoney time dimensions.",
            "reference": "Derived from Stoney units."
        },
        "stoney_mass_mS": {
            "value": 1.85e-9,  # Approximation
            "units": [("kg", 1)],
            "symbol": "m_S",
            "pronunciation": "Stoney mass",
            "date": "1874",
            "name": "George Johnstone Stoney",
            "origin": "Represents a fundamental mass unit derived from constants.",
            "comment": "Precursor to Planck mass in natural units.",
            "reference": "Early concept of natural mass units."
        },
        "stoney_temperature_TS": {
            "value": 1.44e+32,  # Approximation
            "units": [("K", 1)],
            "symbol": "T_S",
            "pronunciation": "Stoney temperature",
            "date": "1874",
            "name": "George Johnstone Stoney",
            "origin": "Defines a temperature scale in Stoney units.",
            "comment": "Analogous to Planck temperature.",
            "reference": "Based on Stoney constants."
        }
    },
    "Other Natural Unit Systems": {
        "electronvolts_to_energy_EeV": {
            "value": 1.602176634e-19,
            "units": [("A", 1), ("s", 1)],
            "symbol": "eV",
            "pronunciation": "Electronvolt",
            "date": "1923",
            "name": "Concept formalized by physicists",
            "origin": "Represents the energy of an electron moving through a potential difference of one volt.",
            "comment": "Widely used in atomic and particle physics.",
            "reference": "Standard in physics calculations."
        },
        "natural_length_ln": {
            "value": 2.8179403262e-15,  # Derived from electron radius
            "units": [("m", 1)],
            "symbol": "l_n",
            "pronunciation": "Natural length",
            "date": "1909",
            "name": "Lorentz model",
            "origin": "Represents a characteristic length scale in atomic physics.",
            "comment": "Often associated with electromagnetic interactions.",
            "reference": "Derived in classical electron theory."
        },
        "natural_time_tn": {
            "value": 9.3132257462e-24,  # Derived from natural length and c
            "units": [("s", 1)],
            "symbol": "t_n",
            "pronunciation": "Natural time",
            "date": "Derived concept",
            "name": "Various physicists",
            "origin": "Time associated with natural length and the speed of light.",
            "comment": "Used in theoretical physics for scaled models.",
            "reference": "Aligned with natural unit systems."
        }
    },
    "Electromagnetic & Atomic": {
        "gravitational_G_Newtons": {
            "value": 6.67430e-11,
            "units": [("m", 1), ("kg", 1), ("s", -2)],
            "symbol": "G_newton",
            "pronunciation": "Gravitational constant",
            "date": "1798",
            "name": "Henry Cavendish",
            "origin": "Defines the strength of the gravitational force between masses, first measured using a torsion balance.",
            "comment": "1.06921e-09 * 32.174 = 3.43979e-8   Key to Newtonian gravitation and general relativity.",
            "reference": "Defined by CODATA 2018."
        },
        "gravitational_constant_G": {
            "value": 6.67430e-11,
            "units": [("m", 3), ("kg", -1), ("s", -2)],
            "symbol": "G",
            "pronunciation": "Gravitational constant",
            "date": "1798",
            "name": "Henry Cavendish",
            "origin": "Defines the strength of the gravitational force between masses, first measured using a torsion balance.",
            "comment": "1.06921e-09 * 32.174 = 3.43979e-8   Key to Newtonian gravitation and general relativity.",
            "reference": "Defined by CODATA 2018."
        },
        "coulombs_constant_k_e": {
            "value": 8.987551787e9,
            "units": [("kg", 1), ("m", 3), ("s", -2), ("C", -2)],
            "symbol": "k_e",
            "comment": "in natural units where e = squart(alpha), kₑ_natural = 1/2pi,  kₑ_natural = 1 / (4π * (1/(2α))) = 2α / (4π) = α / (2π)",
            "formula": "c**2 * 1e-7",
            "pronunciation": "Coulomb’s constant",
            "date": "1785",
            "name": "Charles-Augustin de Coulomb",
            "origin": "Quantifies the force between two point charges, fundamental to electrostatics.",
            "reference": "Derived from Coulomb’s law."
        },
        "vacuum_permittivity_epsilon0": {
            "value": 8.8541878128e-12,
            "units": [("C", 2), ("kg", -1), ("m", -3), ("s", 2)],
            "symbol": "ε₀",
            "comment": "where  e = squart(alpha), kₑ_natural = 1/2, where e=1, ε₀_natural = 1 / (2α)",
            "formula": "1e7 / ( c**2 4 * pi)",
            "pronunciation": "Vacuum permittivity",
            "date": "1879",
            "name": "James Clerk Maxwell (concept)",
            "origin": "Defines the capability of the vacuum to permit electric field lines, derived from Maxwell’s equations.",
            "reference": "Standardized in SI units."
        },
        "vacuum_permeability_mu0": {
            "value": 1.25663706212e-6,
            "units": [("kg", 1), ("m", 1), ("s", -2), ("C", -2)],
            "symbol": "μ₀",
            "comment": "where e= squart(alpha), μ₀_natural = 2,  where e=1, μ₀_natural = 2α",
            "formula": "4* pi / '1e7 ",
            "pronunciation": "Vacuum permeability",
            "date": "1820",
            "name": "Hans Christian Ørsted (concept)",
            "origin": "Defines the magnetic permeability of free space, critical to electromagnetism.",
            "reference": "Standardized in SI units."
        },
        "character impedance vacuum": {
            "value": 376.730313412,
            "units": [("kg", 1), ("m", 2), ("s", -1), ("C", -2)],
            "symbol": "Z_0",
            "comment": "where e= squart(alpha), μ₀_natural = 2,  where e=1, μ₀_natural = 2α",
            "formula": "c * 4 * pi / 1e7",
            "pronunciation": "Characteristic impedance of vacuum",
            "date": "Derived from Maxwell’s equations",
            "name": "James Clerk Maxwell (concept)",
            "origin": "Represents the ratio of electric field to magnetic field intensity in electromagnetic waves in a vacuum.",
            "reference": "Derived from electromagnetism principles."
        },
        "atomic unit of permittivity": {
            "value": 1.112650056e-10,
            "units": [("m", -3), ("kg", -1), ("s", -4), ("C", -2)],
            "symbol": "[ε₀]_au",
            "comment": "",
            "formula": "1e7 / c**2",
            "pronunciation": "Atomic unit of permittivity",
            "date": "Derived from quantum mechanics",
            "name": "Based on atomic unit definitions",
            "origin": "Links atomic-scale interactions to permittivity values in natural units.",
            "reference": "Standard in atomic physics."
        },
        "hartree_energy_Eh": {
            "value": 4.359744722071e-18,
            "units": [("kg", 1), ("m", 2), ("s", -2)],
            "symbol": "E_h",
            "formula": "e**4 * 4 * pi**2 * m_e/ (1e7**2 * Hz_kg**2)",
            "pronunciation": "Hartree energy",
            "date": "1928",
            "name": "Douglas Hartree",
            "origin": "Represents the energy unit used in atomic physics, derived from quantum mechanics.",
            "comment": "Essential in quantum chemistry and spectroscopy.",
            "reference": "Standardized in atomic physics."
        },
        "bohr_magneton_muB": {
            "value": 9.2740100783e-24,
            "units": [("m", 2), ("s", -1), ("C", 1)],
            "symbol": "μ_B",
            "formula": "Hz_kg * c**2 * e / (4 * pi  * m_p)",
            "pronunciation": "Bohr magneton",
            "date": "1913",
            "name": "Niels Bohr",
            "origin": "Defines the quantum unit of magnetic moment for an electron in a Bohr orbit.",
            "comment": "Fundamental to quantum magnetism.",
            "reference": "Derived from Bohr model of the atom."
        },
        "nuclear_magneton_muN": {
            "value": 5.0507837461e-27,
            "units": [("m", 2), ("s", -1), ("C", 1)],  # Correct units A m^2 = C/s m^2
            "symbol": "μ_N",
            "formula": "Hz_kg * c**2 * e / (4 * pi * m_e)",
            "pronunciation": "Nuclear magneton",
            "date": "1920",
            "name": "Attributed to Otto Stern",
            "origin": "Defines the quantum unit of magnetic moment for a proton or nucleus.",
            "comment": "Used in nuclear physics and quantum magnetism.",
            "reference": "Standard in quantum nuclear studies."
        }
    },
    "Wavelengths & Diameters": {
        "electron_compton_wavelength": {
            "value": 2.42631023867e-12,
            "units": [("m", 1)],
            "symbol": "λ_e_C",
            "pronunciation": "Electron Compton wavelength",
            "date": "1923",
            "name": "Arthur Compton",
            "origin": "Represents the wavelength associated with an electron when scattering X-rays in the Compton effect.",
            "comment": "Used in quantum mechanics and particle physics.",
            "reference": "Defined through Compton scattering experiments."
        },
        "neutron Compton wavelength": {
            "value": 1.31959090581e-15,
            "units": [("m", 1)],
            "symbol": "λ_n_C",  # No official symbol
            "pronunciation": "Neutron Compton wavelength",
            "date": "1936",
            "name": "James Chadwick (concept)",
            "origin": "Analogous to the electron Compton wavelength, linked to neutron scattering experiments.",
            "comment": "Useful in neutron diffraction studies and quantum mechanics.",
            "reference": "Calculated from neutron properties."
        },
        "Wien wl d law": {
            "value": 2.897771955e-3,
            "units": [("m", 1), ("K", 1)],
            "symbol": "b",
            "pronunciation": "Wien wavelength displacement constant",
            "date": "1893",
            "name": "Wilhelm Wien",
            "origin": "Defines the relationship between the wavelength of maximum blackbody radiation intensity and temperature.",
            "comment": "Central to blackbody radiation and thermodynamics.",
            "reference": "Derived from Wien’s displacement law."
        },
        "rydberg infinite": {
            "value": 10973731.568160,
            "units": [("m", -1)],
            "symbol": "R_inf",
            "formula": "e**4 * 2 * pi**2 * m_e / (Hz_kg**3 * c**3 * 1e7**2 )",
            "pronunciation": "Ryd-berg constant (infinite mass approximation)",
            "date": "1888",
            "name": "Johannes Rydberg",
            "origin": "Represents the limiting value of the Rydberg formula for atoms with infinitely heavy nuclei.",
            "comment": "Key in spectroscopic studies and atomic physics.",
            "reference": "Based on Rydberg’s formula."
        },
        "electron_radius_re": {
            "value": 2.8179403262e-15,
            "units": [("m", 1)],
            "symbol": "r_e",
            "formula": "e**2 / (m_e * 1e7)",
            "pronunciation": "Electron classical radius",
            "date": "1909",
            "name": "Based on Lorentz model",
            "origin": "Calculated using classical electromagnetism to represent the scale of an electron's electromagnetic interaction.",
            "comment": "Does not represent the physical size of an electron but its interaction scale.",
            "reference": "Defined by classical electron theory."
        },
        "bohr_radius_a0": {
            "value": 5.29177210903e-11,
            "units": [("m", 1)],
            "symbol": "a₀",
            "formula": "Hz_kg**2 * c**2 * 1e7 / (e**2 * 4 * pi**2 * m_e )",
            "pronunciation": "Bohr radius",
            "date": "1913",
            "name": "Niels Bohr",
            "origin": "Represents the average distance between the electron and nucleus in a hydrogen atom at ground state.",
            "comment": "Fundamental to atomic physics and quantum mechanics.",
            "reference": "Defined in the Bohr model of the atom."
        },
        "Angstrom star": {
            "value": 1.00001495e-10,
            "units": [("m", 1)],
            "symbol": "Å_star",
            "pronunciation": "Angstrom star unit",
            "date": "1913",
            "name": "Niels Bohr (concept)",
            "origin": "Used in spectroscopy and crystallography as an approximate wavelength unit.",
            "comment": "Primarily applied in atomic and molecular measurements.",
            "reference": "Derived in atomic physics and spectroscopy studies."
        }
    },
    "Thermodynamic & Other": {
        "stefan_boltzmann_constant_sigma": {
            "value": 5.670374419e-8,
            "units": [("kg", 1), ("s", -3), ("K", -4)],
            "symbol": "σ",
            "pronunciation": "Steh-fahn Boltz-mann constant",
            "date": "1879",
            "name": "Josef Stefan and Ludwig Boltzmann",
            "origin": "Derived from blackbody radiation theory, σ represents the power radiated per unit area of\na blackbody as proportional to the fourth power of its temperature.",
            "formula": "2 * pi**5 * K_Hz**4 * Hz_kg / 15",
            "comment": "Used extensively in thermodynamics and astrophysics to quantify radiation energy.",
            "application": [
                "Describing thermal radiation in astrophysical objects, such as stars.",
                "Heat transfer and blackbody radiation studies."
            ],
            "reference": "Defined by CODATA 2018",
            "dimensionless_form": "Not directly dimensionless in standard unit systems.",
            "visualization": "Commonly visualized as the slope in Stefan-Boltzmann law plots, showing power radiated versus temperature."
        },
        "standard_gravity_g0": {
            "value": 9.80665,
            "units": [("m", 1), ("s", -2)],
            "symbol": "g₀",
            "pronunciation": "gee-naught",
            "date": "1901",
            "name": "Standardized via CGPM conference",
            "origin": "Represents the average acceleration due to gravity at Earth's surface, based on Earth's mass and radius.",
            #"formula": None,
            "comment": "Widely used in engineering and physics as the standard reference for gravitational acceleration.",
            "application": [
                "Determining weight and gravitational forces.",
                "Structural analysis and engineering design."
            ],
            "reference": "Defined as 9.80665 m/s² by the CGPM conference.",
            "dimensionless_form": "Not applicable.",
            "visualization": "Commonly represented by downward acceleration vectors in free-fall illustrations."
        },
        "quantum of circulation": {
            "value": 3.6369475467e-4,
            "units": [("m", 2), ("s", -1)],
            "symbol": "κ",
            "formula": "h / ( 2 * m_e)",
            "pronunciation": "Quantum of circulation",
            "date": "1941",
            "name": "Lars Onsager (concept)",
            "origin": "Represents the quantized circulation in superfluid and superconducting systems.",
            "comment": "Used in studying superfluid helium and quantum vortices.",
            "reference": "Defined in quantum fluid dynamics."
        },
        "cosmological_constant_Lambda": {
            "value": 1.0908000000e-52,
            "units": [("m", -2)],
            "symbol": "Λ",
            "pronunciation": "Lam-duh",
            "date": "1917",
            "name": "Albert Einstein",
            "origin": "Introduced by Einstein in his equations of general relativity to balance the expansion of the universe.\nΛ is now associated with dark energy and the accelerating expansion of the universe.",
            #"formula": None,
            "comment": "Central to modern cosmology, explaining the universe's accelerating expansion due to dark energy.",
            "application": [
                "Modeling the effects of dark energy in the expansion of the universe.",
                "Providing solutions in Einstein's field equations in general relativity."
            ],
            "reference": "Modern values derived from Planck satellite data (2018).",
            "dimensionless_form": "Not directly dimensionless.",
            "visualization": "Often modeled as curvature effects in spacetime diagrams or expansion rate plots of the universe."
        }
    },
    "Material Properties": {
        "youngs_modulus_steel": {
            "value": 2.00e11,
            "units": [("kg", 1), ("m", -1), ("s", -2)],  # Base units: kg/(m·s²)
            "symbol": "E",
            "pronunciation": "Young's modulus",
            "date": "1807",
            "name": "Thomas Young",
            "origin": "Defined as stress (force/area) divided by strain (dimensionless).",
            "formula": "E = (F/A) / (ΔL/L)",
            "comment": "Quantifies stiffness. Steel's high value indicates atomic bond strength.",
            "application": [
                "Beam deflection calculations",
                "Spring design",
                "Seismic wave propagation"
            ],
            "reference": "ISO 6892-1",
            "dimensionless_form": "E_n = 1.25e-5 (kgₙ·mₙ⁻¹·sₙ⁻²)",
            "visualization": "Linear slope of stress-strain curve"
        },

        "thermal_conductivity_copper": {
            "value": 401.0,
            "units": [("kg", 1), ("m", 1), ("s", -3), ("K", -1)],  # kg·m/(s³·K)
            "symbol": "k",
            "pronunciation": "Thermal conductivity",
            "date": "1822",
            "name": "Jean-Baptiste Biot",
            "origin": "Relates heat flux to temperature gradient via Fourier's law.",
            "formula": "k = (Q·d)/(A·t·ΔT)",
            "comment": "High value due to free electron contribution.",
            "application": [
                "Heat sink design",
                "Building insulation",
                "Cryogenic systems"
            ],
            "reference": "ASTM D5470",
            "dimensionless_form": "k_n = 9.33e-3 (kgₙ·mₙ·sₙ⁻³·Kₙ⁻¹)",
            "visualization": "Heat flow rate through a unit cross-section"
        },

        "resistivity_silicon": {
            "value": 2.3e3,
            "units": [("kg", 1), ("m", 3), ("s", -3), ("A", -2)],  # kg·m³/(s³·A²)
            "symbol": "ρ",
            "pronunciation": "Rho",
            "date": "1954",
            "name": "Bell Labs",
            "origin": "Derived from Ohm's law and material geometry.",
            "formula": "ρ = R·A/L",
            "comment": "Doping-dependent semiconductor property.",
            "application": [
                "Transistor fabrication",
                "Thermistor design",
                "Radiation detectors"
            ],
            "reference": "SEMI MF84-02",
            "dimensionless_form": "ρ_n = 4.11e-18 (kgₙ·mₙ³·sₙ⁻³·Aₙ⁻²)",
            "visualization": "Resistance vs. doping concentration curve"
        },
        "fracture_toughness_alumina": {
            "value": 3.5,
            #"units": [("kg", 1), ("m", -1), ("s", -2)],
            "units": [("kg", 1), ("m", -0.5), ("s", -2)],
            "symbol": "K_IC",
            "pronunciation": "Kay one see",
            "date": "1961",
            "name": "A.A. Griffith",
            "origin": "Fracture mechanics testing",
            "formula": "K_IC = σ√(πa)",
            "comment": "Critical stress intensity for crack propagation",
            "application": [
                "Ceramic armor",
                "Cutting tools",
                "Biomedical implants"
            ],
            "reference": "ASTM C1421",
            "dimensionless_form": "K_IC_n = 1.42e-35 (kgₙ·mₙ⁻⁰·⁵·sₙ⁻²)",
            "visualization": "Crack growth resistance curve"
        },

        "curie_temperature_iron": {
            "value": 1043,
            "units": [("K", 1)],
            "symbol": "T_C",
            "pronunciation": "Tee see",
            "date": "1895",
            "name": "Pierre Curie",
            "origin": "Magnetic susceptibility measurements",
            "formula": "M(T_C) = 0",
            "comment": "Transition from ferromagnetic to paramagnetic",
            "application": [
                "Transformer cores",
                "Magnetic storage",
                "Temperature sensors"
            ],
            "reference": "IEEE Magnetics Society",
            "dimensionless_form": "T_C_n = 3.61e22 (Kₙ)",
            "visualization": "Magnetization vs. temperature plot"
        },

        "thermal_conductivity_copper": {
            "value": 401,
            "units": [("kg", 1), ("m", 1), ("s", -3), ("K", -1)],
            "symbol": "k",
            "pronunciation": "kay",
            "date": "1822",
            "name": "Jean-Baptiste Joseph Fourier",
            "origin": "Heat transfer experiments",
            "formula": "q = -k∇T",
            "comment": "Highest conductivity among common metals",
            "application": [
                "Heat exchangers",
                "Electrical wiring",
                "Thermal management"
            ],
            "reference": "NIST SRD 100",
            "dimensionless_form": "k_n = 1.63e-25 (kgₙ·mₙ·sₙ⁻³·Kₙ⁻¹)",
            "visualization": "Temperature gradient decay"
        },

        "surface_tension_water": {
            "value": 0.0728,
            "units": [("kg", 1), ("s", -2)],
            "symbol": "γ",
            "pronunciation": "gamma",
            "date": "1805",
            "name": "Thomas Young",
            "origin": "Capillary rise experiments",
            "formula": "γ = F/L",
            "comment": "Decreases with temperature",
            "application": [
                "Microfluidics",
                "Coating technologies",
                "Lung surfactant"
            ],
            "reference": "IUPAC Technical Report",
            "dimensionless_form": "γ_n = 2.96e-36 (kgₙ·sₙ⁻²)",
            "visualization": "Meniscus formation"
        },
            "mobility_silicon": {
                "value": 0.15,
                #"units": [("m", 2), ("s", -1), ("V", -1)],
                "units": [("kg", -1), ("m", 0), ("s", 4), ("A", 1)],  # V⁻¹ → kg⁻¹·m⁻²·s³·A¹
                "symbol": "μ_n",
                "pronunciation": "mu sub n",
                "date": "1954",
                "name": "William Shockley",
                "origin": "Hall effect measurements",
                "formula": "μ = v_d/E",
                "comment": "Electron mobility in intrinsic silicon at 300K",
                "application": [
                    "Semiconductor devices",
                    "Solar cells",
                    "Transistors"
                ],
                "reference": "IEEE Standard 1620",
                "dimensionless_form": "μ_n_n = 5.84e-24 (mₙ²·sₙ⁻¹·Vₙ⁻¹)",
                "visualization": "Drift velocity vs. electric field"
            },

            "compressibility_diamond": {
                "value": 2.0e-12,
                "units": [("kg", -1), ("m", 1), ("s", 2)],
                "symbol": "β",
                "pronunciation": "beta",
                "date": "1915",
                "name": "Percy Bridgman",
                "origin": "High-pressure X-ray diffraction",
                "formula": "β = -(1/V)(∂V/∂P)",
                "comment": "Lowest compressibility of any known material",
                "application": [
                    "Anvil cells",
                    "Ultrasonic transducers",
                    "High-pressure research"
                ],
                "reference": "NIST SRD 74",
                "dimensionless_form": "β_n = 8.12e-81 (kgₙ⁻¹·mₙ·sₙ²)",
                "visualization": "Volume vs. pressure isotherm"
            },

            "reflectivity_aluminum": {
                "value": 0.92,
                "units": [],
                "symbol": "R",
                "pronunciation": "are",
                "date": "1871",
                "name": "James Clerk Maxwell",
                "origin": "Optical interferometry",
                "formula": "R = I_r/I_i",
                "comment": "At 500nm wavelength, normal incidence",
                "application": [
                    "Mirror coatings",
                    "Solar reflectors",
                    "Radiative cooling"
                ],
                "reference": "Handbook of Optics Vol. 4",
                "dimensionless_form": "R_n = 0.92 (dimensionless)",
                "visualization": "Reflectance spectrum"
            },

            "piezoelectric_coefficient_quartz": {
                "value": 2.3e-12,
                #"units": [("m", 1), ("V", -1)],
                "units": [("kg", -1), ("m", -1), ("s", 3), ("A", 1)],
                "symbol": "d_11",
                "pronunciation": "dee one one",
                "date": "1880",
                "name": "Jacques and Pierre Curie",
                "origin": "Direct piezoelectric effect measurements",
                "formula": "d = ∂x/∂E",
                "comment": "Fundamental mode of alpha-quartz",
                "application": [
                    "Oscillators",
                    "Pressure sensors",
                    "Frequency control"
                ],
                "reference": "IEEE Std 176",
                "dimensionless_form": "d_11_n = 8.95e-37 (mₙ·Vₙ⁻¹)",
                "visualization": "Strain vs. applied voltage"
            },

            "thermal_expansion_invar": {
                "value": 1.2e-6,
                "units": [("K", -1)],
                "symbol": "α",
                "pronunciation": "alpha",
                "date": "1896",
                "name": "Charles Édouard Guillaume",
                "origin": "Dilatometry experiments",
                "formula": "α = (1/L)(∂L/∂T)",
                "comment": "Near-zero expansion nickel-iron alloy",
                "application": [
                    "Precision instruments",
                    "Clock pendulums",
                    "Space telescopes"
                ],
                "reference": "ASTM E228",
                "dimensionless_form": "α_n = 4.15e23 (Kₙ⁻¹)",
                "visualization": "Length vs. temperature curve"
            }
    }
}

