import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 500
BACKGROUND_COLOR = (224, 255,255)
BUBBLE_COLOR = [(255,182,193)]
BUBBLE_RADIUS = 30
BUBBLE_POPPED_COLOR = (255, 0, 0)
POP_SOUND = pygame.mixer.Sound("assets/pop.wav")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Wrap")

bubbles = []

def create_bubble():
    x = random.randint(BUBBLE_RADIUS, WIDTH - BUBBLE_RADIUS)
    y = random.randint(BUBBLE_RADIUS, HEIGHT - BUBBLE_RADIUS)        
    color=random.choice(BUBBLE_COLOR)
    bubbles.append((x, y, BUBBLE_RADIUS,color))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for bubble in bubbles:
                bx, by, br,color = bubble
                if (x - bx) ** 2 + (y - by) ** 2 <= br ** 2:
                    bubbles.remove(bubble)
                    POP_SOUND.play()

 
    if len(bubbles) < 20:  # You can adjust the number of bubbles on the screen at once
        create_bubble()

 
    screen.fill(BACKGROUND_COLOR)


    for bubble in bubbles:
        x, y, r ,color= bubble
        pygame.draw.circle(screen, color, (x, y), r)

    
    pygame.display.flip()

                
pygame.quit()
