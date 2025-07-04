import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

"""
================================================================================
 White-Box Geometric Medical Diagnostic Engine V4 (Hierarchical Rationality)
================================================================================

Author: J. Rogers
Date: June 2025

--- High-Level Overview ---

This program implements a novel, white-box approach to medical diagnosis.
It combines logical rule-based pruning with geometric similarity calculations.
This version (V4) introduces a sophisticated, ethically-aligned test
recommendation engine.

Core Principles:
----------------
1.  **Illness as a Geometric Space:** Each symptom/test is an axis.
2.  **Disease as a Vector:** Each disease is a point in this space.
3.  **Diagnosis as a Two-Stage Process:**
    a.  **Deductive Pruning:** First, apply hard "rule-out" logic based on
        definitive test results. This eliminates impossible diagnoses.
    b.  **Inductive Similarity:** Second, for the remaining plausible diseases,
        calculate the cosine similarity to find the closest match.
4.  **Rational Recommendation:** Suggests next steps using a hierarchical logic:
    a.  **Prioritize by Clinical Urgency:** First, rank tests by a 'Risk Score'
        (Lethality * Prevalence * Similarity).
    b.  **Optimize by Resource Efficiency:** If risks are equal, recommend the
        lower-cost test as a tie-breaker.

This architecture ensures patient safety is the primary driver of decisions,
while cost-effectiveness guides choices between clinically equivalent options.
The entire reasoning process is transparent and auditable.
================================================================================
"""

# ==============================================================================
# DATA: The available tests and their costs (a real-world system would use a DB)
# ==============================================================================
AVAILABLE_TEST_CATALOG = {
    # Blood Tests
    'troponin_elevated': {'type': 'blood_test', 'cost': 50},
    'd_dimer_elevated': {'type': 'blood_test', 'cost': 40},
    'wbc_elevated': {'type': 'blood_test', 'cost': 20},
    'hgb_low': {'type': 'blood_test', 'cost': 20},
    'blood_glucose_high': {'type': 'blood_test', 'cost': 15},
    'hba1c_high': {'type': 'blood_test', 'cost': 45},
    'liver_enzymes_elevated': {'type': 'blood_test', 'cost': 30},
    # EKG
    'ekg_st_elevation': {'type': 'ekg', 'cost': 75},
    'ekg_pr_depression': {'type': 'ekg', 'cost': 75},
    'ekg_brugada_pattern': {'type': 'ekg', 'cost': 75},
    # Imaging
    'chest_xray_infiltrates': {'type': 'imaging_scan', 'cost': 150},
    'ct_angiogram_pe': {'type': 'imaging_scan', 'cost': 800},
    'ct_aorta_dissection': {'type': 'imaging_scan', 'cost': 900},
    'mri_brain_infarct': {'type': 'imaging_scan', 'cost': 1200},
    'ultrasound_gallstones': {'type': 'imaging_scan', 'cost': 300},
    # Procedures
    'upper_endoscopy_esophagitis': {'type': 'endoscopy', 'cost': 1500},
    # Other
    'anxiety_assessment_high': {'type': 'psychological_evaluation', 'cost': 100},
    'stress_test_abnormal': {'type': 'cardiac_test', 'cost': 500},
    'chest_wall_tenderness': {'type': 'physical_exam_finding', 'cost': 10},
    'pulse_deficit': {'type': 'physical_exam_finding', 'cost': 10},
}

