import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns


"""
================================================================================
 White-Box Geometric Medical Diagnostic Engine
================================================================================

Author: J. Rogers
Date: June 2025

--- High-Level Overview ---

This program implements a novel, white-box approach to medical diagnosis that is
fundamentally different from traditional expert systems or modern black-box AI.
Instead of relying on brittle if-then rules or opaque statistical models, this
engine operates on a clear, geometric interpretation of medical knowledge.

Modern diagnostic tools often suffer from a trade-off between complexity,
accuracy, and transparency. This model's goal is to correct these limitations.

Core Principles:
----------------
1.  **Illness as a Geometric Space:** The system defines a multi-dimensional
    "illness space" where each fundamental symptom (e.g., 'fever', 'cough')
    represents an orthogonal axis (a basis vector).

2.  **Disease as a Vector:** Each known disease is defined as a specific point or
    vector within this space. The vector's components represent the
    characteristic pattern and intensity of symptoms for that disease. The
    entire medical knowledge of the system is contained in these vectors.

3.  **Diagnosis as a Measurement of Similarity:** A patient's reported symptoms are
    also converted into a vector in the same space. The diagnostic process is
    then reduced to a simple, deterministic geometric calculation: finding the
    disease vector that is most closely aligned with the patient's vector.
    This "rotational similarity" is calculated using the cosine similarity metric.

4.  **Rotational Similarity as Cosine of the Angle Between Vectors:** The similarity
    between a patient's symptoms and a disease pattern is calculated using cosine
    similarity, a geometric measure that reflects the cosine of the angle between
    the two vectors. A score of 1.0 implies perfect alignment (identical direction),
    while a score near 0 implies orthogonality (no meaningful overlap). This provides
    an intuitive, mathematically grounded measure of how closely a disease explains
    the observed symptoms.

Architectural Advantages:
-------------------------
*   **Explainability:** The system is 100% transparent ("white-box"). For any
    diagnosis, it can provide a precise, quantitative breakdown of which
    symptoms contributed most to the result, making its reasoning fully
    auditable.

*   **Data-Independence:** Unlike machine learning models, this engine does not
    require training on massive, private patient datasets. Its knowledge base
    is built directly from established medical consensus (e.g., textbook
    definitions), making it immune to data bias and privacy concerns.

*   **Maintainability & Scalability:** The knowledge base is separated from the
    core logic. Adding a new disease or symptom is a trivial data entry task
    that does not require retraining or complex rule debugging. The system
    discovers the dimensional space and builds its vectors programmatically.

*   **Robustness:** The geometric approach gracefully handles partial, vague,
    and overlapping symptom profiles, providing a nuanced differential
    diagnosis with clear confidence scores (the similarity metric) rather than
    a single, brittle answer.

*   **Expandability:** New diseases are added by defining their symptom vectors—
    no model retraining required.

This script includes the diagnostic engine itself, a test harness to verify its
accuracy against archetypal cases, and a demonstration of its use in a real-world
diagnostic scenario.


Limitations
-----------
*   **Similar Symptom Overlap:**  Is chest pain like chest pressure, is skin
    redness the same as rash? 

*   **Severity Scaling:**  We would need clinical scales to rate the amount of
    each symptom in a systematic way that does not vary from one doctor's office
    to the next.

*   **Comorbidity Interactions:** The system currently treats diseases as
    independent attractors. It doesn't yet model comorbid blends (e.g., COPD +
    CHF), which can produce nonlinear presentations.

*   **Temporal Evolution of Symptoms:** The model assumes a static symptom snapshot.
    It doesn't account for time-course (e.g., sudden vs. gradual onset), which is often
    key in triage decisions.

*   **Testing Feedback Loop (WIP):** While designed for test-based pruning, the engine
    doesn't yet implement dynamic updates as labs return or new symptoms emerge.

*   **Context-Free Symptom Encoding:** All symptoms are treated as independent dimensions.
    The model doesn’t yet capture joint likelihoods (e.g., rash + joint pain might mean
    something together that neither does alone).

*   **Incomplete Disease Coverage:** The system only includes a curated subset of conditions.
    While extensible, its accuracy is limited by the richness and correctness of the disease
    vector set.

*   **No Negative Weighting:** Diseases that are actively contradicted by certain symptoms
    (e.g., facial droop essentially rules out tension headache) aren't explicitly deweighted.
    All scoring is positive alignment only.

*   **No Localization or Demographics:** The engine doesn’t yet adjust for age, sex, geography,
    or risk profile—which in real clinical reasoning, strongly shapes priors.

================================================================================
"""

