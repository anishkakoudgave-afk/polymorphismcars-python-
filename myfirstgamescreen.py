import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My First Game Screen")

grey = (58, 58, 58)

image = pygame.image.load("beach.jpeg")
image = pygame.transform.scale(image, (300, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)

    screen.blit(image, (100, 100))  # (500-300)/2 = 100

    pygame.display.update()

pygame.quit()