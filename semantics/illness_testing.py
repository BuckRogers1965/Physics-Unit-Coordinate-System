import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns


"""
================================================================================
 White-Box Geometric Medical Diagnostic Engine
================================================================================

Author: J. Rogers
Date: June 2025 (Updated for Iterative Diagnosis)

--- High-Level Overview ---

This program implements a novel, white-box approach to medical diagnosis that is
fundamentally different from traditional expert systems or modern black-box AI.
Instead of relying on brittle if-then rules or opaque statistical models, this
engine operates on a clear, geometric interpretation of medical knowledge.

Core Principles:
----------------
1.  **Illness as a Geometric Space:** Each fundamental symptom and diagnostic
    test result represents an orthogonal axis (a basis vector).

2.  **Disease as a Vector:** Each known disease is defined as a specific point or
    vector within this space, representing the characteristic pattern and
    expected results of symptoms and tests.

3.  **Diagnosis as Iterative Pruning & Similarity:**
    a.  **Rule-Based Exclusion:** Applying hard-coded "rule-out" or "rule-in"
        criteria based on definitive test results (geometric pruning).
    b.  **Similarity Calculation:** For remaining plausible diseases, finding the
        most closely aligned vector using cosine similarity.
    c.  **Test Recommendation & Iteration:** When ambiguity exists (e.g., close
        similarity scores), the system recommends specific tests to further
        differentiate or rule out conditions. It then integrates new test data
        and re-diagnoses, iteratively "zooming in" on the answer.

Architectural Advantages:
-------------------------
*   **Explainability:** Fully transparent ("white-box"). Provides quantitative
    breakdown of symptom/test contributions.
*   **Data-Independence:** Knowledge base from established medical consensus.
*   **Maintainability & Scalability:** Trivial data entry for new diseases/tests.
*   **Robustness:** Handles partial, vague, and overlapping profiles.
*   **Expandability:** New diseases/tests added by defining their vectors.
*   **Inclusion of Definitive Tests:** Explicitly integrates lab/imaging results.
*   **Dynamic Diagnostic Strategy:** Proactively suggests next steps to narrow
    the differential, mirroring clinical workflow.

Limitations (Updated)
--------------------
*   **Symptom/Test Granularity:** Assumes discrete, scalar values; doesn't model
    complex temporal patterns or more nuanced findings.
*   **Comorbidity Interactions:** Still treats diseases as independent attractors.
*   **Context-Free Encoding:** All features are independent dimensions.
*   **Incomplete Disease Coverage:** Limited by the richness and correctness of the KB.
*   **No Localization or Demographics:** No adjustment for age, sex, geography.
*   **Confidence Thresholds for Exclusion:** Rule-out values are currently binary. Could be probabilistic.
*   **Automated Dimensional Expansion (Future):** Proposing entirely *new* conceptual axes is still a human input. This module relies on pre-defined axes.

================================================================================
"""

