import pygame
import sys
import random
import pygame.mixer

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 400, 600
GROUND_HEIGHT = 100
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird ")

# Load assets
bird_image = pygame.image.load("Assets/bird.png")
top_pipe_image = pygame.image.load("Assets/top_pipe.png")  # New top pipe image
bottom_pipe_image = pygame.image.load("Assets/bottom_pipe.png")  # New bottom pipe image
background_image = pygame.image.load("Assets/background.jpg")
ground_image = pygame.image.load("Assets/base.jpg")
start_button_image = pygame.image.load("Assets/start.png")
game_start_screen = pygame.image.load("Assets/background.jpg")
countdown_screen = pygame.image.load("Assets/background.jpg")

# Load font
font = pygame.font.Font(None, 36)

# Resize assets
bird_image = pygame.transform.scale(bird_image, (60,60))
top_pipe_image = pygame.transform.scale(top_pipe_image, (50, HEIGHT - GROUND_HEIGHT))
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (50, HEIGHT - GROUND_HEIGHT))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
ground_image = pygame.transform.scale(ground_image, (WIDTH, GROUND_HEIGHT))
start_button_image = pygame.transform.scale(start_button_image, (150, 50))
game_start_screen = pygame.transform.scale(game_start_screen, (WIDTH, HEIGHT))
countdown_screen = pygame.transform.scale(countdown_screen, (WIDTH, HEIGHT))

# Bird properties
bird_x = 50
bird_y = HEIGHT // 2
bird_speed = 0
bird_gravity = 0.5
bird_jump = -10

# Pipe properties
pipe_width = 50
pipe_gap = 200
pipe_speed = 5
pipe_x = WIDTH
pipe_height = random.randint(100, HEIGHT - GROUND_HEIGHT - pipe_gap - 100)
top_pipe_y = pipe_height - top_pipe_image.get_height()
bottom_pipe_y = pipe_height + pipe_gap

# Game variables
score = 0
high_score = 0
game_over = False
game_started = False

# Restart button properties
restart_button_image = pygame.image.load("Assets/retry.png")
restart_button_image = pygame.transform.scale(restart_button_image, (150, 50))
restart_button_x = (WIDTH - restart_button_image.get_width()) // 2
restart_button_y = HEIGHT - GROUND_HEIGHT + 10  # Move the restart button to the bottom

# Countdown variables
countdown_timer = 180  # 3 seconds at 60 FPS

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_high_score():
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(high_score_text, (10, 50))

def draw_bird():
    screen.blit(bird_image, (bird_x, bird_y))

def draw_top_pipe():
    screen.blit(top_pipe_image, (pipe_x, top_pipe_y))

def draw_bottom_pipe():
    screen.blit(bottom_pipe_image, (pipe_x, bottom_pipe_y))

def check_collision():
    if bird_y < 0 or bird_y + bird_image.get_height() > HEIGHT - GROUND_HEIGHT:
        return True
    if pipe_x < bird_x + bird_image.get_width() < pipe_x + pipe_width:
        if bird_y < top_pipe_y + top_pipe_image.get_height() or bird_y + bird_image.get_height() > bottom_pipe_y:
            return True
    return False

def restart_game():
    global bird_y, bird_speed, pipe_x, pipe_height, top_pipe_y, bottom_pipe_y, score, game_over, game_started, countdown_timer
    bird_y = HEIGHT // 2
    bird_speed = 0
    pipe_x = WIDTH
    pipe_height = random.randint(100, HEIGHT - GROUND_HEIGHT - pipe_gap - 100)
    top_pipe_y = pipe_height - top_pipe_image.get_height()
    bottom_pipe_y = pipe_height + pipe_gap
    score = 0
    game_over = False
    game_started = False
    countdown_timer = 180  # Reset countdown timer

# Game loop
clock = pygame.time.Clock()

jump_sound = pygame.mixer.Sound("Assets/flap.mp3")


hit_sound = pygame.mixer.Sound("Assets/hit.mp3")
fall_sound = pygame.mixer.Sound("Assets/die.mp3")
point_sound = pygame.mixer.Sound("Assets/point.mp3")





while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and not game_over and game_started:
            if event.key == pygame.K_SPACE:
                jump_sound.play()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and not game_over and game_started:
            if event.key == pygame.K_SPACE:
                bird_speed = bird_jump
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                if not game_over:
                    # Check if the user clicked the "Start" button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_x, button_y = (WIDTH - start_button_image.get_width()) // 2, (HEIGHT - start_button_image.get_height()) // 2
                    button_width, button_height = start_button_image.get_width(), start_button_image.get_height()
                    if (
                        button_x <= mouse_x <= button_x + button_width
                        and button_y <= mouse_y <= button_y + button_height
                    ):
                        game_started = True
                elif game_over and countdown_timer <= 0:
                    # Check if the user clicked the "Restart" button when game is over and countdown is done
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_width, button_height = restart_button_image.get_width(), restart_button_image.get_height()
                    if (
                        restart_button_x <= mouse_x <= restart_button_x + button_width
                        and restart_button_y <= mouse_y <= restart_button_y + button_height
                    ):
                        restart_game()
    
# Play jump sound when the bird jumps
    if event.type == pygame.KEYDOWN and not game_over and game_started:
        if event.key == pygame.K_SPACE:
            jump_sound.play()

    if not game_over:
        if not game_started:
            # Display the game start screen with the "Start" button
            screen.blit(game_start_screen, (0, 0))
            screen.blit(start_button_image, ((WIDTH - start_button_image.get_width()) // 2, (HEIGHT - start_button_image.get_height()) // 2))
        else:
            if countdown_timer > 0:
                # Countdown
                screen.blit(countdown_screen, (0, 0))
                countdown_text = font.render(str((countdown_timer // 60) + 1), True, WHITE)
                screen.blit(countdown_text, (WIDTH // 2 - 20, HEIGHT // 2 - 50))
                countdown_timer -= 1
            else:
                # Update bird position
                bird_speed += bird_gravity
                bird_y += bird_speed

                # Update pipe position
                pipe_x -= pipe_speed
                if pipe_x < -pipe_width:
                    pipe_x = WIDTH
                    pipe_height = random.randint(100, HEIGHT - GROUND_HEIGHT - pipe_gap - 100)
                    top_pipe_y = pipe_height - top_pipe_image.get_height()
                    bottom_pipe_y = pipe_height + pipe_gap
                    score += 1

                    # Update high score if needed
                    if score > high_score:
                        high_score = score

                # Check for collisions
                if check_collision():
                    game_over = True
                # When the bird hits an obstacle
                if check_collision():
                    hit_sound.play()

# When the bird falls down (game over)
                if game_over:
                    fall_sound.play()

# When the bird earns a point
                if pipe_x < bird_x < pipe_x + pipe_width:
                    point_sound.play()

                # Draw everything
                screen.blit(background_image, (0, 0))
                draw_top_pipe()
                draw_bottom_pipe()
                draw_bird()
                draw_score()
                draw_high_score()
                screen.blit(ground_image, (0, HEIGHT - GROUND_HEIGHT))
    else:
        # Game over screen with restart button
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        score_text = font.render(f"Your Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 10))
        restart_button_rect = screen.blit(restart_button_image, (restart_button_x, restart_button_y))
        if countdown_timer <= 0:
            # Show restart button only when countdown is done
            if restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, BLUE, restart_button_rect, 2)
                if pygame.mouse.get_pressed()[0]:
                    restart_game()

    if game_over:
        pygame.mixer.music.stop()

    pygame.display.flip()
    clock.tick(FPS)