# ==============================================================================
# The Single Source of Truth: Expanded to ~40 Conditions
# This knowledge base now includes common, serious, chronic, and rare diseases.
# ==============================================================================
DISEASE_KNOWLEDGE_BASE = {
    # Common Viral/Bacterial
    'common_cold': {
        "symptoms": {'fever': 0.2, 'cough': 0.7, 'fatigue': 0.4, 'headache': 0.3, 'runny_nose': 0.9, 'sore_throat': 0.8, 'sneezing': 0.8},
        "metadata": {"icd11": "CA00", "common_name": "Common Cold", "type": "Viral"}
    },
    'flu': {
        "symptoms": {'fever': 0.9, 'cough': 0.8, 'fatigue': 0.9, 'headache': 0.8, 'muscle_aches': 0.9, 'runny_nose': 0.5, 'sore_throat': 0.6, 'chills': 0.9},
        "metadata": {"icd11": "1E31", "common_name": "Influenza", "type": "Viral"}
    },
    'covid19': {
        "symptoms": {'fever': 0.8, 'cough': 0.8, 'fatigue': 0.8, 'headache': 0.6, 'muscle_aches': 0.5, 'sore_throat': 0.5, 'shortness_of_breath': 0.7, 'loss_of_taste_smell': 0.9},
        "metadata": {"icd11": "RA01.0", "common_name": "COVID-19", "type": "Viral"}
    },
    'strep_throat': {
        "symptoms": {'fever': 0.8, 'fatigue': 0.5, 'headache': 0.6, 'sore_throat': 0.9, 'swollen_glands': 0.9, 'difficulty_swallowing': 0.8, 'white_patches_on_tonsils': 0.7},
        "metadata": {"icd11": "1B81", "common_name": "Strep Throat", "type": "Bacterial"}
    },
    'mono': {
        "symptoms": {'fever': 0.7, 'fatigue': 0.9, 'headache': 0.7, 'muscle_aches': 0.6, 'sore_throat': 0.9, 'loss_of_appetite': 0.8, 'swollen_glands': 0.9},
        "metadata": {"icd11": "1D8Z", "common_name": "Mononucleosis", "type": "Viral"}
    },
    # Respiratory
    'pneumonia': {
        "symptoms": {'fever': 0.9, 'cough': 0.9, 'fatigue': 0.8, 'shortness_of_breath': 0.9, 'chest_pain': 0.8, 'chills': 0.9, 'confusion': 0.4},
        "metadata": {"icd11": "CA40", "common_name": "Pneumonia", "type": "Infection"}
    },
    'bronchitis': {
        "symptoms": {'cough': 0.9, 'fatigue': 0.6, 'sore_throat': 0.5, 'shortness_of_breath': 0.5, 'chest_pain': 0.6, 'chills': 0.4, 'wheezing': 0.7},
        "metadata": {"icd11": "CA20", "common_name": "Bronchitis", "type": "Infection/Irritation"}
    },
    'sinusitis': {
        "symptoms": {'fever': 0.3, 'cough': 0.5, 'fatigue': 0.4, 'headache': 0.8, 'runny_nose': 0.9, 'sore_throat': 0.6, 'facial_pain_pressure': 0.9},
        "metadata": {"icd11": "CA04", "common_name": "Sinusitis", "type": "Infection/Inflammation"}
    },
    'asthma': {
        "symptoms": {'cough': 0.7, 'shortness_of_breath': 0.9, 'chest_pain': 0.7, 'wheezing': 0.9},
        "metadata": {"icd11": "CA23", "common_name": "Asthma", "type": "Chronic Respiratory"}
    },
    'tuberculosis': {
        "symptoms": {'fever': 0.7, 'cough': 0.9, 'fatigue': 0.8, 'chest_pain': 0.7, 'chills': 0.7, 'loss_of_appetite': 0.8, 'night_sweats': 0.9, 'weight_loss': 0.8},
        "metadata": {"icd11": "1B11", "common_name": "Tuberculosis", "type": "Bacterial"}
    },
    # Digestive
    'gastroenteritis': {
        "symptoms": {'fever': 0.4, 'fatigue': 0.7, 'nausea': 0.9, 'muscle_aches': 0.5, 'diarrhea': 0.9, 'vomiting': 0.9, 'abdominal_pain': 0.8},
        "metadata": {"icd11": "1A01", "common_name": "Gastroenteritis (Stomach Flu)", "type": "Infection/Irritation"}
    },
    'food_poisoning': {
        "symptoms": {'fever': 0.3, 'fatigue': 0.6, 'headache': 0.5, 'nausea': 0.9, 'diarrhea': 0.9, 'vomiting': 0.9, 'abdominal_pain': 0.9, 'chills': 0.6},
        "metadata": {"icd11": "1A00", "common_name": "Food Poisoning", "type": "Bacterial/Toxin"}
    },
    'appendicitis': {
        "symptoms": {'fever': 0.6, 'nausea': 0.8, 'vomiting': 0.7, 'abdominal_pain': 0.9, 'loss_of_appetite': 0.9, 'constipation': 0.5},
        "metadata": {"icd11": "DC10", "common_name": "Appendicitis", "type": "Acute Medical"}
    },
    'crohns_disease': {
        "symptoms": {'fever': 0.5, 'fatigue': 0.8, 'diarrhea': 0.8, 'abdominal_pain': 0.8, 'joint_pain': 0.5, 'loss_of_appetite': 0.7, 'weight_loss': 0.8},
        "metadata": {"icd11": "DD70", "common_name": "Crohn's Disease", "type": "Autoimmune/Chronic"}
    },
    'pancreatic_cancer': {
        "symptoms": {'fatigue': 0.8, 'nausea': 0.6, 'abdominal_pain': 0.8, 'jaundice': 0.7, 'loss_of_appetite': 0.9, 'weight_loss': 0.9, 'back_pain': 0.7},
        "metadata": {"icd11": "2C10", "common_name": "Pancreatic Cancer", "type": "Oncology"}
    },
    # Neurological / Systemic
    'migraine': {
        "symptoms": {'fatigue': 0.7, 'headache': 0.9, 'nausea': 0.8, 'vomiting': 0.2, 'dizziness': 0.8, 'sensitivity_to_light': 0.9},
        "metadata": {"icd11": "8A80", "common_name": "Migraine", "type": "Neurological"}
    },
    'meningitis': {
        "symptoms": {'fever': 0.9, 'fatigue': 0.8, 'headache': 0.9, 'nausea': 0.7, 'vomiting': 0.6, 'dizziness': 0.8, 'chills': 0.9, 'stiff_neck': 0.9, 'sensitivity_to_light': 0.8},
        "metadata": {"icd11": "1D01", "common_name": "Meningitis", "type": "Acute Medical"}
    },
    'lyme_disease': {
        "symptoms": {'fever': 0.7, 'fatigue': 0.8, 'headache': 0.8, 'muscle_aches': 0.8, 'joint_pain': 0.9, 'skin_rash': 0.8, 'chills': 0.8, 'swollen_glands': 0.7},
        "metadata": {"icd11": "1C15", "common_name": "Lyme Disease", "type": "Bacterial"}
    },
    'anemia': {
        "symptoms": {'fatigue': 0.9, 'headache': 0.5, 'shortness_of_breath': 0.6, 'chest_pain': 0.4, 'dizziness': 0.9, 'chills': 0.7, 'pale_skin': 0.8},
        "metadata": {"icd11": "3A00", "common_name": "Anemia", "type": "Hematological"}
    },
    'lupus': {
        "symptoms": {'fever': 0.7, 'fatigue': 0.9, 'headache': 0.6, 'muscle_aches': 0.7, 'shortness_of_breath': 0.4, 'chest_pain': 0.5, 'joint_pain': 0.8, 'skin_rash': 0.8, 'loss_of_appetite': 0.5, 'swollen_glands': 0.6, 'hair_loss': 0.5},
        "metadata": {"icd11": "4A40", "common_name": "Lupus", "type": "Autoimmune"}
    },
    'diabetes_type1': {
        "symptoms": {'fatigue': 0.8, 'nausea': 0.4, 'vomiting': 0.3, 'abdominal_pain': 0.3, 'weight_loss': 0.7, 'increased_thirst': 0.9, 'frequent_urination': 0.9, 'blurred_vision': 0.6},
        "metadata": {"icd11": "5A10", "common_name": "Diabetes Mellitus, Type 1", "type": "Endocrine"}
    },
    # Acute Emergencies
    'heart_attack': {
        "symptoms": {'fatigue': 0.4, 'nausea': 0.5, 'shortness_of_breath': 0.8, 'chest_pain': 0.9, 'vomiting': 0.2, 'dizziness': 0.7, 'chills': 0.5, 'arm_pain': 0.7},
        "metadata": {"icd11": "BA41", "common_name": "Myocardial Infarction (Heart Attack)", "type": "Cardiovascular Emergency"}
    },
    # Heart Attack Mimics

    'angina': {
        "symptoms": {'chest_pain': 0.9, 'shortness_of_breath': 0.6, 'fatigue': 0.5, 'dizziness': 0.4},
        "metadata": {"icd11": "BA40", "common_name": "Stable Angina", "type": "Cardiovascular"}
    },

    'gerd': {
        "symptoms": {'chest_pain': 0.7, 'nausea': 0.5, 'vomiting': 0.3, 'dizziness': 0.2},
        "metadata": {"icd11": "DA64", "common_name": "Gastroesophageal Reflux Disease (GERD)", "type": "Gastrointestinal"}
    },

    'panic_attack': {
        "symptoms": {'chest_pain': 0.6, 'shortness_of_breath': 0.5, 'dizziness': 0.6, 'nausea': 0.4, 'confusion': 0.4},
        "metadata": {"icd11": "MB23", "common_name": "Panic Attack", "type": "Psychological"}
    },

    'pericarditis': {
        "symptoms": {'chest_pain': 0.8, 'shortness_of_breath': 0.5, 'fatigue': 0.4, 'fever': 0.4},
        "metadata": {"icd11": "BA50", "common_name": "Pericarditis", "type": "Cardiovascular Inflammatory"}
    },

    'pulmonary_embolism': {
        "symptoms": {'chest_pain': 0.8, 'shortness_of_breath': 0.9, 'dizziness': 0.6, 'cough': 0.4, 'nausea': 0.3},
        "metadata": {"icd11": "BD10", "common_name": "Pulmonary Embolism", "type": "Respiratory Emergency"}
    },

    'costochondritis': {
        "symptoms": {'chest_pain': 0.8},
        "metadata": {"icd11": "FA01", "common_name": "Costochondritis", "type": "Musculoskeletal"}
    },

    'gallbladder_disease': {
        "symptoms": {'chest_pain': 0.5, 'nausea': 0.7, 'vomiting': 0.6, 'fatigue': 0.4},
        "metadata": {"icd11": "DC52", "common_name": "Cholelithiasis (Gallbladder Disease)", "type": "Gastrointestinal"}
    },

    'aortic_dissection': {
        "symptoms": {'chest_pain': 0.9, 'arm_pain': 0.7, 'dizziness': 0.5, 'fatigue': 0.4},
        "metadata": {"icd11": "BA60", "common_name": "Aortic Dissection", "type": "Vascular Emergency"}
    },
    'stroke': {
        "symptoms": {'fatigue': 0.5, 'headache': 0.8, 'nausea': 0.4, 'vomiting': 0.3, 'dizziness': 0.8, 'confusion': 0.8, 'difficulty_swallowing': 0.6, 'facial_drooping': 0.9, 'arm_weakness': 0.9, 'speech_difficulty': 0.9},
        "metadata": {"icd11": "8B20", "common_name": "Stroke", "type": "Neurological Emergency"}
    },
    # Cancers
    'lung_cancer': {
        "symptoms": {'cough': 0.8, 'fatigue': 0.7, 'shortness_of_breath': 0.7, 'chest_pain': 0.7, 'loss_of_appetite': 0.6, 'weight_loss': 0.7, 'hoarseness': 0.5},
        "metadata": {"icd11": "2C25", "common_name": "Lung Cancer", "type": "Oncology"}
    },
    # Classic Infectious Diseases
    'measles': {
        "symptoms": {'fever': 0.9, 'cough': 0.8, 'runny_nose': 0.8, 'sore_throat': 0.6, 'skin_rash': 0.9, 'conjunctivitis': 0.8, 'koplik_spots': 0.9},
        "metadata": {"icd11": "1F03", "common_name": "Measles", "type": "Viral"}
    },
    'mumps': {
        "symptoms": {'fever': 0.8, 'fatigue': 0.7, 'headache': 0.6, 'muscle_aches': 0.6, 'loss_of_appetite': 0.7, 'swollen_glands': 0.9, 'jaw_pain': 0.8},
        "metadata": {"icd11": "1F00", "common_name": "Mumps", "type": "Viral"}
    },
    'smallpox': { # Historical disease
        "symptoms": {'fever': 0.9, 'fatigue': 0.9, 'headache': 0.9, 'nausea': 0.6, 'muscle_aches': 0.8, 'vomiting': 0.7, 'back_pain': 0.8, 'skin_rash': 0.9},
        "metadata": {"icd11": "1E61", "common_name": "Smallpox", "type": "Viral (Eradicated)"}
    },

    # Rare Conditions

    'fabry_disease': {
        "symptoms": {'burning_pain_limbs': 0.8, 'abdominal_pain': 0.6, 'fatigue': 0.7, 'nausea': 0.5, 'rash': 0.4, 'kidney_dysfunction': 0.7},
        "metadata": {"icd11": "5C51", "common_name": "Fabry Disease", "type": "Genetic Metabolic"}
    },
    
    'ehlers_danlos': {
        "symptoms": {'joint_hypermobility': 0.9, 'skin_hyperextensibility': 0.8, 'easy_bruising': 0.6, 'fatigue': 0.5},
        "metadata": {"icd11": "LD90", "common_name": "Ehlers-Danlos Syndrome", "type": "Connective Tissue Disorder"}
    },

    'amyloidosis': {
        "symptoms": {'fatigue': 0.8, 'weight_loss': 0.6, 'peripheral_neuropathy': 0.7, 'chest_pain': 0.4, 'shortness_of_breath': 0.5},
        "metadata": {"icd11": "4A43", "common_name": "Amyloidosis", "type": "Protein Misfolding Disorder"}
    },

    'sarcoidosis': {
        "symptoms": {'fatigue': 0.7, 'cough': 0.6, 'chest_pain': 0.5, 'rash': 0.6, 'eye_inflammation': 0.5},
        "metadata": {"icd11": "4A40", "common_name": "Sarcoidosis", "type": "Inflammatory Granulomatous"}
    },

    'takayasu_arteritis': {
        "symptoms": {'arm_pain': 0.7, 'dizziness': 0.6, 'fatigue': 0.6, 'chest_pain': 0.5, 'weak_pulses': 0.9},
        "metadata": {"icd11": "4A44.0", "common_name": "Takayasu Arteritis", "type": "Large Vessel Vasculitis"}
    },

    'brugada_syndrome': {
        "symptoms": {'syncope': 0.9, 'chest_pain': 0.5, 'sudden_cardiac_arrest': 0.9, 'dizziness': 0.6},
        "metadata": {"icd11": "BA81.0", "common_name": "Brugada Syndrome", "type": "Cardiac Channelopathy"}
    },

    'stiff_person_syndrome': {
        "symptoms": {'muscle_rigidity': 0.9, 'muscle_spasms': 0.8, 'anxiety': 0.5, 'startle_response': 0.9},
        "metadata": {"icd11": "8B61.0", "common_name": "Stiff Person Syndrome", "type": "Neurological Autoimmune"}
    },
    
    'kawasaki_disease': {
        "symptoms": {'fever': 0.9, 'rash': 0.7, 'conjunctivitis': 0.8, 'swollen_lymph_nodes': 0.6, 'fatigue': 0.5},
        "metadata": {"icd11": "1A26", "common_name": "Kawasaki Disease", "type": "Pediatric Vasculitis"}
    },
    
    'wilsons_disease': {
        "symptoms": {'tremor': 0.7, 'fatigue': 0.6, 'liver_dysfunction': 0.8, 'psychiatric_symptoms': 0.5, 'abdominal_pain': 0.6},
        "metadata": {"icd11": "5C70", "common_name": "Wilson's Disease", "type": "Genetic Metabolic"}
    },
    
    'addisons_disease': {
        "symptoms": {'fatigue': 0.9, 'hypotension': 0.8, 'hyperpigmentation': 0.7, 'salt_craving': 0.6, 'nausea': 0.5},
        "metadata": {"icd11": "5A71", "common_name": "Addison’s Disease", "type": "Endocrine (Adrenal Insufficiency)"}
    }
    # And more... this structure is infinitely extensible.
}


