## The road map to this directory

This directory hold the unit scaling from SI to other units.

```
tree .
.
└── unit_scaling                    The directory where the units are organized
    ├── atomic_electron_scaling.py  Scales to natural units and then scales the electron mass so it is 1.0
    ├── imperial_scaling.py         Scales from SI to imperial
    ├── natural_scaling.py          Scales from SI to natural units by using contants as scaling factors
    ├── README.md
    ├── si_scaling.py               Scales from SI to SI, a base scaling where it is all 1 to 1
    └── time_scaling.py             Scales the second so you can see the effect on all the units

4 directories, 26 files
```


What we need to do is create base unit scaling corrdinates all realtive to the natural units and scale from natural units to a particlular definition of units in a system.

We should be able to handle composite units without tearing them into base units. 
