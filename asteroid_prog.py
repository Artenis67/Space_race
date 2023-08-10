import pygame
import main

asteroid_skin = pygame.image.load("assets/asteroid/asteroid_skin.png")
time_for_spawn_asteroid = 300

def create_asteroid():
    asteroid_skin.blit(main.screen, main.player_pos)