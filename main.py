import pygame
import sys
from prey import Prey
from predator import Predator
from plant import Plant
from environment import Environment
from sim_controller import SimController
import math

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple life')

prey = Prey(position=(250,250), direction=math.pi/2, vision_range=100, fov=math.pi/2, max_speed=1.5, curr_speed=1, memory=None, genome=None, radius=15, color=(255,0,0))

prey_list = []
predators = []
plants = []
prey_list.append(prey)
environment = Environment(prey_list, predators, plants)

sim_controller = SimController(environment)

def move(prey):
    prey.set_position(prey.calculate_next_position())

def draw_prey(prey):
    pygame.draw.circle(screen, prey.get_color(), prey.get_position(), prey.get_radius())
    
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  

    sim_controller.update_state()

    # move(prey)
    draw_prey(prey)
    
    pygame.display.flip()
    pygame.time.Clock().tick(120)


