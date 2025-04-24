import pygame
import numpy as np
import sys

'''

Interactive Unit Scaling

This program is a fantastic tool for building intuition about the PUCS framework. It allows users to "play" with the unit system and develop a deeper understanding of how the constants are interconnected.


# Improvements
More Constants: Include more constants in the calculation (e.g., the elementary charge e, Boltzmann constant k) to provide a more complete picture of the unit scaling.
Derived Units: Display the values of derived units (e.g., the Newton, Joule) in the new system to further illustrate the effects of the scaling.
Formula Display: Implement a way to input and display simplified physics formulas in the current unit system, as your "Simplified_Constant_Formulas.py" script does. This would allow users to see the direct impact of unit scaling on equations.
Unit Conversion: Add a feature to convert a value from SI units to the current unit system and vice versa.
Preset Unit Systems: Include buttons to quickly switch between common unit systems (SI, CGS, Planck units, etc.).
Multi-Dimensional Scaling: Explore extending the program to handle more base units (e.g., including electric charge as a base unit) for a more comprehensive exploration of unit space.
'''

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Unit Scaling Explorer")
font = pygame.font.SysFont('Arial', 18)
button_font = pygame.font.SysFont('Arial', 24)

# Base SI values
constants = {
    'c': 299792458.0,      # m/s
    'h': 6.62607015e-34,   # J·s
    'k': 1.380649e-23,     # J/K
    'G': 6.67430e-11       # m³/kg/s²
}

# Slider settings
sliders = {
    'second' : {'min': -50, 'max': 50, 'value': np.log10(1/1.35138507828e-43), 'y': 100, 'label': "Time (log10 s)"},
    'meter'  : {'min': -50, 'max': 50, 'value': np.log10(1/4.05135054323E-35), 'y': 150, 'label': "Length (log10 m)"},
    'kg'     : {'min': -50, 'max': 50, 'value': np.log10(1/5.45551186133E-8), 'y': 200, 'label': "Mass (log10 kg)"},
    'kelvin' : {'min': -50, 'max': 50, 'value': np.log10(1/3.55135123991E+32 ), 'y': 250, 'label': "Temp (log10 K)"}
}

# Button settings
dump_button = pygame.Rect(300, 500, 200, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GRAY = (200, 200, 200)
RED = (255, 50, 50)
GREEN = (50, 200, 50)

def draw_button():
    pygame.draw.rect(screen, GREEN, dump_button)
    text = button_font.render("Dump Values", True, BLACK)
    text_rect = text.get_rect(center=dump_button.center)
    screen.blit(text, text_rect)

def draw_slider(name, data):
    y = data['y']
    pygame.draw.rect(screen, GRAY, (150, y, 500, 20))
    pos_x = 150 + (data['value'] - data['min']) / (data['max'] - data['min']) * 500
    pygame.draw.circle(screen, BLUE, (int(pos_x), y + 10), 12)
    
    # Label and value
    label = font.render(f"{data['label']}: {10**data['value']:.8e}", True, BLACK)
    screen.blit(label, (150, y - 25))

def calculate_constants():
    new_units = {name: 10**data['value'] for name, data in sliders.items()}
    
    c_new = constants['c'] * (new_units['meter'] / new_units['second'])
    h_new = constants['h'] * (new_units['kg'] * new_units['meter']**2 / new_units['second'])
    k_new = constants['k'] * (new_units['kg'] * new_units['meter']**2 / (new_units['second']**2 * new_units['kelvin']))
    G_new = constants['G'] * (new_units['meter']**3 / (new_units['kg'] * new_units['second']**2))
    
    return c_new, h_new, k_new, G_new, new_units

def dump_values(new_units, c, h, k, G):
    print("\n=== Current Unit Settings ===")
    for name, value in new_units.items():
        print(f"{name:>6}: {value:.3e} SI units")
    
    print("\n=== Constants in New Units ===")
    print(f"c: {c:.3e} new-meter/new-second")
    print(f"h: {h:.3e} new-kg·new-meter²/new-second")
    print(f"k: {k:.3e} new-kg·new-meter²/(new-second²·new-K)")
    print(f"G: {G:.3e} new-meter³/(new-kg·new-second²)")

def main():
    dragging = None
    
    while True:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for name, data in sliders.items():
                    y = data['y']
                    if (150 <= event.pos[0] <= 650) and (y - 10 <= event.pos[1] <= y + 30):
                        dragging = name

                # Check button
                if dump_button.collidepoint(event.pos):
                    c, h, k, G, new_units = calculate_constants()
                    dump_values(new_units, c, h, k, G)
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = None
                
            elif event.type == pygame.MOUSEMOTION and dragging:
                x = max(150, min(event.pos[0], 650))
                sliders[dragging]['value'] = sliders[dragging]['min'] + (x - 150) / 500 * (sliders[dragging]['max'] - sliders[dragging]['min'])

        
        # Draw all sliders
        for name, data in sliders.items():
            draw_slider(name, data)

        draw_button()
        
        # Calculate and display constants
        c, h, k, G, new_units = calculate_constants()
        
        y_offset = 300
        for name, value in [('Speed of light (c)', c), 
                          ("Planck's const (h)", h),
                          ("Boltzmann (k)", k),
                          ("Gravitation (G)", G)]:
            text = font.render(f"{name}: {value:.8e}", True, BLACK)
            screen.blit(text, (150, y_offset))
            y_offset += 30
        
        # Highlight natural units
        y_offset += 20
        if abs(c - 1) < 0.1:
            text = font.render("★ c ≈ 1 (natural units for relativity!)", True, RED)
            screen.blit(text, (150, y_offset))
            y_offset += 30
        if abs(h - 1) < 0.1:
            text = font.render("★ h ≈ 1 (natural quantum mechanics!)", True, RED)
            screen.blit(text, (150, y_offset))
            y_offset += 30
        if abs(G - 1) < 0.1:
            text = font.render("★ G ≈ 1 (natural general relativity!)", True, RED)
            screen.blit(text, (150, y_offset))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
