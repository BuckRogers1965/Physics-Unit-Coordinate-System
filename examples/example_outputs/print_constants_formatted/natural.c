/* PHYSICS_UNIT_COORDINATE_SYSTEM.h */
#ifndef PUCS_PHYSICS_CONSTANTS_H
#define PUCS_PHYSICS_CONSTANTS_H

/*   --- Scaling Factors Used ---
s          -> 1.00000000000000000000e+00 -> s_n       
m          -> 2.99792458000000000000e+08 -> m_n       
kg         -> 7.37249732381270843547e-51 -> kg_n      
K          -> 4.79924307336622100516e-11 -> K_n       
C          -> 1.60217663399999989376e-19 -> C_n       
A          -> 1.60217663399999989376e-19 -> A_n       
mol        -> 1.66053906717384659585e-24 -> mol_n     
pi         -> 3.14159265358979311600e+00 -> pi_n      
Hz         -> 1.00000000000000000000e+00 -> Hz_n      
amu        -> 4.43982166520664990202e-24 -> kg_n      
*/


#define c                                    1.0 /* speed_of_light_c               m_n s_n^-1 */
#define h                                    1.0 /* planck_constant_h              kg_n m_n^2 s_n^-1 */
#define Hz_kg                 0.9999999999996326 /* Hz_kg                          kg_n Hz_n */
#define k                     0.9999999999999998 /* boltzmann_constant_k           kg_n m_n^2 s_n^-2 K_n^-1 */
#define K_Hz                  1.0000000000001164 /* K_Hz                           Hz_n K_n^-1 */
#define R                     0.9999999999815693 /* molar_gas_constant_R           kg_n m_n^2 s_n^-2 mol_n^-1 K_n^-1 */
#define R_K                   0.9999999996395389 /* klitzing_constant_Rk           kg_n m_n^2 s_n^-1 C_n^-2 */
#define Φ₀                     0.499999999888306 /* magnetic_flux_quantum_Phi0     kg_n m_n^2 s_n^-1 C_n^-1 */
#define F                     0.9999999999656941 /* faraday_constant_F             mol_n^-1 C_n */
#define K_J                   1.9999999999297615 /* josephson_constant_KJ          kg_n^-1 m_n^-2 s_n C_n */
#define G₀                    1.9999999997770679 /* conductance_quantum_G0         kg_n^-1 m_n^-2 s_n C_n^2 */
#define c_1                   1.9999999998969695 /* first radiation constant       kg_n m_n^4 s_n^-3 pi_n */
#define c_1L                   1.999999999333041 /* first radiation constant sr    kg_n m_n^4 s_n^-3 */
#define c_2                   1.0000000000667695 /* second_radiation_constant_c2   m_n K_n */
#define 1 kg               1.356392489652132e+50 /* 1 kg                           kg_n */
#define 1 m               3.3356409519815204e-09 /* 1 meter                        m_n */
#define 1 s                                  1.0 /* 1 second                       s_n */
#define Hz                                   1.0 /* 1 Hz                           s_n^-1 */
#define A                  0.0011614097322526476 /* Amp force                      kg_n m_n s_n^-2 A_n^-2 */
#define A                  4.524438335443822e+34 /* Amp force scaled in alpha      kg_n m_n s_n^-2 A_old^-2 */
#define J                 1.5091901796421518e+33 /* 1 J                            kg_n m_n^2 s_n^-2 */
#define e                                    1.0 /* elementary_charge_e            C_n */
#define Na                    0.9999999999999999 /* avogadro_constant_Na           mol_n^-1 */
#define me                 1.235589963807414e+20 /* electron_mass_me               kg_n */
#define m_{π^±}           3.3747966133045517e+22 /* pion_charged_mass_pi_pm        kg_n */
#define m_{π^0}            3.263724752029665e+22 /* pion_neutral_mass_pi0          kg_n */
#define m_μ                2.554808152885061e+22 /* muon_mass_mu                   kg_n */
#define m_τ               4.2963325191984383e+23 /* tau_mass_tau                   kg_n */
#define m_{Λ^0}           2.6970236985745062e+23 /* lambda_baryon_mass_Lambda0     kg_n */
#define mp                2.2687318153206176e+23 /* proton_mass_mp                 kg_n */
#define mn                 2.271859079053292e+23 /* neutron_mass_mn                kg_n */
#define u                 2.2523427187102014e+23 /* atomic_mass_unit_u             kg_n */
#define m_H                3.027522292603145e+25 /* Higgs_boson_mass_H             kg_n */
#define m_Z                2.204910939403816e+25 /* Z_boson_mass_Z                 kg_n */
#define m_W               1.9432899559997127e+25 /* W_boson_mass_W                 kg_n */
#define l_P                5.391246366844893e-44 /* planck_length_lP               m_n */
#define t_P                         5.391247e-44 /* planck_time                    s_n */
#define m_P               2.9520987318235486e+42 /* planck_mass                    kg_n */
#define T_P               2.9520988588024534e+42 /* planck_temperature             K_n */
#define l_S                4.603184513734498e-42 /* stoney_length_lS               m_n */
#define t_S                              4.6e-43 /* stoney_time_tS                 s_n */
#define m_S               2.5093261058564442e+41 /* stoney_mass_mS                 kg_n */
#define T_S                3.000473153759171e+42 /* stoney_temperature_TS          K_n */
#define eV                       1.602176634e-19 /* electronvolts_to_energy_EeV    J */
#define l_n                9.399637152312884e-24 /* natural_length_ln              m_n */
#define t_n                     9.3132257462e-24 /* natural_time_tn                s_n */
#define G                 1.8262416298105014e-86 /* gravitational_constant_G       m_n^3 kg_n^-1 s_n^-2 */
#define k_e                0.0011614097322050704 /* coulombs_constant_k_e          kg_n m_n^3 s_n^-2 C_n^-2 */
#define ε₀                     68.51799954205417 /* vacuum_permittivity_epsilon0   C_n^2 kg_n^-1 m_n^-3 s_n^2 */
#define μ₀                  0.014594705138555429 /* vacuum_permeability_mu0        kg_n m_n s_n^-2 C_n^-2 */
#define Z_0                  0.01459470512868229 /* character impedance vacuum     kg_n m_n^2 s_n^-1 C_n^-2 */
#define [ε₀]_au            5.673566034269007e-73 /* atomic unit of permittivity    m_n^-3 kg_n^-1 s_n^-4 C_n^-2 */
#define E_h                   6579683920296256.0 /* hartree_energy_Eh              kg_n m_n^2 s_n^-2 */
#define μ_B                6.440443340944591e-22 /* bohr_magneton_muB              m_n^2 s_n^-1 C_n */
#define μ_N               3.5075750694120227e-25 /* nuclear_magneton_muN           m_n^2 s_n^-1 C_n */
#define λ_e_C              8.093299794319709e-21 /* electron_compton_wavelength    m_n */
#define λ_n_C              4.401681465282225e-24 /* neutron Compton wavelength     m_n */
#define b                    0.20140523525977205 /* Wien wl d law                  m_n K_n */
#define R_inf                 3289841960250881.0 /* rydberg infinite               m_n^-1 */
#define r_e                9.399637152312884e-24 /* electron_radius_re             m_n */
#define a₀                1.7651451755434086e-19 /* bohr_radius_a0                 m_n */
#define Å_star            3.3356908198137523e-19 /* Angstrom star                  m_n */
#define σ                     40.802624636710405 /* stefan_boltzmann_constant_sigma kg_n s_n^-3 K_n^-4 */
#define g₀                 3.271146334174958e-08 /* standard_gravity_g0            m_n s_n^-2 */
#define κ                 4.0466498916998256e-21 /* quantum of circulation         m_n^2 s_n^-1 */
#define Λ                  9.803621489661207e-36 /* cosmological_constant_Lambda   m_n^-2 */

#endif /* PUCS PHYSICS_CONSTANTS_H */
