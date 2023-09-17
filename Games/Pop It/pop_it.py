import pygame
import random

pygame.init()


WIDTH, HEIGHT = 400, 500
BUBBLE_RADIUS = 30 

BACKGROUND_COLOR_TOP = (173, 216, 230)
BACKGROUND_COLOR_BOTTOM = (255, 255, 255)  


POP_SOUND = pygame.mixer.Sound("images/pop.wav")


def generate_gradient_color(start_color, end_color, ratio):
    r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
    return (r, g, b)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Wrap")


def create_bubble():
    x = random.randint(BUBBLE_RADIUS, WIDTH - BUBBLE_RADIUS)
    y = random.randint(BUBBLE_RADIUS, HEIGHT - BUBBLE_RADIUS)
    gradient_ratio = random.random()  
    color = generate_gradient_color((255, 182, 193), (255, 0, 0), gradient_ratio)  
    radius = random.randint(10, 40)
    bubbles.append((x, y, radius, color))


running = True
bubbles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for bubble in bubbles:
                bx, by, br, _ = bubble
                if (x - bx) ** 2 + (y - by) ** 2 <= br ** 2:
                    bubbles.remove(bubble)
                    POP_SOUND.play()  # Play the pop sound when a bubble is popped

   
    if len(bubbles) < 20:
        create_bubble()

   
    for y in range(HEIGHT):
        gradient_color = generate_gradient_color(BACKGROUND_COLOR_TOP, BACKGROUND_COLOR_BOTTOM, y / HEIGHT)
        pygame.draw.line(screen, gradient_color, (0, y), (WIDTH, y))

   
    for bubble in bubbles:
        x, y, r, color = bubble
        pygame.draw.circle(screen, color, (x, y), r)

  
    pygame.display.flip()


pygame.quit()
