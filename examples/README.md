**Physics Unit Coordinate System**

This project takes the Modular Unit Scaling Factors to the next level.

We collect all the unit scalings into a single data structure that we can
apply to scale the complete coordinates of a unit system allowing us to
see that all a unit system is is another scaled version of each other.

What this means is that there is only a single unit system that is merely
scaled in unit coordinate space to a specific set of values.

c, h, and k are the specific vectors that reflecting the distance the meter, 
kg, and temperature scales are away from natural units where

``` 1 K = 1 f = 1 kg = 1 J ```

**Example Directory Tree**
```
├── load_mods.py                        A shim to load the modular parts
├── modular                             This holds the modular parts
│   ├── print_periodic_table.py         The module to conver the periodic table
│   ├── print_rescaling.py              The module to convert the constants
│   ├── rescale_units.py                The module that converts the units
│   └── unit_scaling                    The specific sets of coordinates 
│       ├── atomic_electron_scaling.py
│       ├── imperial_scaling.py
│       ├── natural_scaling.py
│       ├── si_scaling.py
│       └── time_scaling.py
├── natural_units.py                    The non modular version to convert constants
├── physics_unit_coordinate_scaling.py  Converts contants to new unit system
├── print_constants_formatted.py        Outputs constants in different formats
├── print_periodic_table.py             Shows how to process the periodit table
└── README.md                           You are here.

```


The examples are:  

- **physics_unit_coordinate_scaling.py**
- **print_constants_formatted.py**
- **print_periodic_table.py**

physics_unit_coordinate_scaling.py converts a set of the constants in the ```../data_sets/constnats.py```

print_constants_formatted.py outputs constants in differnt formats from the ```../data_sets/constnats.py```

print_periodic_table.py converts a set of the elements in the ```../data_sets/periodic_table.py```

These two programs are written in a modular way to allow easy updates.

**natural_units.py** is an older version that is not as uptodate as the modular version.
