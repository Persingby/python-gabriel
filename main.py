import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela com Imagem")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.event.QUIT:
            running = Falserunning = True

pygame.quit()