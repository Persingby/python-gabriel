import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame)
pygame.display.set_caption("Mover Imagem com Setas")

BG_COLOR = (30, 30, 40)

image_file = "player.png"
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
else:
    print("Imagem não enconrada!")

is.maximized = False

SPEED = 1 

def center_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)


def toggle_maximize():
    global is.maximized, WIDTH, HEIGHT, img_rect
    if is.maximized:
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        is.maximized = False
    else:
        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        center_image()
        is.maximized = True
   

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                toggle_maximize()

    WIDTH, HEIGHT = screen.get_size()
    center_image()
    
    screen.fill(BG_COLOR)

    screen.blit(img, img_rect.topleft)

    pygame.display.flip()

pygame.quit()