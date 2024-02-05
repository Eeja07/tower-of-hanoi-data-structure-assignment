import pygame
from hanoi import window1, window2, window3, window4
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tower Of Hanoi 1.0 By Eeja")

white = (255, 255, 255)

# Create a font
font = pygame.font.Font(None, 36)
# Game Loop
current_window = "window1"  # Initial window
while True:
    screen.fill(white)

    # Get mouse coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Render and display mouse coordinates
    text = font.render(f"Mouse Coordinates: X = {mouse_x}, Y = {mouse_y}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    if current_window == "window1":
        result = window1(screen)
        if result == "window2":
            current_window = "window2"
        elif result == "window4":
            current_window = "window4"
        elif result == "window3":
            current_window = "window3"
    elif current_window == "window2":
        result = window2(screen)
        if result == "window1":
            current_window = "window1"
        elif result == "window4":
            current_window = "window4"
        elif result == "window3":
            current_window = "window3"
    elif current_window == "window3":
        result = window3(screen)
        if result == "window1":
            current_window = "window1"
        elif result == "window2":
            current_window = "window2"
        elif result == "window4":
            current_window = "window4"
    elif current_window == "window4":
        result = window4(screen)
        if result == "window1":
            current_window = "window1"
        elif result == "window2":
            current_window = "window2"
        elif result == "window3":
            current_window = "window3"

    # Update the display
    pygame.display.update()
