# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Snowman Snowcone"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
BROWN = (102, 51, 0)
PURPLE = (153, 0, 153)


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(PURPLE)
    pygame.draw.ellipse(screen, WHITE, [290, 160, 200, 200])
    pygame.draw.ellipse(screen, WHITE, [270, 280, 240, 240])
    pygame.draw.ellipse(screen, WHITE, [310, 50, 160, 160])
    pygame.draw.polygon(screen, BROWN, [[252, 420], [526, 420], [390, 590]])
    pygame.draw.line(screen, BLACK, [140, 320], [300, 240], 5)
    pygame.draw.line(screen, BLACK, [480, 240], [600, 320], 5)
    pygame.draw.rect(screen, BLACK, [387, 200, 5, 5])
    pygame.draw.rect(screen, BLACK, [387, 240, 5, 5])
    pygame.draw.rect(screen, BLACK, [387, 280, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [357, 100, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [410, 100, 10, 10])
    pygame.draw.polygon(screen, ORANGE, [[378, 125], [397, 125], [390, 135]])
    pygame.draw.ellipse(screen, BLACK, [385, 150, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [424, 140, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [405, 146, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [347, 140, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [365, 146, 10, 10])
    pygame.draw.rect(screen, BLACK, [305, 65, 170, 10])
    pygame.draw.rect(screen, BLACK, [335, 10, 110, 65])
    pygame.draw.line(screen, BLACK, [300, 480], [463, 500], 1)
    pygame.draw.line(screen, BLACK, [287, 465], [475, 485], 1)
    pygame.draw.line(screen, BLACK, [276, 450], [486, 470], 1)
    pygame.draw.line(screen, BLACK, [264, 435], [498, 455], 1)
    pygame.draw.line(screen, BLACK, [264, 420], [510, 440], 1)
    pygame.draw.line(screen, BLACK, [478, 420], [524, 425], 1)
    pygame.draw.line(screen, BLACK, [310, 495], [450, 515], 1)
    pygame.draw.line(screen, BLACK, [324, 510], [440, 530], 1)
    pygame.draw.line(screen, BLACK, [335, 525], [427, 545], 1)
    pygame.draw.line(screen, BLACK, [348, 540], [415, 560], 1)
    pygame.draw.line(screen, BLACK, [360, 555], [404, 575], 1)
    pygame.draw.line(screen, BLACK, [373, 570], [393, 589], 1)
    
    pygame.draw.line(screen, BLACK, [285, 420], [268, 440], 1)
    pygame.draw.line(screen, BLACK, [305, 420], [280, 457], 1)
    pygame.draw.line(screen, BLACK, [325, 420], [292, 471], 1)
    pygame.draw.line(screen, BLACK, [345, 420], [304, 486], 1)
    pygame.draw.line(screen, BLACK, [365, 420], [316, 500], 1)
    pygame.draw.line(screen, BLACK, [385, 420], [328, 516], 1)
    pygame.draw.line(screen, BLACK, [405, 420], [340, 530], 1)
    pygame.draw.line(screen, BLACK, [425, 420], [352, 546], 1)
    pygame.draw.line(screen, BLACK, [445, 420], [364, 560], 1)
    pygame.draw.line(screen, BLACK, [465, 420], [376, 575], 1)
    pygame.draw.line(screen, BLACK, [485, 420], [388, 588], 1)
    pygame.draw.line(screen, BLACK, [505, 420], [400, 577], 1)
    pygame.draw.line(screen, BLACK, [525, 420], [412, 562], 1)
   


    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    # pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    # pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
