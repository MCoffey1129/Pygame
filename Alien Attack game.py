"""
 Python game
"""

# Packages
import random
import numpy as np
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (180, 0, 30)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Initiate the positions of objects
rect_x = 50 # position of rectangle
rect_y = 50 # position of rectangle

rect_change_x = 5  # vector direction and speed
rect_change_y = 3  # vector direction and speed

star_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    star_list.append([x,y])


def draw_tree():
    pygame.draw.rect(screen, BROWN, [60, 400, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150, 400], [75, 250], [0, 400]])
    pygame.draw.polygon(screen, GREEN, [[140, 350], [75, 230], [10, 350]])

def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])

def draw_person(screen,x,y):
    pygame.draw.ellipse(screen, WHITE, [96-95+x, 83-83+y, 10, 10], 0) # Head
    pygame.draw.line(screen, WHITE, [100-95+x, 100-83+y], [105-95+x, 110-83+y], 2) # Legs
    pygame.draw.line(screen, WHITE, [100-95+x, 100-83+y], [95-95+x, 110-83+y], 2) # Legs
    pygame.draw.line(screen, RED, [100-95+x, 100-83+y], [100-95+x, 90-83+y], 2) # Body
    pygame.draw.line(screen, RED, [100-95+x, 90-83+y], [104-95+x, 100-83+y], 2) # Arms
    pygame.draw.line(screen, RED, [100-95+x, 90-83+y], [96-95+x, 100-83+y], 2) # Arms


x_coord = 10
y_coord = 10

x_speed = 0
y_speed = 0

background_image = pygame.image.load("space_image.jpg").convert()
laser_sound = pygame.mixer.Sound("laser5.ogg")

pygame.display.set_caption("Alien Attack")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_sound.play()

    # --- Game logic should go here
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_x > 649 or rect_x < 0:
        rect_change_x *= -1

    if rect_y > 449 or rect_y < 0:
        rect_change_y *= -1

    x_coord += x_speed
    y_coord += y_speed


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image,[0, 0])

    # for item in star_list:
    #     item[1] += 1
    #     pygame.draw.circle(screen, WHITE, item, 2)
    #     if item[1] > 500:
    #         item[1] = random.randrange(-20,-5)
    #         item[0] = random.randrange(700)

    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50],2)
    # draw_tree()

    # Draw multiple snowmen
    # draw_snowman(screen,200,100)
    # draw_snowman(screen, 80, 40)
    # draw_snowman(screen, 25, 90)

    # draw_person(screen,200,200)
    draw_person(screen, x_coord , y_coord )
    # draw_person(screen, 400, 400)
    # draw_person(screen, 500, 500)
    # draw_person(screen, 600, 400)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
