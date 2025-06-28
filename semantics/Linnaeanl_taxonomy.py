import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

"""
================================================================================
 White-Box Traditional Taxonomic Classifier Engine
================================================================================

Author: J. Rogers (Updated for Traditional Linnaean Taxonomy)
Date: June 2025

--- High-Level Overview ---

This program demonstrates traditional Linnaean taxonomy based on morphological
characteristics - the way Carl Linnaeus and classical taxonomists classified
animals by observable physical traits and structures.

Uses historical taxonomic criteria: body structure, skeletal system, 
body covering, appendages, reproductive features, and feeding apparatus.

================================================================================
"""

# ==============================================================================
# The Single Source of Truth: Traditional Morphological Knowledge Base
# Based on classical Linnaean taxonomy using observable physical characteristics
# ==============================================================================
KNOWLEDGE_BASE = {
    # --- CLASS MAMMALIA (Hair/fur, warm-blooded, milk production) ---
    'horse': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'single_hoof': 1.0, 'herbivore_teeth': 1.0,
            'large_molars': 1.0, 'elongated_skull': 1.0, 'long_tail': 1.0, 'mane_present': 0.8
        },
        "metadata": {"class": "Mammalia", "order": "Perissodactyla", "family": "Equidae", "status": "Living"}
    },
    
    'zebra': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'single_hoof': 1.0, 'herbivore_teeth': 1.0,
            'large_molars': 1.0, 'elongated_skull': 1.0, 'long_tail': 1.0, 'striped_pattern': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Perissodactyla", "family": "Equidae", "status": "Living"}
    },
    
    'rhinoceros': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 0.2, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'three_toes': 1.0, 'herbivore_teeth': 1.0,
            'thick_skin': 1.0, 'horn_on_nose': 1.0, 'massive_body': 1.0, 'short_tail': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Perissodactyla", "family": "Rhinocerotidae", "status": "Living"}
    },
    
    'lion': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'retractable_claws': 1.0, 'carnivore_teeth': 1.0,
            'prominent_canines': 1.0, 'short_snout': 1.0, 'long_tail': 1.0, 'mane_present': 0.5
        },
        "metadata": {"class": "Mammalia", "order": "Carnivora", "family": "Felidae", "status": "Living"}
    },
    
    'tiger': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'retractable_claws': 1.0, 'carnivore_teeth': 1.0,
            'prominent_canines': 1.0, 'short_snout': 1.0, 'long_tail': 1.0, 'striped_pattern': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Carnivora", "family": "Felidae", "status": "Living"}
    },
    
    'domestic_cat': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'retractable_claws': 1.0, 'carnivore_teeth': 1.0,
            'prominent_canines': 1.0, 'short_snout': 1.0, 'long_tail': 1.0, 'small_body_size': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Carnivora", "family": "Felidae", "status": "Living"}
    },
    
    'wolf': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'non_retractable_claws': 1.0, 'carnivore_teeth': 1.0,
            'prominent_canines': 1.0, 'elongated_snout': 1.0, 'long_tail': 1.0, 'erect_ears': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Carnivora", "family": "Canidae", "status": "Living"}
    },
    
    'domestic_dog': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'non_retractable_claws': 1.0, 'carnivore_teeth': 1.0,
            'prominent_canines': 1.0, 'elongated_snout': 0.8, 'long_tail': 0.8, 'variable_ears': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Carnivora", "family": "Canidae", "status": "Living"}
    },
    
    'elephant': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 0.1, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'columnar_legs': 1.0, 'herbivore_teeth': 1.0,
            'trunk_elongated': 1.0, 'tusks_present': 0.7, 'massive_body': 1.0, 'large_ears': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Proboscidea", "family": "Elephantidae", "status": "Living"}
    },
    
    'mammoth': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'columnar_legs': 1.0, 'herbivore_teeth': 1.0,
            'trunk_elongated': 1.0, 'tusks_present': 1.0, 'massive_body': 1.0, 'curved_tusks': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Proboscidea", "family": "Elephantidae", "status": "Extinct"}
    },
    
    'saber_tooth_cat': {
        "traits": {
            'has_vertebrae': 1.0, 'has_hair_fur': 1.0, 'warm_blooded': 1.0, 'produces_milk': 1.0,
            'live_birth': 1.0, 'four_limbs': 1.0, 'retractable_claws': 1.0, 'carnivore_teeth': 1.0,
            'enlarged_canines': 1.0, 'short_snout': 1.0, 'muscular_build': 1.0, 'robust_skull': 1.0
        },
        "metadata": {"class": "Mammalia", "order": "Carnivora", "family": "Felidae", "status": "Extinct"}
    },
    
    # --- CLASS AVES (Feathers, wings, beak, lay eggs) ---
    'eagle': {
        "traits": {
            'has_vertebrae': 1.0, 'has_feathers': 1.0, 'warm_blooded': 1.0, 'lays_eggs': 1.0,
            'hard_shelled_eggs': 1.0, 'two_wings': 1.0, 'two_legs': 1.0, 'beak_present': 1.0,
            'hooked_beak': 1.0, 'talons_present': 1.0, 'hollow_bones': 1.0, 'keen_vision': 1.0
        },
        "metadata": {"class": "Aves", "order": "Accipitriformes", "family": "Accipitridae", "status": "Living"}
    },
    
    'sparrow': {
        "traits": {
            'has_vertebrae': 1.0, 'has_feathers': 1.0, 'warm_blooded': 1.0, 'lays_eggs': 1.0,
            'hard_shelled_eggs': 1.0, 'two_wings': 1.0, 'two_legs': 1.0, 'beak_present': 1.0,
            'straight_beak': 1.0, 'small_body_size': 1.0, 'hollow_bones': 1.0, 'perching_feet': 1.0
        },
        "metadata": {"class": "Aves", "order": "Passeriformes", "family": "Passeridae", "status": "Living"}
    },
    
    'dodo': {
        "traits": {
            'has_vertebrae': 1.0, 'has_feathers': 1.0, 'warm_blooded': 1.0, 'lays_eggs': 1.0,
            'hard_shelled_eggs': 1.0, 'vestigial_wings': 1.0, 'two_legs': 1.0, 'beak_present': 1.0,
            'large_beak': 1.0, 'flightless': 1.0, 'heavy_body': 1.0, 'short_wings': 1.0
        },
        "metadata": {"class": "Aves", "order": "Columbiformes", "family": "Columbidae", "status": "Extinct"}
    },
    
    # --- CLASS REPTILIA (Scales, cold-blooded, lay eggs) ---
    'crocodile': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'leathery_eggs': 1.0, 'four_limbs': 1.0, 'elongated_body': 1.0, 'carnivore_teeth': 1.0,
            'conical_teeth': 1.0, 'long_tail': 1.0, 'armored_skin': 1.0, 'elongated_snout': 1.0
        },
        "metadata": {"class": "Reptilia", "order": "Crocodilia", "family": "Crocodylidae", "status": "Living"}
    },
    
    'snake': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 0.8,
            'elongated_body': 1.0, 'no_limbs': 1.0, 'carnivore_teeth': 1.0, 'forked_tongue': 1.0,
            'flexible_jaw': 1.0, 'overlapping_scales': 1.0, 'long_vertebral_column': 1.0
        },
        "metadata": {"class": "Reptilia", "order": "Squamata", "family": "Various", "status": "Living"}
    },
    
    'turtle': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 0.3, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'hard_shelled_eggs': 1.0, 'four_limbs': 1.0, 'shell_present': 1.0, 'beak_like_mouth': 1.0,
            'retractable_head': 1.0, 'short_tail': 1.0, 'protective_carapace': 1.0
        },
        "metadata": {"class": "Reptilia", "order": "Testudines", "family": "Various", "status": "Living"}
    },
    
    'tyrannosaurus': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'two_legs': 1.0, 'small_arms': 1.0, 'carnivore_teeth': 1.0, 'massive_skull': 1.0,
            'serrated_teeth': 1.0, 'long_tail': 1.0, 'bipedal_stance': 1.0, 'enormous_size': 1.0
        },
        "metadata": {"class": "Reptilia", "order": "Saurischia", "family": "Tyrannosauridae", "status": "Extinct"}
    },
    
    'triceratops': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'four_limbs': 1.0, 'herbivore_teeth': 1.0, 'beak_like_mouth': 1.0, 'three_horns': 1.0,
            'bony_frill': 1.0, 'massive_skull': 1.0, 'quadrupedal_stance': 1.0, 'enormous_size': 1.0
        },
        "metadata": {"class": "Reptilia", "order": "Ornithischia", "family": "Ceratopsidae", "status": "Extinct"}
    },
    
    # --- CLASS ACTINOPTERYGII (Bony Fish - fins, scales, gills) ---
    'salmon': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'external_fertilization': 1.0, 'fins_present': 1.0, 'gills_present': 1.0, 'streamlined_body': 1.0,
            'lateral_line': 1.0, 'swim_bladder': 1.0, 'bony_skeleton': 1.0, 'overlapping_scales': 1.0
        },
        "metadata": {"class": "Actinopterygii", "order": "Salmoniformes", "family": "Salmonidae", "status": "Living"}
    },
    
    'goldfish': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'external_fertilization': 1.0, 'fins_present': 1.0, 'gills_present': 1.0, 'rounded_body': 1.0,
            'lateral_line': 1.0, 'swim_bladder': 1.0, 'bony_skeleton': 1.0, 'small_body_size': 1.0
        },
        "metadata": {"class": "Actinopterygii", "order": "Cypriniformes", "family": "Cyprinidae", "status": "Living"}
    },
    
    # --- CLASS CHONDRICHTHYES (Cartilaginous Fish - sharks, rays) ---
    'shark': {
        "traits": {
            'has_vertebrae': 1.0, 'has_scales': 0.0, 'cold_blooded': 1.0, 'lays_eggs': 0.6,
            'cartilaginous_skeleton': 1.0, 'fins_present': 1.0, 'gills_present': 1.0, 'streamlined_body': 1.0,
            'multiple_gill_slits': 1.0, 'carnivore_teeth': 1.0, 'replaceable_teeth': 1.0, 'placoid_scales': 1.0
        },
        "metadata": {"class": "Chondrichthyes", "order": "Carcharhiniformes", "family": "Carcharhinidae", "status": "Living"}
    },
    
    # --- CLASS AMPHIBIA (Smooth skin, metamorphosis) ---
    'frog': {
        "traits": {
            'has_vertebrae': 1.0, 'smooth_skin': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'external_fertilization': 1.0, 'four_limbs': 1.0, 'metamorphosis': 1.0, 'moist_skin': 1.0,
            'no_tail_adult': 1.0, 'webbed_feet': 1.0, 'long_hind_legs': 1.0, 'vocal_sac': 0.5
        },
        "metadata": {"class": "Amphibia", "order": "Anura", "family": "Various", "status": "Living"}
    },
    
    'salamander': {
        "traits": {
            'has_vertebrae': 1.0, 'smooth_skin': 1.0, 'cold_blooded': 1.0, 'lays_eggs': 1.0,
            'external_fertilization': 1.0, 'four_limbs': 1.0, 'metamorphosis': 1.0, 'moist_skin': 1.0,
            'long_tail': 1.0, 'elongated_body': 1.0, 'short_legs': 1.0, 'regeneration_ability': 1.0
        },
        "metadata": {"class": "Amphibia", "order": "Caudata", "family": "Various", "status": "Living"}
    }
}


