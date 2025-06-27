import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns


"""
================================================================================
 White-Box Geometric Legal Case Matching Engine
================================================================================

Author: Based on medical diagnostic engine concept
Date: June 2025

--- High-Level Overview ---

This program implements a white-box approach to legal case matching that operates
on a clear, geometric interpretation of legal knowledge. Instead of relying on
black-box text analysis or opaque statistical models, this engine maps legal
cases into a multi-dimensional "legal space" where each fundamental legal factor
represents an orthogonal axis.

Core Principles:
----------------
1.  **Legal Space as Geometry:** The system defines a multi-dimensional "legal
    space" where each fundamental legal factor (e.g., 'constitutional_law',
    'contract_breach', 'damages_claimed') represents an axis.

2.  **Cases as Vectors:** Each precedent case is defined as a specific point or
    vector within this space. The vector's components represent the presence
    and weight of various legal factors in that case.

3.  **Case Matching as Similarity:** A new case's legal factors are converted
    into a vector in the same space. Finding similar precedents becomes a
    geometric calculation using cosine similarity.

4.  **Precedent Priority:** Cases can be weighted by their precedential strength,
    jurisdiction hierarchy, and recency to influence matching results.

Legal Factors (Dimensions):
---------------------------
- Constitutional Law Issues
- Contract Law Elements  
- Tort/Personal Injury
- Criminal Law Aspects
- Property Rights
- Civil Rights
- Corporate/Business Law
- Family Law
- Labor/Employment
- Environmental Law
- Intellectual Property
- Tax Law
- Administrative Law
- Evidence/Procedure
- Damages/Remedies
- Jurisdiction/Standing
- Statutory Interpretation
- Common Law Principles
- Equity Considerations
- Public Policy Impact

================================================================================
"""

# ==============================================================================
# Legal Case Knowledge Base
# Each case is represented by legal factors and metadata including precedential weight
# ==============================================================================

