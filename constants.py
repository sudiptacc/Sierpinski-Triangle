
class Constants():
    
    # Window constants
    WIDTH = 500
    HEIGHT = 500

    # Aesthetic constants
    BACKGROUND_COLOR = (255, 255, 255)
    POINT_COLOR = (0, 0, 0)
    CENTER_COLOR = (255, 0, 0)
    NEW_POINT_COLOR = (0, 0, 255)
    POINT_SIZE = 1

    # Triangle constants
    TOP_BOUNDARY = 0
    BOTTOM_BOUNDARY = WIDTH
    LEFT_BOUNDARY = 0
    RIGHT_BOUNDARY = HEIGHT
    MARGIN = 75
    CENTER_WIDTH = WIDTH / 2
    CENTER_HEIGHT = HEIGHT / 2

    triangle_vertices = [
        (CENTER_WIDTH, TOP_BOUNDARY + MARGIN),
        (LEFT_BOUNDARY + MARGIN, BOTTOM_BOUNDARY - MARGIN),
        (RIGHT_BOUNDARY - MARGIN, BOTTOM_BOUNDARY - MARGIN)
    ]