#!/usr/bin/env python3
"""
Geometric Library Catalog System
A prototype demonstrating books as vectors in high-dimensional conceptual space,
where genre is just another axis, not metadata.

Based on the geometric framework where:
- Books are vectors in N-dimensional space
- Each axis represents a fundamental concept (theme, style, complexity, etc.)
- Genre emerges from clusters in this space rather than being imposed
- Search becomes geometric navigation
- Recommendations are based on vector proximity
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import math

# ==============================================================================
# The Single Source of Truth: Books as Vectors in Conceptual Space
# Each book is defined by its coordinates along fundamental conceptual axes
# ==============================================================================

LIBRARY_KNOWLEDGE_BASE = {
    # Science Fiction Cluster
    'dune': {
        "coordinates": {
            'political_complexity': 0.9, 'ecological_themes': 0.8, 'mysticism': 0.7, 
            'technology': 0.8, 'social_commentary': 0.7, 'adventure': 0.6,
            'psychological_depth': 0.8, 'world_building': 0.9, 'philosophical': 0.8,
            'violence': 0.6, 'romance': 0.3, 'humor': 0.2, 'coming_of_age': 0.7
        },
        "metadata": {"author": "Frank Herbert", "year": 1965, "pages": 688}
    },
    
    'neuromancer': {
        "coordinates": {
            'technology': 0.9, 'cyberpunk_aesthetic': 0.9, 'dystopian': 0.8,
            'psychological_depth': 0.7, 'noir_elements': 0.8, 'philosophical': 0.6,
            'social_commentary': 0.7, 'adventure': 0.8, 'violence': 0.7,
            'romance': 0.4, 'humor': 0.1, 'world_building': 0.8, 'drug_themes': 0.6
        },
        "metadata": {"author": "William Gibson", "year": 1984, "pages": 271}
    },
    
    'foundation': {
        "coordinates": {
            'mathematical_concepts': 0.8, 'political_complexity': 0.9, 'technology': 0.7,
            'social_commentary': 0.9, 'philosophical': 0.8, 'world_building': 0.9,
            'adventure': 0.5, 'psychological_depth': 0.6, 'romance': 0.2,
            'humor': 0.3, 'violence': 0.4, 'historical_scope': 0.9
        },
        "metadata": {"author": "Isaac Asimov", "year": 1951, "pages": 244}
    },
    
    # Fantasy Cluster  
    'lord_of_the_rings': {
        "coordinates": {
            'mythological': 0.9, 'heroic_journey': 0.9, 'world_building': 0.9,
            'good_vs_evil': 0.9, 'friendship': 0.8, 'sacrifice': 0.8,
            'nature_themes': 0.8, 'adventure': 0.9, 'violence': 0.7,
            'romance': 0.4, 'humor': 0.3, 'linguistic_complexity': 0.8,
            'coming_of_age': 0.6, 'melancholy': 0.7
        },
        "metadata": {"author": "J.R.R. Tolkien", "year": 1954, "pages": 1216}
    },
    
    'game_of_thrones': {
        "coordinates": {
            'political_complexity': 0.9, 'moral_ambiguity': 0.9, 'violence': 0.9,
            'sexual_content': 0.8, 'betrayal': 0.8, 'power_themes': 0.9,
            'world_building': 0.8, 'multiple_perspectives': 0.9, 'cynicism': 0.7,
            'romance': 0.6, 'humor': 0.3, 'historical_elements': 0.7,
            'psychological_depth': 0.8, 'brutality': 0.8
        },
        "metadata": {"author": "George R.R. Martin", "year": 1996, "pages": 694}
    },
    
    # Literary Fiction Cluster
    'one_hundred_years_solitude': {
        "coordinates": {
            'magical_realism': 0.9, 'family_saga': 0.9, 'cyclical_time': 0.8,
            'latin_american_culture': 0.9, 'political_allegory': 0.7, 'isolation_themes': 0.8,
            'psychological_depth': 0.8, 'poetic_language': 0.9, 'surreal': 0.8,
            'melancholy': 0.8, 'romance': 0.7, 'humor': 0.5, 'violence': 0.6,
            'philosophical': 0.7, 'multi_generational': 0.9
        },
        "metadata": {"author": "Gabriel García Márquez", "year": 1967, "pages": 417}
    },
    
    'beloved': {
        "coordinates": {
            'historical_trauma': 0.9, 'psychological_depth': 0.9, 'supernatural_elements': 0.7,
            'slavery_themes': 0.9, 'motherhood': 0.8, 'memory_themes': 0.8,
            'african_american_experience': 0.9, 'violence': 0.8, 'love_themes': 0.7,
            'guilt': 0.8, 'redemption': 0.6, 'poetic_language': 0.8,
            'fragmented_narrative': 0.7, 'brutality': 0.8
        },
        "metadata": {"author": "Toni Morrison", "year": 1987, "pages": 324}
    },
    
    # Mystery/Thriller Cluster
    'big_sleep': {
        "coordinates": {
            'noir_elements': 0.9, 'detective_work': 0.9, 'urban_setting': 0.8,
            'cynicism': 0.8, 'moral_ambiguity': 0.7, 'violence': 0.7,
            'sexual_tension': 0.6, 'corruption_themes': 0.8, 'first_person': 0.9,
            'dialogue_heavy': 0.8, 'atmospheric': 0.8, 'crime': 0.9,
            'psychological_depth': 0.6, 'humor': 0.4
        },
        "metadata": {"author": "Raymond Chandler", "year": 1939, "pages": 231}
    },
    
    'gone_girl': {
        "coordinates": {
            'psychological_thriller': 0.9, 'unreliable_narrator': 0.9, 'marriage_themes': 0.8,
            'deception': 0.9, 'media_manipulation': 0.7, 'dual_perspective': 0.9,
            'modern_setting': 0.9, 'twist_ending': 0.8, 'psychological_depth': 0.8,
            'violence': 0.6, 'sexual_content': 0.5, 'cynicism': 0.8,
            'social_commentary': 0.6, 'suspense': 0.9
        },
        "metadata": {"author": "Gillian Flynn", "year": 2012, "pages": 419}
    },
    
    # Horror Cluster
    'the_shining': {
        "coordinates": {
            'psychological_horror': 0.9, 'supernatural_elements': 0.8, 'isolation_themes': 0.9,
            'madness': 0.9, 'family_dysfunction': 0.8, 'violence': 0.8,
            'atmospheric': 0.9, 'claustrophobic': 0.8, 'alcoholism': 0.6,
            'child_endangerment': 0.7, 'haunted_location': 0.9, 'psychological_depth': 0.7,
            'winter_setting': 0.8, 'writer_protagonist': 0.7
        },
        "metadata": {"author": "Stephen King", "year": 1977, "pages": 447}
    },
    
    # Romance Cluster
    'pride_and_prejudice': {
        "coordinates": {
            'romance': 0.9, 'social_class_themes': 0.8, 'wit_humor': 0.8,
            'marriage_themes': 0.9, 'character_development': 0.8, 'dialogue_heavy': 0.8,
            'period_setting': 0.9, 'social_commentary': 0.7, 'family_dynamics': 0.7,
            'misunderstandings': 0.8, 'happy_ending': 0.9, 'female_protagonist': 0.9,
            'courtship': 0.9, 'manners_morals': 0.8
        },
        "metadata": {"author": "Jane Austen", "year": 1813, "pages": 279}
    },
    
    # Historical Fiction
    'all_quiet_western_front': {
        "coordinates": {
            'war_themes': 0.9, 'anti_war_message': 0.9, 'coming_of_age': 0.8,
            'friendship': 0.8, 'brutality': 0.9, 'loss_of_innocence': 0.9,
            'psychological_trauma': 0.8, 'first_person': 0.9, 'violence': 0.9,
            'death_themes': 0.9, 'disillusionment': 0.9, 'historical_accuracy': 0.8,
            'male_bonding': 0.8, 'survival': 0.8
        },
        "metadata": {"author": "Erich Maria Remarque", "year": 1929, "pages": 295}
    },
    
    # Philosophy/Non-fiction style fiction
    'stranger': {
        "coordinates": {
            'existentialism': 0.9, 'absurdism': 0.9, 'alienation': 0.9,
            'moral_indifference': 0.8, 'philosophical': 0.9, 'minimalist_style': 0.8,
            'first_person': 0.9, 'violence': 0.6, 'death_themes': 0.7,
            'social_commentary': 0.7, 'psychological_depth': 0.8, 'nihilism': 0.7,
            'french_setting': 0.8, 'colonial_themes': 0.6
        },
        "metadata": {"author": "Albert Camus", "year": 1942, "pages": 123}
    },
    'enders_game': {
        "coordinates": {
            'coming_of_age': 0.9, 'military_sf': 0.8, 'psychological_depth': 0.9, 'child_protagonist': 0.9,
            'strategic_thinking': 0.9, 'violence': 0.8, 'technology': 0.7, 'betrayal': 0.7,
            'moral_ambiguity': 0.8, 'space_opera': 0.6, 'adventure': 0.7, 'alien_species': 0.8
        },
        "metadata": {"author": "Orson Scott Card", "year": 1985, "pages": 324}
    },
    'hyperion': {
        "coordinates": {
            'literary_allusion': 0.9, 'philosophical': 0.9, 'multiple_perspectives': 0.9, 'space_opera': 0.8,
            'technology': 0.8, 'horror_elements': 0.6, 'romance': 0.5, 'adventure': 0.7,
            'world_building': 0.9, 'religious_themes': 0.7, 'violence': 0.7, 'historical_scope': 0.8
        },
        "metadata": {"author": "Dan Simmons", "year": 1989, "pages": 482}
    },
    'slaughterhouse_five': {
        "coordinates": {
            'anti_war_message': 0.9, 'non_linear_narrative': 0.9, 'black_humor': 0.8, 'fatalism': 0.9,
            'ptsd_themes': 0.8, 'science_fiction_elements': 0.6, 'philosophical': 0.8,
            'social_commentary': 0.7, 'autobiographical': 0.7, 'alien_species': 0.5, 'humor': 0.8
        },
        "metadata": {"author": "Kurt Vonnegut", "year": 1969, "pages": 275}
    },
    'the_hitchhikers_guide': {
        "coordinates": {
            'humor': 0.9, 'absurdism': 0.9, 'satire': 0.9, 'adventure': 0.8, 'technology': 0.6,
            'philosophical': 0.7, 'social_commentary': 0.8, 'space_opera': 0.7, 'british_humor': 0.9
        },
        "metadata": {"author": "Douglas Adams", "year": 1979, "pages": 224}
    },
    'do_androids_dream': {
        "coordinates": {
            'philosophical': 0.9, 'what_is_human': 0.9, 'dystopian': 0.8, 'noir_elements': 0.7,
            'technology': 0.8, 'psychological_depth': 0.8, 'empathy_themes': 0.9,
            'ecological_themes': 0.6, 'cyberpunk_aesthetic': 0.7, 'melancholy': 0.7
        },
        "metadata": {"author": "Philip K. Dick", "year": 1968, "pages": 210}
    },
    
    # --- Additional Fantasy ---
    'harry_potter_stone': {
        "coordinates": {
            'coming_of_age': 0.9, 'magic_school': 0.9, 'friendship': 0.9, 'good_vs_evil': 0.8,
            'adventure': 0.8, 'mystery_elements': 0.7, 'child_protagonist': 0.9,
            'world_building': 0.8, 'humor': 0.6, 'moral_clarity': 0.7, 'boarding_school': 0.9
        },
        "metadata": {"author": "J.K. Rowling", "year": 1997, "pages": 309}
    },
    'mistborn': {
        "coordinates": {
            'hard_magic_system': 0.9, 'heist_plot': 0.8, 'adventure': 0.8, 'social_commentary': 0.7,
            'world_building': 0.8, 'romance': 0.6, 'political_complexity': 0.7,
            'violence': 0.7, 'rebellion_themes': 0.9, 'philosophical': 0.6
        },
        "metadata": {"author": "Brandon Sanderson", "year": 2006, "pages": 541}
    },
    'the_name_of_the_wind': {
        "coordinates": {
            'storytelling': 0.9, 'poetic_language': 0.9, 'coming_of_age': 0.8, 'magic_school': 0.8,
            'music_themes': 0.8, 'adventure': 0.7, 'mystery_elements': 0.7,
            'first_person': 0.9, 'world_building': 0.8, 'melancholy': 0.6, 'unreliable_narrator': 0.6
        },
        "metadata": {"author": "Patrick Rothfuss", "year": 2007, "pages": 662}
    },
    'american_gods': {
        "coordinates": {
            'mythological': 0.9, 'road_trip_narrative': 0.8, 'modern_setting': 0.9, 'social_commentary': 0.8,
            'violence': 0.8, 'philosophical': 0.7, 'gods_and_mortals': 0.9, 'cynicism': 0.7,
            'world_building': 0.7, 'mystery_elements': 0.6, 'melancholy': 0.7
        },
        "metadata": {"author": "Neil Gaiman", "year": 2001, "pages": 588}
    },
    
    # --- Additional Literary Fiction & Classics ---
    'moby_dick': {
        "coordinates": {
            'obsession_themes': 0.9, 'philosophical': 0.9, 'adventure': 0.8, 'symbolism': 0.9,
            'nature_vs_man': 0.9, 'masculinity': 0.8, 'encyclopedic_digressions': 0.8,
            'friendship': 0.7, 'violence': 0.7, 'melancholy': 0.8, 'historical_details': 0.7
        },
        "metadata": {"author": "Herman Melville", "year": 1851, "pages": 635}
    },
    'to_the_lighthouse': {
        "coordinates": {
            'stream_of_consciousness': 0.9, 'psychological_depth': 0.9, 'memory_themes': 0.9,
            'family_dynamics': 0.8, 'philosophical': 0.8, 'passage_of_time': 0.9,
            'poetic_language': 0.9, 'internal_monologue': 0.9, 'melancholy': 0.8, 'symbolism': 0.7
        },
        "metadata": {"author": "Virginia Woolf", "year": 1927, "pages": 209}
    },
    'the_great_gatsby': {
        "coordinates": {
            'social_commentary': 0.9, 'wealth_and_class': 0.9, 'american_dream': 0.9, 'tragedy': 0.8,
            'romance': 0.7, 'melancholy': 0.8, 'poetic_language': 0.8,
            'unreliable_narrator': 0.7, 'period_setting': 0.9, 'symbolism': 0.8
        },
        "metadata": {"author": "F. Scott Fitzgerald", "year": 1925, "pages": 180}
    },
    'crime_and_punishment': {
        "coordinates": {
            'psychological_depth': 0.9, 'philosophical': 0.9, 'guilt': 0.9, 'crime': 0.8,
            'alienation': 0.8, 'poverty_themes': 0.7, 'redemption': 0.7, 'moral_ambiguity': 0.8,
            'urban_setting': 0.8, 'religious_themes': 0.6, 'nihilism': 0.7
        },
        "metadata": {"author": "Fyodor Dostoevsky", "year": 1866, "pages": 576}
    },
    
    # --- Additional Mystery/Thriller ---
    'and_then_there_were_none': {
        "coordinates": {
            'mystery_elements': 0.9, 'locked_room_mystery': 0.9, 'suspense': 0.9,
            'psychological_thriller': 0.8, 'guilt': 0.8, 'paranoia': 0.8, 'crime': 0.9,
            'multiple_perspectives': 0.7, 'isolation_themes': 0.8, 'twist_ending': 0.9
        },
        "metadata": {"author": "Agatha Christie", "year": 1939, "pages": 272}
    },
    'the_silence_of_the_lambs': {
        "coordinates": {
            'psychological_horror': 0.8, 'serial_killer': 0.9, 'detective_work': 0.8,
            'suspense': 0.9, 'forensic_science': 0.7, 'female_protagonist': 0.8,
            'manipulation': 0.9, 'violence': 0.8, 'psychological_depth': 0.8, 'crime': 0.9
        },
        "metadata": {"author": "Thomas Harris", "year": 1988, "pages": 367}
    },
    
    # --- Additional Horror ---
    'frankenstein': {
        "coordinates": {
            'gothic_horror': 0.9, 'philosophical': 0.9, 'scientific_hubris': 0.9, 'creation_themes': 0.9,
            'alienation': 0.8, 'monster_as_victim': 0.8, 'responsibility': 0.8,
            'melancholy': 0.8, 'epistolary_novel': 0.7, 'nature_themes': 0.6
        },
        "metadata": {"author": "Mary Shelley", "year": 1818, "pages": 280}
    },
    'house_of_leaves': {
        "coordinates": {
            'experimental_format': 0.9, 'psychological_horror': 0.9, 'metafiction': 0.8,
            'unreliable_narrator': 0.8, 'claustrophobic': 0.9, 'academic_satire': 0.7,
            'love_themes': 0.6, 'paranoia': 0.8, 'found_footage_style': 0.7
        },
        "metadata": {"author": "Mark Z. Danielewski", "year": 2000, "pages": 709}
    },
    
    # --- Dystopian Cluster ---
    '1984': {
        "coordinates": {
            'dystopian': 0.9, 'totalitarianism': 0.9, 'surveillance': 0.9, 'psychological_manipulation': 0.8,
            'social_commentary': 0.9, 'political_allegory': 0.8, 'hopelessness': 0.9,
            'linguistic_control': 0.8, 'romance': 0.5, 'violence': 0.7
        },
        "metadata": {"author": "George Orwell", "year": 1949, "pages": 328}
    },
    'brave_new_world': {
        "coordinates": {
            'dystopian': 0.9, 'social_engineering': 0.9, 'biotechnology': 0.8, 'consumerism': 0.8,
            'social_commentary': 0.9, 'philosophical': 0.8, 'loss_of_individuality': 0.9,
            'drug_themes': 0.7, 'sexual_content': 0.6, 'caste_system': 0.9
        },
        "metadata": {"author": "Aldous Huxley", "year": 1932, "pages": 311}
    },
    'the_handmaids_tale': {
        "coordinates": {
            'dystopian': 0.9, 'feminist_themes': 0.9, 'theocracy': 0.9, 'social_commentary': 0.8,
            'psychological_depth': 0.8, 'loss_of_individuality': 0.8, 'first_person': 0.9,
            'sexual_content': 0.7, 'violence': 0.6, 'hopelessness': 0.8, 'rebellion_themes': 0.6
        },
        "metadata": {"author": "Margaret Atwood", "year": 1985, "pages": 311}
    },
    
    # --- Non-Fiction / Philosophy ---
    'sapiens': {
        "coordinates": {
            'historical_scope': 0.9, 'anthropology': 0.9, 'sociology': 0.8, 'big_picture_history': 0.9,
            'social_commentary': 0.8, 'non_fiction': 1.0, 'accessible_prose': 0.8,
            'technological_determinism': 0.7, 'philosophical': 0.6
        },
        "metadata": {"author": "Yuval Noah Harari", "year": 2011, "pages": 443}
    },
    'the_selfish_gene': {
        "coordinates": {
            'evolutionary_biology': 0.9, 'genetics': 0.9, 'scientific_argument': 0.9, 'non_fiction': 1.0,
            'philosophical_implications': 0.8, 'reductionism': 0.7, 'game_theory': 0.6,
            'controversial_ideas': 0.8
        },
        "metadata": {"author": "Richard Dawkins", "year": 1976, "pages": 360}
}
}

class GeometricLibraryCatalog:
    """
    A library catalog system that treats books as vectors in conceptual space.
    Genre emerges from geometric clustering rather than being imposed as metadata.
    """
    
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        
        # Extract all conceptual axes from the knowledge base
        all_concepts = set()
        for book_data in self.kb.values():
            all_concepts.update(book_data["coordinates"].keys())
        self.concepts = sorted(list(all_concepts))
        
        # Create vector representations for all books
        self.book_vectors = {}
        for book_title, book_data in self.kb.items():
            vector = np.zeros(len(self.concepts))
            for concept, value in book_data["coordinates"].items():
                if concept in self.concepts:
                    idx = self.concepts.index(concept)
                    vector[idx] = value
            self.book_vectors[book_title] = vector
    
    def encode_reader_preferences(self, preferences):
        """Convert reader preferences into a vector in the same conceptual space"""
        preference_vector = np.zeros(len(self.concepts))
        for concept, intensity in preferences.items():
            if concept in self.concepts:
                idx = self.concepts.index(concept)
                preference_vector[idx] = intensity
        return preference_vector
    
    def find_similar_books(self, target_book, top_n=5):
        """Find books most similar to a given book using cosine similarity"""
        if target_book not in self.book_vectors:
            return []
        
        target_vector = self.book_vectors[target_book]
        similarities = {}
        
        for book_title, book_vector in self.book_vectors.items():
            if book_title != target_book:  # Don't include the target book itself
                similarity = cosine_similarity([target_vector], [book_vector])[0][0]
                similarities[book_title] = similarity
        
        sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_similarities[:top_n]
    
    def recommend_by_preferences(self, reader_preferences, top_n=5):
        """Recommend books based on reader's conceptual preferences"""
        preference_vector = self.encode_reader_preferences(reader_preferences)
        
        if np.linalg.norm(preference_vector) == 0:
            return []
        
        similarities = {}
        for book_title, book_vector in self.book_vectors.items():
            similarity = cosine_similarity([preference_vector], [book_vector])[0][0]
            similarities[book_title] = similarity
        
        sorted_recommendations = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_recommendations[:top_n]
    
    def discover_conceptual_voids(self, concept_combination, threshold=0.3):
        """
        Identify conceptual voids - combinations of concepts that would be coherent
        but are not well-represented in the current collection
        """
        target_vector = self.encode_reader_preferences(concept_combination)
        
        # Find the closest existing book
        max_similarity = 0
        closest_book = None
        
        for book_title, book_vector in self.book_vectors.items():
            similarity = cosine_similarity([target_vector], [book_vector])[0][0]
            if similarity > max_similarity:
                max_similarity = similarity
                closest_book = book_title
        
        # If the closest book is still far away, this represents a void
        if max_similarity < threshold:
            return {
                'void_detected': True,
                'similarity_to_closest': max_similarity,
                'closest_existing_book': closest_book,
                'void_description': concept_combination
            }
        else:
            return {
                'void_detected': False,
                'similarity_to_closest': max_similarity,
                'closest_existing_book': closest_book
            }
    
    def emergent_genre_analysis(self, book_title):
        """
        Analyze what 'genre' emerges from a book's position in conceptual space,
        rather than imposing predefined genre categories
        """
        if book_title not in self.book_vectors:
            return None
        
        book_vector = self.book_vectors[book_title]
        
        # Find the strongest conceptual dimensions
        concept_strengths = [(self.concepts[i], book_vector[i]) for i in range(len(self.concepts))]
        concept_strengths.sort(key=lambda x: x[1], reverse=True)
        
        # Get top conceptual dimensions
        dominant_concepts = [concept for concept, strength in concept_strengths[:8] if strength > 0.5]
        
        # Find books with similar conceptual profiles
        similar_books = self.find_similar_books(book_title, top_n=3)
        
        return {
            'book': book_title,
            'dominant_concepts': dominant_concepts,
            'emergent_genre_cluster': [book for book, similarity in similar_books],
            'conceptual_signature': concept_strengths[:5]
        }
    
    def explain_recommendation(self, book_title, reader_preferences):
        """Provide a geometric explanation of why a book was recommended"""
        if book_title not in self.book_vectors:
            return None
        
        preference_vector = self.encode_reader_preferences(reader_preferences)
        book_vector = self.book_vectors[book_title]
        
        # Calculate contribution of each concept to the similarity
        contributions = []
        for i, concept in enumerate(self.concepts):
            preference_val = preference_vector[i]
            if preference_val > 0:  # Only show concepts the reader expressed interest in
                book_val = book_vector[i]
                contribution = preference_val * book_val
                contributions.append((concept, preference_val, book_val, contribution))
        
        contributions.sort(key=lambda x: x[3], reverse=True)
        
        return {
            'book': book_title,
            'overall_similarity': cosine_similarity([preference_vector], [book_vector])[0][0],
            'concept_contributions': contributions,
            'metadata': self.kb[book_title].get('metadata', {})
        }