LEGAL_CASE_KNOWLEDGE_BASE = {
    # Constitutional Law Cases
    'brown_v_board': {
        "factors": {
            'constitutional_law': 1.0, 'civil_rights': 1.0, 'equal_protection': 1.0,
            'education_law': 0.9, 'public_policy': 0.9, 'statutory_interpretation': 0.3,
            'administrative_law': 0.2
        },
        "metadata": {
            "citation": "347 U.S. 483 (1954)",
            "court": "Supreme Court",
            "precedent_weight": 1.0,  # Maximum precedential value
            "jurisdiction": "Federal",
            "area_of_law": "Constitutional/Civil Rights",
            "year": 1954
        }
    },
    
    'miranda_v_arizona': {
        "factors": {
            'constitutional_law': 0.9, 'criminal_law': 1.0, 'due_process': 1.0,
            'evidence_procedure': 0.8, 'civil_rights': 0.7, 'police_powers': 0.9
        },
        "metadata": {
            "citation": "384 U.S. 436 (1966)",
            "court": "Supreme Court", 
            "precedent_weight": 1.0,
            "jurisdiction": "Federal",
            "area_of_law": "Criminal Procedure",
            "year": 1966
        }
    },

    'roe_v_wade': {
        "factors": {
            'constitutional_law': 1.0, 'privacy_rights': 1.0, 'due_process': 0.9,
            'medical_law': 0.6, 'civil_rights': 0.8, 'public_policy': 0.9,
            'state_regulation': 0.7
        },
        "metadata": {
            "citation": "410 U.S. 113 (1973)",
            "court": "Supreme Court",
            "precedent_weight": 0.9,  # Reduced due to recent overturn
            "jurisdiction": "Federal", 
            "area_of_law": "Constitutional/Privacy",
            "year": 1973
        }
    },

    # Contract Law Cases
    'hadley_v_baxendale': {
        "factors": {
            'contract_law': 1.0, 'breach_of_contract': 0.9, 'damages_remedies': 1.0,
            'foreseeability': 1.0, 'commercial_law': 0.8, 'common_law': 0.9
        },
        "metadata": {
            "citation": "9 Ex. 341 (1854)",
            "court": "English Court of Exchequer",
            "precedent_weight": 0.8,  # Historical but foundational
            "jurisdiction": "Common Law",
            "area_of_law": "Contract Damages",
            "year": 1854
        }
    },

    'carlill_v_carbolic_smoke_ball': {
        "factors": {
            'contract_law': 1.0, 'offer_acceptance': 1.0, 'consideration': 0.8,
            'commercial_law': 0.7, 'advertising_law': 0.9, 'consumer_protection': 0.6,
            'common_law': 0.9
        },
        "metadata": {
            "citation": "[1893] 1 QB 256",
            "court": "English Court of Appeal",
            "precedent_weight": 0.8,
            "jurisdiction": "Common Law",
            "area_of_law": "Contract Formation",
            "year": 1893
        }
    },

    'williams_v_roffey': {
        "factors": {
            'contract_law': 1.0, 'consideration': 1.0, 'contract_modification': 0.9,
            'commercial_law': 0.8, 'practical_benefit': 1.0, 'common_law': 0.7,
            'construction_law': 0.4
        },
        "metadata": {
            "citation": "[1991] 1 QB 1",
            "court": "English Court of Appeal", 
            "precedent_weight": 0.7,
            "jurisdiction": "Common Law",
            "area_of_law": "Contract Consideration",
            "year": 1991
        }
    },

    # Tort Law Cases
    'donoghue_v_stevenson': {
        "factors": {
            'tort_law': 1.0, 'negligence': 1.0, 'duty_of_care': 1.0,
            'product_liability': 0.8, 'consumer_protection': 0.7, 'common_law': 0.9,
            'neighbor_principle': 1.0
        },
        "metadata": {
            "citation": "[1932] AC 562",
            "court": "House of Lords",
            "precedent_weight": 1.0,
            "jurisdiction": "Common Law",
            "area_of_law": "Negligence",
            "year": 1932
        }
    },

    'rylands_v_fletcher': {
        "factors": {
            'tort_law': 1.0, 'strict_liability': 1.0, 'property_rights': 0.8,
            'environmental_law': 0.6, 'nuisance': 0.7, 'common_law': 0.9,
            'hazardous_activities': 1.0
        },
        "metadata": {
            "citation": "(1868) LR 3 HL 330",
            "court": "House of Lords",
            "precedent_weight": 0.8,
            "jurisdiction": "Common Law", 
            "area_of_law": "Strict Liability",
            "year": 1868
        }
    },

    'palsgraf_v_long_island_railroad': {
        "factors": {
            'tort_law': 1.0, 'negligence': 1.0, 'proximate_cause': 1.0,
            'duty_of_care': 0.9, 'foreseeability': 1.0, 'personal_injury': 0.8,
            'common_law': 0.8
        },
        "metadata": {
            "citation": "248 N.Y. 339 (1928)",
            "court": "New York Court of Appeals",
            "precedent_weight": 0.9,
            "jurisdiction": "State",
            "area_of_law": "Negligence/Causation",
            "year": 1928
        }
    },

    # Criminal Law Cases
    'mcculloch_v_maryland': {
        "factors": {
            'constitutional_law': 1.0, 'federal_supremacy': 1.0, 'taxation': 0.8,
            'necessary_proper_clause': 1.0, 'state_federal_relations': 0.9,
            'banking_law': 0.5, 'statutory_interpretation': 0.7
        },
        "metadata": {
            "citation": "17 U.S. 316 (1819)",
            "court": "Supreme Court",
            "precedent_weight": 1.0,
            "jurisdiction": "Federal",
            "area_of_law": "Constitutional/Federalism",
            "year": 1819
        }
    },

    'gideon_v_wainwright': {
        "factors": {
            'constitutional_law': 0.9, 'criminal_law': 1.0, 'right_to_counsel': 1.0,
            'due_process': 1.0, 'civil_rights': 0.8, 'indigent_defense': 1.0,
            'sixth_amendment': 1.0
        },
        "metadata": {
            "citation": "372 U.S. 335 (1963)",
            "court": "Supreme Court",
            "precedent_weight": 1.0,
            "jurisdiction": "Federal",
            "area_of_law": "Criminal Procedure",
            "year": 1963
        }
    },

    # Property Law Cases
    'pierson_v_post': {
        "factors": {
            'property_rights': 1.0, 'ownership': 1.0, 'wild_animals': 1.0,
            'possession': 0.9, 'hunting_rights': 0.8, 'common_law': 0.9,
            'first_possession': 1.0
        },
        "metadata": {
            "citation": "3 Cai. R. 175 (N.Y. 1805)",
            "court": "New York Supreme Court",
            "precedent_weight": 0.7,
            "jurisdiction": "State",
            "area_of_law": "Property/Ownership",
            "year": 1805
        }
    },

    'kelo_v_city_of_new_london': {
        "factors": {
            'constitutional_law': 0.8, 'property_rights': 1.0, 'eminent_domain': 1.0,
            'public_use': 1.0, 'economic_development': 0.9, 'takings_clause': 1.0,
            'municipal_law': 0.7
        },
        "metadata": {
            "citation": "545 U.S. 469 (2005)",
            "court": "Supreme Court",
            "precedent_weight": 0.8,
            "jurisdiction": "Federal",
            "area_of_law": "Property/Takings",
            "year": 2005
        }
    },

    # Corporate/Business Law Cases
    'dodge_v_ford': {
        "factors": {
            'corporate_law': 1.0, 'fiduciary_duty': 1.0, 'shareholder_rights': 1.0,
            'business_judgment': 0.9, 'profit_maximization': 0.8, 'director_duties': 1.0,
            'common_law': 0.7
        },
        "metadata": {
            "citation": "204 Mich. 459 (1919)",
            "court": "Michigan Supreme Court",
            "precedent_weight": 0.7,
            "jurisdiction": "State",
            "area_of_law": "Corporate Governance",
            "year": 1919
        }
    },

    'citizens_united_v_fec': {
        "factors": {
            'constitutional_law': 1.0, 'corporate_law': 0.8, 'free_speech': 1.0,
            'campaign_finance': 1.0, 'first_amendment': 1.0, 'political_law': 0.9,
            'administrative_law': 0.4
        },
        "metadata": {
            "citation": "558 U.S. 310 (2010)",
            "court": "Supreme Court",
            "precedent_weight": 0.9,
            "jurisdiction": "Federal",
            "area_of_law": "Constitutional/Corporate",
            "year": 2010
        }
    },

    # Employment Law Cases
    'griggs_v_duke_power': {
        "factors": {
            'employment_law': 1.0, 'civil_rights': 1.0, 'discrimination': 1.0,
            'title_vii': 1.0, 'disparate_impact': 1.0, 'testing_requirements': 0.8,
            'statutory_interpretation': 0.7
        },
        "metadata": {
            "citation": "401 U.S. 424 (1971)",
            "court": "Supreme Court",
            "precedent_weight": 1.0,
            "jurisdiction": "Federal",
            "area_of_law": "Employment Discrimination",
            "year": 1971
        }
    },

    # Family Law Cases
    'loving_v_virginia': {
        "factors": {
            'constitutional_law': 1.0, 'civil_rights': 1.0, 'family_law': 1.0,
            'marriage_rights': 1.0, 'equal_protection': 1.0, 'due_process': 0.8,
            'racial_discrimination': 1.0
        },
        "metadata": {
            "citation": "388 U.S. 1 (1967)",
            "court": "Supreme Court",
            "precedent_weight": 1.0,
            "jurisdiction": "Federal",
            "area_of_law": "Family/Civil Rights",
            "year": 1967
        }
    },

    # Environmental Law Cases
    'massachusetts_v_epa': {
        "factors": {
            'environmental_law': 1.0, 'administrative_law': 1.0, 'climate_change': 0.9,
            'standing': 0.8, 'statutory_interpretation': 0.9, 'regulatory_law': 0.9,
            'clean_air_act': 1.0
        },
        "metadata": {
            "citation": "549 U.S. 497 (2007)",
            "court": "Supreme Court",
            "precedent_weight": 0.9,
            "jurisdiction": "Federal",
            "area_of_law": "Environmental/Administrative",
            "year": 2007
        }
    },

    # Intellectual Property Cases
    'diamond_v_chakrabarty': {
        "factors": {
            'intellectual_property': 1.0, 'patent_law': 1.0, 'biotechnology': 0.9,
            'patentable_subject_matter': 1.0, 'statutory_interpretation': 0.8,
            'scientific_innovation': 0.7
        },
        "metadata": {
            "citation": "447 U.S. 303 (1980)",
            "court": "Supreme Court",
            "precedent_weight": 0.9,
            "jurisdiction": "Federal",
            "area_of_law": "Intellectual Property",
            "year": 1980
        }
    },

    # Administrative Law Cases
    'chevron_v_nrdc': {
        "factors": {
            'administrative_law': 1.0, 'statutory_interpretation': 1.0, 'agency_deference': 1.0,
            'environmental_law': 0.6, 'regulatory_law': 0.9, 'separation_of_powers': 0.7,
            'judicial_review': 0.8
        },
        "metadata": {
            "citation": "467 U.S. 837 (1984)",
            "court": "Supreme Court",
            "precedent_weight": 0.9,
            "jurisdiction": "Federal",
            "area_of_law": "Administrative Law",
            "year": 1984
        }
    },

    # Evidence/Procedure Cases
    'frye_v_united_states': {
        "factors": {
            'evidence_procedure': 1.0, 'scientific_evidence': 1.0, 'expert_testimony': 1.0,
            'criminal_law': 0.6, 'admissibility_standards': 1.0, 'common_law': 0.8
        },
        "metadata": {
            "citation": "293 F. 1013 (D.C. Cir. 1923)",
            "court": "D.C. Circuit Court of Appeals",
            "precedent_weight": 0.7,  # Superseded by Daubert in federal courts
            "jurisdiction": "Federal",
            "area_of_law": "Evidence",
            "year": 1923
        }
    },

    'daubert_v_merrell_dow': {
        "factors": {
            'evidence_procedure': 1.0, 'scientific_evidence': 1.0, 'expert_testimony': 1.0,
            'tort_law': 0.5, 'product_liability': 0.4, 'admissibility_standards': 1.0,
            'judicial_gatekeeping': 1.0
        },
        "metadata": {
            "citation": "509 U.S. 579 (1993)",
            "court": "Supreme Court",
            "precedent_weight": 1.0,
            "jurisdiction": "Federal",
            "area_of_law": "Evidence",
            "year": 1993
        }
    },

    # Recent Technology Cases
    'carpenter_v_united_states': {
        "factors": {
            'constitutional_law': 0.9, 'criminal_law': 0.8, 'privacy_rights': 1.0,
            'fourth_amendment': 1.0, 'technology_law': 1.0, 'digital_privacy': 1.0,
            'surveillance': 0.9
        },
        "metadata": {
            "citation": "585 U.S. ___ (2018)",
            "court": "Supreme Court",
            "precedent_weight": 0.9,
            "jurisdiction": "Federal",
            "area_of_law": "Privacy/Technology",
            "year": 2018
        }
    },

    # Commercial Law Cases  
    'ucc_battle_of_forms': {
        "factors": {
            'contract_law': 1.0, 'commercial_law': 1.0, 'offer_acceptance': 0.9,
            'uniform_commercial_code': 1.0, 'conflicting_terms': 1.0, 'sales_law': 0.9,
            'statutory_interpretation': 0.6
        },
        "metadata": {
            "citation": "UCC § 2-207 cases (various)",
            "court": "Various",
            "precedent_weight": 0.8,
            "jurisdiction": "State/Uniform",
            "area_of_law": "Commercial/Sales",
            "year": 1960
        }
    }
}


