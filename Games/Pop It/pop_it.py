import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
BACKGROUND_COLOR = (224, 255,255)#pygame.transform.scale(pygame.image.load("img/x.png"), (80, 80))
BUBBLE_COLOR = [(255,182,193)]#pygame.transform.scale(pygame.image.load("img/x.png"), (80, 80))
BUBBLE_RADIUS = 30
BUBBLE_POPPED_COLOR = (255, 0, 0)
POP_SOUND = pygame.mixer.Sound("images/pop.wav")  # Replace with a sound file of your choice

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Wrap")

# Create a list to store bubble positions
bubbles = []

# Function to create a new bubble
def create_bubble():
    x = random.randint(BUBBLE_RADIUS, WIDTH - BUBBLE_RADIUS)
    y = random.randint(BUBBLE_RADIUS, HEIGHT - BUBBLE_RADIUS)
    color=random.choice(BUBBLE_COLOR)
    bubbles.append((x, y, BUBBLE_RADIUS,color))

# Game loop
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

    # Create a new bubble periodically
    if len(bubbles) < 20:  # You can adjust the number of bubbles on the screen at once
        create_bubble()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw bubbles
    for bubble in bubbles:
        x, y, r ,color= bubble
        pygame.draw.circle(screen, color, (x, y), r)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