# ==============================================================================
# DATA: The Disease Knowledge Base with Lethality & Prevalence
# ==============================================================================
DISEASE_KNOWLEDGE_BASE = {
    # Acute Emergencies
    'heart_attack': {
        "symptoms": {'chest_pain': 0.9, 'shortness_of_breath': 0.8, 'arm_pain': 0.7, 'nausea': 0.5, 'dizziness': 0.6},
        "tests": {'troponin_elevated': 1.0, 'ekg_st_elevation': 1.0},
        "metadata": {"lethality": 0.9, "prevalence": 0.7, "common_name": "Heart Attack"}
    },
    'pulmonary_embolism': {
        "symptoms": {'chest_pain': 0.8, 'shortness_of_breath': 0.9, 'dizziness': 0.6},
        "tests": {'d_dimer_elevated': 1.0, 'ct_angiogram_pe': 1.0},
        "metadata": {"lethality": 0.8, "prevalence": 0.5, "common_name": "Pulmonary Embolism"}
    },
    'aortic_dissection': {
        "symptoms": {'chest_pain': 0.9, 'arm_pain': 0.7, 'dizziness': 0.5},
        "tests": {'ct_aorta_dissection': 1.0, 'pulse_deficit': 1.0},
        "metadata": {"lethality": 0.95, "prevalence": 0.2, "common_name": "Aortic Dissection"}
    },
    # Heart Attack Mimics (Lower Lethality but common)
    'angina': {
        "symptoms": {'chest_pain': 0.9, 'shortness_of_breath': 0.6},
        "tests": {'stress_test_abnormal': 1.0, 'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0},
        "metadata": {"lethality": 0.2, "prevalence": 0.8, "common_name": "Angina"}
    },
    'gerd': {
        "symptoms": {'chest_pain': 0.7, 'nausea': 0.5},
        "tests": {'upper_endoscopy_esophagitis': 1.0, 'troponin_elevated': 0.0},
        "metadata": {"lethality": 0.01, "prevalence": 0.9, "common_name": "GERD"}
    },
    'panic_attack': {
        "symptoms": {'chest_pain': 0.6, 'shortness_of_breath': 0.5, 'dizziness': 0.6},
        "tests": {'anxiety_assessment_high': 1.0, 'troponin_elevated': 0.0},
        "metadata": {"lethality": 0.0, "prevalence": 0.8, "common_name": "Panic Attack"}
    },
    'pericarditis': {
        "symptoms": {'chest_pain': 0.8, 'shortness_of_breath': 0.5, 'fever': 0.4},
        "tests": {'ekg_pr_depression': 1.0, 'troponin_elevated': 0.3}, # Can have mild elevation
        "metadata": {"lethality": 0.1, "prevalence": 0.4, "common_name": "Pericarditis"}
    },
    'asthma': {
        "symptoms": {'cough': 0.7, 'shortness_of_breath': 0.9, 'chest_pain': 0.7, 'wheezing': 0.9},
        "tests": {},
        "metadata": {"lethality": 0.1, "prevalence": 0.6, "common_name": "Asthma"}
    },
}

class WhiteBoxMedicalDiagnostic:
    def __init__(self, knowledge_base, test_catalog):
        self.kb = knowledge_base
        self.test_catalog = test_catalog
        
        # Create a master list of all features (symptoms + tests) to define the space
        all_features = set()
        for data in self.kb.values():
            all_features.update(data["symptoms"].keys())
            all_features.update(data.get("tests", {}).keys())
        self.features = sorted(list(all_features))
        
        # Pre-process the KB into vectors and rule sets for efficiency
        self.disease_vectors = {}
        self.definitive_rules = {}
        for name, data in self.kb.items():
            # Create disease vector
            vector = np.zeros(len(self.features))
            combined_features = {**data["symptoms"], **data.get("tests", {})}
            for feature, value in combined_features.items():
                if feature in self.features:
                    vector[self.features.index(feature)] = value
            self.disease_vectors[name] = vector
            
            # Extract definitive rules for this disease
            self.definitive_rules[name] = data.get("tests", {})

    def encode_patient_features(self, patient_features):
        """Converts a dictionary of patient features into a numerical vector."""
        vector = np.zeros(len(self.features))
        for feature, intensity in patient_features.items():
            if feature in self.features:
                vector[self.features.index(feature)] = intensity
        return vector

    def apply_definitive_rules(self, patient_features, possible_diseases):
        """Prunes the list of possible diseases based on hard rules."""
        plausible_diagnoses = []
        rule_out_explanations = []
        for disease in possible_diseases:
            is_ruled_out = False
            rules = self.definitive_rules.get(disease, {})
            for test_name, required_value in rules.items():
                if test_name in patient_features:
                    patient_value = patient_features[test_name]
                    # Rule out if a required positive test is negative
                    if required_value >= 0.9 and patient_value < 0.1:
                        is_ruled_out = True
                        rule_out_explanations.append(f"Ruled out {disease}: required {test_name} to be positive, but it was negative.")
                        break
                    # Rule out if a required negative test is positive
                    if required_value <= 0.1 and patient_value > 0.9:
                        is_ruled_out = True
                        rule_out_explanations.append(f"Ruled out {disease}: required {test_name} to be negative, but it was positive.")
                        break
            if not is_ruled_out:
                plausible_diagnoses.append(disease)
        return plausible_diagnoses, rule_out_explanations

    def diagnose(self, patient_features, top_n=5):
        """Performs a two-stage diagnosis: rule-based pruning then similarity."""
        # Step 1: Prune possibilities with definitive rules
        plausible_diagnoses, explanations = self.apply_definitive_rules(patient_features, self.kb.keys())

        # Step 2: Calculate similarity for the remaining plausible diseases
        patient_vector = self.encode_patient_features(patient_features)
        if np.linalg.norm(patient_vector) == 0: return [], explanations
        
        similarities = {}
        for disease_name in plausible_diagnoses:
            disease_vector = self.disease_vectors[disease_name]
            if np.linalg.norm(disease_vector) > 0:
                similarity = cosine_similarity([patient_vector], [disease_vector])[0][0]
                similarities[disease_name] = similarity
        
        sorted_diagnoses = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_diagnoses[:top_n], explanations

    def recommend_tests(self, current_differential, patient_features_current_state, top_n=3):
        """Recommends tests using a hierarchical logic: Risk > Cost."""
        potential_recommendations = []
        performed_tests = set(patient_features_current_state.keys())

        for disease_name, similarity_score in current_differential:
            if disease_name not in self.kb: continue
            
            metadata = self.kb[disease_name]['metadata']
            lethality = metadata.get('lethality', 0.1)
            prevalence = metadata.get('prevalence', 0.1)

            # Calculate the pure clinical risk score for this disease hypothesis
            risk_score = lethality * prevalence * similarity_score
            
            # Find all relevant, unperformed tests that could confirm or deny this hypothesis
            relevant_tests = self.definitive_rules.get(disease_name, {}).keys()
            for test_name in relevant_tests:
                if test_name in self.test_catalog and test_name not in performed_tests:
                    test_info = self.test_catalog[test_name]
                    cost = test_info.get('cost', 9999) # Default to high cost
                    
                    potential_recommendations.append({
                        'test_name': test_name,
                        'test_type': test_info['type'],
                        'for_disease': disease_name,
                        'risk_score': risk_score, # The primary sorting key
                        'cost': cost             # The secondary sorting key
                    })

        # The crucial two-tiered sort: first by risk (desc), then by cost (asc)
        sorted_recs = sorted(potential_recommendations, key=lambda x: (-x['risk_score'], x['cost']))
        
        # Return the top N unique recommendations
        unique_recs = []
        seen = set()
        for rec in sorted_recs:
            if rec['test_name'] not in seen:
                unique_recs.append(rec)
                seen.add(rec['test_name'])
            if len(unique_recs) >= top_n: break
        return unique_recs

    def explain_diagnosis(self, patient_features, diagnosis):
        """Provides a breakdown of the final diagnosis."""
        # This function would be fully implemented in a production system
        print(f"\n--- Explanation for {diagnosis.upper()} would be generated here ---")


# --- Main Execution: The Corrected 5-Step Narrative ---
if __name__ == "__main__":
    diagnostic_system = WhiteBoxMedicalDiagnostic(DISEASE_KNOWLEDGE_BASE, AVAILABLE_TEST_CATALOG)
    
    print("\n" + "="*60)
    print("      ITERATIVE DIAGNOSIS DEMO (V4: HIERARCHICAL RATIONALITY)")
    print("="*60)
    
    # This dictionary will be updated step-by-step to simulate the diagnostic process
    patient_features = {}

    # --- STEP 1: Initial Presentation ---
    print("\n--- STEP 1: Initial Presentation (Symptoms Only) ---")
    patient_features.update({
        'chest_pain': 0.9, 'shortness_of_breath': 0.7, 'arm_pain': 0.6,
        'nausea': 0.5, 'dizziness': 0.6
    })
    differential, explanations = diagnostic_system.diagnose(patient_features, top_n=5)
    print("Patient features:", patient_features)
    print("\nInitial Differential Diagnosis:")
    for d, s in differential: print(f"  - {d:<20} (Similarity: {s:.3f})")
    recommendations = diagnostic_system.recommend_tests(differential, patient_features)
    print("\nSystem Recommends Tests (sorted by Risk, then Cost):")
    for rec in recommendations: print(f"  - Test: {rec['test_name']:<25} | For: {rec['for_disease']:<20} | Risk Score: {rec['risk_score']:.3f} | Cost: ${rec['cost']}")

    # --- STEP 2: Negative Cardiac Tests ---
    print("\n--- STEP 2: Negative cardiac tests received (Troponin, EKG) ---")
    patient_features.update({'troponin_elevated': 0.0, 'ekg_st_elevation': 0.0, 'ekg_pr_depression': 0.0})
    differential, explanations = diagnostic_system.diagnose(patient_features, top_n=5)
    print("\nUpdated patient features:", patient_features)
    if explanations:
        print("\nRules Applied:")
        for exp in explanations: print(f"  - {exp}")
    print("\nNew Differential Diagnosis:")
    for d, s in differential: print(f"  - {d:<20} (Similarity: {s:.3f})")
    recommendations = diagnostic_system.recommend_tests(differential, patient_features)
    print("\nSystem Recommends Next Tests:")
    for rec in recommendations: print(f"  - Test: {rec['test_name']:<25} | For: {rec['for_disease']:<20} | Risk Score: {rec['risk_score']:.3f} | Cost: ${rec['cost']}")

    # --- STEP 3: Elevated D-Dimer ---
    print("\n--- STEP 3: D-Dimer test is elevated ---")
    patient_features.update({'d_dimer_elevated': 1.0})
    differential, explanations = diagnostic_system.diagnose(patient_features, top_n=5)
    print("\nUpdated patient features:", patient_features)
    if explanations:
        print("\nRules Applied:")
        for exp in explanations: print(f"  - {exp}")
    print("\nNew Differential Diagnosis:")
    for d, s in differential: print(f"  - {d:<20} (Similarity: {s:.3f})")
    recommendations = diagnostic_system.recommend_tests(differential, patient_features)
    print("\nSystem Recommends Next Tests:")
    for rec in recommendations: print(f"  - Test: {rec['test_name']:<25} | For: {rec['for_disease']:<20} | Risk Score: {rec['risk_score']:.3f} | Cost: ${rec['cost']}")

    # --- STEP 4: Negative CT Angiogram ---
    print("\n--- STEP 4: CT Angiogram for PE is negative ---")
    patient_features.update({'ct_angiogram_pe': 0.0})
    differential, explanations = diagnostic_system.diagnose(patient_features, top_n=5)
    print("\nUpdated patient features:", patient_features)
    if explanations:
        print("\nRules Applied:")
        for exp in explanations: print(f"  - {exp}")
    print("\nNew Differential Diagnosis:")
    for d, s in differential: print(f"  - {d:<20} (Similarity: {s:.3f})")
    recommendations = diagnostic_system.recommend_tests(differential, patient_features)
    print("\nSystem Recommends Next Tests:")
    for rec in recommendations: print(f"  - Test: {rec['test_name']:<25} | For: {rec['for_disease']:<20} | Risk Score: {rec['risk_score']:.3f} | Cost: ${rec['cost']}")

    # --- STEP 5: Confirming Panic Attack ---
    print("\n--- STEP 5: Patient undergoes psychological assessment, confirms high anxiety ---")
    patient_features.update({'anxiety_assessment_high': 1.0})
    differential, explanations = diagnostic_system.diagnose(patient_features, top_n=5)
    print("\nUpdated patient features:", patient_features)
    if explanations:
        print("\nRules Applied:")
        for exp in explanations: print(f"  - {exp}")
    print("\nFinal Differential Diagnosis:")
    for d, s in differential: print(f"  - {d:<20} (Similarity: {s:.3f})")
