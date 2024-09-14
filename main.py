import pygame
import sys
from prey import Prey
from predator import Predator
from plant import Plant
from environment import Environment
from sim_controller import SimController
import math
from pygame.math import Vector2


pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple life')

prey = Prey(
    position=Vector2(400, 400),  
    velocity=Vector2(0, 0),        
    mass=1.0,                      
    max_force=.1,           
    max_speed=2.0,            
    orientation=0.0,                
    vision_range=50.0,               
    fov=math.radians(90),            
    memory=None,               
    genome=None,                 
    radius=5.0,                      
    color=(255, 0, 0)                 
)

prey_list = []
predators = []
plants = []
prey_list.append(prey)
environment = Environment(prey_list, predators, plants)

sim_controller = SimController(environment)

def move(prey):
    prey.set_position(prey.calculate_next_position())

def draw_prey(prey):
    position = prey.get_position()
    
    triangle_points = [
        Vector2(2 * prey.get_radius(), 0).rotate_rad(prey.get_orientation() ),  
        Vector2(-prey.get_radius(), prey.get_radius()).rotate_rad(prey.get_orientation() ),  
        Vector2(-prey.get_radius(), -prey.get_radius()).rotate_rad(prey.get_orientation() )   
    ]

    translated_points = []
    for p in triangle_points:
        translated_point = (p.x + prey.get_position()[0], p.y + prey.get_position()[1]) 
        translated_points.append(translated_point)

    pygame.draw.polygon(screen, prey.get_color(), translated_points)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  

    sim_controller.update_state()

    draw_prey(prey)
    
    pygame.display.flip()
    pygame.time.Clock().tick(120)


