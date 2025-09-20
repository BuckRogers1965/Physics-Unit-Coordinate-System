composite_units = [
    # handle the Hz append as just composite scaling
    # this reduces code that was in every module
    { #"Hertz":
        "symbol": "Hz",
        "units": [("s", -1)],
    },
    { #"UnitA":
        "symbol": "Atest",
        "units": [("Btest", 1), ("kg", 1)]  # UnitA depends on UnitB and kg
    },
    # Mechanics
    { #"Momentum":
        "symbol": "p",
        "units": [("kg", 1), ("m", 1), ("s", -1)],
    },
    { #"Newton":
        "symbol": "N",
        "units": [("kg", 1), ("m", 1), ("s", -2)],
    },
    { #"Joule":
        "symbol": "J",
        "units": [("kg", 1), ("m", 2), ("s", -2)],
    },
    { #"Watt":
        "symbol": "W",
        "units": [("kg", 1), ("m", 2), ("s", -3)],
    },
    { #"Pascal":
        "symbol": "Pa",
        "units": [("kg", 1), ("m", -1), ("s", -2)],
    },
    { #"UnitB":
        "symbol": "Btest",
        "units": [("Atest", 1), ("s", 1)]   # UnitB depends on UnitA and s
    },
    { #"Hertz":
        "symbol": "Hz",
        "units": [("s", -1)],
    },
    { #"Coulomb":
        "symbol": "C",
        "units": [("A", 1), ("s", 1)],
    },
    { #"Volt":
        "symbol": "V",
        "units": [("kg", 1), ("m", 2), ("s", -3), ("A", -1)],
    },
    { #"Ohm":
        "symbol": "Ω",
        "units": [("kg", 1), ("m", 2), ("s", -3), ("A", -2)],
    },
    { #"Siemens":
        "symbol": "S",
        "units": [("kg", -1), ("m", -2), ("s", 3), ("A", 2)],
    },
    { #"Farad":
        "symbol": "F",
        "units": [("kg", -1), ("m", -2), ("s", 4), ("A", 2)],
    },
    { #"Henry":
        "symbol": "H",
        "units": [("kg", 1), ("m", 2), ("s", -2), ("A", -2)],
    },
    { #"Weber":
        "symbol": "Wb",
        "units": [("kg", 1), ("m", 2), ("s", -2), ("A", -1)],
    },
    { #"Tesla":
        "symbol": "T",
        "units": [("kg", 1), ("s", -2), ("A", -1)], # Derived from Wb/m^2 = (kg m^2 s^-2 A^-1) / m^2
    },
    # Radiation and Nuclear
    { # Radioactivity, decay events per unit time "Becquerel":
        "symbol": "Bq",
        "units": [("s", -1)], # Same units as Hz
    },
    { # Absorbed Dose "Gray":
        "symbol": "Gy",
        "units": [("m", 2), ("s", -2)], # J/kg
    },
    { # Dose Equivalent - Same units as Gray, different interpretation "Sievert":
        "symbol": "Sv",
        "units": [("m", 2), ("s", -2)], # J/kg
    },
    { # Catalytic Activity "Katal":
        "symbol": "kat",
        "units": [("mol", 1), ("s", -1)],
    },
]
