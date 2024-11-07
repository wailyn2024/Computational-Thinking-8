import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BASKET_COLOR = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basketball Game")

# Load assets
basket_image = pygame.Surface((100, 20))
basket_image.fill(BASKET_COLOR)
basket_rect = basket_image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

# Ball settings
ball_radius = 15
ball_color = (0, 0, 255)
ball_speed = 10
ball_pos = [WIDTH // 2, HEIGHT - 100]
ball_moving = False

# Game variables
score = 0
font = pygame.font.SysFont(None, 48)

def draw_ball(screen, pos):
    pygame.draw.circle(screen, ball_color, pos, ball_radius)

def display_score(score):
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the basket
    screen.blit(basket_image, basket_rect.topleft)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not ball_moving:
                ball_moving = True
                ball_pos[1] -= ball_speed  # Simulate shooting

    # Ball movement logic
    if ball_moving:
        ball_pos[1] -= ball_speed
        if ball_pos[1] < 0:  # Reset if it goes off screen
            ball_pos[1] = HEIGHT - 100
            ball_moving = False

        # Check if the ball goes into the basket
        if (basket_rect.left < ball_pos[0] < basket_rect.right and
                basket_rect.top < ball_pos[1] < basket_rect.bottom):
            score += 1
            ball_pos[1] = HEIGHT - 100  # Reset ball position
            ball_moving = False

    draw_ball(screen, (ball_pos[0], ball_pos[1]))
    display_score(score)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()