class WhiteBoxClassifier:
    """A traditional taxonomic white-box classifier using morphological characteristics."""
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        
        # Discover all unique traits automatically to create the morphological axes
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
        """Convert observed morphological traits into a vector in the trait space."""
        observation_vector = np.zeros(len(self.trait_axes))
        for trait, intensity in observed_traits.items():
            if trait in self.trait_axes:
                idx = self.trait_axes.index(trait)
                observation_vector[idx] = intensity
        return observation_vector
    
    def classify(self, observed_traits, top_n=3):
        """Classify by finding the animal vector most similar to the observation vector."""
        observation_vector = self.encode_observation(observed_traits)
        if np.linalg.norm(observation_vector) == 0: return []
        
        similarities = {}
        for item_name, item_vector in self.item_vectors.items():
            similarity = cosine_similarity([observation_vector], [item_vector])[0][0]
            similarities[item_name] = similarity
        
        sorted_classifications = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_classifications[:top_n]
    
    def explain_classification(self, observed_traits, classification):
        """Provide a transparent breakdown of the morphological classification."""
        if classification not in self.item_vectors:
            print(f"Explanation for '{classification}' cannot be provided.")
            return

        observation_vector = self.encode_observation(observed_traits)
        item_vector = self.item_vectors[classification]
        metadata = self.kb[classification].get('metadata', {})
        
        print(f"\n--- Morphological Analysis for {classification.upper()} ---")
        if metadata:
            print(f"  Class: {metadata.get('class', 'N/A')}")
            print(f"  Order: {metadata.get('order', 'N/A')}, Family: {metadata.get('family', 'N/A')}")
            print(f"  Status: {metadata.get('status', 'N/A')}")
        print("Morphological trait contributions (Observation * Animal Pattern):")
        
        contributions = []
        for i, trait in enumerate(self.trait_axes):
            obs_val = observation_vector[i]
            if obs_val > 0:
                item_val = item_vector[i]
                contribution = obs_val * item_val
                contributions.append((trait, obs_val, item_val, contribution))
        
        contributions.sort(key=lambda x: x[3], reverse=True)
        for trait, obs_val, item_val, contribution in contributions:
            print(f"  - {trait:<25} | Observed: {obs_val:.1f}, Animal: {item_val:.1f} -> Match: {contribution:.2f}")

    def get_taxonomic_summary(self):
        """Display the taxonomic structure of the knowledge base."""
        class_groups = {}
        for animal, data in self.kb.items():
            class_name = data['metadata']['class']
            if class_name not in class_groups:
                class_groups[class_name] = []
            class_groups[class_name].append(animal)
        
        print("\n=== TAXONOMIC STRUCTURE ===")
        for class_name, animals in sorted(class_groups.items()):
            print(f"\nClass {class_name}:")
            for animal in sorted(animals):
                status = self.kb[animal]['metadata']['status']
                print(f"  - {animal:<15} ({status})")


