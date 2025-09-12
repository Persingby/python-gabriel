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

SPEED = 2
JUMP_STRENGTH = 10
GRAVITY = 0.3
JUMPING = False
VELOCITY_Y = 0

def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)

last_width, last_height = WIDTH, HEIGHT

def limit_movement():
    global img_rect, WIDTH, HEIGHT
    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH
    if img_rect.top < 0:
        img_rect.top = 0
    if img_rect.bottom > HEIGHT:
        img_rect.bottom = HEIGHT

def jump():
    global JUMPING, VELOCITY_Y
    if not JUMPING:
        JUMPING = True
        VELOCITY_Y = -JUMP_STRENGTH

def update_jump():
    global JUMPING, VELOCITY_Y, img_rect
    if JUMPING:
        VELOCITY_Y += GRAVITY
        img_rect.y += VELOCITY_Y

        if img_rect.bottom >= HEIGHT:
            img_rect.bottom = HEIGHT
            JUMPING = False
            VELOCITY_Y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_width, current_height = screen.get_size()


    if (current_width, current_height) != (last_width, last_height):
        WIDTH, HEIGHT = current_width, current_height
        centralize_image()
        last_width, last_height = current_width, current_height
        

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED
    if keys[pygame.K_UP]:
        img_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED

    if keys[pygame.K_SPACE]:
        jump()

    update_jump()

    screen.fill(BG_COLOR)

    screen.fill(BG_COLOR)

    screen.blit(img, img_rect.topleft)

    pygame.display.flip()

pygame.quit()