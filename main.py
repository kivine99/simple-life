import pygame
import sys
from prey import Prey
from predator import Predator
from plant import Plant
from environment import Environment
from sim_controller import SimController
from environment_setup import EnvironmentSetup
import math
from pygame.math import Vector2

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple life')

environment = EnvironmentSetup(map_size=(screen_width,screen_height), num_prey=1, num_predators=0, num_plants=80).initialize()
sim_controller = SimController(environment)

def draw_plant(screen: pygame.Surface, plant: Plant):
    plants = environment.get_plants()
    prey = environment.get_prey()
    predators = environment.get_predators()

    for plant in plants:
        draw_plant(screen, plant)

    for p in prey:
        draw_prey(p)

def draw_plant(screen: pygame.Surface, plant: Plant):
    pygame.draw.circle(screen, plant.get_color(), (int(plant.get_position().x), int(plant.get_position().y)), plant.get_size())

def draw_prey_fov(screen: pygame.Surface, prey: Prey, color=(255, 255, 255, 100), segments=30):
    orientation = prey.get_orientation()  
    position = prey.get_position()  
    vision_range = prey.get_vision_range()
    fov_half = prey.get_fov() / 2 

    points = [position]

    start_angle = orientation - fov_half
    end_angle = orientation + fov_half

    for i in range(segments + 1):
        angle = start_angle + (end_angle - start_angle) * (i / segments)

        point = Vector2(
            vision_range * math.cos(angle),
            vision_range * math.sin(angle)
        ) + position

        points.append(point)

    fov_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

    pygame.draw.polygon(fov_surface, color, points)

    screen.blit(fov_surface, (0, 0))



def draw_prey(screen: pygame.Surface, prey: Prey):
    orientation = prey.get_orientation()
    position = prey.get_position()
    radius = prey.get_radius()

    triangle_points = [
        Vector2(2 * radius, 0), 
        Vector2(-radius, radius),  
        Vector2(-radius, -radius) 
    ]

    rotated_points = []
    for point in triangle_points:
        rotated_point = point.rotate_rad(orientation)
        translated_point = (rotated_point.x + position[0], rotated_point.y + position[1])
        rotated_points.append(translated_point)

    draw_prey_fov(screen, prey)
    pygame.draw.polygon(screen, prey.get_color(), rotated_points)



def draw_environment(screen: pygame.Surface, environment: Environment):
    plants = environment.get_plants()
    prey = environment.get_prey()
    predators = environment.get_predators()

    for plant in plants:
        draw_plant(screen, plant)

    for p in prey:
        draw_prey(screen, p)

###
### MAIN LOOP
###
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  

    sim_controller.update_state()

    draw_environment(screen, environment)
    
    pygame.display.flip()
    pygame.time.Clock().tick(120)