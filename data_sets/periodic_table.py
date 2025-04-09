periodic_table = {
    1: {
        "name": "Hydrogen",
        "symbol": "H",
        "group": 1,
        "period": 1,
        "atomic_number": 1,
        "discovery": {
            "discoverer": "Henry Cavendish",
            "year": 1766,
            "notes": "Isolated as 'inflammable air'; named by Lavoisier in 1783."
        },
        "physical_properties": {
            "atomic_mass": {"value": 1.008, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 0.08988, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 13.83, "units": [('K', 1)], "notes": "Under pressure."},
            "boiling_point": {"value": 20.271, "units": [('K', 1)], "notes": "At 1 atm."},
        },
        "electron_configuration": "1s¹",
        "common_uses": ["Rocket fuel", "Ammonia production", "Fuel cells"],
    },
    2: {
        "name": "Helium",
        "symbol": "He",
        "group": 18,
        "period": 1,
        "atomic_number": 2,
        "discovery": {
            "discoverer": "Janssen and Lockyer",
            "year": 1868,
            "notes": "Identified via spectral lines in sunlight."
        },
        "physical_properties": {
            "atomic_mass": {"value": 4.002602, "units": [('amu', 1)], "notes": "Stable isotope He-4."},
            "density": {"value": 0.1786, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": None, "units": [('K', 1)], "notes": "Does not solidify under normal pressure."},
            "boiling_point": {"value": 4.222, "units": [('K', 1)], "notes": "Lowest boiling point of any element."},
        },
        "electron_configuration": "1s²",
        "common_uses": ["Cryogenics", "Welding", "Inflating balloons"],
    },
    3: {
        "name": "Lithium",
        "symbol": "Li",
        "group": 1,
        "period": 2,
        "atomic_number": 3,
        "discovery": {
            "discoverer": "Johan August Arfvedson",
            "year": 1817,
            "notes": "Found in petalite, a mineral."
        },
        "physical_properties": {
            "atomic_mass": {"value": 6.94, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 0.534, "units": [('kg', 1), ('m', -3)], "notes": "Lowest density of all metals."},
            "melting_point": {"value": 453.69, "units": [('K', 1)], "notes": "Metallic state."},
            "boiling_point": {"value": 1603, "units": [('K', 1)], "notes": "Metallic state."},
        },
        "electron_configuration": "[He] 2s¹",
        "common_uses": ["Rechargeable batteries", "Medication", "Ceramics"],
    },
    4: {
        "name": "Beryllium",
        "symbol": "Be",
        "group": 2,
        "period": 2,
        "atomic_number": 4,
        "discovery": {
            "discoverer": "Louis-Nicolas Vauquelin",
            "year": 1798,
            "notes": "Found in beryl and emeralds."
        },
        "physical_properties": {
            "atomic_mass": {"value": 9.0122, "units": [('amu', 1)], "notes": "Stable isotope Be-9."},
            "density": {"value": 1.85, "units": [('kg', 1), ('m', -3)], "notes": "Lightweight metal."},
            "melting_point": {"value": 1560, "units": [('K', 1)], "notes": "High melting point."},
            "boiling_point": {"value": 2742, "units": [('K', 1)], "notes": "High boiling point."},
        },
        "electron_configuration": "[He] 2s²",
        "common_uses": ["Aerospace applications", "X-ray windows", "Alloys"],
    },
    5: {
        "name": "Boron",
        "symbol": "B",
        "group": 13,
        "period": 2,
        "atomic_number": 5,
        "discovery": {
            "discoverer": "Humphry Davy, Joseph-Louis Gay-Lussac, and Louis Jacques Thénard",
            "year": 1808,
            "notes": "Isolated independently by multiple scientists."
        },
        "physical_properties": {
            "atomic_mass": {"value": 10.81, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 2.34, "units": [('kg', 1), ('m', -3)], "notes": "At room temperature."},
            "melting_point": {"value": 2349, "units": [('K', 1)], "notes": "High melting point for a metalloid."},
            "boiling_point": {"value": 4200, "units": [('K', 1)], "notes": "Extremely high due to strong covalent bonds."},
        },
        "electron_configuration": "[He] 2s² 2p¹",
        "common_uses": ["Semiconductors", "Neutron detectors", "Reinforced materials (borosilicate glass)"],
        },
    6: {
        "name": "Carbon",
        "symbol": "C",
        "group": 14,
        "period": 2,
        "atomic_number": 6,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times in the form of soot and charcoal."
        },
        "physical_properties": {
            "atomic_mass": {"value": 12.011, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 2.267, "units": [('kg', 1), ('m', -3)], "notes": "For graphite form."},
            "melting_point": {"value": 4100, "units": [('K', 1)], "notes": "Sublimation temperature."},
            "boiling_point": {"value": 4300, "units": [('K', 1)], "notes": "Depends on the form (e.g., diamond, graphite)."},
        },
        "electron_configuration": "[He] 2s² 2p²",
        "common_uses": ["Steel production", "Organic chemistry", "Fossil fuels"],
    },
    7: {
        "name": "Nitrogen",
        "symbol": "N",
        "group": 15,
        "period": 2,
        "atomic_number": 7,
        "discovery": {
            "discoverer": "Daniel Rutherford",
            "year": 1772,
            "notes": "Identified as 'noxious air' that does not support combustion."
        },
        "physical_properties": {
            "atomic_mass": {"value": 14.007, "units": [('amu', 1)], "notes": "Dominated by isotope N-14."},
            "density": {"value": 1.2506, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 63.15, "units": [('K', 1)], "notes": "Solidifies under low temperature."},
            "boiling_point": {"value": 77.355, "units": [('K', 1)], "notes": "At 1 atm."},
        },
        "electron_configuration": "[He] 2s² 2p³",
        "common_uses": ["Fertilizers", "Cryogenics", "Inert gas in industry"],
    },
    8: {
        "name": "Oxygen",
        "symbol": "O",
        "group": 16,
        "period": 2,
        "atomic_number": 8,
        "discovery": {
            "discoverer": "Carl Wilhelm Scheele and Joseph Priestley",
            "year": 1774,
            "notes": "Discovered independently; named by Lavoisier."
        },
        "physical_properties": {
            "atomic_mass": {"value": 15.999, "units": [('amu', 1)], "notes": "Dominated by isotope O-16."},
            "density": {"value": 1.429, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 54.36, "units": [('K', 1)], "notes": "Solidifies under low temperature."},
            "boiling_point": {"value": 90.188, "units": [('K', 1)], "notes": "At 1 atm."},
        },
        "electron_configuration": "[He] 2s² 2p⁴",
        "common_uses": ["Respiration", "Steelmaking", "Water purification"],
    },
    9: {
        "name": "Fluorine",
        "symbol": "F",
        "group": 17,
        "period": 2,
        "atomic_number": 9,
        "discovery": {
            "discoverer": "Henri Moissan",
            "year": 1886,
            "notes": "Isolated using electrolysis of potassium fluoride and hydrogen fluoride."
        },
        "physical_properties": {
            "atomic_mass": {"value": 18.998, "units": [('amu', 1)], "notes": "Isotope F-19 dominates."},
            "density": {"value": 1.696, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 53.48, "units": [('K', 1)], "notes": "Solidifies under low temperature."},
            "boiling_point": {"value": 85.03, "units": [('K', 1)], "notes": "At 1 atm."},
        },
        "electron_configuration": "[He] 2s² 2p⁵",
        "common_uses": ["Teflon production", "Refrigerants", "Nuclear fuel processing"],
    },
    10: {
        "name": "Neon",
        "symbol": "Ne",
        "group": 18,
        "period": 2,
        "atomic_number": 10,
        "discovery": {
            "discoverer": "William Ramsay and Morris Travers",
            "year": 1898,
            "notes": "Discovered while studying liquid air."
        },
        "physical_properties": {
            "atomic_mass": {"value": 20.180, "units": [('amu', 1)], "notes": "Dominated by isotope Ne-20."},
            "density": {"value": 0.9002, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 24.56, "units": [('K', 1)], "notes": "Solidifies under low temperature."},
            "boiling_point": {"value": 27.07, "units": [('K', 1)], "notes": "At 1 atm."},
        },
        "electron_configuration": "[He] 2s² 2p⁶",
        "common_uses": ["Neon signs", "High-voltage indicators", "Cryogenics"],
    },
    11: {
        "name": "Sodium",
        "symbol": "Na",
        "group": 1,
        "period": 3,
        "atomic_number": 11,
        "discovery": {
            "discoverer": "Humphry Davy",
            "year": 1807,
            "notes": "Isolated via electrolysis of molten sodium hydroxide."
        },
        "physical_properties": {
            "atomic_mass": {"value": 22.989769, "units": [('amu', 1)], "notes": "Stable isotope Na-23."},
            "density": {"value": 0.968, "units": [('kg', 1), ('m', -3)], "notes": "At room temperature."},
            "melting_point": {"value": 370.87, "units": [('K', 1)], "notes": "Soft metallic solid."},
            "boiling_point": {"value": 1156, "units": [('K', 1)], "notes": "Low boiling point for a metal."},
        },
        "electron_configuration": "[Ne] 3s¹",
        "common_uses": ["Salt production", "Heat exchangers", "Street lamps"],
    },
    12: {
        "name": "Magnesium",
        "symbol": "Mg",
        "group": 2,
        "period": 3,
        "atomic_number": 12,
        "discovery": {
            "discoverer": "Joseph Black",
            "year": 1755,
            "notes": "Identified in magnesia alba (magnesium carbonate)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 24.305, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 1.738, "units": [('kg', 1), ('m', -3)], "notes": "Light metal."},
            "melting_point": {"value": 923, "units": [('K', 1)], "notes": "Metallic solid."},
            "boiling_point": {"value": 1363, "units": [('K', 1)], "notes": "Useful for casting alloys."},
        },
        "electron_configuration": "[Ne] 3s²",
        "common_uses": ["Structural alloys", "Flash photography", "Medicine (magnesium supplements)"],
    },
    13: {
        "name": "Aluminum",
        "symbol": "Al",
        "group": 13,
        "period": 3,
        "atomic_number": 13,
        "discovery": {
            "discoverer": "Hans Christian Ørsted",
            "year": 1825,
            "notes": "First isolated as an impure form."
        },
        "physical_properties": {
            "atomic_mass": {"value": 26.981538, "units": [('amu', 1)], "notes": "Stable isotope Al-27."},
            "density": {"value": 2.70, "units": [('kg', 1), ('m', -3)], "notes": "Lightweight metal."},
            "melting_point": {"value": 933.47, "units": [('K', 1)], "notes": "Metallic solid."},
            "boiling_point": {"value": 2743, "units": [('K', 1)], "notes": "High boiling point for practical applications."},
        },
        "electron_configuration": "[Ne] 3s² 3p¹",
        "common_uses": ["Aircraft construction", "Packaging (foil, cans)", "Electrical wiring"],
    },
    14: {
        "name": "Silicon",
        "symbol": "Si",
        "group": 14,
        "period": 3,
        "atomic_number": 14,
        "discovery": {
            "discoverer": "Jöns Jacob Berzelius",
            "year": 1823,
            "notes": "Isolated in pure form."
        },
        "physical_properties": {
            "atomic_mass": {"value": 28.085, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 2.33, "units": [('kg', 1), ('m', -3)], "notes": "At room temperature."},
            "melting_point": {"value": 1687, "units": [('K', 1)], "notes": "High melting point for semiconductors."},
            "boiling_point": {"value": 3538, "units": [('K', 1)], "notes": "Useful for electronics and alloys."},
        },
        "electron_configuration": "[Ne] 3s² 3p²",
        "common_uses": ["Semiconductors", "Solar panels", "Glass production"],
    },
    15: {
        "name": "Phosphorus",
        "symbol": "P",
        "group": 15,
        "period": 3,
        "atomic_number": 15,
        "discovery": {
            "discoverer": "Hennig Brand",
            "year": 1669,
            "notes": "Discovered while distilling urine, producing a glowing substance."
        },
        "physical_properties": {
            "atomic_mass": {"value": 30.973762, "units": [('amu', 1)], "notes": "Stable isotope P-31."},
            "density": {"value": 1.82, "units": [('kg', 1), ('m', -3)], "notes": "For white phosphorus form."},
            "melting_point": {"value": 317.3, "units": [('K', 1)], "notes": "For white phosphorus form."},
            "boiling_point": {"value": 550, "units": [('K', 1)], "notes": "Highly reactive element."},
        },
        "electron_configuration": "[Ne] 3s² 3p³",
        "common_uses": ["Fertilizers", "Matches", "Steel production"],
    },
    16: {
        "name": "Sulfur",
        "symbol": "S",
        "group": 16,
        "period": 3,
        "atomic_number": 16,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; referred to as 'brimstone.'"
        },
        "physical_properties": {
            "atomic_mass": {"value": 32.06, "units": [('amu', 1)], "notes": "Weighted average of isotopes."},
            "density": {"value": 2.067, "units": [('kg', 1), ('m', -3)], "notes": "For solid at room temperature."},
            "melting_point": {"value": 388.36, "units": [('K', 1)], "notes": "Solid sulfur transitions to liquid."},
            "boiling_point": {"value": 717.8, "units": [('K', 1)], "notes": "Boils into gaseous form."},
        },
        "electron_configuration": "[Ne] 3s² 3p⁴",
        "common_uses": ["Fertilizers", "Gunpowder", "Sulfuric acid production"],
    },
    17: {
        "name": "Chlorine",
        "symbol": "Cl",
        "group": 17,
        "period": 3,
        "atomic_number": 17,
        "discovery": {
            "discoverer": "Carl Wilhelm Scheele",
            "year": 1774,
            "notes": "Identified as a gas with a greenish color."
        },
        "physical_properties": {
            "atomic_mass": {"value": 35.45, "units": [('amu', 1)], "notes": "Weighted average of isotopes Cl-35 and Cl-37."},
            "density": {"value": 3.214, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 171.6, "units": [('K', 1)], "notes": "Solid under very low temperature."},
            "boiling_point": {"value": 239.11, "units": [('K', 1)], "notes": "Gaseous at room temperature."},
        },
        "electron_configuration": "[Ne] 3s² 3p⁵",
        "common_uses": ["Water purification", "Disinfectants", "PVC production"],
    },
    18: {
        "name": "Argon",
        "symbol": "Ar",
        "group": 18,
        "period": 3,
        "atomic_number": 18,
        "discovery": {
            "discoverer": "Lord Rayleigh and William Ramsay",
            "year": 1894,
            "notes": "First noble gas discovered."
        },
        "physical_properties": {
            "atomic_mass": {"value": 39.948, "units": [('amu', 1)], "notes": "Dominated by isotope Ar-40."},
            "density": {"value": 1.784, "units": [('kg', 1), ('m', -3)], "notes": "Gas at STP."},
            "melting_point": {"value": 83.81, "units": [('K', 1)], "notes": "Solidifies under low temperature."},
            "boiling_point": {"value": 87.30, "units": [('K', 1)], "notes": "At 1 atm."},
        },
        "electron_configuration": "[Ne] 3s² 3p⁶",
        "common_uses": ["Shielding gas in welding", "Lighting (argon lamps)", "Electronics"],
    },
    19: {
        "name": "Potassium",
        "symbol": "K",
        "group": 1,
        "period": 4,
        "atomic_number": 19,
        "discovery": {
            "discoverer": "Humphry Davy",
            "year": 1807,
            "notes": "Isolated via electrolysis of molten potash (potassium hydroxide)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 39.0983, "units": [('amu', 1)], "notes": "Stable isotope K-39."},
            "density": {"value": 0.862, "units": [('kg', 1), ('m', -3)], "notes": "Soft metallic solid."},
            "melting_point": {"value": 336.53, "units": [('K', 1)], "notes": "Low melting point for a metal."},
            "boiling_point": {"value": 1032, "units": [('K', 1)], "notes": "Used in heat transfer applications."},
        },
        "electron_configuration": "[Ar] 4s¹",
        "common_uses": ["Fertilizers", "Glass production", "Medications"],
    },
    20: {
        "name": "Calcium",
        "symbol": "Ca",
        "group": 2,
        "period": 4,
        "atomic_number": 20,
        "discovery": {
            "discoverer": "Humphry Davy",
            "year": 1808,
            "notes": "Isolated via electrolysis of lime (calcium oxide)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 40.078, "units": [('amu', 1)], "notes": "Stable isotope Ca-40 dominates."},
            "density": {"value": 1.55, "units": [('kg', 1), ('m', -3)], "notes": "Soft metal at room temperature."},
            "melting_point": {"value": 1115, "units": [('K', 1)], "notes": "Higher melting point for reactive metals."},
            "boiling_point": {"value": 1757, "units": [('K', 1)], "notes": "Metallic vapor at high temperatures."},
        },
        "electron_configuration": "[Ar] 4s²",
        "common_uses": ["Concrete production", "Dietary supplements", "Steelmaking"],
    },
    21: {
        "name": "Scandium",
        "symbol": "Sc",
        "group": 3,
        "period": 4,
        "atomic_number": 21,
        "discovery": {
            "discoverer": "Lars Fredrik Nilson",
            "year": 1879,
            "notes": "Found in minerals euxenite and gadolinite."
        },
        "physical_properties": {
            "atomic_mass": {"value": 44.955908, "units": [('amu', 1)], "notes": "Stable isotope Sc-45."},
            "density": {"value": 2.985, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1814, "units": [('K', 1)], "notes": "Metallic solid."},
            "boiling_point": {"value": 3109, "units": [('K', 1)], "notes": "High boiling point for transition metals."},
        },
        "electron_configuration": "[Ar] 3d¹ 4s²",
        "common_uses": ["Alloys in aerospace", "High-intensity lamps", "Research applications"],
    },
    22: {
        "name": "Titanium",
        "symbol": "Ti",
        "group": 4,
        "period": 4,
        "atomic_number": 22,
        "discovery": {
            "discoverer": "William Gregor",
            "year": 1791,
            "notes": "Found in ilmenite and later named by Klaproth."
        },
        "physical_properties": {
            "atomic_mass": {"value": 47.867, "units": [('amu', 1)], "notes": "Dominated by isotope Ti-48."},
            "density": {"value": 4.54, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1941, "units": [('K', 1)], "notes": "High melting point for lightweight metals."},
            "boiling_point": {"value": 3560, "units": [('K', 1)], "notes": "Extremely high boiling point."},
        },
        "electron_configuration": "[Ar] 3d² 4s²",
        "common_uses": ["Aerospace alloys", "Medical implants", "Pigments"],
    },
    23: {
        "name": "Vanadium",
        "symbol": "V",
        "group": 5,
        "period": 4,
        "atomic_number": 23,
        "discovery": {
            "discoverer": "Andrés Manuel del Río",
            "year": 1801,
            "notes": "Named after the Norse goddess Vanadis; rediscovered by Nils Sefström."
        },
        "physical_properties": {
            "atomic_mass": {"value": 50.9415, "units": [('amu', 1)], "notes": "Dominated by isotope V-51."},
            "density": {"value": 6.11, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 2183, "units": [('K', 1)], "notes": "Used for high-temperature applications."},
            "boiling_point": {"value": 3680, "units": [('K', 1)], "notes": "Transition metal with high stability."},
        },
        "electron_configuration": "[Ar] 3d³ 4s²",
        "common_uses": ["Steel alloys", "Catalysts", "Tools"],
    },
    24: {
        "name": "Chromium",
        "symbol": "Cr",
        "group": 6,
        "period": 4,
        "atomic_number": 24,
        "discovery": {
            "discoverer": "Louis Nicolas Vauquelin",
            "year": 1797,
            "notes": "Named for its colorful compounds."
        },
        "physical_properties": {
            "atomic_mass": {"value": 51.9961, "units": [('amu', 1)], "notes": "Dominated by isotope Cr-52."},
            "density": {"value": 7.19, "units": [('kg', 1), ('m', -3)], "notes": "Hard metal at room temperature."},
            "melting_point": {"value": 2180, "units": [('K', 1)], "notes": "Important for refractory applications."},
            "boiling_point": {"value": 2944, "units": [('K', 1)], "notes": "Highly resistant to corrosion."},
        },
        "electron_configuration": "[Ar] 3d⁵ 4s¹",
        "common_uses": ["Stainless steel production", "Electroplating", "Pigments"],
    },
    25: {
        "name": "Manganese",
        "symbol": "Mn",
        "group": 7,
        "period": 4,
        "atomic_number": 25,
        "discovery": {
            "discoverer": "Carl Wilhelm Scheele and Johann Gottlieb Gahn",
            "year": 1774,
            "notes": "Isolated from pyrolusite (manganese dioxide)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 54.938044, "units": [('amu', 1)], "notes": "Stable isotope Mn-55."},
            "density": {"value": 7.21, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1519, "units": [('K', 1)], "notes": "Used in steelmaking."},
            "boiling_point": {"value": 2334, "units": [('K', 1)], "notes": "Transition metal with wide applications."},
        },
        "electron_configuration": "[Ar] 3d⁵ 4s²",
        "common_uses": ["Steelmaking", "Batteries", "Pigments"],
    },
    26: {
        "name": "Iron",
        "symbol": "Fe",
        "group": 8,
        "period": 4,
        "atomic_number": 26,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since antiquity; used in tools and weapons for thousands of years."
        },
        "physical_properties": {
            "atomic_mass": {"value": 55.845, "units": [('amu', 1)], "notes": "Dominated by isotope Fe-56."},
            "density": {"value": 7.874, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1811, "units": [('K', 1)], "notes": "Used widely in metallurgy."},
            "boiling_point": {"value": 3134, "units": [('K', 1)], "notes": "Essential in manufacturing and construction."},
        },
        "electron_configuration": "[Ar] 3d⁶ 4s²",
        "common_uses": ["Steel production", "Construction", "Biological processes (hemoglobin)"],
    },
    27: {
        "name": "Cobalt",
        "symbol": "Co",
        "group": 9,
        "period": 4,
        "atomic_number": 27,
        "discovery": {
            "discoverer": "Georg Brandt",
            "year": 1735,
            "notes": "First identified as an element in cobalt ores."
        },
        "physical_properties": {
            "atomic_mass": {"value": 58.933194, "units": [('amu', 1)], "notes": "Stable isotope Co-59."},
            "density": {"value": 8.90, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1768, "units": [('K', 1)], "notes": "Used in high-temperature applications."},
            "boiling_point": {"value": 3200, "units": [('K', 1)], "notes": "Transition metal with versatile uses."},
        },
        "electron_configuration": "[Ar] 3d⁷ 4s²",
        "common_uses": ["Alloys (superalloys)", "Batteries", "Pigments"],
    },
    28: {
        "name": "Nickel",
        "symbol": "Ni",
        "group": 10,
        "period": 4,
        "atomic_number": 28,
        "discovery": {
            "discoverer": "Axel Fredrik Cronstedt",
            "year": 1751,
            "notes": "Discovered in the mineral niccolite (nickel arsenide)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 58.6934, "units": [('amu', 1)], "notes": "Dominated by isotope Ni-58."},
            "density": {"value": 8.908, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1728, "units": [('K', 1)], "notes": "Highly corrosion-resistant."},
            "boiling_point": {"value": 3186, "units": [('K', 1)], "notes": "Widely used in industrial applications."},
        },
        "electron_configuration": "[Ar] 3d⁸ 4s²",
        "common_uses": ["Stainless steel", "Plating", "Batteries"],
    },
    29: {
        "name": "Copper",
        "symbol": "Cu",
        "group": 11,
        "period": 4,
        "atomic_number": 29,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; essential in early metallurgy."
        },
        "physical_properties": {
            "atomic_mass": {"value": 63.546, "units": [('amu', 1)], "notes": "Weighted average of isotopes Cu-63 and Cu-65."},
            "density": {"value": 8.96, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 1357.77, "units": [('K', 1)], "notes": "Important for electrical conductivity."},
            "boiling_point": {"value": 2835, "units": [('K', 1)], "notes": "High conductivity for industrial use."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s¹",
        "common_uses": ["Electrical wiring", "Coins", "Plumbing"],
    },
    30: {
        "name": "Zinc",
        "symbol": "Zn",
        "group": 12,
        "period": 4,
        "atomic_number": 30,
        "discovery": {
            "discoverer": "India (ancient)",
            "year": None,
            "notes": "Used as early as 1000 BCE; named zinc in the West by Paracelsus."
        },
        "physical_properties": {
            "atomic_mass": {"value": 65.38, "units": [('amu', 1)], "notes": "Dominated by isotope Zn-64."},
            "density": {"value": 7.14, "units": [('kg', 1), ('m', -3)], "notes": "Metal at room temperature."},
            "melting_point": {"value": 692.68, "units": [('K', 1)], "notes": "Low melting point for a metal."},
            "boiling_point": {"value": 1180, "units": [('K', 1)], "notes": "Used for galvanization."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s²",
        "common_uses": ["Galvanization", "Alloys (brass)", "Batteries"],
    },
    31: {
        "name": "Gallium",
        "symbol": "Ga",
        "group": 13,
        "period": 4,
        "atomic_number": 31,
        "discovery": {
            "discoverer": "Lecoq de Boisbaudran",
            "year": 1875,
            "notes": "Predicted by Mendeleev; discovered via spectroscopy."
        },
        "physical_properties": {
            "atomic_mass": {"value": 69.723, "units": [('amu', 1)], "notes": "Weighted average of isotopes Ga-69 and Ga-71."},
            "density": {"value": 5.91, "units": [('kg', 1), ('m', -3)], "notes": "Liquid at slightly above room temperature."},
            "melting_point": {"value": 302.91, "units": [('K', 1)], "notes": "Melts in the palm of your hand."},
            "boiling_point": {"value": 2477, "units": [('K', 1)], "notes": "Useful for high-temperature applications."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p¹",
        "common_uses": ["Semiconductors", "LEDs", "Solar panels"],
    },
    32: {
        "name": "Germanium",
        "symbol": "Ge",
        "group": 14,
        "period": 4,
        "atomic_number": 32,
        "discovery": {
            "discoverer": "Clemens Winkler",
            "year": 1886,
            "notes": "Predicted by Mendeleev; confirmed through silver ore analysis."
        },
        "physical_properties": {
            "atomic_mass": {"value": 72.630, "units": [('amu', 1)], "notes": "Isotopes include Ge-70 and Ge-74."},
            "density": {"value": 5.32, "units": [('kg', 1), ('m', -3)], "notes": "A metalloid at room temperature."},
            "melting_point": {"value": 1211.40, "units": [('K', 1)], "notes": "High melting point for electronic applications."},
            "boiling_point": {"value": 3106, "units": [('K', 1)], "notes": "Useful for semiconductors."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p²",
        "common_uses": ["Semiconductors", "Fiber optics", "Infrared optics"],
    },
    33: {
        "name": "Arsenic",
        "symbol": "As",
        "group": 15,
        "period": 4,
        "atomic_number": 33,
        "discovery": {
            "discoverer": "Albertus Magnus",
            "year": 1250,
            "notes": "Isolated in the Middle Ages; known for its toxicity."
        },
        "physical_properties": {
            "atomic_mass": {"value": 74.9216, "units": [('amu', 1)], "notes": "Dominated by isotope As-75."},
            "density": {"value": 5.73, "units": [('kg', 1), ('m', -3)], "notes": "A metalloid at room temperature."},
            "melting_point": {"value": 1090, "units": [('K', 1)], "notes": "Sublimates rather than melts under normal pressure."},
            "boiling_point": {"value": None, "units": [], "notes": "Sublimates directly to gas phase."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p³",
        "common_uses": ["Pesticides", "Alloys", "Semiconductors"],
    },
    34: {
        "name": "Selenium",
        "symbol": "Se",
        "group": 16,
        "period": 4,
        "atomic_number": 34,
        "discovery": {
            "discoverer": "Jöns Jacob Berzelius",
            "year": 1817,
            "notes": "Discovered during sulfuric acid production."
        },
        "physical_properties": {
            "atomic_mass": {"value": 78.971, "units": [('amu', 1)], "notes": "Dominated by isotope Se-80."},
            "density": {"value": 4.81, "units": [('kg', 1), ('m', -3)], "notes": "Non-metal at room temperature."},
            "melting_point": {"value": 494, "units": [('K', 1)], "notes": "Low melting point for a non-metal."},
            "boiling_point": {"value": 958, "units": [('K', 1)], "notes": "Used in glass production and electronics."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p⁴",
        "common_uses": ["Glass production", "Photocells", "Pigments"],
    },
    35: {
        "name": "Bromine",
        "symbol": "Br",
        "group": 17,
        "period": 4,
        "atomic_number": 35,
        "discovery": {
            "discoverer": "Antoine Jérôme Balard",
            "year": 1826,
            "notes": "Isolated from brine water; named for its strong odor."
        },
        "physical_properties": {
            "atomic_mass": {"value": 79.904, "units": [('amu', 1)], "notes": "Dominated by isotopes Br-79 and Br-81."},
            "density": {"value": 3.12, "units": [('kg', 1), ('m', -3)], "notes": "Liquid at room temperature."},
            "melting_point": {"value": 265.8, "units": [('K', 1)], "notes": "Low melting point for a halogen."},
            "boiling_point": {"value": 332, "units": [('K', 1)], "notes": "Used in flame retardants and photography."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p⁵",
        "common_uses": ["Flame retardants", "Photography", "Water purification"],
    },
    36: {
        "name": "Krypton",
        "symbol": "Kr",
        "group": 18,
        "period": 4,
        "atomic_number": 36,
        "discovery": {
            "discoverer": "William Ramsay and Morris Travers",
            "year": 1898,
            "notes": "Discovered in the residue of liquid air distillation."
        },
        "physical_properties": {
            "atomic_mass": {"value": 83.798, "units": [('amu', 1)], "notes": "Dominated by isotope Kr-84."},
            "density": {"value": 3.75, "units": [('kg', 1), ('m', -3)], "notes": "Gas at room temperature."},
            "melting_point": {"value": 116, "units": [('K', 1)], "notes": "Low melting point for a noble gas."},
            "boiling_point": {"value": 119.93, "units": [('K', 1)], "notes": "Used in lighting and photography."},
        },
        "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p⁶",
        "common_uses": ["Lighting", "Photography", "Insulation"],
    },
    37: {
        "name": "Rubidium",
        "symbol": "Rb",
        "group": 1,
        "period": 5,
        "atomic_number": 37,
        "discovery": {
            "discoverer": "Robert Bunsen and Gustav Kirchhoff",
            "year": 1861,
            "notes": "Discovered via spectroscopy; named after its red spectral lines."
        },
        "physical_properties": {
            "atomic_mass": {"value": 85.4678, "units": [('amu', 1)], "notes": "Dominated by isotope Rb-85."},
            "density": {"value": 1.53, "units": [('kg', 1), ('m', -3)], "notes": "Soft alkali metal."},
            "melting_point": {"value": 312.46, "units": [('K', 1)], "notes": "Low melting point for a metal."},
            "boiling_point": {"value": 961, "units": [('K', 1)], "notes": "Highly reactive in air and water."},
        },
        "electron_configuration": "[Kr] 5s¹",
        "common_uses": ["Specialized glasses", "Atomic clocks", "Electronics"],
    },
    38: {
        "name": "Strontium",
        "symbol": "Sr",
        "group": 2,
        "period": 5,
        "atomic_number": 38,
        "discovery": {
            "discoverer": "Adair Crawford",
            "year": 1790,
            "notes": "Identified in strontianite; named after the Scottish village of Strontian."
        },
        "physical_properties": {
            "atomic_mass": {"value": 87.62, "units": [('amu', 1)], "notes": "Dominated by isotope Sr-88."},
            "density": {"value": 2.64, "units": [('kg', 1), ('m', -3)], "notes": "Soft alkaline earth metal."},
            "melting_point": {"value": 1050, "units": [('K', 1)], "notes": "Used in fireworks for red coloration."},
            "boiling_point": {"value": 1650, "units": [('K', 1)], "notes": "Reacts strongly with water."},
        },
        "electron_configuration": "[Kr] 5s²",
        "common_uses": ["Fireworks", "Medical imaging (strontium-90)", "Glass production"],
    },
    39: {
        "name": "Yttrium",
        "symbol": "Y",
        "group": 3,
        "period": 5,
        "atomic_number": 39,
        "discovery": {
            "discoverer": "Johan Gadolin",
            "year": 1794,
            "notes": "Discovered in the mineral gadolinite; named for Ytterby, Sweden."
        },
        "physical_properties": {
            "atomic_mass": {"value": 88.905, "units": [('amu', 1)], "notes": "Dominated by isotope Y-89."},
            "density": {"value": 4.47, "units": [('kg', 1), ('m', -3)], "notes": "Transition metal with high strength."},
            "melting_point": {"value": 1799, "units": [('K', 1)], "notes": "Useful for high-temperature applications."},
            "boiling_point": {"value": 3609, "units": [('K', 1)], "notes": "Used in superconductors and lasers."},
        },
        "electron_configuration": "[Kr] 4d¹ 5s²",
        "common_uses": ["Superconductors", "Lasers", "Alloys (aluminum and magnesium)"],
    },
    40: {
        "name": "Zirconium",
        "symbol": "Zr",
        "group": 4,
        "period": 5,
        "atomic_number": 40,
        "discovery": {
            "discoverer": "Martin Heinrich Klaproth",
            "year": 1789,
            "notes": "Discovered in zircon; named after the mineral zirconium silicate."
        },
        "physical_properties": {
            "atomic_mass": {"value": 91.224, "units": [('amu', 1)], "notes": "Dominated by isotope Zr-90."},
            "density": {"value": 6.52, "units": [('kg', 1), ('m', -3)], "notes": "Corrosion-resistant metal."},
            "melting_point": {"value": 2128, "units": [('K', 1)], "notes": "Used in nuclear reactors."},
            "boiling_point": {"value": 4678, "units": [('K', 1)], "notes": "Extremely high melting and boiling points."},
        },
        "electron_configuration": "[Kr] 4d² 5s²",
        "common_uses": ["Nuclear reactors", "Ceramics", "Surgical instruments"],
    },
    41: {
        "name": "Niobium",
        "symbol": "Nb",
        "group": 5,
        "period": 5,
        "atomic_number": 41,
        "discovery": {
            "discoverer": "Charles Hatchett",
            "year": 1801,
            "notes": "Initially named columbium; later renamed niobium after Niobe in mythology."
        },
        "physical_properties": {
            "atomic_mass": {"value": 92.906, "units": [('amu', 1)], "notes": "Dominated by isotope Nb-93."},
            "density": {"value": 8.57, "units": [('kg', 1), ('m', -3)], "notes": "Transition metal with high strength."},
            "melting_point": {"value": 2750, "units": [('K', 1)], "notes": "Used in superconducting magnets."},
            "boiling_point": {"value": 5017, "units": [('K', 1)], "notes": "Extremely high temperature tolerance."},
        },
        "electron_configuration": "[Kr] 4d⁴ 5s¹",
        "common_uses": ["Superconducting magnets", "Jet engines", "Steel alloys"],
    },
    42: {
        "name": "Molybdenum",
        "symbol": "Mo",
        "group": 6,
        "period": 5,
        "atomic_number": 42,
        "discovery": {
            "discoverer": "Carl Wilhelm Scheele",
            "year": 1778,
            "notes": "Isolated from molybdenite ore; named after the Greek word 'molybdos' (lead)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 95.95, "units": [('amu', 1)], "notes": "Dominated by isotope Mo-98."},
            "density": {"value": 10.22, "units": [('kg', 1), ('m', -3)], "notes": "Dense transition metal."},
            "melting_point": {"value": 2896, "units": [('K', 1)], "notes": "High melting point suitable for alloys."},
            "boiling_point": {"value": 4912, "units": [('K', 1)], "notes": "Used in extreme-temperature environments."},
        },
        "electron_configuration": "[Kr] 4d⁵ 5s¹",
        "common_uses": ["Steel alloys", "Catalysts", "High-strength components"],
    },
    43: {
        "name": "Technetium",
        "symbol": "Tc",
        "group": 7,
        "period": 5,
        "atomic_number": 43,
        "discovery": {
            "discoverer": "Emilio Segrè and Carlo Perrier",
            "year": 1937,
            "notes": "First artificially produced element; derived from molybdenum."
        },
        "physical_properties": {
            "atomic_mass": {"value": 98, "units": [('amu', 1)], "notes": "Only synthetic isotopes; unstable."},
            "density": {"value": 11.5, "units": [('kg', 1), ('m', -3)], "notes": "Radioactive and dense."},
            "melting_point": {"value": 2430, "units": [('K', 1)], "notes": "Used in nuclear medicine."},
            "boiling_point": {"value": 4538, "units": [('K', 1)], "notes": "Rarely occurs in nature."},
        },
        "electron_configuration": "[Kr] 4d⁵ 5s²",
        "common_uses": ["Medical imaging (radiopharmaceuticals)", "Corrosion-resistant alloys"],
    },
    44: {
        "name": "Ruthenium",
        "symbol": "Ru",
        "group": 8,
        "period": 5,
        "atomic_number": 44,
        "discovery": {
            "discoverer": "Karl Ernst Claus",
            "year": 1844,
            "notes": "Named after Ruthenia, the Latin name for Russia."
        },
        "physical_properties": {
            "atomic_mass": {"value": 101.07, "units": [('amu', 1)], "notes": "Dominated by isotope Ru-102."},
            "density": {"value": 12.37, "units": [('kg', 1), ('m', -3)], "notes": "Hard, corrosion-resistant metal."},
            "melting_point": {"value": 2607, "units": [('K', 1)], "notes": "Used in electrical contacts."},
            "boiling_point": {"value": 4423, "units": [('K', 1)], "notes": "Maintains stability at high temperatures."},
        },
        "electron_configuration": "[Kr] 4d⁷ 5s¹",
        "common_uses": ["Electrical contacts", "Catalysts", "Platinum-based alloys"],
    },
    45: {
        "name": "Rhodium",
        "symbol": "Rh",
        "group": 9,
        "period": 5,
        "atomic_number": 45,
        "discovery": {
            "discoverer": "William Hyde Wollaston",
            "year": 1803,
            "notes": "Discovered in platinum ore; named after its rose-colored compounds."
        },
        "physical_properties": {
            "atomic_mass": {"value": 102.905, "units": [('amu', 1)], "notes": "Dominated by isotope Rh-103."},
            "density": {"value": 12.41, "units": [('kg', 1), ('m', -3)], "notes": "Highly reflective transition metal."},
            "melting_point": {"value": 2237, "units": [('K', 1)], "notes": "Ideal for high-temperature applications."},
            "boiling_point": {"value": 3968, "units": [('K', 1)], "notes": "Corrosion-resistant under extreme conditions."},
        },
        "electron_configuration": "[Kr] 4d⁸ 5s¹",
        "common_uses": ["Catalytic converters", "Jewelry", "Reflective coatings"],
    },
    46: {
        "name": "Palladium",
        "symbol": "Pd",
        "group": 10,
        "period": 5,
        "atomic_number": 46,
        "discovery": {
            "discoverer": "William Hyde Wollaston",
            "year": 1803,
            "notes": "Named after the asteroid Pallas; discovered alongside rhodium."
        },
        "physical_properties": {
            "atomic_mass": {"value": 106.42, "units": [('amu', 1)], "notes": "Dominated by isotope Pd-106."},
            "density": {"value": 12.02, "units": [('kg', 1), ('m', -3)], "notes": "Soft, ductile transition metal."},
            "melting_point": {"value": 1828.05, "units": [('K', 1)], "notes": "Useful in hydrogen storage."},
            "boiling_point": {"value": 3236, "units": [('K', 1)], "notes": "Highly versatile in catalytic processes."},
        },
        "electron_configuration": "[Kr] 4d¹⁰",
        "common_uses": ["Catalysts", "Electronics", "Hydrogen storage"],
    },
    47: {
        "name": "Silver",
        "symbol": "Ag",
        "group": 11,
        "period": 5,
        "atomic_number": 47,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; highly valued for its luster and conductivity."
        },
        "physical_properties": {
            "atomic_mass": {"value": 107.868, "units": [('amu', 1)], "notes": "Dominated by isotope Ag-107."},
            "density": {"value": 10.49, "units": [('kg', 1), ('m', -3)], "notes": "High conductivity among metals."},
            "melting_point": {"value": 1234.93, "units": [('K', 1)], "notes": "Used in jewelry and industrial applications."},
            "boiling_point": {"value": 2435, "units": [('K', 1)], "notes": "Useful in electronics and photography."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s¹",
        "common_uses": ["Jewelry", "Electronics", "Photography"],
    },
    48: {
        "name": "Cadmium",
        "symbol": "Cd",
        "group": 12,
        "period": 5,
        "atomic_number": 48,
        "discovery": {
            "discoverer": "Friedrich Stromeyer",
            "year": 1817,
            "notes": "Discovered during zinc ore analysis; named for the Greek word 'kadmeia' (calamine)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 112.414, "units": [('amu', 1)], "notes": "Dominated by isotope Cd-114."},
            "density": {"value": 8.65, "units": [('kg', 1), ('m', -3)], "notes": "Soft, toxic metal."},
            "melting_point": {"value": 594.22, "units": [('K', 1)], "notes": "Used in coatings and alloys."},
            "boiling_point": {"value": 1040, "units": [('K', 1)], "notes": "Moderate boiling point for industrial use."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s²",
        "common_uses": ["Batteries (Ni-Cd)", "Electroplating", "Pigments"],
    },
    49: {
        "name": "Indium",
        "symbol": "In",
        "group": 13,
        "period": 5,
        "atomic_number": 49,
        "discovery": {
            "discoverer": "Ferdinand Reich and Hieronymous Richter",
            "year": 1863,
            "notes": "Discovered via spectroscopy; named for its indigo spectral lines."
        },
        "physical_properties": {
            "atomic_mass": {"value": 114.818, "units": [('amu', 1)], "notes": "Dominated by isotope In-115."},
            "density": {"value": 7.31, "units": [('kg', 1), ('m', -3)], "notes": "Soft, malleable metal."},
            "melting_point": {"value": 429.75, "units": [('K', 1)], "notes": "Melts easily for industrial use."},
            "boiling_point": {"value": 2345, "units": [('K', 1)], "notes": "Used in semiconductors and alloys."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p¹",
        "common_uses": ["Semiconductors", "LCD screens", "Alloys (low-melting-point)"],
    },
    50: {
        "name": "Tin",
        "symbol": "Sn",
        "group": 14,
        "period": 5,
        "atomic_number": 50,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Used since antiquity; essential for making bronze with copper."
        },
        "physical_properties": {
            "atomic_mass": {"value": 118.710, "units": [('amu', 1)], "notes": "Dominated by isotope Sn-120."},
            "density": {"value": 7.29, "units": [('kg', 1), ('m', -3)], "notes": "Soft metal with low toxicity."},
            "melting_point": {"value": 505.08, "units": [('K', 1)], "notes": "Low melting point for soldering."},
            "boiling_point": {"value": 2875, "units": [('K', 1)], "notes": "Common in alloys."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p²",
        "common_uses": ["Soldering", "Plating", "Alloys (bronze, pewter)"],
    },
    51: {
        "name": "Antimony",
        "symbol": "Sb",
        "group": 15,
        "period": 5,
        "atomic_number": 51,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; used in cosmetics and alloys."
        },
        "physical_properties": {
            "atomic_mass": {"value": 121.760, "units": [('amu', 1)], "notes": "Dominated by isotope Sb-121."},
            "density": {"value": 6.68, "units": [('kg', 1), ('m', -3)], "notes": "Metalloid with high density."},
            "melting_point": {"value": 903.78, "units": [('K', 1)], "notes": "Used in flame retardants."},
            "boiling_point": {"value": 1860, "units": [('K', 1)], "notes": "Useful for heat-resistant applications."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p³",
        "common_uses": ["Flame retardants", "Batteries", "Alloys (type metal)"],
    },
    52: {
        "name": "Tellurium",
        "symbol": "Te",
        "group": 16,
        "period": 5,
        "atomic_number": 52,
        "discovery": {
            "discoverer": "Franz-Joseph Müller von Reichenstein",
            "year": 1782,
            "notes": "Identified in gold ores; named after the Latin word 'tellus' (earth)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 127.60, "units": [('amu', 1)], "notes": "Dominated by isotope Te-130."},
            "density": {"value": 6.24, "units": [('kg', 1), ('m', -3)], "notes": "Brittle metalloid."},
            "melting_point": {"value": 722.66, "units": [('K', 1)], "notes": "Used in thermoelectric devices."},
            "boiling_point": {"value": 1261, "units": [('K', 1)], "notes": "Useful for semiconductors and alloys."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁴",
        "common_uses": ["Thermoelectric devices", "Semiconductors", "Alloys"],
    },
    53: {
        "name": "Iodine",
        "symbol": "I",
        "group": 17,
        "period": 5,
        "atomic_number": 53,
        "discovery": {
            "discoverer": "Bernard Courtois",
            "year": 1811,
            "notes": "Discovered in seaweed ash; named for its violet vapor."
        },
        "physical_properties": {
            "atomic_mass": {"value": 126.904, "units": [('amu', 1)], "notes": "Dominated by isotope I-127."},
            "density": {"value": 4.93, "units": [('kg', 1), ('m', -3)], "notes": "Solid halogen at room temperature."},
            "melting_point": {"value": 386.85, "units": [('K', 1)], "notes": "Used in medical applications."},
            "boiling_point": {"value": 457.4, "units": [('K', 1)], "notes": "Essential for thyroid health."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁵",
        "common_uses": ["Antiseptics", "Photography", "Nutrition"],
    },
    54: {
        "name": "Xenon",
        "symbol": "Xe",
        "group": 18,
        "period": 5,
        "atomic_number": 54,
        "discovery": {
            "discoverer": "William Ramsay and Morris Travers",
            "year": 1898,
            "notes": "Discovered during liquid air distillation."
        },
        "physical_properties": {
            "atomic_mass": {"value": 131.293, "units": [('amu', 1)], "notes": "Dominated by isotope Xe-132."},
            "density": {"value": 5.9, "units": [('kg', 1), ('m', -3)], "notes": "Noble gas at room temperature."},
            "melting_point": {"value": 161.4, "units": [('K', 1)], "notes": "Used in lighting and medical imaging."},
            "boiling_point": {"value": 165.03, "units": [('K', 1)], "notes": "Rare and inert gas."},
        },
        "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁶",
        "common_uses": ["Lighting", "Medical imaging", "Ion propulsion"],
    },
    55: {
        "name": "Cesium",
        "symbol": "Cs",
        "group": 1,
        "period": 6,
        "atomic_number": 55,
        "discovery": {
            "discoverer": "Robert Bunsen and Gustav Kirchhoff",
            "year": 1860,
            "notes": "Discovered via spectroscopy; named after its blue spectral lines."
        },
        "physical_properties": {
            "atomic_mass": {"value": 132.905, "units": [('amu', 1)], "notes": "Dominated by isotope Cs-133."},
            "density": {"value": 1.93, "units": [('kg', 1), ('m', -3)], "notes": "Soft, highly reactive alkali metal."},
            "melting_point": {"value": 301.59, "units": [('K', 1)], "notes": "Melts at a temperature near room temperature."},
            "boiling_point": {"value": 944, "units": [('K', 1)], "notes": "Used in atomic clocks."},
        },
        "electron_configuration": "[Xe] 6s¹",
        "common_uses": ["Atomic clocks", "Photoelectric cells", "Specialized glasses"],
    },
    56: {
        "name": "Barium",
        "symbol": "Ba",
        "group": 2,
        "period": 6,
        "atomic_number": 56,
        "discovery": {
            "discoverer": "Carl Scheele",
            "year": 1774,
            "notes": "Identified in barite; named after the Greek word 'barys' (heavy)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 137.327, "units": [('amu', 1)], "notes": "Dominated by isotope Ba-138."},
            "density": {"value": 3.62, "units": [('kg', 1), ('m', -3)], "notes": "Soft alkaline earth metal."},
            "melting_point": {"value": 1000, "units": [('K', 1)], "notes": "Used in drilling fluids and radiology."},
            "boiling_point": {"value": 2118, "units": [('K', 1)], "notes": "Useful for fireworks and electronics."},
        },
        "electron_configuration": "[Xe] 6s²",
        "common_uses": ["Drilling fluids", "Fireworks", "Medical imaging (barium sulfate)"],
    },
    57: {
        "name": "Lanthanum",
        "symbol": "La",
        "group": 3,
        "period": 6,
        "atomic_number": 57,
        "discovery": {
            "discoverer": "Carl Gustaf Mosander",
            "year": 1839,
            "notes": "Discovered in cerium nitrate; named after the Greek word 'lanthanein' (to lie hidden)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 138.905, "units": [('amu', 1)], "notes": "Dominated by isotope La-139."},
            "density": {"value": 6.15, "units": [('kg', 1), ('m', -3)], "notes": "Soft, ductile rare-earth metal."},
            "melting_point": {"value": 1193, "units": [('K', 1)], "notes": "Useful in hydrogen storage and lighting."},
            "boiling_point": {"value": 3737, "units": [('K', 1)], "notes": "High temperature tolerance."},
        },
        "electron_configuration": "[Xe] 5d¹ 6s²",
        "common_uses": ["Hydrogen storage", "Lighting", "Optics (camera lenses)"],
    },
    58: {
        "name": "Cerium",
        "symbol": "Ce",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 58,
        "discovery": {
            "discoverer": "Martin Heinrich Klaproth, Jöns Jacob Berzelius, and Wilhelm Hisinger",
            "year": 1803,
            "notes": "Named after the dwarf planet Ceres."
        },
        "physical_properties": {
            "atomic_mass": {"value": 140.116, "units": [('amu', 1)], "notes": "Dominated by isotope Ce-140."},
            "density": {"value": 6.77, "units": [('kg', 1), ('m', -3)], "notes": "Reactive rare-earth metal."},
            "melting_point": {"value": 1068, "units": [('K', 1)], "notes": "Used in catalytic converters."},
            "boiling_point": {"value": 3716, "units": [('K', 1)], "notes": "Useful in glass polishing and metallurgy."},
        },
        "electron_configuration": "[Xe] 4f¹ 5d¹ 6s²",
        "common_uses": ["Catalytic converters", "Glass polishing", "Alloys"],
    },
    59: {
        "name": "Praseodymium",
        "symbol": "Pr",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 59,
        "discovery": {
            "discoverer": "Carl Auer von Welsbach",
            "year": 1885,
            "notes": "Separated from neodymium; named after the Greek words for 'green twin.'"
        },
        "physical_properties": {
            "atomic_mass": {"value": 140.907, "units": [('amu', 1)], "notes": "Dominated by isotope Pr-141."},
            "density": {"value": 6.77, "units": [('kg', 1), ('m', -3)], "notes": "Soft, malleable rare-earth metal."},
            "melting_point": {"value": 1208, "units": [('K', 1)], "notes": "Used in high-strength alloys."},
            "boiling_point": {"value": 3793, "units": [('K', 1)], "notes": "Applications in lighting and magnets."},
        },
        "electron_configuration": "[Xe] 4f³ 6s²",
        "common_uses": ["Alloys", "Magnets", "Lighting (arc lamps)"],
    },
    60: {
        "name": "Neodymium",
        "symbol": "Nd",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 60,
        "discovery": {
            "discoverer": "Carl Auer von Welsbach",
            "year": 1885,
            "notes": "Separated from praseodymium; named after the Greek words for 'new twin.'"
        },
        "physical_properties": {
            "atomic_mass": {"value": 144.242, "units": [('amu', 1)], "notes": "Dominated by isotope Nd-142."},
            "density": {"value": 7.01, "units": [('kg', 1), ('m', -3)], "notes": "Hard, rare-earth metal."},
            "melting_point": {"value": 1297, "units": [('K', 1)], "notes": "Essential for modern magnets."},
            "boiling_point": {"value": 3347, "units": [('K', 1)], "notes": "Useful for lasers and glass coloring."},
        },
        "electron_configuration": "[Xe] 4f⁴ 6s²",
        "common_uses": ["Magnets", "Lasers", "Glass coloring"],
    },
    61: {
        "name": "Promethium",
        "symbol": "Pm",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 61,
        "discovery": {
            "discoverer": "Jacob A. Marinsky, Lawrence E. Glendenin, and Charles D. Coryell",
            "year": 1945,
            "notes": "First isolated from nuclear fission products; named after Prometheus."
        },
        "physical_properties": {
            "atomic_mass": {"value": 145, "units": [('amu', 1)], "notes": "Only radioactive isotopes exist."},
            "density": {"value": 7.26, "units": [('kg', 1), ('m', -3)], "notes": "Radioactive rare-earth metal."},
            "melting_point": {"value": 1315, "units": [('K', 1)], "notes": "Used in luminous paints."},
            "boiling_point": {"value": 3273, "units": [('K', 1)], "notes": "Rare and used in specialized applications."},
        },
        "electron_configuration": "[Xe] 4f⁵ 6s²",
        "common_uses": ["Luminous paints", "Nuclear batteries", "Research"],
    },
    62: {
        "name": "Samarium",
        "symbol": "Sm",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 62,
        "discovery": {
            "discoverer": "Paul-Émile Lecoq de Boisbaudran",
            "year": 1879,
            "notes": "Discovered in samarskite mineral; named after Colonel Samarski."
        },
        "physical_properties": {
            "atomic_mass": {"value": 150.36, "units": [('amu', 1)], "notes": "Dominated by isotope Sm-152."},
            "density": {"value": 7.52, "units": [('kg', 1), ('m', -3)], "notes": "Dense rare-earth metal."},
            "melting_point": {"value": 1345, "units": [('K', 1)], "notes": "Useful for magnets and nuclear applications."},
            "boiling_point": {"value": 2067, "units": [('K', 1)], "notes": "Applications in high-performance alloys."},
        },
        "electron_configuration": "[Xe] 4f⁶ 6s²",
        "common_uses": ["Magnets", "Nuclear reactors", "Spectroscopy"],
    },
    63: {
        "name": "Europium",
        "symbol": "Eu",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 63,
        "discovery": {
            "discoverer": "Eugène-Anatole Demarçay",
            "year": 1896,
            "notes": "Named after the continent Europe."
        },
        "physical_properties": {
            "atomic_mass": {"value": 151.964, "units": [('amu', 1)], "notes": "Dominated by isotope Eu-153."},
            "density": {"value": 5.24, "units": [('kg', 1), ('m', -3)], "notes": "Soft rare-earth metal."},
            "melting_point": {"value": 1099, "units": [('K', 1)], "notes": "Used in phosphorescent materials."},
            "boiling_point": {"value": 1802, "units": [('K', 1)], "notes": "Applications in display technologies."},
        },
        "electron_configuration": "[Xe] 4f⁷ 6s²",
        "common_uses": ["Phosphorescent compounds", "CRT displays", "Lasers"],
    },
    64: {
        "name": "Gadolinium",
        "symbol": "Gd",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 64,
        "discovery": {
            "discoverer": "Jean Charles Galissard de Marignac",
            "year": 1880,
            "notes": "Named after the mineral gadolinite."
        },
        "physical_properties": {
            "atomic_mass": {"value": 157.25, "units": [('amu', 1)], "notes": "Dominated by isotope Gd-158."},
            "density": {"value": 7.90, "units": [('kg', 1), ('m', -3)], "notes": "Magnetic rare-earth metal."},
            "melting_point": {"value": 1585, "units": [('K', 1)], "notes": "Used in MRI contrast agents."},
            "boiling_point": {"value": 3546, "units": [('K', 1)], "notes": "Applications in nuclear reactors and alloys."},
        },
        "electron_configuration": "[Xe] 4f⁷ 5d¹ 6s²",
        "common_uses": ["MRI contrast agents", "Magnets", "Nuclear reactors"],
    },
    65: {
        "name": "Terbium",
        "symbol": "Tb",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 65,
        "discovery": {
            "discoverer": "Carl Gustaf Mosander",
            "year": 1843,
            "notes": "Named after the village Ytterby, Sweden."
        },
        "physical_properties": {
            "atomic_mass": {"value": 158.925, "units": [('amu', 1)], "notes": "Dominated by isotope Tb-159."},
            "density": {"value": 8.23, "units": [('kg', 1), ('m', -3)], "notes": "Rare-earth metal with high density."},
            "melting_point": {"value": 1629, "units": [('K', 1)], "notes": "Useful for phosphors and magnets."},
            "boiling_point": {"value": 3500, "units": [('K', 1)], "notes": "Applications in electronic devices."},
        },
        "electron_configuration": "[Xe] 4f⁹ 6s²",
        "common_uses": ["Phosphors", "Magnets", "Electronic devices"],
    },
    66: {
        "name": "Dysprosium",
        "symbol": "Dy",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 66,
        "discovery": {
            "discoverer": "Paul-Émile Lecoq de Boisbaudran",
            "year": 1886,
            "notes": "Named after the Greek word 'dysprositos' (hard to get)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 162.500, "units": [('amu', 1)], "notes": "Dominated by isotope Dy-164."},
            "density": {"value": 8.54, "units": [('kg', 1), ('m', -3)], "notes": "Soft, lustrous rare-earth metal."},
            "melting_point": {"value": 1680, "units": [('K', 1)], "notes": "Used in magnetic applications."},
            "boiling_point": {"value": 2840, "units": [('K', 1)], "notes": "Applications in high-performance magnets."},
        },
        "electron_configuration": "[Xe] 4f¹⁰ 6s²",
        "common_uses": ["Magnets", "Nuclear reactors", "Lasers"],
    },
    67: {
        "name": "Holmium",
        "symbol": "Ho",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 67,
        "discovery": {
            "discoverer": "Marc Delafontaine and Jacques-Louis Soret",
            "year": 1878,
            "notes": "Named after Stockholm, Sweden (Latin: Holmia)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 164.930, "units": [('amu', 1)], "notes": "Dominated by isotope Ho-165."},
            "density": {"value": 8.80, "units": [('kg', 1), ('m', -3)], "notes": "Magnetic rare-earth metal."},
            "melting_point": {"value": 1734, "units": [('K', 1)], "notes": "Used in magnets and nuclear control rods."},
            "boiling_point": {"value": 2993, "units": [('K', 1)], "notes": "Applications in magnetic devices and lasers."},
        },
        "electron_configuration": "[Xe] 4f¹¹ 6s²",
        "common_uses": ["Magnets", "Nuclear control rods", "Lasers"],
    },
 68: {
        "name": "Erbium",
        "symbol": "Er",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 68,
        "discovery": {
            "discoverer": "Carl Gustaf Mosander",
            "year": 1843,
            "notes": "Named after the village Ytterby, Sweden."
        },
        "physical_properties": {
            "atomic_mass": {"value": 167.259, "units": [('amu', 1)], "notes": "Dominated by isotope Er-166."},
            "density": {"value": 9.06, "units": [('kg', 1), ('m', -3)], "notes": "Rare-earth metal with moderate density."},
            "melting_point": {"value": 1802, "units": [('K', 1)], "notes": "Used in lasers and nuclear technology."},
            "boiling_point": {"value": 3141, "units": [('K', 1)], "notes": "Applications in optical fibers and alloys."},
        },
        "electron_configuration": "[Xe] 4f¹² 6s²",
        "common_uses": ["Lasers", "Optical fibers", "Nuclear reactors"],
    },
    69: {
        "name": "Thulium",
        "symbol": "Tm",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 69,
        "discovery": {
            "discoverer": "Per Teodor Cleve",
            "year": 1879,
            "notes": "Named after 'Thule,' an ancient name for Scandinavia."
        },
        "physical_properties": {
            "atomic_mass": {"value": 168.934, "units": [('amu', 1)], "notes": "Dominated by isotope Tm-169."},
            "density": {"value": 9.32, "units": [('kg', 1), ('m', -3)], "notes": "Dense, lustrous rare-earth metal."},
            "melting_point": {"value": 1818, "units": [('K', 1)], "notes": "Used in portable X-ray devices."},
            "boiling_point": {"value": 2223, "units": [('K', 1)], "notes": "Applications in nuclear technology."},
        },
        "electron_configuration": "[Xe] 4f¹³ 6s²",
        "common_uses": ["Portable X-ray devices", "Nuclear reactors", "Lasers"],
    },
    70: {
        "name": "Ytterbium",
        "symbol": "Yb",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 70,
        "discovery": {
            "discoverer": "Jean Charles Galissard de Marignac",
            "year": 1878,
            "notes": "Named after the village Ytterby, Sweden."
        },
        "physical_properties": {
            "atomic_mass": {"value": 173.045, "units": [('amu', 1)], "notes": "Dominated by isotope Yb-174."},
            "density": {"value": 6.90, "units": [('kg', 1), ('m', -3)], "notes": "Soft, rare-earth metal."},
            "melting_point": {"value": 1097, "units": [('K', 1)], "notes": "Applications in atomic clocks and lasers."},
            "boiling_point": {"value": 1469, "units": [('K', 1)], "notes": "Useful in alloy production and electronics."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 6s²",
        "common_uses": ["Atomic clocks", "Alloys", "Lasers"],
    },
    71: {
        "name": "Lutetium",
        "symbol": "Lu",
        "group": "Lanthanide",
        "period": 6,
        "atomic_number": 71,
        "discovery": {
            "discoverer": "Georges Urbain",
            "year": 1907,
            "notes": "Named after Lutetia, the ancient name for Paris."
        },
        "physical_properties": {
            "atomic_mass": {"value": 174.966, "units": [('amu', 1)], "notes": "Dominated by isotope Lu-175."},
            "density": {"value": 9.84, "units": [('kg', 1), ('m', -3)], "notes": "Hard, dense rare-earth metal."},
            "melting_point": {"value": 1936, "units": [('K', 1)], "notes": "Used in catalysts and nuclear applications."},
            "boiling_point": {"value": 3675, "units": [('K', 1)], "notes": "Applications in medical imaging."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d¹ 6s²",
        "common_uses": ["Catalysts", "Medical imaging", "Nuclear reactors"],
    },
    72: {
        "name": "Hafnium",
        "symbol": "Hf",
        "group": 4,
        "period": 6,
        "atomic_number": 72,
        "discovery": {
            "discoverer": "Dirk Coster and George de Hevesy",
            "year": 1923,
            "notes": "Named after Hafnia, the Latin name for Copenhagen."
        },
        "physical_properties": {
            "atomic_mass": {"value": 178.49, "units": [('amu', 1)], "notes": "Dominated by isotope Hf-180."},
            "density": {"value": 13.31, "units": [('kg', 1), ('m', -3)], "notes": "Dense transition metal."},
            "melting_point": {"value": 2506, "units": [('K', 1)], "notes": "Used in nuclear control rods."},
            "boiling_point": {"value": 4876, "units": [('K', 1)], "notes": "Applications in high-temperature alloys."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d² 6s²",
        "common_uses": ["Nuclear control rods", "High-temperature alloys", "Semiconductors"],
    },
    73: {
        "name": "Tantalum",
        "symbol": "Ta",
        "group": 5,
        "period": 6,
        "atomic_number": 73,
        "discovery": {
            "discoverer": "Anders Gustaf Ekeberg",
            "year": 1802,
            "notes": "Named after Tantalus from Greek mythology."
        },
        "physical_properties": {
            "atomic_mass": {"value": 180.947, "units": [('amu', 1)], "notes": "Dominated by isotope Ta-181."},
            "density": {"value": 16.69, "units": [('kg', 1), ('m', -3)], "notes": "Dense, corrosion-resistant metal."},
            "melting_point": {"value": 3290, "units": [('K', 1)], "notes": "Used in electronics and medical implants."},
            "boiling_point": {"value": 5731, "units": [('K', 1)], "notes": "Useful in extreme-temperature environments."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d³ 6s²",
        "common_uses": ["Capacitors", "Medical implants", "High-temperature alloys"],
    },
    74: {
        "name": "Tungsten",
        "symbol": "W",
        "group": 6,
        "period": 6,
        "atomic_number": 74,
        "discovery": {
            "discoverer": "Fausto and Juan José Elhuyar",
            "year": 1783,
            "notes": "Isolated from wolframite; known for its high density and strength."
        },
        "physical_properties": {
            "atomic_mass": {"value": 183.84, "units": [('amu', 1)], "notes": "Dominated by isotope W-184."},
            "density": {"value": 19.25, "units": [('kg', 1), ('m', -3)], "notes": "Extremely dense and strong metal."},
            "melting_point": {"value": 3695, "units": [('K', 1)], "notes": "Highest melting point of any metal."},
            "boiling_point": {"value": 5828, "units": [('K', 1)], "notes": "Useful in high-temperature applications."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d⁴ 6s²",
        "common_uses": ["Light bulb filaments", "Alloys", "Aerospace applications"],
    },
    75: {
        "name": "Rhenium",
        "symbol": "Re",
        "group": 7,
        "period": 6,
        "atomic_number": 75,
        "discovery": {
            "discoverer": "Ida Noddack, Walter Noddack, and Otto Berg",
            "year": 1925,
            "notes": "Discovered in platinum ores; named after the Rhine River."
        },
        "physical_properties": {
            "atomic_mass": {"value": 186.207, "units": [('amu', 1)], "notes": "Dominated by isotope Re-187."},
            "density": {"value": 21.02, "units": [('kg', 1), ('m', -3)], "notes": "Third densest element."},
            "melting_point": {"value": 3459, "units": [('K', 1)], "notes": "Useful in high-temperature turbine blades."},
            "boiling_point": {"value": 5869, "units": [('K', 1)], "notes": "Applications in extreme heat environments."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d⁵ 6s²",
        "common_uses": ["Turbine blades", "Catalysts", "Electrical contacts"],
    },
    76: {
        "name": "Osmium",
        "symbol": "Os",
        "group": 8,
        "period": 6,
        "atomic_number": 76,
        "discovery": {
            "discoverer": "Smithson Tennant",
            "year": 1804,
            "notes": "Discovered in platinum residues; named for its strong odor ('osme' in Greek)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 190.23, "units": [('amu', 1)], "notes": "Dominated by isotope Os-192."},
            "density": {"value": 22.59, "units": [('kg', 1), ('m', -3)], "notes": "Densest natural element."},
            "melting_point": {"value": 3306, "units": [('K', 1)], "notes": "Used in specialized high-strength alloys."},
            "boiling_point": {"value": 5285, "units": [('K', 1)], "notes": "Useful for durable industrial applications."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d⁶ 6s²",
        "common_uses": ["Alloys", "Fountain pen tips", "Electrical contacts"],
    },
    77: {
        "name": "Iridium",
        "symbol": "Ir",
        "group": 9,
        "period": 6,
        "atomic_number": 77,
        "discovery": {
            "discoverer": "Smithson Tennant",
            "year": 1803,
            "notes": "Discovered alongside osmium; named for its colorful salts ('iris' in Greek)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 192.217, "units": [('amu', 1)], "notes": "Dominated by isotope Ir-193."},
            "density": {"value": 22.56, "units": [('kg', 1), ('m', -3)], "notes": "Second densest element."},
            "melting_point": {"value": 2719, "units": [('K', 1)], "notes": "Useful for high-temperature environments."},
            "boiling_point": {"value": 4701, "units": [('K', 1)], "notes": "Applications in durable alloys."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d⁷ 6s²",
        "common_uses": ["Alloys", "Spark plugs", "Spacecraft components"],
    },
    78: {
        "name": "Platinum",
        "symbol": "Pt",
        "group": 10,
        "period": 6,
        "atomic_number": 78,
        "discovery": {
            "discoverer": "Pre-Columbian South Americans",
            "year": None,
            "notes": "Known in ancient times; named 'platina' (little silver) by Spanish explorers."
        },
        "physical_properties": {
            "atomic_mass": {"value": 195.084, "units": [('amu', 1)], "notes": "Dominated by isotope Pt-195."},
            "density": {"value": 21.45, "units": [('kg', 1), ('m', -3)], "notes": "Dense, corrosion-resistant metal."},
            "melting_point": {"value": 2041.4, "units": [('K', 1)], "notes": "Widely used in jewelry and catalysts."},
            "boiling_point": {"value": 4098, "units": [('K', 1)], "notes": "Applications in electronics and medicine."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d⁹ 6s¹",
        "common_uses": ["Jewelry", "Catalysts", "Medical equipment"],
    },
    79: {
        "name": "Gold",
        "symbol": "Au",
        "group": 11,
        "period": 6,
        "atomic_number": 79,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; prized for its beauty and rarity."
        },
        "physical_properties": {
            "atomic_mass": {"value": 196.967, "units": [('amu', 1)], "notes": "Dominated by isotope Au-197."},
            "density": {"value": 19.32, "units": [('kg', 1), ('m', -3)], "notes": "Dense, malleable metal."},
            "melting_point": {"value": 1337.33, "units": [('K', 1)], "notes": "Used in electronics and jewelry."},
            "boiling_point": {"value": 3129, "units": [('K', 1)], "notes": "Corrosion-resistant under high temperatures."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s¹",
        "common_uses": ["Jewelry", "Electronics", "Currency"],
    },
    80: {
        "name": "Mercury",
        "symbol": "Hg",
        "group": 12,
        "period": 6,
        "atomic_number": 80,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; named 'hydrargyrum' for its liquid state."
        },
        "physical_properties": {
            "atomic_mass": {"value": 200.592, "units": [('amu', 1)], "notes": "Dominated by isotope Hg-202."},
            "density": {"value": 13.53, "units": [('kg', 1), ('m', -3)], "notes": "Liquid at room temperature."},
            "melting_point": {"value": 234.32, "units": [('K', 1)], "notes": "Low melting point for metals."},
            "boiling_point": {"value": 629.88, "units": [('K', 1)], "notes": "Used in thermometers and barometers."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s²",
        "common_uses": ["Thermometers", "Barometers", "Lighting"],
    },
    81: {
        "name": "Thallium",
        "symbol": "Tl",
        "group": 13,
        "period": 6,
        "atomic_number": 81,
        "discovery": {
            "discoverer": "William Crookes",
            "year": 1861,
            "notes": "Discovered via spectroscopy; named for its green spectral lines ('thallos' in Greek)."
        },
        "physical_properties": {
            "atomic_mass": {"value": 204.38, "units": [('amu', 1)], "notes": "Dominated by isotope Tl-205."},
            "density": {"value": 11.85, "units": [('kg', 1), ('m', -3)], "notes": "Soft and highly toxic metal."},
            "melting_point": {"value": 577, "units": [('K', 1)], "notes": "Low melting point for a heavy metal."},
            "boiling_point": {"value": 1730, "units": [('K', 1)], "notes": "Applications in electronics and optics."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹",
        "common_uses": ["Optics", "Electronics", "Medical imaging"],
    },
    82: {
        "name": "Lead",
        "symbol": "Pb",
        "group": 14,
        "period": 6,
        "atomic_number": 82,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; widely used in plumbing and construction."
        },
        "physical_properties": {
            "atomic_mass": {"value": 207.2, "units": [('amu', 1)], "notes": "Dominated by isotope Pb-208."},
            "density": {"value": 11.34, "units": [('kg', 1), ('m', -3)], "notes": "Dense and soft metal."},
            "melting_point": {"value": 600.61, "units": [('K', 1)], "notes": "Low melting point for a heavy metal."},
            "boiling_point": {"value": 2022, "units": [('K', 1)], "notes": "Applications in batteries and radiation shielding."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²",
        "common_uses": ["Batteries", "Radiation shielding", "Plumbing"],
    },
    83: {
        "name": "Bismuth",
        "symbol": "Bi",
        "group": 15,
        "period": 6,
        "atomic_number": 83,
        "discovery": {
            "discoverer": "Prehistoric",
            "year": None,
            "notes": "Known since ancient times; thought to be stable but faintly radioactive."
        },
        "physical_properties": {
            "atomic_mass": {"value": 208.980, "units": [('amu', 1)], "notes": "Dominated by isotope Bi-209."},
            "density": {"value": 9.78, "units": [('kg', 1), ('m', -3)], "notes": "Brittle, lustrous metal."},
            "melting_point": {"value": 544.7, "units": [('K', 1)], "notes": "Used in low-melting-point alloys."},
            "boiling_point": {"value": 1837, "units": [('K', 1)], "notes": "Applications in medical and industrial uses."},
        },
        "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³",
        "common_uses": ["Alloys", "Medical treatments", "Cosmetics"],
    },
}