class WhiteBoxMedicalDiagnostic:
    # ... The class code remains IDENTICAL to v2 ...
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        all_symptoms = set()
        for disease_data in self.kb.values():
            all_symptoms.update(disease_data["symptoms"].keys())
        self.symptoms = sorted(list(all_symptoms))
        self.disease_vectors = {}
        for disease_name, disease_data in self.kb.items():
            vector = np.zeros(len(self.symptoms))
            for symptom, value in disease_data["symptoms"].items():
                if symptom in self.symptoms:
                    idx = self.symptoms.index(symptom)
                    vector[idx] = value
            self.disease_vectors[disease_name] = vector

    def encode_symptoms(self, patient_symptoms):
        symptom_vector = np.zeros(len(self.symptoms))
        for symptom, intensity in patient_symptoms.items():
            if symptom in self.symptoms:
                idx = self.symptoms.index(symptom)
                symptom_vector[idx] = intensity
        return symptom_vector

    def diagnose(self, patient_symptoms, top_n=5):
        patient_vector = self.encode_symptoms(patient_symptoms)
        if np.linalg.norm(patient_vector) == 0: return []
        similarities = {}
        for disease_name, disease_vector in self.disease_vectors.items():
            similarity = cosine_similarity([patient_vector], [disease_vector])[0][0]
            similarities[disease_name] = similarity
        sorted_diagnoses = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_diagnoses[:top_n]

    def explain_diagnosis(self, patient_symptoms, diagnosis):
        if diagnosis not in self.disease_vectors:
            print(f"Explanation for '{diagnosis}' cannot be provided (not in knowledge base).")
            return
        patient_vector = self.encode_symptoms(patient_symptoms)
        disease_vector = self.disease_vectors[diagnosis]
        metadata = self.kb[diagnosis].get('metadata', {})
        print(f"\n--- Explanation for {diagnosis.upper()} ---")
        if metadata:
            print(f"  Common Name: {metadata.get('common_name', 'N/A')}, ICD-11 Code: {metadata.get('icd11', 'N/A')}, Type: {metadata.get('type', 'N/A')}")
        print("Symptom contributions (Patient Symptom Value * Disease Pattern Value):")
        contributions = []
        for i, symptom in enumerate(self.symptoms):
            patient_val = patient_vector[i]
            if patient_val > 0:
                disease_val = disease_vector[i]
                contribution = patient_val * disease_val
                contributions.append((symptom, patient_val, disease_val, contribution))
        contributions.sort(key=lambda x: x[3], reverse=True)
        for symptom, patient_val, disease_val, contribution in contributions:
            print(f"  - {symptom:<25} | Patient: {patient_val:.1f}, Disease Pattern: {disease_val:.1f} -> Contribution: {contribution:.2f}")


