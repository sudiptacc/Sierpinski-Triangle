# run: .venv\Scripts\activate
import pygame
import random
from constants import Constants

# Window setup
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
screen.fill(Constants.BACKGROUND_COLOR)
pygame.display.set_caption('Sierpinski Triangle')

def draw_point(color: tuple, coordinate: tuple):
    pygame.draw.circle(screen, color, coordinate, Constants.POINT_SIZE)
    
def draw_points(color: tuple, coordinates: tuple):
    for coordinate in coordinates:
        draw_point(color, coordinate)

def point_within_triangle() -> tuple:
    while True:
        x = random.randint(0, Constants.WIDTH)
        y = random.randint(0, Constants.HEIGHT)
        point = (x, y)
        
        # Check if the point is within the bounds of the triangle
        if y >= 2 * x - 450 and y >= -2 * x + 550 and y >= 50 and y <= 450:
            return point
            
def midpoint(first_point: tuple, second_point: tuple) -> tuple:
    return (
        (first_point[0] + second_point[0]) / 2,
        (first_point[1] + second_point[1]) / 2
        )

# Runtime data
running = True
points = [point_within_triangle()]

while running:
    pygame.display.flip()
    draw_points(Constants.POINT_COLOR, Constants.triangle_vertices)
    draw_point(Constants.CENTER_COLOR, (Constants.CENTER_WIDTH, Constants.CENTER_HEIGHT))
    
    vertex_choice = random.choice(Constants.triangle_vertices)
    new_point = midpoint(points[-1], vertex_choice)
    
    points.append(new_point)
    draw_point(Constants.NEW_POINT_COLOR, new_point)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False