# ==============================================================================
# The Single Source of Truth: Expanded to ~40 Conditions + Test Axes
# Test axes added: troponin_elevated, ekg_st_elevation, d_dimer_elevated, ct_angiogram_pe, etc.
# Values for tests: 1.0 for "positive/present", 0.0 for "negative/absent"
# ==============================================================================
DISEASE_KNOWLEDGE_BASE = {
    # Common Viral/Bacterial
    'common_cold': {
        "symptoms": {'fever': 0.2, 'cough': 0.7, 'fatigue': 0.4, 'headache': 0.3, 'runny_nose': 0.9, 'sore_throat': 0.8, 'sneezing': 0.8},
        "tests": {'strep_test_positive': 0.0, 'covid_test_positive': 0.0, 'flu_test_positive': 0.0},
        "metadata": {"icd11": "CA00", "common_name": "Common Cold", "type": "Viral"}
    },
    'flu': {
        "symptoms": {'fever': 0.9, 'cough': 0.8, 'fatigue': 0.9, 'headache': 0.8, 'muscle_aches': 0.9, 'runny_nose': 0.5, 'sore_throat': 0.6, 'chills': 0.9},
        "tests": {'flu_test_positive': 1.0, 'covid_test_positive': 0.0, 'strep_test_positive': 0.0},
        "metadata": {"icd11": "1E31", "common_name": "Influenza", "type": "Viral"}
    },
    'covid19': {
        "symptoms": {'fever': 0.8, 'cough': 0.8, 'fatigue': 0.8, 'headache': 0.6, 'muscle_aches': 0.5, 'sore_throat': 0.5, 'shortness_of_breath': 0.7, 'loss_of_taste_smell': 0.9},
        "tests": {'covid_test_positive': 1.0, 'flu_test_positive': 0.0, 'strep_test_positive': 0.0},
        "metadata": {"icd11": "RA01.0", "common_name": "COVID-19", "type": "Viral"}
    },
    'strep_throat': {
        "symptoms": {'fever': 0.8, 'fatigue': 0.5, 'headache': 0.6, 'sore_throat': 0.9, 'swollen_glands': 0.9, 'difficulty_swallowing': 0.8, 'white_patches_on_tonsils': 0.7},
        "tests": {'strep_test_positive': 1.0, 'flu_test_positive': 0.0, 'covid_test_positive': 0.0},
        "metadata": {"icd11": "1B81", "common_name": "Strep Throat", "type": "Bacterial"}
    },
    'mono': {
        "symptoms": {'fever': 0.7, 'fatigue': 0.9, 'headache': 0.7, 'muscle_aches': 0.6, 'sore_throat': 0.9, 'loss_of_appetite': 0.8, 'swollen_glands': 0.9},
        "tests": {'mono_spot_test_positive': 1.0},
        "metadata": {"icd11": "1D8Z", "common_name": "Mononucleosis", "type": "Viral"}
    },
    # Respiratory
    'pneumonia': {
        "symptoms": {'fever': 0.9, 'cough': 0.9, 'fatigue': 0.8, 'shortness_of_breath': 0.9, 'chest_pain': 0.8, 'chills': 0.9, 'confusion': 0.4},
        "tests": {'chest_xray_infiltrates': 1.0, 'wbc_elevated': 0.8},
        "metadata": {"icd11": "CA40", "common_name": "Pneumonia", "type": "Infection"}
    },
    'bronchitis': {
        "symptoms": {'cough': 0.9, 'fatigue': 0.6, 'sore_throat': 0.5, 'shortness_of_breath': 0.5, 'chest_pain': 0.6, 'chills': 0.4, 'wheezing': 0.7},
        "tests": {'chest_xray_infiltrates': 0.0}, # No infiltrates typically
        "metadata": {"icd11": "CA20", "common_name": "Bronchitis", "type": "Infection/Irritation"}
    },
    'sinusitis': {
        "symptoms": {'fever': 0.3, 'cough': 0.5, 'fatigue': 0.4, 'headache': 0.8, 'runny_nose': 0.9, 'sore_throat': 0.6, 'facial_pain_pressure': 0.9},
        "tests": {},
        "metadata": {"icd11": "CA04", "common_name": "Sinusitis", "type": "Infection/Inflammation"}
    },
    'asthma': {
        "symptoms": {'cough': 0.7, 'shortness_of_breath': 0.9, 'chest_pain': 0.7, 'wheezing': 0.9},
        "tests": {'spirometry_obstruction': 1.0},
        "metadata": {"icd11": "CA23", "common_name": "Asthma", "type": "Chronic Respiratory"}
    },
    'tuberculosis': {
        "symptoms": {'fever': 0.7, 'cough': 0.9, 'fatigue': 0.8, 'chest_pain': 0.7, 'chills': 0.7, 'loss_of_appetite': 0.8, 'night_sweats': 0.9, 'weight_loss': 0.8},
        "tests": {'chest_xray_cavitary_lesions': 1.0, 'acid_fast_bacilli_positive': 1.0},
        "metadata": {"icd11": "1B11", "common_name": "Tuberculosis", "type": "Bacterial"}
    },
    # Digestive
    'gastroenteritis': {
        "symptoms": {'fever': 0.4, 'fatigue': 0.7, 'nausea': 0.9, 'muscle_aches': 0.5, 'diarrhea': 0.9, 'vomiting': 0.9, 'abdominal_pain': 0.8},
        "tests": {'stool_culture_positive': 0.5}, # Can be viral or bacterial
        "metadata": {"icd11": "1A01", "common_name": "Gastroenteritis (Stomach Flu)", "type": "Infection/Irritation"}
    },
    'food_poisoning': {
        "symptoms": {'fever': 0.3, 'fatigue': 0.6, 'headache': 0.5, 'nausea': 0.9, 'diarrhea': 0.9, 'vomiting': 0.9, 'abdominal_pain': 0.9, 'chills': 0.6},
        "tests": {'stool_culture_positive': 0.8},
        "metadata": {"icd11": "1A00", "common_name": "Food Poisoning", "type": "Bacterial/Toxin"}
    },
    'appendicitis': {
        "symptoms": {'fever': 0.6, 'nausea': 0.8, 'vomiting': 0.7, 'abdominal_pain': 0.9, 'loss_of_appetite': 0.9, 'constipation': 0.5},
        "tests": {'wbc_elevated': 0.9, 'ct_abd_pelvis_inflammation': 1.0},
        "metadata": {"icd11": "DC10", "common_name": "Appendicitis", "type": "Acute Medical"}
    },
    'crohns_disease': {
        "symptoms": {'fever': 0.5, 'fatigue': 0.8, 'diarrhea': 0.8, 'abdominal_pain': 0.8, 'joint_pain': 0.5, 'loss_of_appetite': 0.7, 'weight_loss': 0.8},
        "tests": {'colonoscopy_inflammation': 1.0, 'calprotectin_elevated': 1.0},
        "metadata": {"icd11": "DD70", "common_name": "Crohn's Disease", "type": "Autoimmune/Chronic"}
    },
    'pancreatic_cancer': {
        "symptoms": {'fatigue': 0.8, 'nausea': 0.6, 'abdominal_pain': 0.8, 'jaundice': 0.7, 'loss_of_appetite': 0.9, 'weight_loss': 0.9, 'back_pain': 0.7},
        "tests": {'ct_abd_pelvis_mass': 1.0, 'ca19_9_elevated': 0.9},
        "metadata": {"icd11": "2C10", "common_name": "Pancreatic Cancer", "type": "Oncology"}
    },
    # Neurological / Systemic
    'migraine': {
        "symptoms": {'fatigue': 0.7, 'headache': 0.9, 'nausea': 0.8, 'vomiting': 0.2, 'dizziness': 0.8, 'sensitivity_to_light': 0.9},
        "tests": {'mri_brain_normal': 1.0, 'csf_culture_positive': 0.0}, # Rules out serious causes
        "metadata": {"icd11": "8A80", "common_name": "Migraine", "type": "Neurological"}
    },
    'meningitis': {
        "symptoms": {'fever': 0.9, 'fatigue': 0.8, 'headache': 0.9, 'nausea': 0.7, 'vomiting': 0.6, 'dizziness': 0.8, 'chills': 0.9, 'stiff_neck': 0.9, 'sensitivity_to_light': 0.8},
        "tests": {'csf_culture_positive': 1.0, 'lumbar_puncture_abnormal': 1.0, 'mri_brain_normal': 0.0}, # Rule out structural issue if LP is for inf.
        "metadata": {"icd11": "1D01", "common_name": "Meningitis", "type": "Acute Medical"}
    },
    'lyme_disease': {
        "symptoms": {'fever': 0.7, 'fatigue': 0.8, 'headache': 0.8, 'muscle_aches': 0.8, 'joint_pain': 0.9, 'skin_rash': 0.8, 'chills': 0.8, 'swollen_glands': 0.7},
        "tests": {'lyme_antibody_positive': 1.0},
        "metadata": {"icd11": "1C15", "common_name": "Lyme Disease", "type": "Bacterial"}
    },
    'anemia': {
        "symptoms": {'fatigue': 0.9, 'headache': 0.5, 'shortness_of_breath': 0.6, 'chest_pain': 0.4, 'dizziness': 0.9, 'chills': 0.7, 'pale_skin': 0.8},
        "tests": {'hgb_low': 1.0},
        "metadata": {"icd11": "3A00", "common_name": "Anemia", "type": "Hematological"}
    },
    'lupus': {
        "symptoms": {'fever': 0.7, 'fatigue': 0.9, 'headache': 0.6, 'muscle_aches': 0.7, 'shortness_of_breath': 0.4, 'chest_pain': 0.5, 'joint_pain': 0.8, 'skin_rash': 0.8, 'loss_of_appetite': 0.5, 'swollen_glands': 0.6, 'hair_loss': 0.5},
        "tests": {'ana_positive': 1.0, 'anti_dsdna_positive': 1.0},
        "metadata": {"icd11": "4A40", "common_name": "Lupus", "type": "Autoimmune"}
    },
    'diabetes_type1': {
        "symptoms": {'fatigue': 0.8, 'nausea': 0.4, 'vomiting': 0.3, 'abdominal_pain': 0.3, 'weight_loss': 0.7, 'increased_thirst': 0.9, 'frequent_urination': 0.9, 'blurred_vision': 0.6},
        "tests": {'blood_glucose_high': 1.0, 'hba1c_high': 1.0, 'autoantibodies_positive': 1.0},
        "metadata": {"icd11": "5A10", "common_name": "Diabetes Mellitus, Type 1", "type": "Endocrine"}
    },
    # Acute Emergencies
    'heart_attack': {
        "symptoms": {'fatigue': 0.4, 'nausea': 0.5, 'shortness_of_breath': 0.8, 'chest_pain': 0.9, 'vomiting': 0.2, 'dizziness': 0.7, 'chills': 0.5, 'arm_pain': 0.7},
        "tests": {'troponin_elevated': 1.0, 'ekg_st_elevation': 1.0},
        "metadata": {"icd11": "BA41", "common_name": "Myocardial Infarction (Heart Attack)", "type": "Cardiovascular Emergency"}
    },
    # Heart Attack Mimics
    'angina': {
        "symptoms": {'chest_pain': 0.9, 'shortness_of_breath': 0.6, 'fatigue': 0.5, 'dizziness': 0.4},
        "tests": {'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0, 'stress_test_abnormal': 1.0},
        "metadata": {"icd11": "BA40", "common_name": "Stable Angina", "type": "Cardiovascular"}
    },
    'gerd': {
        "symptoms": {'chest_pain': 0.7, 'nausea': 0.5, 'vomiting': 0.3, 'dizziness': 0.2},
        "tests": {'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0, 'upper_endoscopy_esophagitis': 1.0},
        "metadata": {"icd11": "DA64", "common_name": "Gastroesophageal Reflux Disease (GERD)", "type": "Gastrointestinal"}
    },
    'panic_attack': {
        "symptoms": {'chest_pain': 0.6, 'shortness_of_breath': 0.5, 'dizziness': 0.6, 'nausea': 0.4, 'confusion': 0.4},
        "tests": {'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0, 'anxiety_assessment_high': 1.0},
        "metadata": {"icd11": "MB23", "common_name": "Panic Attack", "type": "Psychological"}
    },
    'pericarditis': {
        "symptoms": {'chest_pain': 0.8, 'shortness_of_breath': 0.5, 'fatigue': 0.4, 'fever': 0.4},
        "tests": {'ekg_pr_depression': 1.0, 'troponin_elevated': 0.3}, # Troponin can be mildly elevated
        "metadata": {"icd11": "BA50", "common_name": "Pericarditis", "type": "Cardiovascular Inflammatory"}
    },
    'pulmonary_embolism': {
        "symptoms": {'chest_pain': 0.8, 'shortness_of_breath': 0.9, 'dizziness': 0.6, 'cough': 0.4, 'nausea': 0.3},
        "tests": {'d_dimer_elevated': 1.0, 'ct_angiogram_pe': 1.0, 'troponin_elevated': 0.0}, # No primary troponin elevation
        "metadata": {"icd11": "BD10", "common_name": "Pulmonary Embolism", "type": "Respiratory Emergency"}
    },
    'costochondritis': {
        "symptoms": {'chest_pain': 0.8},
        "tests": {'chest_wall_tenderness': 1.0, 'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0},
        "metadata": {"icd11": "FA01", "common_name": "Costochondritis", "type": "Musculoskeletal"}
    },
    'gallbladder_disease': {
        "symptoms": {'chest_pain': 0.5, 'nausea': 0.7, 'vomiting': 0.6, 'fatigue': 0.4},
        "tests": {'ultrasound_gallstones': 1.0, 'liver_enzymes_elevated': 0.7},
        "metadata": {"icd11": "DC52", "common_name": "Cholelithiasis (Gallbladder Disease)", "type": "Gastrointestinal"}
    },
    'aortic_dissection': {
        "symptoms": {'chest_pain': 0.9, 'arm_pain': 0.7, 'dizziness': 0.5, 'fatigue': 0.4},
        "tests": {'ct_aorta_dissection': 1.0, 'pulse_deficit': 1.0, 'troponin_elevated': 0.0}, # No primary troponin elevation
        "metadata": {"icd11": "BA60", "common_name": "Aortic Dissection", "type": "Vascular Emergency"}
    },
    'stroke': {
        "symptoms": {'fatigue': 0.5, 'headache': 0.8, 'nausea': 0.4, 'vomiting': 0.3, 'dizziness': 0.8, 'confusion': 0.8, 'difficulty_swallowing': 0.6, 'facial_drooping': 0.9, 'arm_weakness': 0.9, 'speech_difficulty': 0.9},
        "tests": {'mri_brain_infarct': 1.0, 'ct_brain_hemorrhage': 1.0}, # Or hemorrhage
        "metadata": {"icd11": "8B20", "common_name": "Stroke", "type": "Neurological Emergency"}
    },
    # Cancers
    'lung_cancer': {
        "symptoms": {'cough': 0.8, 'fatigue': 0.7, 'shortness_of_breath': 0.7, 'chest_pain': 0.7, 'loss_of_appetite': 0.6, 'weight_loss': 0.7, 'hoarseness': 0.5},
        "tests": {'chest_ct_mass': 1.0, 'biopsy_malignant': 1.0},
        "metadata": {"icd11": "2C25", "common_name": "Lung Cancer", "type": "Oncology"}
    },
    # Classic Infectious Diseases
    'measles': {
        "symptoms": {'fever': 0.9, 'cough': 0.8, 'runny_nose': 0.8, 'sore_throat': 0.6, 'skin_rash': 0.9, 'conjunctivitis': 0.8, 'koplik_spots': 0.9},
        "tests": {'measles_igm_positive': 1.0},
        "metadata": {"icd11": "1F03", "common_name": "Measles", "type": "Viral"}
    },
    'mumps': {
        "symptoms": {'fever': 0.8, 'fatigue': 0.7, 'headache': 0.6, 'muscle_aches': 0.6, 'loss_of_appetite': 0.7, 'swollen_glands': 0.9, 'jaw_pain': 0.8},
        "tests": {'mumps_igm_positive': 1.0},
        "metadata": {"icd11": "1F00", "common_name": "Mumps", "type": "Viral"}
    },
    'smallpox': { # Historical disease
        "symptoms": {'fever': 0.9, 'fatigue': 0.9, 'headache': 0.9, 'nausea': 0.6, 'muscle_aches': 0.8, 'vomiting': 0.7, 'back_pain': 0.8, 'skin_rash': 0.9},
        "tests": {'smallpox_pcr_positive': 1.0},
        "metadata": {"icd11": "1E61", "common_name": "Smallpox", "type": "Viral (Eradicated)"}
    },

    # Rare Conditions

    'fabry_disease': {
        "symptoms": {'burning_pain_limbs': 0.8, 'abdominal_pain': 0.6, 'fatigue': 0.7, 'nausea': 0.5, 'rash': 0.4, 'kidney_dysfunction': 0.7},
        "tests": {'alpha_gal_a_low': 1.0, 'genetic_test_gla_mutation': 1.0},
        "metadata": {"icd11": "5C51", "common_name": "Fabry Disease", "type": "Genetic Metabolic"}
    },
    
    'ehlers_danlos': {
        "symptoms": {'joint_hypermobility': 0.9, 'skin_hyperextensibility': 0.8, 'easy_bruising': 0.6, 'fatigue': 0.5},
        "tests": {'beighton_score_high': 1.0, 'genetic_test_collagen_mutation': 1.0},
        "metadata": {"icd11": "LD90", "common_name": "Ehlers-Danlos Syndrome", "type": "Connective Tissue Disorder"}
    },

    'amyloidosis': {
        "symptoms": {'fatigue': 0.8, 'weight_loss': 0.6, 'peripheral_neuropathy': 0.7, 'chest_pain': 0.4, 'shortness_of_breath': 0.5},
        "tests": {'biopsy_amyloid_deposits': 1.0, 'serum_free_light_chain_abnormal': 1.0},
        "metadata": {"icd11": "4A43", "common_name": "Amyloidosis", "type": "Protein Misfolding Disorder"}
    },

    'sarcoidosis': {
        "symptoms": {'fatigue': 0.7, 'cough': 0.6, 'chest_pain': 0.5, 'rash': 0.6, 'eye_inflammation': 0.5},
        "tests": {'chest_xray_hilar_lymphadenopathy': 1.0, 'biopsy_non_caseating_granulomas': 1.0},
        "metadata": {"icd11": "4A40", "common_name": "Sarcoidosis", "type": "Inflammatory Granulomatous"}
    },

    'takayasu_arteritis': {
        "symptoms": {'arm_pain': 0.7, 'dizziness': 0.6, 'fatigue': 0.6, 'chest_pain': 0.5, 'weak_pulses': 0.9},
        "tests": {'mra_aorta_narrowing': 1.0, 'esr_crp_elevated': 1.0},
        "metadata": {"icd11": "4A44.0", "common_name": "Takayasu Arteritis", "type": "Large Vessel Vasculitis"}
    },

    'brugada_syndrome': {
        "symptoms": {'syncope': 0.9, 'chest_pain': 0.5, 'sudden_cardiac_arrest': 0.9, 'dizziness': 0.6},
        "tests": {'ekg_brugada_pattern': 1.0, 'genetic_test_scn5a_mutation': 1.0},
        "metadata": {"icd11": "BA81.0", "common_name": "Brugada Syndrome", "type": "Cardiac Channelopathy"}
    },

    'stiff_person_syndrome': {
        "symptoms": {'muscle_rigidity': 0.9, 'muscle_spasms': 0.8, 'anxiety': 0.5, 'startle_response': 0.9},
        "tests": {'anti_gad_antibody_positive': 1.0, 'emg_continuous_motor_unit_activity': 1.0},
        "metadata": {"icd11": "8B61.0", "common_name": "Stiff Person Syndrome", "type": "Neurological Autoimmune"}
    },
    
    'kawasaki_disease': {
        "symptoms": {'fever': 0.9, 'rash': 0.7, 'conjunctivitis': 0.8, 'swollen_lymph_nodes': 0.6, 'fatigue': 0.5},
        "tests": {'crp_elevated': 1.0, 'echo_coronary_aneurysm': 1.0},
        "metadata": {"icd11": "1A26", "common_name": "Kawasaki Disease", "type": "Pediatric Vasculitis"}
    },
    
    'wilsons_disease': {
        "symptoms": {'tremor': 0.7, 'fatigue': 0.6, 'liver_dysfunction': 0.8, 'psychiatric_symptoms': 0.5, 'abdominal_pain': 0.6},
        "tests": {'serum_ceruloplasmin_low': 1.0, 'urine_copper_high': 1.0, 'kayser_fleischer_rings': 1.0},
        "metadata": {"icd11": "5C70", "common_name": "Wilson's Disease", "type": "Genetic Metabolic"}
    },
    
    'addisons_disease': {
        "symptoms": {'fatigue': 0.9, 'hypotension': 0.8, 'hyperpigmentation': 0.7, 'salt_craving': 0.6, 'nausea': 0.5},
        "tests": {'cortisol_low': 1.0, 'acth_high': 1.0},
        "metadata": {"icd11": "5A71", "common_name": "Addison’s Disease", "type": "Endocrine (Adrenal Insufficiency)"}
    }
}


class WhiteBoxMedicalDiagnostic:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        all_features = set() # Combined symptoms and tests
        for disease_data in self.kb.values():
            all_features.update(disease_data["symptoms"].keys())
            all_features.update(disease_data.get("tests", {}).keys()) # Include test keys
        self.features = sorted(list(all_features)) # Renamed from 'symptoms' to 'features'
        
        self.disease_vectors = {}
        for disease_name, disease_data in self.kb.items():
            vector = np.zeros(len(self.features))
            # Add symptoms to vector
            for symptom, value in disease_data["symptoms"].items():
                if symptom in self.features:
                    idx = self.features.index(symptom)
                    vector[idx] = value
            # Add tests to vector
            for test, value in disease_data.get("tests", {}).items():
                if test in self.features:
                    idx = self.features.index(test)
                    vector[idx] = value
            self.disease_vectors[disease_name] = vector

        # Define explicit rule-out/rule-in criteria for tests
        # Format: {disease_name: {test_name: required_value (0.0 for negative, 1.0 for positive)}}
        self.definitive_test_rules = {
            'heart_attack': {'troponin_elevated': 1.0, 'ekg_st_elevation': 1.0},
            'pulmonary_embolism': {'ct_angiogram_pe': 1.0, 'troponin_elevated': 0.0}, # ADDED troponin_elevated: 0.0
            'stroke': {'mri_brain_infarct': 1.0, 'ct_brain_hemorrhage': 1.0},
            'appendicitis': {'ct_abd_pelvis_inflammation': 1.0},
            'meningitis': {'csf_culture_positive': 1.0},
            'strep_throat': {'strep_test_positive': 1.0},
            'covid19': {'covid_test_positive': 1.0},
            'flu': {'flu_test_positive': 1.0},
            'pneumonia': {'chest_xray_infiltrates': 1.0},
            'tuberculosis': {'acid_fast_bacilli_positive': 1.0},
            'anemia': {'hgb_low': 1.0},
            'lupus': {'ana_positive': 1.0, 'anti_dsdna_positive': 1.0},
            'diabetes_type1': {'blood_glucose_high': 1.0, 'hba1c_high': 1.0},
            'aortic_dissection': {'ct_aorta_dissection': 1.0, 'troponin_elevated': 0.0}, # ADDED troponin_elevated: 0.0
            'lung_cancer': {'biopsy_malignant': 1.0},
            'measles': {'measles_igm_positive': 1.0},
            'mumps': {'mumps_igm_positive': 1.0},
            'smallpox': {'smallpox_pcr_positive': 1.0},
            'fabry_disease': {'genetic_test_gla_mutation': 1.0},
            'ehlers_danlos': {'genetic_test_collagen_mutation': 1.0},
            'amyloidosis': {'biopsy_amyloid_deposits': 1.0},
            'sarcoidosis': {'biopsy_non_caseating_granulomas': 1.0},
            'takayasu_arteritis': {'mra_aorta_narrowing': 1.0},
            'brugada_syndrome': {'ekg_brugada_pattern': 1.0},
            'stiff_person_syndrome': {'anti_gad_antibody_positive': 1.0},
            'kawasaki_disease': {'echo_coronary_aneurysm': 1.0},
            'wilsons_disease': {'urine_copper_high': 1.0},
            'addisons_disease': {'cortisol_low': 1.0, 'acth_high': 1.0},
            # Negative exclusions (test MUST be 0.0 to be considered)
            'bronchitis': {'chest_xray_infiltrates': 0.0},
            'migraine': {'mri_brain_normal': 1.0, 'csf_culture_positive': 0.0}, 
            'gerd': {'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0},
            'panic_attack': {'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0},
            'costochondritis': {'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0},
        }

        # Define test recommendations for each disease, ordered by priority/impact
        self.test_recommendations = {
            'panic_attack': [('anxiety_assessment_high', 'psychological_evaluation')],
            'pulmonary_embolism': [('d_dimer_elevated', 'blood_test'), ('ct_angiogram_pe', 'imaging_scan')],
            'angina': [('stress_test_abnormal', 'cardiac_test')],
            'aortic_dissection': [('ct_aorta_dissection', 'imaging_scan'), ('pulse_deficit', 'physical_exam_finding')],
            'gerd': [('upper_endoscopy_esophagitis', 'endoscopy')],
            'pericarditis': [('ekg_pr_depression', 'ekg'), ('echo_pericardial_effusion', 'imaging_scan')],
            'costochondritis': [('chest_wall_tenderness', 'physical_exam_finding')],
            'gallbladder_disease': [('ultrasound_gallstones', 'imaging_scan')],
            'sinusitis': [('ct_sinuses_inflammation', 'imaging_scan')], # Hypothetical for demo
            # Add more for other diseases as needed...
        }

    def encode_patient_features(self, patient_features):
        feature_vector = np.zeros(len(self.features))
        for feature, intensity in patient_features.items():
            if feature in self.features:
                idx = self.features.index(feature)
                feature_vector[idx] = intensity
        return feature_vector

    def apply_definitive_rules(self, patient_features):
        """
        Applies rule-in/rule-out criteria based on specific test results.
        Returns a list of diseases that are NOT ruled out.
        """
        possible_diagnoses = list(self.kb.keys())
        ruled_out_diagnoses = set()

        for disease_name, rules in self.definitive_test_rules.items():
            is_ruled_out = False
            
            # Skip diseases not in our possible list (if the full KB is larger than actual rules)
            if disease_name not in possible_diagnoses:
                continue

            for test_name, required_value in rules.items():
                patient_test_value = patient_features.get(test_name, None) # None if test not provided

                # If the test is explicitly required (e.g., troponin_elevated for MI)
                if required_value == 1.0:
                    if test_name in patient_features: # Test result was explicitly provided
                        if patient_test_value < 0.9: # Patient's test is negative/low, but disease requires positive
                            is_ruled_out = True
                            # print(f"  RULE-OUT (POSITIVE REQ): {disease_name} by {test_name} (Patient: {patient_test_value:.1f}, Required: {required_value})")
                            break 
                    # else: # Test required but not provided - CANNOT definitively rule out on absence for now
                    #     pass # Keep it plausible for now, wait for more data

                # If the test must be negative (e.g., no infiltrates for Bronchitis)
                elif required_value == 0.0:
                    if test_name in patient_features: # Test result was explicitly provided
                        if patient_test_value > 0.1: # Patient's test is positive/high, but disease requires negative
                            is_ruled_out = True
                            # print(f"  RULE-OUT (NEGATIVE REQ): {disease_name} by {test_name} (Patient: {patient_test_value:.1f}, Required: {required_value})")
                            break
                    # else: # Test required to be negative but not provided - CANNOT definitively rule out on absence for now
                    #     pass # Keep it plausible for now

            if is_ruled_out:
                ruled_out_diagnoses.add(disease_name)
        
        # print(f"Ruled out diagnoses: {ruled_out_diagnoses}") # For debugging
        return [d for d in possible_diagnoses if d not in ruled_out_diagnoses]


    def diagnose(self, patient_features, top_n=5, verbose=False):
        patient_vector = self.encode_patient_features(patient_features)
        if np.linalg.norm(patient_vector) == 0: return []

        # Step 1: Apply definitive rules to prune the list of possibilities
        plausible_diagnoses = self.apply_definitive_rules(patient_features)
        
        similarities = {}
        for disease_name in plausible_diagnoses:
            disease_vector = self.disease_vectors[disease_name]
            # Ensure vectors are not zero vectors before calculating similarity
            if np.linalg.norm(patient_vector) > 0 and np.linalg.norm(disease_vector) > 0:
                similarity = cosine_similarity([patient_vector], [disease_vector])[0][0]
                similarities[disease_name] = similarity
            else:
                similarities[disease_name] = 0.0 # If either vector is zero, similarity is zero

        sorted_diagnoses = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_diagnoses[:top_n]

    def recommend_tests(self, current_differential, patient_features_current_state): # Added patient_features_current_state
        """
        Recommends tests to differentiate between diseases in the current differential.
        Prioritizes tests that are likely to confirm/rule out high-similarity diseases
        and have a defined recommendation in self.test_recommendations.
        Avoids recommending tests already provided in patient_features_current_state.
        """
        recommended_tests = []
        for disease, similarity in current_differential:
            if disease in self.test_recommendations:
                for test_name, test_type in self.test_recommendations[disease]:
                    # Avoid recommending tests already known (or implicitly ruled out if they were definitive)
                    if test_name not in patient_features_current_state: # Check if test result is already present
                        recommended_tests.append((test_name, test_type, disease, similarity))
        
        # Prioritize based on disease similarity (highest first)
        recommended_tests.sort(key=lambda x: x[3], reverse=True)
        
        # Remove duplicates while maintaining order
        unique_recommendations = []
        seen_tests = set()
        for test, test_type, disease, similarity in recommended_tests:
            if test not in seen_tests:
                unique_recommendations.append((test, test_type, disease, similarity))
                seen_tests.add(test)
        
        return unique_recommendations[:3] # Recommend top 3 unique tests


    def explain_diagnosis(self, patient_features, diagnosis):
        if diagnosis not in self.kb:
            print(f"Explanation for '{diagnosis}' cannot be provided (not in knowledge base).")
            return
        
        patient_vector = self.encode_patient_features(patient_features)
        disease_vector = self.disease_vectors[diagnosis]
        metadata = self.kb[diagnosis].get('metadata', {})
        
        print(f"\n--- Explanation for {diagnosis.upper()} ---")
        if metadata:
            print(f"  Common Name: {metadata.get('common_name', 'N/A')}, ICD-11 Code: {metadata.get('icd11', 'N/A')}, Type: {metadata.get('type', 'N/A')}")
        
        print("Feature contributions (Patient Feature Value * Disease Pattern Value):")
        contributions = []
        for i, feature in enumerate(self.features):
            patient_val = patient_vector[i]
            if patient_val > 0: # Only show features present in the patient
                disease_val = disease_vector[i]
                contribution = patient_val * disease_val
                contributions.append((feature, patient_val, disease_val, contribution))
        
        contributions.sort(key=lambda x: x[3], reverse=True)
        for feature, patient_val, disease_val, contribution in contributions:
            print(f"  - {feature:<25} | Patient: {patient_val:.1f}, Disease Pattern: {disease_val:.1f} -> Contribution: {contribution:.2f}")

        # Add explicit check for definitive rule applications (for explanation)
        rules_applied = []
        for disease_name, rules in self.definitive_test_rules.items():
            if disease_name == diagnosis: # Only check rules for the final diagnosis
                for test_name, required_value in rules.items():
                    patient_test_value = patient_features.get(test_name, None)
                    if patient_test_value is not None:
                        if required_value == 1.0 and patient_test_value >= 0.9:
                            rules_applied.append(f"Confirmed by {test_name} (Patient: {patient_test_value:.1f}, Required: >=0.9)")
                        elif required_value == 0.0 and patient_test_value <= 0.1:
                            rules_applied.append(f"Not ruled out by {test_name} (Patient: {patient_test_value:.1f}, Required: <=0.1)")
        if rules_applied:
            print("\nDefinitive Rule Applications for this Diagnosis:")
            for rule in rules_applied:
                print(f"  - {rule}")


class TestHarness:
    def __init__(self, diagnostic_system):
        self.diagnostics = diagnostic_system
        self.diseases = list(diagnostic_system.kb.keys())

    def create_archetypal_patient(self, disease_name):
        archetype_features = {}
        disease_data = self.diagnostics.kb[disease_name]
        archetype_features.update(disease_data["symptoms"])
        archetype_features.update(disease_data.get("tests", {}))
        return archetype_features

    def run_full_test(self):
        # ... (unchanged from previous version) ...
        print("="*60)
        print("           RUNNING DIAGNOSTIC SYSTEM TEST HARNESS (V4)")
        print("="*60)
        
        correct_top_1 = 0
        total_tests = len(self.diseases)
        confusion_matrix = {d: {d2: 0 for d2 in self.diseases} for d in self.diseases}

        for disease in self.diseases:
            archetype_features = self.create_archetypal_patient(disease)
            diagnoses = self.diagnostics.diagnose(archetype_features, top_n=1)
            
            top_diagnosis = diagnoses[0][0] if diagnoses else "N/A"
            if top_diagnosis == disease:
                correct_top_1 += 1
            if top_diagnosis != "N/A":
                confusion_matrix[disease][top_diagnosis] += 1
        
        accuracy = (correct_top_1 / total_tests) * 100 if total_tests > 0 else 0
        print(f"Top-1 Accuracy: {correct_top_1}/{total_tests} = {accuracy:.2f}%\n")
        return confusion_matrix

    def plot_confusion_matrix(self, matrix, filename="diagnostic_confusion_matrix_v4.png"):
        # ... (unchanged from previous version) ...
        print(f"Generating and saving confusion matrix to '{filename}'...")
        labels = self.diseases
        matrix_array = np.array([[matrix[d1][d2] for d2 in labels] for d1 in labels])

        plt.figure(figsize=(24, 22)) # Increased size for more diseases
        sns.heatmap(matrix_array, annot=True, fmt='d', cmap='viridis', 
                    xticklabels=labels, yticklabels=labels)
        plt.xlabel('Predicted Diagnosis', fontsize=14)
        plt.ylabel('True Disease (Archetype)', fontsize=14)
        plt.title('Diagnostic System Confusion Matrix (V4)', fontsize=16)
        plt.xticks(rotation=75, ha='right', fontsize=9)
        plt.yticks(rotation=0, fontsize=9)
        plt.tight_layout()
        
        try:
            plt.savefig(filename, dpi=300)
            print(f"Plot successfully saved as '{filename}'")
        except Exception as e:
            print(f"Error saving plot: {e}")
        
        plt.close()


# --- Main Execution ---
if __name__ == "__main__":
    diagnostic_system = WhiteBoxMedicalDiagnostic(DISEASE_KNOWLEDGE_BASE)
    
    # --- INDIVIDUAL DIAGNOSIS DEMO (ITERATIVE REFINEMENT) ---
    print("\n" + "="*60)
    print("                 ITERATIVE DIAGNOSIS DEMO (ZOOMING IN)")
    print("="*60)
    
    # Initial patient features (symptoms of heart attack mimic, no tests yet)
    patient_features_current_state = {
        'chest_pain': 0.9,
        'shortness_of_breath': 0.7,
        'arm_pain': 0.6,
        'nausea': 0.5,
        'dizziness': 0.6
    }

    print("--- STEP 1: Initial Presentation (No Tests) ---")
    print("Patient features:", patient_features_current_state)
    current_differential = diagnostic_system.diagnose(patient_features_current_state, top_n=5)
    print("\nInitial Differential Diagnosis (Top 5):")
    for d, s in current_differential:
        print(f"  - {d:<20} (Similarity: {s:.3f})")
    
    # Simulate Executive LLM recommending tests based on current differential
    recommended_tests_step1 = diagnostic_system.recommend_tests(current_differential, patient_features_current_state)
    if recommended_tests_step1:
        print("\nSystem recommends tests to differentiate:")
        for test, test_type, disease, sim in recommended_tests_step1:
            print(f"  - {test} ({test_type}) for {disease} (current sim: {sim:.3f})")

    # --- STEP 2: Patient reports negative cardiac tests (e.g., after ED visit) ---
    print("\n" + "="*60)
    print("--- STEP 2: Patient reports negative cardiac tests (ruling out MI/Angina/Pericarditis/Aortic Dissection) ---")
    patient_features_current_state.update({
        'troponin_elevated': 0.0,
        'ekg_st_elevation': 0.0,
        'ekg_pr_depression': 0.0, # Rule out Pericarditis too
        'ct_aorta_dissection': 0.0, # Rule out Aortic Dissection
        'pulse_deficit': 0.0
    })
    print("Updated patient features:", patient_features_current_state)
    current_differential = diagnostic_system.diagnose(patient_features_current_state, top_n=5)
    print("\nDifferential Diagnosis (Top 5, after ruling out cardiac emergencies):")
    for d, s in current_differential:
        print(f"  - {d:<20} (Similarity: {s:.3f})")

    recommended_tests_step2 = diagnostic_system.recommend_tests(current_differential, patient_features_current_state)
    if recommended_tests_step2:
        print("\nSystem recommends further tests:")
        for test, test_type, disease, sim in recommended_tests_step2:
            print(f"  - {test} ({test_type}) for {disease} (current sim: {sim:.3f})")
    else:
        print("\nNo further specific test recommendations from this differential for available tests.")

    # --- STEP 3: Patient undergoes D-dimer, which is elevated (still ambiguity) ---
    print("\n" + "="*60)
    print("--- STEP 3: Patient undergoes D-dimer, which is elevated (still ambiguity) ---")
    patient_features_current_state.update({
        'd_dimer_elevated': 1.0 # Elevated D-dimer, keeping PE on the list
    })
    print("Updated patient features:", patient_features_current_state)
    current_differential = diagnostic_system.diagnose(patient_features_current_state, top_n=5)
    print("\nDifferential Diagnosis (Top 5, after D-dimer):")
    for d, s in current_differential:
        print(f"  - {d:<20} (Similarity: {s:.3f})")
    
    recommended_tests_step3 = diagnostic_system.recommend_tests(current_differential, patient_features_current_state)
    if recommended_tests_step3:
        print("\nSystem recommends further tests:")
        for test, test_type, disease, sim in recommended_tests_step3:
            print(f"  - {test} ({test_type}) for {disease} (current sim: {sim:.3f})")
    else:
        print("\nNo further specific test recommendations from this differential for available tests.")

    # --- STEP 4: Patient undergoes CT Angiogram, which is negative (ruling out PE) ---
    print("\n" + "="*60)
    print("--- STEP 4: Patient undergoes CT Angiogram, which is negative (ruling out PE) ---")
    patient_features_current_state.update({
        'ct_angiogram_pe': 0.0 # CT Angio negative, ruling out PE
    })
    print("Updated patient features:", patient_features_current_state)
    current_differential = diagnostic_system.diagnose(patient_features_current_state, top_n=5)
    print("\nDifferential Diagnosis (Top 5, after ruling out PE):")
    for d, s in current_differential:
        print(f"  - {d:<20} (Similarity: {s:.3f})")

    recommended_tests_step4 = diagnostic_system.recommend_tests(current_differential, patient_features_current_state)
    if recommended_tests_step4:
        print("\nSystem recommends further tests:")
        for test, test_type, disease, sim in recommended_tests_step4:
            print(f"  - {test} ({test_type}) for {disease} (current sim: {sim:.3f})")
    else:
        print("\nNo further specific test recommendations from this differential for available tests.")

    # --- STEP 5: Patient has clear anxiety (Confirming Panic Attack) ---
    print("\n" + "="*60)
    print("--- STEP 5: Patient has clear anxiety (Confirming Panic Attack) ---")
    patient_features_current_state.update({
        'anxiety_assessment_high': 1.0 # Confirms panic attack
    })
    print("Updated patient features:", patient_features_current_state)
    final_diagnoses = diagnostic_system.diagnose(patient_features_current_state, top_n=5)
    print("\nFinal Differential Diagnosis (Top 5, after confirming Panic Attack):")
    for d, s in final_diagnoses:
        print(f"  - {d:<20} (Similarity: {s:.3f})")
    
    if final_diagnoses:
        diagnostic_system.explain_diagnosis(patient_features_current_state, final_diagnoses[0][0])