class TestHarness:
    def __init__(self, diagnostic_system):
        self.diagnostics = diagnostic_system
        self.diseases = list(diagnostic_system.kb.keys())

    def create_archetypal_patient(self, disease_name):
        return self.diagnostics.kb[disease_name]["symptoms"]

    def run_full_test(self):
        print("="*60)
        print("           RUNNING DIAGNOSTIC SYSTEM TEST HARNESS (V3)")
        print("="*60)
        
        correct_top_1 = 0
        total_tests = len(self.diseases)
        confusion_matrix = {d: {d2: 0 for d2 in self.diseases} for d in self.diseases}

        for disease in self.diseases:
            archetype_symptoms = self.create_archetypal_patient(disease)
            diagnoses = self.diagnostics.diagnose(archetype_symptoms, top_n=1)
            
            top_diagnosis = diagnoses[0][0] if diagnoses else "N/A"
            if top_diagnosis == disease:
                correct_top_1 += 1
            if top_diagnosis != "N/A":
                confusion_matrix[disease][top_diagnosis] += 1
        
        accuracy = (correct_top_1 / total_tests) * 100 if total_tests > 0 else 0
        print(f"Top-1 Accuracy: {correct_top_1}/{total_tests} = {accuracy:.2f}%\n")
        return confusion_matrix

    def plot_confusion_matrix(self, matrix, filename="diagnostic_confusion_matrix.png"):
        print(f"Generating and saving confusion matrix to '{filename}'...")
        labels = self.diseases
        matrix_array = np.array([[matrix[d1][d2] for d2 in labels] for d1 in labels])

        plt.figure(figsize=(18, 16))
        sns.heatmap(matrix_array, annot=True, fmt='d', cmap='viridis', 
                    xticklabels=labels, yticklabels=labels)
        plt.xlabel('Predicted Diagnosis', fontsize=14)
        plt.ylabel('True Disease (Archetype)', fontsize=14)
        plt.title('Diagnostic System Confusion Matrix', fontsize=16)
        plt.xticks(rotation=65, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout() # Adjusts plot to ensure everything fits without overlapping
        
        try:
            plt.savefig(filename, dpi=300) # dpi=300 for higher resolution
            print(f"Plot successfully saved as '{filename}'")
        except Exception as e:
            print(f"Error saving plot: {e}")
        
        plt.close() # Important to close the figure to free memory


# --- Main Execution ---
if __name__ == "__main__":
    diagnostic_system = WhiteBoxMedicalDiagnostic(DISEASE_KNOWLEDGE_BASE)
    test_harness = TestHarness(diagnostic_system)
    
    # Run the tests and get the data for the confusion matrix
    #diagnoses_map_data = test_harness.run_full_test()
    
    # Plot the results
    #test_harness.plot_confusion_matrix(diagnoses_map_data)

    # --- INDIVIDUAL DIAGNOSIS DEMO ---
    print("\n" + "="*60)
    print("                 INDIVIDUAL DIAGNOSIS DEMO (SERIOUS CASE)")
    print("="*60)
    # Patient presents with symptoms that could be a heart attack
    patient_symptoms = {
        'chest_pain': 0.9,
        'shortness_of_breath': 0.7,
        'arm_pain': 0.6,
        'nausea': 0.5,
        'dizziness': 0.6
    }
    print("Patient has symptoms:", patient_symptoms)
    final_diagnoses = diagnostic_system.diagnose(patient_symptoms, top_n=5)
    
    print("\nDifferential Diagnosis (Top 5):")
    for d, s in final_diagnoses:
        print(f"  - {d:<20} (Similarity: {s:.3f})")

    if final_diagnoses:
        diagnostic_system.explain_diagnosis(patient_symptoms, final_diagnoses[0][0])

    print("")
    print("A less clear cut diagnosis")
    # Patient presents with low-grade fatigue, diffuse pain, and mild neurological symptoms
    patient_symptoms = {
        'fatigue': 0.7,
        'headache': 0.5,
        'dizziness': 0.6,
        'joint_hypermobility': 0.3,
        'abdominal_pain': 0.5,
        'tremor': 0.5,
        'rash': 0.6,
    }
    print("Patient has symptoms:", patient_symptoms)
    final_diagnoses = diagnostic_system.diagnose(patient_symptoms, top_n=5)
    
    print("\nDifferential Diagnosis (Top 5):")
    for d, s in final_diagnoses:
        print(f"  - {d:<20} (Similarity: {s:.3f})")

    if final_diagnoses:
        diagnostic_system.explain_diagnosis(patient_symptoms, final_diagnoses[0][0])
