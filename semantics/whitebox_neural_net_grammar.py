import numpy as np

class SentenceAssembler:
    """
    Takes structured semantic data and assembles a grammatically correct English sentence.
    This internalizes all word order and conjugation logic.
    """
    def __init__(self, subject_data, verb_data, object_phrase, mods_data):
        self.s = subject_data
        self.v = verb_data
        self.o = object_phrase
        self.m = mods_data

    def assemble(self):
        sentence_parts = [self.s['word'].capitalize()]
        modal = self.m['modals'][0] if self.m['modals'] else None
        adverbs = self.m['adverbs']
        
        auxiliaries = []
        main_verb_form = self.v['root']

        # 1. Determine the auxiliary verb chain (e.g., "will have been")
        if modal:
            auxiliaries.append(modal)
        elif self.v['tense'] == 'future':
            auxiliaries.append('will')

        if self.v['aspect'] == 'progressive':
            if auxiliaries and auxiliaries[0] in ['will', 'must', 'should', 'might', 'can']:
                auxiliaries.append('be')
            elif not auxiliaries: # Simple progressive tenses
                if self.v['tense'] == 'present':
                    aux = 'am' if self.s['person'] == 1 and self.s['number'] == 1 else \
                          'is' if self.s['person'] == 3 and self.s['number'] == 1 else 'are'
                    auxiliaries.append(aux)
                elif self.v['tense'] == 'past':
                    auxiliaries.append('was' if self.s['number'] == 1 else 'were')

        # 2. Handle negation
        if self.v['polarity'] == 'negative' and 'never' not in adverbs:
            if auxiliaries:
                if auxiliaries[0] == 'can': # Form contraction 'cannot'
                    auxiliaries[0] = 'cannot'
                else:
                    auxiliaries.insert(1, 'not')
            else: # No other auxiliaries, must use 'do'-support
                if self.v['tense'] == 'present':
                    auxiliaries.append('does' if self.s['person'] == 3 and self.s['number'] == 1 else 'do')
                elif self.v['tense'] == 'past':
                    auxiliaries.append('did')
                auxiliaries.append('not')

        # 3. Determine the final form of the main verb
        if self.v['voice'] == 'passive':
            main_verb_form = self.v['form_ed']
            # Add 'be' if not already present for passive voice
            if 'be' not in auxiliaries and 'am' not in auxiliaries and 'is' not in auxiliaries and 'are' not in auxiliaries and 'was' not in auxiliaries and 'were' not in auxiliaries:
                # This is a simplification; full passive logic is very complex
                if self.v['tense'] == 'future': auxiliaries.append('be')
                elif self.v['tense'] == 'past': auxiliaries.append('was' if self.s['number'] == 1 else 'were')
        elif self.v['aspect'] == 'progressive':
            main_verb_form = self.v['form_ing']
        elif auxiliaries:
            main_verb_form = self.v['root'] # After any auxiliary, use the root form
        else: # Simple tenses (no auxiliaries)
            main_verb_form = self.v['form']

        # 4. Assemble the sentence with correct adverb placement
        if auxiliaries:
            sentence_parts.append(" ".join(auxiliaries))

        freq_adverbs = [adv for adv in adverbs if adv in ['always', 'never', 'sometimes', 'often', 'rarely', 'really', 'completely', 'sadly']]
        if freq_adverbs:
            sentence_parts.append(" ".join(freq_adverbs))
        
        sentence_parts.append(main_verb_form)

        if self.o:
            sentence_parts.append(self.o)

        manner_adverbs = [adv for adv in adverbs if adv not in freq_adverbs]
        # Crude handling of adverb-adverb pairs
        if 'very' in manner_adverbs and 'quickly' in manner_adverbs:
             manner_adverbs = [adv for adv in manner_adverbs if adv not in ['very', 'quickly']] + ['very quickly']

        if manner_adverbs:
            sentence_parts.append(" ".join(manner_adverbs))

        return " ".join(sentence_parts)