class WhiteBoxLegalCaseMatcher:
    """
    A white-box system for matching legal cases based on geometric similarity
    in a multi-dimensional legal factor space.
    """
    
    def __init__(self, case_knowledge_base):
        self.kb = case_knowledge_base
        
        # Extract all unique legal factors from the knowledge base
        all_factors = set()
        for case_data in self.kb.values():
            all_factors.update(case_data["factors"].keys())
        self.legal_factors = sorted(list(all_factors))
        
        # Create vectors for each precedent case
        self.case_vectors = {}
        for case_name, case_data in self.kb.items():
            vector = np.zeros(len(self.legal_factors))
            for factor, value in case_data["factors"].items():
                if factor in self.legal_factors:
                    idx = self.legal_factors.index(factor)
                    vector[idx] = value
            self.case_vectors[case_name] = vector

    def encode_case_factors(self, case_factors):
        """Convert case factors to vector representation"""
        factor_vector = np.zeros(len(self.legal_factors))
        for factor, strength in case_factors.items():
            if factor in self.legal_factors:
                idx = self.legal_factors.index(factor)
                factor_vector[idx] = strength
        return factor_vector

    def find_similar_cases(self, case_factors, top_n=5, apply_precedent_weight=True):
        """
        Find similar precedent cases based on legal factor similarity
        
        Args:
            case_factors: Dictionary of legal factors and their strengths (0.0-1.0)
            top_n: Number of similar cases to return
            apply_precedent_weight: Whether to weight results by precedential strength
        """
        case_vector = self.encode_case_factors(case_factors)
        
        # If the case vector is empty, return empty results
        if np.linalg.norm(case_vector) == 0:
            return []
        
        similarities = {}
        for case_name, precedent_vector in self.case_vectors.items():
            # Calculate geometric similarity
            similarity = cosine_similarity([case_vector], [precedent_vector])[0][0]
            
            # Apply precedent weight if requested
            if apply_precedent_weight:
                precedent_weight = self.kb[case_name]["metadata"].get("precedent_weight", 0.5)
                # Weight the similarity by precedential strength
                weighted_similarity = similarity * precedent_weight
                similarities[case_name] = (weighted_similarity, similarity, precedent_weight)
            else:
                similarities[case_name] = (similarity, similarity, 1.0)
        
        # Sort by weighted similarity (or raw similarity if not weighted)
        sorted_cases = sorted(similarities.items(), key=lambda x: x[1][0], reverse=True)
        return sorted_cases[:top_n]

    def explain_case_match(self, case_factors, matched_case):
        """Provide detailed explanation of why cases match"""
        if matched_case not in self.case_vectors:
            print(f"Explanation for '{matched_case}' cannot be provided (not in knowledge base).")
            return
        
        case_vector = self.encode_case_factors(case_factors)
        precedent_vector = self.case_vectors[matched_case]
        metadata = self.kb[matched_case].get('metadata', {})
        
        print(f"\n--- Legal Analysis for {matched_case.upper().replace('_', ' ')} ---")
        if metadata:
            print(f"  Citation: {metadata.get('citation', 'N/A')}")
            print(f"  Court: {metadata.get('court', 'N/A')}")
            print(f"  Area of Law: {metadata.get('area_of_law', 'N/A')}")
            print(f"  Precedent Weight: {metadata.get('precedent_weight', 'N/A')}")
            print(f"  Year: {metadata.get('year', 'N/A')}")
        
        print("\nLegal Factor Analysis (Your Case × Precedent Strength):")
        
        # Calculate factor contributions
        contributions = []
        for i, factor in enumerate(self.legal_factors):
            your_case_strength = case_vector[i]
            if your_case_strength > 0:  # Only show factors present in your case
                precedent_strength = precedent_vector[i]
                contribution = your_case_strength * precedent_strength
                contributions.append((factor, your_case_strength, precedent_strength, contribution))
        
        # Sort by contribution strength
        contributions.sort(key=lambda x: x[3], reverse=True)
        
        for factor, your_strength, precedent_strength, contribution in contributions:
            print(f"  - {factor:<25} | Your Case: {your_strength:.1f}, Precedent: {precedent_strength:.1f} -> Match: {contribution:.2f}")


