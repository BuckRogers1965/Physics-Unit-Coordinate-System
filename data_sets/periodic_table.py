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

}
