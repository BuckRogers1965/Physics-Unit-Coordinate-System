import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

"""
================================================================================
 White-Box Geometric Classifier Engine
================================================================================

Author: J. Rogers
Date: June 2025

--- High-Level Overview ---

This program demonstrates a universal, white-box reasoning architecture. It
classifies concepts (animals, diseases, legal cases, etc.) by representing
them as vectors in a high-dimensional "conceptual space." Each axis of this
space is a fundamental, named trait.

Diagnosis or classification is reduced to a simple, deterministic geometric
measurement: finding the known concept vector that is most closely aligned with
the vector of an unknown observation.

The core principle is that the system's knowledge is explicitly architected,
not statistically learned. It is 100% transparent, explainable, and robust.
The knowledge base is separated from the logic engine, making it trivially
easy to maintain and extend.

This implementation uses a mixed knowledge base of real and mythical creatures
to prove the system's ability to reason about both physical and ontological
traits.
================================================================================
"""

# ==============================================================================
# The Single Source of Truth: The Knowledge Base
# To add a new creature or trait, simply edit this dictionary.
# The 'is_mythical' trait is the key ontological differentiator.
# ==============================================================================
KNOWLEDGE_BASE = {
    # --- Real Mammals ---
    'horse': {
        "traits": {'is_mammal': 1.0, 'has_fur': 0.8, 'is_herbivore': 1.0, 'is_domesticated': 0.9, 'has_four_legs': 1.0, 'is_fast_runner': 0.9},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },
    'lion': {
        "traits": {'is_mammal': 1.0, 'has_fur': 0.9, 'is_carnivore': 1.0, 'is_predator': 1.0, 'lives_in_savannah': 0.8, 'is_feline': 0.9, 'has_four_legs': 1.0},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },
    'bat': {
        "traits": {'is_mammal': 1.0, 'has_fur': 0.7, 'can_fly': 0.9, 'is_nocturnal': 1.0, 'eats_insects': 0.8},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },
    'dolphin': {
        "traits": {'is_mammal': 1.0, 'can_swim': 1.0, 'is_intelligent': 0.95, 'echolocates': 1.0, 'lives_in_water': 1.0, 'has_fur': 0.0},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },
    'elephant': {
        "traits": {'is_mammal': 1.0, 'is_herbivore': 1.0, 'has_trunk': 1.0, 'has_tusks': 1.0, 'has_four_legs': 1.0, 'is_large': 1.0, 'is_social': 0.9},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },
    'wolf': {
        "traits": {'is_mammal': 1.0, 'is_carnivore': 1.0, 'howls': 1.0, 'is_predator': 1.0, 'is_social': 0.9, 'has_four_legs': 1.0},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },
    'platypus': {
        "traits": {'is_mammal': 1.0, 'lays_eggs': 1.0, 'can_swim': 1.0, 'has_beak': 1.0, 'has_fur': 0.7, 'is_venomous': 0.2},
        "metadata": {"class": "Mammalia", "type": "Real"}
    },

    # --- Real Birds ---
    'eagle': {
        "traits": {'is_bird': 1.0, 'has_feathers': 1.0, 'can_fly': 1.0, 'is_carnivore': 1.0, 'is_predator': 1.0, 'has_beak': 1.0, 'has_talons': 0.9},
        "metadata": {"class": "Aves", "type": "Real"}
    },
    'penguin': {
        "traits": {'is_bird': 1.0, 'has_feathers': 1.0, 'can_fly': 0.0, 'can_swim': 1.0, 'lives_in_cold': 1.0},
        "metadata": {"class": "Aves", "type": "Real"}
    },
    'owl': {
        "traits": {'is_bird': 1.0, 'has_feathers': 1.0, 'is_nocturnal': 1.0, 'can_fly': 1.0, 'rotates_head': 1.0, 'is_predator': 0.9},
        "metadata": {"class": "Aves", "type": "Real"}
    },

    
    # --- Real Reptiles ---

    'snake': {
        "traits": {'is_reptile': 1.0, 'has_scales': 1.0, 'is_carnivore': 1.0, 'is_legless': 1.0, 'is_venomous': 0.3},
        "metadata": {"class": "Reptilia", "type": "Real"}
    },
    'crocodile': {
        "traits": {'is_reptile': 1.0, 'has_scales': 1.0, 'is_carnivore': 1.0, 'can_swim': 1.0, 'is_predator': 1.0, 'lives_in_water': 0.9},
        "metadata": {"class": "Reptilia", "type": "Real"}
    },
    'chameleon': {
        "traits": {'is_reptile': 1.0, 'has_scales': 1.0, 'can_change_color': 1.0, 'is_insectivore': 1.0, 'has_eyesight': 0.95},
        "metadata": {"class": "Reptilia", "type": "Real"}
    },


    # --- Real Fish ---

    'clownfish': {
        "traits": {'is_fish': 1.0, 'can_swim': 1.0, 'is_small': 1.0, 'lives_in_coral_reef': 1.0, 'is_colorful': 0.9},
        "metadata": {"class": "Actinopterygii", "type": "Real"}
    },
    'shark': {
        "traits": {'is_fish': 1.0, 'is_predator': 1.0, 'can_smell_blood': 1.0, 'can_swim': 1.0, 'is_large': 1.0, 'is_carnivore': 1.0},
        "metadata": {"class": "Chondrichthyes", "type": "Real"}
    },

    # --- Extinct Land Animals ---
    'woolly_mammoth': {
        "traits": {'is_mammal': 1.0, 'has_fur': 1.0, 'is_herbivore': 1.0, 'has_tusks': 1.0, 'lives_in_cold': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Mammalia", "type": "Extinct"}
    },
    'saber_tooth_cat': {
        "traits": {'is_mammal': 1.0, 'is_predator': 1.0, 'has_fur': 1.0, 'has_saber_teeth': 1.0, 'is_carnivore': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Mammalia", "type": "Extinct"}
    },

    # --- Extinct Dinosaurs (Land/Flying) ---
    'tyrannosaurus_rex': {
        "traits": {'is_reptile': 1.0, 'is_carnivore': 1.0, 'has_teeth': 1.0, 'is_large': 1.0, 'has_small_arms': 1.0, 'is_predator': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Theropoda", "type": "Dinosaur"}
    },
    'triceratops': {
        "traits": {'is_reptile': 1.0, 'is_herbivore': 1.0, 'has_horns': 1.0, 'has_frill': 1.0, 'has_four_legs': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Ceratopsidae", "type": "Dinosaur"}
    },
    'stegosaurus': {
        "traits": {'is_reptile': 1.0, 'is_herbivore': 1.0, 'has_plates': 1.0, 'has_spiked_tail': 1.0, 'has_four_legs': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Stegosauria", "type": "Dinosaur"}
    },
    'velociraptor': {
        "traits": {'is_reptile': 1.0, 'is_carnivore': 1.0, 'is_fast_runner': 1.0, 'has_claws': 1.0, 'is_intelligent': 0.8, 'is_predator': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Dromaeosauridae", "type": "Dinosaur"}
    },

    # --- Flying Prehistoric ---
    'pteranodon': {
        "traits": {'is_reptile': 1.0, 'can_fly': 1.0, 'has_wings': 1.0, 'has_beak': 1.0, 'is_carnivore': 0.8, 'is_extinct': 1.0},
        "metadata": {"class": "Pterosauria", "type": "Prehistoric Flying"}
    },
    'archaeopteryx': {
        "traits": {'is_bird': 0.6, 'is_reptile': 0.6, 'can_fly': 0.8, 'has_feathers': 1.0, 'has_teeth': 0.7, 'is_extinct': 1.0},
        "metadata": {"class": "Avialae", "type": "Prehistoric Flying"}
    },

    # --- Aquatic Extinct Species ---
    'megalodon': {
        "traits": {'is_fish': 1.0, 'is_predator': 1.0, 'is_large': 1.0, 'can_swim': 1.0, 'is_extinct': 1.0, 'is_carnivore': 1.0},
        "metadata": {"class": "Chondrichthyes", "type": "Extinct Aquatic"}
    },
    'plesiosaurus': {
        "traits": {'is_reptile': 1.0, 'can_swim': 1.0, 'has_long_neck': 1.0, 'has_flippers': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Sauropterygia", "type": "Extinct Aquatic"}
    },
    'ichthyosaurus': {
        "traits": {'is_reptile': 1.0, 'can_swim': 1.0, 'has_fins': 1.0, 'is_carnivore': 1.0, 'is_extinct': 1.0},
        "metadata": {"class": "Ichthyosauria", "type": "Extinct Aquatic"}
    },


    # --- Mythical Creatures ---

    'dragon': {
        "traits": {'is_reptile': 0.9, 'has_scales': 1.0, 'can_fly': 1.0, 'is_carnivore': 1.0, 'is_predator': 1.0, 'breathes_fire': 1.0, 'is_intelligent': 0.8, 'is_mythical': 2.0},
        "metadata": {"class": "Draconic", "type": "Mythical"}
    },
    'unicorn': {
        "traits": {'is_mammal': 1.0, 'has_fur': 0.8, 'is_herbivore': 1.0, 'has_four_legs': 1.0, 'has_horn': 1.0, 'is_magical': 0.9, 'is_mythical': 2.0},
        "metadata": {"class": "Equine", "type": "Mythical"}
    },
    'pegasus': {
        "traits": {'is_mammal': 1.0, 'has_fur': 0.8, 'is_herbivore': 1.0, 'has_four_legs': 1.0, 'is_fast_runner': 0.9, 'can_fly': 1.0, 'is_mythical': 2.0},
        "metadata": {"class": "Equine", "type": "Mythical"}
    },
    'griffin': {
        "traits": {'is_mammal': 0.5, 'is_bird': 0.5, 'can_fly': 1.0, 'has_beak': 1.0, 'has_talons': 1.0, 'is_predator': 1.0, 'has_fur': 0.9, 'is_predator': 1.0, 'is_feline': 0.9, 'has_four_legs': 1.0, 'is_mythical': 2.0},
        "metadata": {"class": "Hybrid", "type": "Mythical"}
    },
    'mermaid': {
        "traits": {'is_mammal': 0.9, 'can_swim': 1.0, 'is_intelligent': 0.9, 'is_mythical': 2.0, 'has_fish_tail': 1.0, 'is_humanoid': 0.8},
        "metadata": {"class": "Aquatic-Hybrid", "type": "Mythical"}
    },
    'phoenix': {
        "traits": {'is_bird': 1.0, 'can_fly': 1.0, 'has_feathers': 1.0, 'is_immortal': 1.0, 'rebirth_from_ashes': 1.0, 'is_mythical': 2.0},
        "metadata": {"class": "Mystic-Aves", "type": "Mythical"}
    },
    'kraken': {
        "traits": {'is_cephalopod': 1.0, 'is_predator': 1.0, 'can_swim': 1.0, 'is_large': 1.0, 'has_tentacles': 1.0, 'is_mythical': 2.0},
        "metadata": {"class": "Mythical-Cephalopoda", "type": "Mythical"}
    }
}


class WhiteBoxClassifier:
    """A generic, white-box classifier using the geometric similarity model."""
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        
        # Discover all unique traits automatically to create the conceptual axes
        all_traits = set()
        for item_data in self.kb.values():
            all_traits.update(item_data["traits"].keys())
        
        self.trait_axes = sorted(list(all_traits))
        
        # Build the item vectors dynamically from the knowledge base
        self.item_vectors = {}
        for item_name, item_data in self.kb.items():
            vector = np.zeros(len(self.trait_axes))
            for trait, value in item_data["traits"].items():
                if trait in self.trait_axes:
                    idx = self.trait_axes.index(trait)
                    vector[idx] = value
            self.item_vectors[item_name] = vector
        
    def encode_observation(self, observed_traits):
        """Convert observed traits into a vector in the trait space."""
        observation_vector = np.zeros(len(self.trait_axes))
        for trait, intensity in observed_traits.items():
            if trait in self.trait_axes:
                idx = self.trait_axes.index(trait)
                observation_vector[idx] = intensity
        return observation_vector
    
    def classify(self, observed_traits, top_n=3):
        """Classify by finding the item vector most similar to the observation vector."""
        observation_vector = self.encode_observation(observed_traits)
        if np.linalg.norm(observation_vector) == 0: return []
        
        similarities = {}
        for item_name, item_vector in self.item_vectors.items():
            similarity = cosine_similarity([observation_vector], [item_vector])[0][0]
            similarities[item_name] = similarity
        
        sorted_classifications = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_classifications[:top_n]
    
    def explain_classification(self, observed_traits, classification):
        """Provide a transparent breakdown of the classification."""
        if classification not in self.item_vectors:
            print(f"Explanation for '{classification}' cannot be provided.")
            return

        observation_vector = self.encode_observation(observed_traits)
        item_vector = self.item_vectors[classification]
        metadata = self.kb[classification].get('metadata', {})
        
        print(f"\n--- Explanation for {classification.upper()} ---")
        if metadata:
            print(f"  Type: {metadata.get('type', 'N/A')}, Class: {metadata.get('class', 'N/A')}")
        print("Trait contributions (Observation Strength * Creature Pattern Strength):")
        
        contributions = []
        for i, trait in enumerate(self.trait_axes):
            obs_val = observation_vector[i]
            if obs_val > 0:
                item_val = item_vector[i]
                contribution = obs_val * item_val
                contributions.append((trait, obs_val, item_val, contribution))
        
        contributions.sort(key=lambda x: x[3], reverse=True)
        for trait, obs_val, item_val, contribution in contributions:
            print(f"  - {trait:<25} | Observed: {obs_val:.1f}, Creature Pattern: {item_val:.1f} -> Match: {contribution:.2f}")

# ==============================================================================
# Main Execution Block - Demonstrating Core Logic
# ==============================================================================

# ==============================================================================
# Main Execution Block - Systematic Demonstration of Ontological Disambiguation
# ==============================================================================
if __name__ == "__main__":
    # Instantiate the classifier ONCE with the complete knowledge base.
    classifier = WhiteBoxClassifier(KNOWLEDGE_BASE)
    
    # Define which creatures in the KB are considered "real" for the test
    real_animals = [name for name, data in KNOWLEDGE_BASE.items() if data.get('metadata', {}).get('type') == 'Real']

    print("="*80)
    print("      WHITE-BOX CLASSIFIER: REALITY vs. MYTHOLOGY TEST")
    print("="*80)

    # ==============================================================================
    # STAGE 1: IDENTIFYING REAL ANIMALS FROM REAL TRAITS
    # ==============================================================================
    print("\n\n--- STAGE 1: Testing Identification of Real Animals ---")
    print("The system is given traits for known real animals. The 'is_mythical' trait is implicitly 0.")
    print("-" * 80)
    
    correct_identifications = 0
    for animal_name in real_animals:
        print(f"\n>>> Testing Archetype: {animal_name.upper()}")
        
        # Create an observation based on the real animal's traits from the KB
        observed_traits = {k: v for k, v in KNOWLEDGE_BASE[animal_name]['traits'].items() if k != 'is_mythical'}
        
        # Get the top 5 classifications to see the differential
        classifications = classifier.classify(observed_traits, top_n=5)
        
        if classifications:
            print("    Top Matches:")
            top_match = classifications[0][0]
            for creature, score in classifications:
                creature_type = KNOWLEDGE_BASE.get(creature, {}).get('metadata', {}).get('type', 'N/A')
                # Add a checkmark for the correct identification
                hit_marker = "✅" if creature == animal_name else "  "
                print(f"      {hit_marker} - {creature:<10} (Type: {creature_type:<8}) | Similarity: {score:.3f}")

            if top_match == animal_name:
                correct_identifications += 1
        else:
            print("    [FAIL] No classification returned.")

    print("\n" + "-"*80)
    print(f"Stage 1 Summary: Correctly identified {correct_identifications}/{len(real_animals)} real animals as the top match.")
    print("-" * 80)


    # ==============================================================================
    # STAGE 2: FINDING THE "CLOSEST MYTHICAL RELATIVE"
    # ==============================================================================
    print("\n\n--- STAGE 2: Augmenting Real Animals with the 'is_mythical' Trait ---")
    print("We now take the same physical traits, but assert 'is_mythical': 2.0.")
    print("This forces the system to find the closest mythical relative.")
    print("-" * 80)

    for animal_name in real_animals:
        print(f"\n>>> Mythical counterpart for: {animal_name.upper()}")
        
        # Start with the same physical traits as before
        observed_traits = {k: v for k, v in KNOWLEDGE_BASE[animal_name]['traits'].items() if k != 'is_mythical'}
        
        # Assert the observation is mythical
        observed_traits['is_mythical'] = 2.0

        # Get the top 5 classifications
        classifications = classifier.classify(observed_traits, top_n=5)

        if classifications:
            print("    Top Matches:")
            for creature, score in classifications:
                creature_type = KNOWLEDGE_BASE.get(creature, {}).get('metadata', {}).get('type', 'N/A')
                print(f"      - {creature:<10} (Type: {creature_type:<8}) | Similarity: {score:.3f}")
        else:
            print("    [FAIL] No classification returned.")

    print("\n" + "-"*80)
    print("Stage 2 Summary: Demonstrated how adding the ontological 'is_mythical' axis fundamentally changes the classification outcome.")
    print("=" * 80)
