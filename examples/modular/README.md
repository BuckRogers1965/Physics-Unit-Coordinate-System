
## The road map to this directory

The parent directy loads these modules and data from the ```../../data_sets``` directly in order to process the data and generate outputs.


```
tree .
.
├── print_outputs.py                Module to generate rescaled constants in different formats
├── print_periodic_table.py         Scales the value of the periodic table to various unit systems
├── print_rescaling.py              Scales the physical constants to new unit systems
├── README.md                       This file
├── rescale_units.py
└── unit_scaling                    The directory where the units are organized
    ├── atomic_electron_scaling.py  Scales to natural units and then scales the electron mass so it is 1.0
    ├── imperial_scaling.py         Scales from SI to imperial
    ├── natural_scaling.py          Scales from SI to natural units by using contants as scaling factors
    ├── README.md
    ├── si_scaling.py               Scales from SI to SI, a base scaling where it is all 1 to 1
    └── time_scaling.py             Scales the second so you can see the effect on all the units

4 directories, 26 files
```