class ExtendedSemanticSVOTransformer:
    def __init__(self):
        # [action, tense, aspect, relation, modality, voice, polarity, mood, intensity, duration]
        self.verb_embeddings = {
            'walk': np.array([0.2, 0.0, 0.1, 0.5, 0.0, 0.0, 0.0, 0.0, 0.3, 0.6]),
            'run':  np.array([0.4, 0.0, 0.2, 0.6, 0.0, 0.0, 0.0, 0.0, 0.8, 0.4]),
            'eat':  np.array([0.1, 0.0, 0.3, 0.4, 0.0, 0.0, 0.0, 0.0, 0.4, 0.5]),
            'think': np.array([0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.5, 0.8]),
            'dance': np.array([0.3, 0.0, 0.4, 0.6, 0.0, 0.0, 0.0, 0.0, 0.5, 0.7]),
            'whisper': np.array([0.05, 0.0, 0.0, 0.4, 0.0, 0.0, 0.0, 0.0, 0.1, 0.3]),
            'shout': np.array([0.3, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1]),
            'love': np.array([0.0, 0.0, 0.0, 0.9, 0.0, 0.0, 0.0, 0.0, 0.8, 0.9]),
            'make': np.array([0.3, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.6]),
            'drive': np.array([0.3, 0.0, 0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.7, 0.5]),
            'believe': np.array([0.0, 0.0, 0.0, 0.9, 0.3, 0.0, 0.0, 0.0, 0.6, 0.9]),
            'create': np.array([0.3, 0.0, 0.0, 0.7, 0.0, 0.0, 0.0, 0.0, 0.7, 0.7]),
            'understand': np.array([0.0, 0.0, 0.0, 0.85, 0.6, 0.0, 0.0, 0.0, 0.6, 0.8]),
            'fear': np.array([0.0, 0.0, 0.0, 0.7, 0.0, 0.0, 0.0, 0.0, 0.6, 0.8]),
            'enjoy': np.array([0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.7, 0.6]),
            'doubt': np.array([0.0, 0.0, 0.0, 0.7, -0.5, 0.0, 0.0, 0.0, 0.4, 0.6]),
            'know': np.array([0.0, 0.0, 0.0, 0.95, 0.8, 0.0, 0.0, 0.0, 0.7, 0.95]),
            'say': np.array([0.1, 0.0, 0.0, 0.6, 0.0, 0.0, 0.0, 0.0, 0.3, 0.2]),
            'build': np.array([0.4, 0.0, 0.0, 0.6, 0.0, 0.0, 0.0, 0.0, 0.6, 0.8])
        }
        self.subjects = {
            'I': {'word': 'I', 'person': 1, 'number': 1}, 'you': {'word': 'you', 'person': 2, 'number': 1},
            'he': {'word': 'he', 'person': 3, 'number': 1}, 'she': {'word': 'she', 'person': 3, 'number': 1},
            'it': {'word': 'it', 'person': 3, 'number': 0}, 'we': {'word': 'we', 'person': 1, 'number': 2},
            'they': {'word': 'they', 'person': 3, 'number': 2}, 'everyone': {'word': 'everyone', 'person': 3, 'number': 1},
            'nobody': {'word': 'nobody', 'person': 3, 'number': 1, 'polarity': 'negative'},
            'someone': {'word': 'someone', 'person': 3, 'number': 1}
        }
        self.axis_jacobians = {
            'tense_past': np.array([0.0, -0.8, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            'tense_present': np.array([0.0, 0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            'tense_future':    np.array([0.0,  0.9, -0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            'aspect_progressive': np.array([0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2]),
            'voice_passive':   np.array([0.0, 0.0, 0.0, -0.2, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0]),
            'polarity_neg':    np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.2, 0.0, 0.0, 0.0]),
            'mood_subjunctive': np.array([0.0, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 1.1, 0.0, 0.0]),
            'modal_must':      np.array([0.0, 0.0, 0.0, 0.0, 1.2, 0.0, 0.0, 0.0, 0.2, 0.0]),
            'modal_should':    np.array([0.0, 0.0, 0.0, 0.0, 0.9, 0.0, 0.0, 0.0, 0.0, 0.0]),
            'modal_might':     np.array([0.0, 0.0, 0.0, 0.0, 0.4, 0.0, 0.0, 0.0, -0.2, 0.0]),
            'modal_cannot':    np.array([0.0, 0.0, 0.0, 0.0, 0.8, 0.0, -1.2, 0.0, 0.0, 0.0]),
            'adv_quickly':     np.array([0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, -0.4]),
            'adv_quietly':     np.array([-0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.3, 0.0]),
            'adv_always':      np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8]),
            'adv_never':       np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0]),
            'adv_gracefully':  np.array([0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0]),
            'adv_very':        np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6, 0.0]),
            'adv_sadly':       np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            'adv_completely':  np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, -0.5])
        }
        self.irregular_forms = {
            'run': {'past': 'ran', 'past_participle': 'run'},
            'eat': {'past': 'ate', 'past_participle': 'eaten'},
            'make': {'past': 'made', 'past_participle': 'made'},
            'think': {'past': 'thought', 'past_participle': 'thought'},
            'know': {'past': 'knew', 'past_participle': 'known'},
            'say': {'past': 'said', 'past_participle': 'said'},
            'drive': {'past': 'drove', 'past_participle': 'driven'},
            'be': {'present_1s': 'am', 'present_3s': 'is', 'present_plural': 'are', 'past_s': 'was', 'past_plural': 'were', 'past_participle': 'been'}
        }

    def _get_verb_form(self, verb, form_type, person=None, number=None):
        """Main internal conjugation engine."""
        # Check for irregular forms first
        if form_type in self.irregular_forms.get(verb, {}):
            return self.irregular_forms[verb][form_type]
        
        # Rule-based regular verb conjugation
        if form_type == 'past' or form_type == 'past_participle':
            if verb.endswith('e'): return verb + 'd'
            if verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou': return verb[:-1] + 'ied'
            # Simple consonant doubling
            if len(verb) > 1 and verb[-2] in 'aeiou' and verb[-1] not in 'aeiouwx' : return verb + verb[-1] + 'ed'
            return verb + 'ed'
            
        if form_type == 'present_3s':
            if verb.endswith(('s', 'sh', 'ch', 'x', 'z')): return verb + 'es'
            if verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou': return verb[:-1] + 'ies'
            return verb + 's'
            
        if form_type == 'ing':
            if verb.endswith('e') and verb not in ['be', 'see']: return verb[:-1] + 'ing'
            if verb.endswith('ie'): return verb[:-2] + 'ying'
            if len(verb) > 1 and verb[-2] in 'aeiou' and verb[-1] not in 'aeiouwx' : return verb + verb[-1] + 'ing'
            return verb + 'ing'
        
        return verb # Return root form by default

    def generate_svo(self, subj_word, verb_root, obj_phrase, mods):
        if subj_word not in self.subjects or verb_root not in self.verb_embeddings:
            return f"[Input error: {subj_word} or {verb_root} unknown]"

        vec = np.copy(self.verb_embeddings[verb_root])
        for mod in mods:
            if mod in self.axis_jacobians:
                vec += self.axis_jacobians[mod]
        
        subject_data = self.subjects[subj_word]
        person, number = subject_data['person'], subject_data['number']
        
        tense = 'past' if vec[1] < -0.3 else 'present' if abs(vec[1]) < 0.3 else 'future'
        aspect = 'progressive' if vec[2] > 0.4 else 'simple'
        voice = 'passive' if vec[5] > 0.6 else 'active'
        polarity = 'negative' if 'polarity' in subject_data or vec[6] < -0.6 else 'affirmative'

        simple_present_form = verb_root if person != 3 or number != 2 else self._get_verb_form(verb_root, 'present_3s', person, number)
        if person != 3 or number != 1: simple_present_form = verb_root
        else: simple_present_form = self._get_verb_form(verb_root, 'present_3s', person, number)
        
        verb_data = {
            'root': verb_root,
            'form': simple_present_form if tense == 'present' else self._get_verb_form(verb_root, 'past'),
            'form_ing': self._get_verb_form(verb_root, 'ing'),
            'form_ed': self._get_verb_form(verb_root, 'past_participle'),
            'tense': tense, 'aspect': aspect, 'voice': voice, 'polarity': polarity
        }

        adjectives = [m[4:] for m in mods if m.startswith('adj_')]
        full_object = obj_phrase
        if adjectives and obj_phrase:
            obj_parts = obj_phrase.split()
            determiners = ['a', 'an', 'the', 'her', 'his', 'my', 'their', 'our']
            if obj_parts[0].lower() in determiners:
                obj_parts.insert(1, " ".join(adjectives))
                full_object = " ".join(obj_parts)
            else:
                full_object = f"{' '.join(adjectives)} {obj_phrase}"

        mods_data = {
            'adverbs': [m[4:] for m in mods if m.startswith('adv_')],
            'modals': [m[6:] for m in mods if m.startswith('modal_') and m != 'modal_cannot'] + (['can'] if 'modal_cannot' in mods else [])
        }

        assembler = SentenceAssembler(subject_data, verb_data, full_object, mods_data)
        return assembler.assemble()