# ==============================================================================
# Main Execution Block - Traditional Taxonomic Classification Testing
# ==============================================================================
if __name__ == "__main__":
    # Instantiate the classifier with the morphological knowledge base
    classifier = WhiteBoxClassifier(KNOWLEDGE_BASE)
    
    print("="*80)
    print("      TRADITIONAL LINNAEAN TAXONOMIC CLASSIFIER")
    print("      Based on Morphological Characteristics")
    print("="*80)
    
    # Show the taxonomic structure
    classifier.get_taxonomic_summary()

    # ==============================================================================
    # STAGE 1: SELF-RECOGNITION TEST
    # ==============================================================================
    print("\n\n--- STAGE 1: Morphological Self-Recognition Test ---")
    print("Testing if each animal can identify itself using traditional morphological traits.")
    print("-" * 80)
    
    correct_self_identifications = 0
    total_animals = len(KNOWLEDGE_BASE)
    
    for animal_name, animal_data in KNOWLEDGE_BASE.items():
        print(f"\n>>> Testing: {animal_name.upper()}")
        
        # Use the animal's exact morphological traits
        observed_traits = animal_data['traits'].copy()
        
        # Get the top 3 classifications
        classifications = classifier.classify(observed_traits, top_n=3)
        
        if classifications:
            print("    Top morphological matches:")
            top_match = classifications[0][0]
            for i, (creature, score) in enumerate(classifications):
                metadata = KNOWLEDGE_BASE.get(creature, {}).get('metadata', {})
                class_name = metadata.get('class', 'N/A')
                hit_marker = "✅" if creature == animal_name else "  "
                print(f"      {hit_marker} {i+1}. {creature:<15} (Class: {class_name:<12}) | Similarity: {score:.3f}")

            if top_match == animal_name:
                correct_self_identifications += 1
        else:
            print("    [FAIL] No classification returned.")

    print(f"\nSelf-Recognition: {correct_self_identifications}/{total_animals} animals ({(correct_self_identifications/total_animals)*100:.1f}%)")
    
    # ==============================================================================
    # STAGE 2: TRADITIONAL TAXONOMIC CLASS TESTING
    # ==============================================================================
    print("\n\n--- STAGE 2: Classical Taxonomic Class Relationships ---")
    print("Testing morphological similarity within traditional Linnaean classes.")
    print("-" * 80)
    
    # Test relationships within major classes
    test_relationships = [
        ('horse', 'zebra', 'Both Mammalia, same Order (Perissodactyla)'),
        ('lion', 'tiger', 'Both Mammalia, same Family (Felidae)'),
        ('wolf', 'domestic_dog', 'Both Mammalia, same Family (Canidae)'),
        ('elephant', 'mammoth', 'Both Mammalia, same Family (Elephantidae)'),
        ('eagle', 'sparrow', 'Both Aves (birds)'),
        ('crocodile', 'tyrannosaurus', 'Both Reptilia'),
        ('salmon', 'goldfish', 'Both bony fish (Actinopterygii)'),
        ('frog', 'salamander', 'Both Amphibia'),
    ]
    
    for animal1, animal2, relationship in test_relationships:
        if animal1 in KNOWLEDGE_BASE and animal2 in KNOWLEDGE_BASE:
            print(f"\n>>> Morphological Comparison: {animal1.upper()} vs {animal2.upper()}")
            print(f"    Expected relationship: {relationship}")
            
            # Use animal1's traits to find matches
            observed_traits = KNOWLEDGE_BASE[animal1]['traits'].copy()
            classifications = classifier.classify(observed_traits, top_n=5)
            
            # Find where animal2 appears in the ranking
            animal2_rank = None
            for i, (creature, score) in enumerate(classifications):
                if creature == animal2:
                    animal2_rank = i + 1
                    animal2_score = score
                    break
            
            if animal2_rank:
                print(f"    Result: {animal2} ranked #{animal2_rank} (similarity: {animal2_score:.3f})")
                if animal2_rank <= 3:
                    print("    ✅ Strong morphological similarity confirmed!")
                else:
                    print("    ⚠️  Relationship detected but weaker similarity")
            else:
                print(f"    ❌ {animal2} not in top 5 morphological matches")
    
    # ==============================================================================
    # STAGE 3: MORPHOLOGICAL FEATURE ANALYSIS
    # ==============================================================================
    print("\n\n--- STAGE 3: Key Morphological Differentiators ---")
    print("Analyzing which traditional traits best distinguish major animal classes.")
    print("-" * 80)
    
    # Show key distinguishing features for each class
    class_features = {
        'Mammalia': ['has_hair_fur', 'warm_blooded', 'produces_milk', 'live_birth'],
        'Aves': ['has_feathers', 'two_wings', 'beak_present', 'lays_eggs', 'hollow_bones'],
        'Reptilia': ['has_scales', 'cold_blooded', 'lays_eggs'],
        'Actinopterygii': ['fins_present', 'gills_present', 'has_scales', 'bony_skeleton'],
        'Chondrichthyes': ['cartilaginous_skeleton', 'multiple_gill_slits', 'placoid_scales'],
        'Amphibia': ['smooth_skin', 'metamorphosis', 'moist_skin']
    }
    
    print("\nTraditional Linnaean Class Characteristics:")
    for class_name, key_traits in class_features.items():
        animals_in_class = [name for name, data in KNOWLEDGE_BASE.items() 
                           if data['metadata']['class'] == class_name]
        if animals_in_class:
            print(f"\nClass {class_name} ({len(animals_in_class)} species):")
            print(f"  Key morphological traits: {', '.join(key_traits)}")
            print(f"  Examples: {', '.join(animals_in_class[:3])}")
    
    print("\n" + "="*80)
    print("Traditional Morphological Classification Test Complete!")
    print("This demonstrates how Linnaeus would have classified these animals")
    print("based purely on observable physical characteristics.")
    print("="*80)

  # ==============================================================================
    # STAGE 4: FAILURE TEST - Comparing Distantly Related Species
    # ==============================================================================
    print("\n\n--- STAGE 4: Failure Test - Goldfish vs Horse Comparison ---")
    print("Testing the system's behavior when comparing taxonomically distant species.")
    print("This should demonstrate LOW similarity scores between unrelated animals.")
    print("-" * 80)
    
    print(f"\n>>> Using GOLDFISH traits to find matches:")
    goldfish_traits = KNOWLEDGE_BASE['goldfish']['traits'].copy()
    print(f"    Goldfish taxonomy: {KNOWLEDGE_BASE['goldfish']['metadata']}")
    
    classifications = classifier.classify(goldfish_traits, top_n=len(KNOWLEDGE_BASE))
    
    # Find where horse appears in the goldfish classification
    horse_rank = None
    horse_score = None
    for i, (creature, score) in enumerate(classifications):
        if creature == 'horse':
            horse_rank = i + 1
            horse_score = score
            break
    
    print(f"\n    Top 5 matches for goldfish traits:")
    for i, (creature, score) in enumerate(classifications[:5]):
        metadata = KNOWLEDGE_BASE[creature]['metadata']
        hit_marker = "🐟" if creature == 'goldfish' else "  "
        print(f"      {hit_marker} {i+1}. {creature:<15} ({metadata['class']:<12}) | Similarity: {score:.3f}")
    
    print(f"\n    HORSE ranking when using goldfish traits:")
    if horse_rank:
        print(f"      Rank: #{horse_rank}/{len(KNOWLEDGE_BASE)} | Similarity: {horse_score:.3f}")
        if horse_score < 0.3:
            print("      ✅ EXPECTED FAILURE: Very low similarity score confirms taxonomic distance")
        else:
            print("      ❌ UNEXPECTED: Similarity score higher than expected")
    else:
        print("      ❌ Horse not found in results")
    
    # Now test the reverse: horse traits looking for goldfish
    print(f"\n>>> Using HORSE traits to find matches:")
    horse_traits = KNOWLEDGE_BASE['horse']['traits'].copy()
    print(f"    Horse taxonomy: {KNOWLEDGE_BASE['horse']['metadata']}")
    
    classifications = classifier.classify(horse_traits, top_n=len(KNOWLEDGE_BASE))
    
    # Find where goldfish appears in the horse classification
    goldfish_rank = None
    goldfish_score = None
    for i, (creature, score) in enumerate(classifications):
        if creature == 'goldfish':
            goldfish_rank = i + 1
            goldfish_score = score
            break
    
    print(f"\n    Top 5 matches for horse traits:")
    for i, (creature, score) in enumerate(classifications[:5]):
        metadata = KNOWLEDGE_BASE[creature]['metadata']
        hit_marker = "🐎" if creature == 'horse' else "  "
        print(f"      {hit_marker} {i+1}. {creature:<15} ({metadata['class']:<12}) | Similarity: {score:.3f}")
    
    print(f"\n    GOLDFISH ranking when using horse traits:")
    if goldfish_rank:
        print(f"      Rank: #{goldfish_rank}/{len(KNOWLEDGE_BASE)} | Similarity: {goldfish_score:.3f}")
        if goldfish_score < 0.3:
            print("      ✅ EXPECTED FAILURE: Very low similarity score confirms taxonomic distance")
        else:
            print("      ❌ UNEXPECTED: Similarity score higher than expected")
    else:
        print("      ❌ Goldfish not found in results")
    
    # Summary of the failure test
    print(f"\n    FAILURE TEST SUMMARY:")
    print(f"    ==================")
    print(f"    Goldfish (Actinopterygii) vs Horse (Mammalia)")
    print(f"    - These species diverged ~400 million years ago")
    print(f"    - Share only basic vertebrate traits")
    print(f"    - Expected: Very low similarity scores")
    if horse_score and goldfish_score:
        avg_similarity = (horse_score + goldfish_score) / 2
        print(f"    - Average bidirectional similarity: {avg_similarity:.3f}")
        if avg_similarity < 0.3:
            print("    - ✅ System correctly identifies taxonomic distance")
        else:
            print("    - ⚠️  System may need trait refinement")

    print("\n" + "="*80)
    print("Taxonomic Classification Test Complete!")
    print("="*80)
