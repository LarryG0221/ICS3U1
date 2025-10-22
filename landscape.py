import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autumn Landscape")

# Colors
SKY_DAY = (135, 206, 235)
SKY_NIGHT = (20, 24, 82)
SUN_COLOR = (255, 223, 0)
MOON_COLOR = (240, 240, 255)
DARK_Brown = (165, 42, 42)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GROUND_COLOR = (34, 139, 34)
PUMPKIN_ORANGE = (255, 140, 0)
STEM_GREEN = (34, 139, 34)
Brass = (225, 193, 110)
BROWN = (139, 69, 19)
Dark_Tan = (152, 133, 88)

# Clock for frame rate control
clock = pygame.time.Clock()

# Orb (sun or moon) properties
radius = 40
speed = 2.5
x_pos = -radius  # Start off-screen to the left
is_day = True    # Start with the sun

# Arc function: y = a(x - h)^2 + k
def get_y(x):
    h = WIDTH // 2        # Peak of the arc at screen center
    k = HEIGHT // 4       # Height of the arc
    a = 0.0015            # Arc steepness
    return int(a * (x - h) ** 2 + k)


def draw_cloud(cloud_x, cloud_y, is_day):
  if is_day:
    color = WHITE
  else:
    color = GRAY
  pygame.draw.circle(screen, color, (cloud_x, cloud_y), 30)
  pygame.draw.circle(screen, color, (cloud_x + 30, cloud_y - 10), 35)
  pygame.draw.circle(screen, color, (cloud_x + 60, cloud_y), 30)
  pygame.draw.circle(screen, color, (cloud_x + 30, cloud_y + 10), 30)
  
# Main loop
running = True
while running:
    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background different color
    if is_day:
      screen.fill(SKY_DAY)
    else:
      screen.fill(SKY_NIGHT)

    # Get vertical position from arc
    y_pos = get_y(x_pos)

    # Draw the sun or moon
    if is_day:
        pygame.draw.circle(screen, SUN_COLOR, (x_pos, y_pos), radius)
    else:
        pygame.draw.circle(screen, MOON_COLOR, (x_pos, y_pos), radius)

    # Move the orb to the right
    x_pos += speed

    # When the orb exits to the right, reset and switch
    if x_pos - radius > WIDTH:
        is_day = not is_day       # Toggle between day and night
        x_pos = -radius           # Reset to start from left
    
    # draw a small house
    pygame.draw.rect(screen, Brass, (200, 300, 400, 200)) 
    roof_points = [(180, 300), (620, 300), (400, 150)]

    pygame.draw.polygon(screen, DARK_Brown, roof_points)
    # window in different color
    if is_day:
      pygame.draw.rect(screen, SKY_DAY, (250, 380, 80, 80))
    else:
      pygame.draw.rect(screen, YELLOW, (250, 380, 80, 80))
    # Horizontal pane
    pygame.draw.line(screen, WHITE, (250, 420), (330, 420), 2)
    # Vertical pane
    pygame.draw.line(screen, WHITE, (290, 380), (290, 460), 2) 
    # draw a door
    pygame.draw.rect(screen, Dark_Tan, (480, 350, 80, 150))
    pygame.draw.rect(screen, BLACK, (485, 420, 10, 15))
    # draw front yark
    pygame.draw.rect(screen, GREEN, (0, 600 - 100, 800, 100))
    
    # draw pumpkin
    center_x = 600
    center_y = 550
    width = 50
    height = 45

    # Draw overlapping ellipses to simulate pumpkin ridges
    for i in range(-2, 3):
        ellipse_rect = pygame.Rect(center_x - width // 2 + i * 5, center_y - height // 2, width, height)
        pygame.draw.ellipse(screen, PUMPKIN_ORANGE, ellipse_rect)
    # Draw Stem
    stem_rect = pygame.Rect(center_x-5, center_y - height // 10 - 30, 7.5, 10)
    pygame.draw.rect(screen, BROWN, stem_rect)
    
    # draw cloud
    cloud_x = 200
    cloud_y = 100
    
    draw_cloud(cloud_x, cloud_y, is_day)
    cloud_x = 380
    cloud_y = 70
    
    draw_cloud(cloud_x, cloud_y, is_day)
    
    cloud_x = 580
    cloud_y = 170
    
    draw_cloud(cloud_x, cloud_y, is_day)
    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

# Exit Pygame
pygame.quit()
sys.exit()