# === DEMO ===
if __name__ == "__main__":
    model = ExtendedSemanticSVOTransformer()
    print("=== PURE SEMANTIC GRAMMAR TRANSFORMER (Definitive Version) ===\n")
    examples = [
        ('she', 'walk', 'the dog', ['tense_present']),
        ('she', 'walk', 'the dog', ['tense_present', 'polarity_neg']),
        ('they', 'run', 'quickly', ['tense_present', 'adv_quickly']),
        ('he', 'eat', 'dinner', ['modal_must', 'tense_present']),
        ('we', 'think', 'about it', ['modal_should', 'tense_present']),
        ('I', 'know', 'the answer', ['modal_might', 'polarity_neg']),
        ('she', 'dance', 'ballet', ['tense_present', 'aspect_progressive', 'adv_gracefully']),
        ('he', 'whisper', 'secrets', ['tense_past', 'adv_quietly']),
        ('they', 'shout', 'loudly', ['tense_present']),
        ('I', 'eat', 'breakfast', ['adv_always', 'tense_present']),
        ('we', 'run', 'marathons', ['adv_never', 'tense_present']),
        ('she', 'love', 'her cat', ['tense_present', 'adj_beautiful']),
        ('he', 'make', 'a cake', ['tense_past', 'adj_huge']),
        ('they', 'drive', 'cars', ['tense_present', 'adj_red']),
        ('she', 'run', 'the race', ['tense_future', 'adv_very', 'adv_quickly']),
        ('he', 'believe', 'the story', ['modal_cannot']),
        ('we', 'create', 'art', ['tense_present', 'aspect_progressive', 'adj_beautiful']),
        ('I', 'understand', 'the problem', ['modal_should', 'adv_completely']),
        ('everyone', 'fear', 'the dark', ['tense_present', 'adv_sometimes']),
        ('nobody', 'enjoy', 'waiting', ['tense_present']),
        ('someone', 'doubt', 'the plan', ['modal_might', 'tense_present']),
        ('she', 'walk', 'to school', ['tense_present', 'aspect_progressive']),
        ('they', 'build', 'a house', ['tense_present', 'aspect_progressive', 'adv_carefully']),
        ('he', 'eat', 'the meal', ['tense_past', 'adv_extremely', 'adv_quickly']),
        ('she', 'say', 'goodbye', ['modal_must', 'adv_sadly'])
    ]
    for i, (subj, verb, obj, mods) in enumerate(examples, 1):
        print(f"{i:2d}. Input: {subj} + {verb} + {mods} + {obj}")
        result = model.generate_svo(subj, verb, obj, mods)
        print(f"    Output: {result}")
        if i < len(examples): print()