# Demonstration and test harness
class LibraryTestHarness:
    def __init__(self, catalog_system):
        self.catalog = catalog_system
    
    def demonstrate_similarity_search(self):
        print("="*80)
        print("GEOMETRIC SIMILARITY SEARCH")
        print("="*80)
        
        test_book = 'dune'
        print(f"Finding books similar to '{test_book}':")
        
        similar_books = self.catalog.find_similar_books(test_book, top_n=5)
        for book, similarity in similar_books:
            metadata = self.catalog.kb[book]['metadata']
            print(f"  {book:<25} | Similarity: {similarity:.3f} | {metadata['author']} ({metadata['year']})")
    
    def demonstrate_preference_based_recommendations(self):
        print("\n" + "="*80)
        print("PREFERENCE-BASED RECOMMENDATIONS")
        print("="*80)
        
        # Reader who likes complex psychological narratives with philosophical depth
        reader_preferences = {
            'psychological_depth': 0.9,
            'philosophical': 0.8,
            'moral_ambiguity': 0.7,
            'social_commentary': 0.6
        }
        
        print("Reader preferences:", reader_preferences)
        recommendations = self.catalog.recommend_by_preferences(reader_preferences, top_n=5)
        
        print("\nRecommended books:")
        for book, similarity in recommendations:
            metadata = self.catalog.kb[book]['metadata']
            print(f"  {book:<25} | Match: {similarity:.3f} | {metadata['author']} ({metadata['year']})")
    
    def demonstrate_void_detection(self):
        print("\n" + "="*80)
        print("CONCEPTUAL VOID DETECTION")
        print("="*80)
        
        # Look for a void: High-tech comedy with romance
        void_concept = {
            'technology': 0.8,
            'humor': 0.8,
            'romance': 0.7,
            'adventure': 0.6
        }
        
        print("Searching for conceptual void:", void_concept)
        void_analysis = self.catalog.discover_conceptual_voids(void_concept, threshold=0.4)
        
        if void_analysis['void_detected']:
            print(f"✓ VOID DETECTED! This concept combination is underrepresented.")
            print(f"  Closest existing book: {void_analysis['closest_existing_book']}")
            print(f"  Similarity to closest: {void_analysis['similarity_to_closest']:.3f}")
            print("  This represents an opportunity for acquisition or creation!")
        else:
            print(f"✗ No significant void. Closest match: {void_analysis['closest_existing_book']}")
            print(f"  Similarity: {void_analysis['similarity_to_closest']:.3f}")
    
    def demonstrate_emergent_genre_analysis(self):
        print("\n" + "="*80)
        print("EMERGENT GENRE ANALYSIS")
        print("="*80)
        
        test_books = ['neuromancer', 'beloved', 'pride_and_prejudice']
        
        for book in test_books:
            analysis = self.catalog.emergent_genre_analysis(book)
            print(f"\n--- Analysis of '{book}' ---")
            print(f"Dominant concepts: {', '.join(analysis['dominant_concepts'])}")
            print(f"Emergent genre cluster: {', '.join(analysis['emergent_genre_cluster'])}")
            print("Top conceptual signature:")
            for concept, strength in analysis['conceptual_signature']:
                if strength > 0.3:
                    print(f"  {concept}: {strength:.2f}")
    
    def demonstrate_recommendation_explanation(self):
        print("\n" + "="*80)
        print("RECOMMENDATION EXPLANATION")
        print("="*80)
        
        reader_preferences = {
            'violence': 0.3,  # Low tolerance for violence
            'psychological_depth': 0.8,
            'romance': 0.6,
            'humor': 0.7
        }
        
        recommendations = self.catalog.recommend_by_preferences(reader_preferences, top_n=1)
        if recommendations:
            top_recommendation = recommendations[0][0]
            explanation = self.catalog.explain_recommendation(top_recommendation, reader_preferences)
            
            print(f"Why we recommended '{top_recommendation}':")
            print(f"Overall compatibility: {explanation['overall_similarity']:.3f}")
            print("\nConcept-by-concept breakdown:")
            
            for concept, pref_val, book_val, contribution in explanation['concept_contributions'][:8]:
                if contribution > 0.1:
                    print(f"  {concept:<20} | Your interest: {pref_val:.1f}, Book level: {book_val:.1f} → Match: {contribution:.2f}")

# Main execution
if __name__ == "__main__":
    # Initialize the geometric library catalog
    catalog = GeometricLibraryCatalog(LIBRARY_KNOWLEDGE_BASE)
    test_harness = LibraryTestHarness(catalog)
    
    # Run all demonstrations
    test_harness.demonstrate_similarity_search()
    test_harness.demonstrate_preference_based_recommendations()
    test_harness.demonstrate_void_detection()
    test_harness.demonstrate_emergent_genre_analysis()
    test_harness.demonstrate_recommendation_explanation()
    
    print("\n" + "="*80)
    print("GEOMETRIC INSIGHTS")
    print("="*80)
    print("Notice how 'genre' emerges from geometric clustering rather than")
    print("being imposed as metadata. Books cluster naturally based on their")
    print("conceptual coordinates, revealing deeper structural relationships")
    print("than traditional categorical systems.")
    print("\nThis system can:")
    print("• Identify acquisition opportunities (conceptual voids)")
    print("• Provide explainable recommendations")
    print("• Discover emergent genre patterns")
    print("• Navigate the conceptual space of literature systematically")
