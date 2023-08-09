import pygame
import spaceship_files.spaceship_prog as spaceship_prog
import spaceship_files.spaceship_skills as spaceship_skills
import asteroid_files.asteroid_prog as asteroid_prog
import asteroid_files.asteroid_skills as asteroid_skills

pygame.init() 

# Example file showing a player image moving on screen
screen_width = 1000
screen_height = 1000

# pygame setup
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

# Bullets
bullets = []

# Game speed
speed_game = 1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Charger l'image du joueur
player_image = pygame.image.load("assets/player/spacesheep_player.png").convert_alpha()
# Redimensionner l'image si nécessaire
player_image = pygame.transform.scale(player_image, (250, 250))

# Background
background_image = pygame.image.load("assets/background/space_background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
    current_time = pygame.time.get_ticks()

    # Afficher l'image du fond d'écran
    screen.blit(background_image, (0, 0))
    # Mettre à jour l'affichage
    pygame.display.update()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_SPACE] and current_time - spaceship_prog.last_shoot_time >= spaceship_prog.shoot_delay:
        spaceship_prog.add_bullet(bullets, player_pos, player_image)
        spaceship_prog.last_shoot_time = current_time
        
    spaceship_prog.update_bullets(bullets)
    spaceship_prog.draw_bullets(screen, bullets)

    # if current_time >= asteroid_prog.time_for_spawn_asteroid:
    #     asteroid_prog.create_asteroid
        
    # Afficher l'image du joueur à la position player_pos
    screen.blit(player_image, player_pos)
    
    pygame.display.flip()

    dt = clock.tick(40) / 1000

pygame.quit()