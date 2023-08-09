import pygame
import time
import spaceship_files.spaceship_skills as spaceship_skills
import main

# vars
last_shoot_time = 0
shoot_delay = spaceship_skills.spaceship_fire_rate

def add_bullet(bullets, player_pos, player_image):
    bullet_width = 10
    bullet_height = 20
    bullet_color = (255, 0, 0)  # Rouge
    

    bullet_rect = pygame.Rect(player_pos.x + player_image.get_width() / 2 - bullet_width / 2 + 2,
                                player_pos.y - bullet_height + 80,
                                bullet_width, bullet_height)
    bullets.append(bullet_rect)
   

def update_bullets(bullets):
    for bullet in bullets:
        bullet.y -= spaceship_skills.spaceship_speed_shoot  # Fais avancer les tirs vers le haut

def draw_bullets(screen, bullets):
    bullet_color = (255, 0, 0)  # Rouge
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