class LegalTestHarness:
    """Test harness for validating the legal case matching system"""
    
    def __init__(self, legal_matcher):
        self.matcher = legal_matcher
        self.cases = list(legal_matcher.kb.keys())

    def create_archetypal_case(self, case_name):
        """Create a test case based on a known precedent's factors"""
        return self.matcher.kb[case_name]["factors"]

    def run_self_matching_test(self):
        """Test if each case matches itself when used as input"""
        print("="*80)
        print("           LEGAL CASE MATCHING SYSTEM - SELF-MATCHING TEST")
        print("="*80)
        
        correct_matches = 0
        total_tests = len(self.cases)
        
        for case in self.cases:
            archetype_factors = self.create_archetypal_case(case)
            similar_cases = self.matcher.find_similar_cases(archetype_factors, top_n=1)
            
            top_match = similar_cases[0][0] if similar_cases else "N/A"
            if top_match == case:
                correct_matches += 1
            else:
                print(f"MISMATCH: {case} matched to {top_match}")
        
        accuracy = (correct_matches / total_tests) * 100 if total_tests > 0 else 0
        print(f"\nSelf-Matching Accuracy: {correct_matches}/{total_tests} = {accuracy:.2f}%")
        return accuracy


# --- Main Execution and Demo ---
if __name__ == "__main__":
    # Initialize the legal case matching system
    legal_matcher = WhiteBoxLegalCaseMatcher(LEGAL_CASE_KNOWLEDGE_BASE)
    test_harness = LegalTestHarness(legal_matcher)
    
    # Run validation test
    test_harness.run_self_matching_test()
    
    # --- DEMO: New Case Analysis ---
    print("\n" + "="*80)
    print("                    NEW CASE ANALYSIS DEMO")
    print("="*80)
    
    # Test Case 1: Constitutional Privacy Case
    print("\n--- TEST CASE 1: Constitutional Privacy Case ---")
    new_case_1 = {
        'constitutional_law': 0.9,
        'privacy_rights': 0.8,
        'due_process': 0.7,
        'technology_law': 0.6,
        'fourth_amendment': 0.5
    }
    
    print("New Case Factors:", new_case_1)
    similar_cases_1 = legal_matcher.find_similar_cases(new_case_1, top_n=5)
    
    print("\nMost Similar Precedents:")
    for case, (weighted_sim, raw_sim, precedent_weight) in similar_cases_1:
        print(f"  - {case:<30} | Weighted: {weighted_sim:.3f} | Raw: {raw_sim:.3f} | Precedent: {precedent_weight:.1f}")
    
    if similar_cases_1:
        legal_matcher.explain_case_match(new_case_1, similar_cases_1[0][0])
    
    # Test Case 2: Contract Dispute
    print("\n" + "="*60)
    print("\n--- TEST CASE 2: Commercial Contract Dispute ---")
    new_case_2 = {
        'contract_law': 1.0,
        'breach_of_contract': 0.8,
        'commercial_law': 0.9,
        'damages_remedies': 0.7,
        'foreseeability': 0.6
    }
    
    print("New Case Factors:", new_case_2)
    similar_cases_2 = legal_matcher.find_similar_cases(new_case_2, top_n=5)
    
    print("\nMost Similar Precedents:")
    for case, (weighted_sim, raw_sim, precedent_weight) in similar_cases_2:
        print(f"  - {case:<30} | Weighted: {weighted_sim:.3f} | Raw: {raw_sim:.3f} | Precedent: {precedent_weight:.1f}")
    
    if similar_cases_2:
        legal_matcher.explain_case_match(new_case_2, similar_cases_2[0][0])
    
    # Test Case 3: Employment Discrimination  
    print("\n" + "="*60)
    print("\n--- TEST CASE 3: Employment Discrimination ---")
    new_case_3 = {
        'employment_law': 1.0,
        'discrimination': 0.9,
        'civil_rights': 0.8,
        'constitutional_law': 0.4,
        'statutory_interpretation': 0.5
    }
    
    print("New Case Factors:", new_case_3)
    similar_cases_3 = legal_matcher.find_similar_cases(new_case_3, top_n=5)
    
    print("\nMost Similar Precedents:")
    for case, (weighted_sim, raw_sim, precedent_weight) in similar_cases_3:
        print(f"  - {case:<30} | Weighted: {weighted_sim:.3f} | Raw: {raw_sim:.3f} | Precedent: {precedent_weight:.1f}")
    
    if similar_cases_3:
        legal_matcher.explain_case_match(new_case_3, similar_cases_3[0][0])

    print("\n" + "="*80)
    print("Analysis complete. The system successfully matches cases based on")
    print("geometric similarity in legal factor space, weighted by precedential strength.")
    print("="*80)
