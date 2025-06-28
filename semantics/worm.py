import numpy as np
import matplotlib.pyplot as plt
import time
import os
from collections import deque


"""
================================================================================
 White-Box Geometric Worm Brain (C. elegans Paradigm)
================================================================================

Author: J. Rogers
Date: June 2025

--- High-Level Overview ---

This program models the navigational intelligence of a simple organism like
the nematode C. elegans, using the principles of the white-box geometric
framework. It rejects the notion of complex, black-box neural computation in
favor of a direct, hard-wired, and efficient geometric model.

Core Hypothesis:
----------------
The worm's neural architecture is not a statistical approximation engine. It is
a physical implementation of a geometric transformation system. Sensory inputs
and internal states are treated as vectors in a conceptual space. Behavior
emerges as the direct result of vector operations, projecting a 'desire' vector
onto a space of possible motor actions.

This model demonstrates how sophisticated and effective survival behavior can
emerge from an incredibly simple, explainable, and computationally cheap
architecture, mirroring the observed efficiency of C. elegans.
================================================================================
"""


class NeurosceintificWorm:
    """
    Enhanced worm model that explicitly demonstrates neuroscience principles:
    - Homeostatic regulation (hunger drive)
    - Sensory-motor integration through geometric computation
    - State-dependent behavioral switching
    - Neural circuit-like vector transformations
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        # Multiple internal state variables (like real animals)
        self.hunger = 0.5      # Metabolic state
        self.fatigue = 0.0     # Energy level
        self.exploration_drive = 0.3  # Curiosity/exploration motivation
        
        # Behavioral history for analysis
        self.position_history = deque(maxlen=100)
        self.action_history = deque(maxlen=50)
        self.hunger_history = deque(maxlen=100)
        
        # Motor command repertoire (like a real motor cortex)
        self.motor_commands = {
            'move_north': np.array([0, 1]),
            'move_south': np.array([0, -1]),
            'move_east':  np.array([1, 0]),
            'move_west':  np.array([-1, 0]),
            'move_northeast': np.array([1, 1]) / np.sqrt(2),
            'move_northwest': np.array([-1, 1]) / np.sqrt(2),
            'move_southeast': np.array([1, -1]) / np.sqrt(2),
            'move_southwest': np.array([-1, -1]) / np.sqrt(2),
            'stay': np.array([0, 0])
        }
    
    def get_sensory_input(self, food_location):
        """
        Chemosensory processing: like real C. elegans chemotaxis
        Models how chemoreceptor neurons encode concentration gradients
        """
        food_x, food_y = food_location
        grad_x = food_x - self.x
        grad_y = food_y - self.y
        
        vector = np.array([grad_x, grad_y])
        distance = np.linalg.norm(vector)
        
        if distance == 0:
            return np.array([0, 0])
        
        # Weber-Fechner law: sensory response logarithmic in stimulus strength
        signal_strength = 1 / (1 + 0.1 * distance)
        normalized_direction = vector / distance
        
        return normalized_direction * signal_strength

    def update_internal_state(self):
        """
        Homeostatic regulation: multiple internal state variables
        Models how real neural circuits maintain internal balance
        """
        # Hunger increases over time (metabolic demand)
        self.hunger = min(1.0, self.hunger + 0.03)
        
        # Fatigue increases with movement
        if len(self.action_history) > 0 and self.action_history[-1] != 'stay':
            self.fatigue = min(1.0, self.fatigue + 0.02)
        else:
            # Rest reduces fatigue
            self.fatigue = max(0.0, self.fatigue - 0.01)
        
        # Exploration drive varies periodically (circadian-like rhythm)
        self.exploration_drive = 0.3 + 0.2 * np.sin(len(self.position_history) * 0.1)
        
        # Record state history
        self.hunger_history.append(self.hunger)
        self.position_history.append((self.x, self.y))

    def compute_behavioral_state(self):
        """
        Behavioral state computation: like real neural state machines
        Different internal states activate different behavioral programs
        """
        # Compute composite motivational state
        if self.hunger > 0.7:
            return "foraging"  # Strong hunger overrides everything
        elif self.fatigue > 0.8:
            return "resting"   # Too tired to move efficiently
        elif self.hunger < 0.2 and self.exploration_drive > 0.4:
            return "exploring" # Well-fed and curious
        else:
            return "idle"      # Low motivation state

    def decide_action(self, food_location):
        """
        Decision making through geometric neural computation
        Models how real neural circuits integrate multiple information streams
        """
        sensory_vector = self.get_sensory_input(food_location)
        behavioral_state = self.compute_behavioral_state()
        
        # State-dependent behavior (like real neural switching circuits)
        if behavioral_state == "foraging":
            # Strong food-seeking behavior
            motivation_factor = self.hunger ** 2
            desire_vector = sensory_vector * motivation_factor
            
        elif behavioral_state == "exploring":
            # Add random exploration component
            explore_vector = np.random.normal(0, 0.3, 2)
            weak_food_vector = sensory_vector * 0.2
            desire_vector = weak_food_vector + explore_vector
            
        elif behavioral_state == "resting":
            # Minimal movement
            desire_vector = np.array([0, 0])
            
        else:  # idle
            # Weak food-seeking
            motivation_factor = max(0, self.hunger - 0.3)
            desire_vector = sensory_vector * motivation_factor
        
        # Neural decision threshold (prevents jittering)
        if np.linalg.norm(desire_vector) < 0.1:
            return 'stay', behavioral_state # Return the state along with the action

        #if np.linalg.norm(desire_vector) < 0.1:
        #    return 'stay'

        # Motor command selection (like motor cortex winner-take-all)
        best_action = 'stay'
        max_similarity = -1.0

        for action_name, action_vector in self.motor_commands.items():
            if action_name == 'stay':
                continue
                
            # Cosine similarity (like neural dot-product computation)
            if np.linalg.norm(desire_vector) > 0 and np.linalg.norm(action_vector) > 0:
                similarity = np.dot(desire_vector, action_vector) / (
                    np.linalg.norm(desire_vector) * np.linalg.norm(action_vector)
                )
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_action = action_name
        
        return best_action, behavioral_state

    def perform_action(self, action):
        """Motor execution: translates decision into movement"""
        if action != 'stay':
            move_vector = self.motor_commands[action]
            self.x += move_vector[0]
            self.y += move_vector[1]
        
        self.action_history.append(action)
    
    def eat(self):
        """Consummatory behavior: resets homeostatic drives"""
        self.hunger = 0.0
        self.fatigue = max(0.0, self.fatigue - 0.1)  # Eating provides some energy

    def get_neural_state_summary(self):
        """Returns current neural state for analysis"""
        return {
            'hunger': self.hunger,
            'fatigue': self.fatigue,
            'exploration_drive': self.exploration_drive,
            'position': (self.x, self.y),
            'recent_actions': list(self.action_history)[-5:]
        }


class NeuroscienceWorld:
    """Enhanced world with behavioral analysis capabilities"""
    
    def __init__(self, size=20):
        self.size = size
        self.worm = NeurosceintificWorm(size // 2, size // 2)
        self.food = self.place_food()
        self.step_count = 0
        self.behavioral_data = []
        
    def place_food(self):
        return np.random.randint(1, self.size-1, 2)

    def step(self):
        """Single simulation step with detailed logging"""
        self.step_count += 1
        self.worm.update_internal_state()
        
        action, behavioral_state = self.worm.decide_action(self.food)
        self.worm.perform_action(action)
        
        # Log behavioral data
        neural_state = self.worm.get_neural_state_summary()
        neural_state['behavioral_state'] = behavioral_state
        neural_state['step'] = self.step_count
        self.behavioral_data.append(neural_state)

        # Check for eating
        distance_to_food = np.linalg.norm(np.array([self.worm.x, self.worm.y]) - self.food)
        if distance_to_food < 1.5:
            self.worm.eat()
            self.food = self.place_food()
            return f"🍎 FOOD FOUND! New food at {self.food}. State: {behavioral_state}"
        
        return f"Pos: ({self.worm.x:.1f}, {self.worm.y:.1f}), Action: {action}, State: {behavioral_state}"

    def display(self):
        """Enhanced display with neural state information"""
        grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        
        # Place food
        fx, fy = self.food
        if 0 <= fx < self.size and 0 <= fy < self.size:
            grid[int(fy)][int(fx)] = 'F'
        
        # Place worm
        wx, wy = self.worm.x, self.worm.y
        if 0 <= int(wx) < self.size and 0 <= int(wy) < self.size:
            grid[int(wy)][int(wx)] = 'W'

        # Show recent path
        for i, (px, py) in enumerate(list(self.worm.position_history)[-10:]):
            if 0 <= int(px) < self.size and 0 <= int(py) < self.size:
                if grid[int(py)][int(px)] == '.':
                    grid[int(py)][int(px)] = '·'

        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("🧠 GEOMETRIC NEURAL SIMULATION 🧠")
        print("="*40)
        for row in reversed(grid):
            print(' '.join(row))
        print("="*40)
        
        # Neural state display
        state = self.worm.get_neural_state_summary()
        print(f"🔥 Hunger: {self.worm.hunger:.2f} | 😴 Fatigue: {self.worm.fatigue:.2f}")
        print(f"🔍 Exploration: {self.worm.exploration_drive:.2f}")
        print(f"📍 Position: ({self.worm.x:.1f}, {self.worm.y:.1f})")
        
        if self.behavioral_data:
            current_state = self.behavioral_data[-1]['behavioral_state']
            print(f"🧬 Behavioral State: {current_state.upper()}")

    def analyze_behavior(self):
        """Analyze behavioral patterns (like real neuroscience data analysis)"""
        if len(self.behavioral_data) < 10:
            return
            
        print("\n" + "="*50)
        print("🔬 NEURAL BEHAVIOR ANALYSIS")
        print("="*50)
        
        # State transition analysis
        states = [d['behavioral_state'] for d in self.behavioral_data[-20:]]
        state_counts = {}
        for state in states:
            state_counts[state] = state_counts.get(state, 0) + 1
        
        print("Recent Behavioral State Distribution:")
        for state, count in state_counts.items():
            percentage = (count / len(states)) * 100
            print(f"  {state.capitalize()}: {percentage:.1f}%")
        
        # Movement efficiency
        if len(self.worm.position_history) > 10:
            positions = list(self.worm.position_history)
            distances = []
            for i in range(1, len(positions)):
                dist = np.linalg.norm(np.array(positions[i]) - np.array(positions[i-1]))
                distances.append(dist)
            avg_movement = np.mean(distances) if distances else 0
            print(f"\nMovement Efficiency: {avg_movement:.2f} units/step")


# --- Enhanced Demonstration ---
if __name__ == "__main__":
    print("🚀 Starting Enhanced Geometric Neural Simulation...")
    print("This models real neuroscience principles:")
    print("- Homeostatic regulation (hunger/fatigue)")
    print("- State-dependent behavior switching") 
    print("- Sensory-motor integration")
    print("- Neural decision thresholds")
    print("\nPress Ctrl+C to stop and see analysis...\n")
    
    world = NeuroscienceWorld(size=15)
    
    try:
        for i in range(200):
            status = world.step()
            world.display()
            print(f"Step {i+1}: {status}")
            
            # Periodic analysis
            #if i % 50 == 49:
                #world.analyze_behavior()
                #print("\nPress Enter to continue...")
                #input()
            
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        print("\n\n🔬 FINAL BEHAVIORAL ANALYSIS")
        world.analyze_behavior()
        
        print("\n🧠 KEY NEUROSCIENCE INSIGHTS DEMONSTRATED:")
        print("1. Internal states (hunger, fatigue) modulate behavior")
        print("2. Geometric computation enables flexible decision-making")
        print("3. Behavioral states switch based on internal thresholds") 
        print("4. Sensory-motor integration through vector transformations")
        print("5. Neural-like winner-take-all motor command selection")
        
    print("\n✨ Simulation complete. This is how real brains work!")
