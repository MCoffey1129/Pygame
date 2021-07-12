"""
 Python game
"""

# Packages
import random
import numpy as np
import pygame
import matplotlib.pyplot as plt
import  numpy as np

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (180, 0, 30)


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # Blank surface to draw on
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Create a rectangle - set it to whatever the image is
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(680)

    def update(self):
        self.rect.y += 1
        self.rect.x += random.randrange(-8,9,1)

        if self.rect.y > 550:
            self.reset_pos()


# Position of our player
class Player(Alien):
    def update(self):
        self.rect.x = self.rect.x + x_speed
        self.rect.y = self.rect.y + y_speed

class Alien_horiz(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # Blank surface to draw on
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Create a rectangle - set it to whatever the image is
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(0,500)
        self.rect.x = random.randrange(700,750)

    def update(self):
        self.rect.y += 0
        self.rect.x += -3

        if self.rect.x < -0:
            self.reset_pos()

class Alien_boss(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # Blank surface to draw on
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Create a rectangle - set it to whatever the image is
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(680)

    def update(self):
        self.rect.y += 2
        self.rect.x += random.randrange(-10,11,1)

        if self.rect.y > 550:
            self.reset_pos()



class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([5, 5])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        # move the bullet up 5 pixels
        self.rect.y -= 5


# Initialise the game
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# List of aliens
alien_list = pygame.sprite.Group()

# List of aliens
alien_horiz_list = pygame.sprite.Group()

# List of alien bosses
alien_boss_list = pygame.sprite.Group()

# List of all aliens and the player as well
all_sprites_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

for i in range(50):
    alien = Alien(RED, 20, 20)

    # set a random location for the aliens
    alien.rect.x = random.randrange(680)
    alien.rect.y = random.randrange(-50,-20)

    # Add the alien to the list of objects
    alien_list.add(alien)
    all_sprites_list.add(alien)


for i in range(8):
    alien_boss = Alien_boss(GREEN, 20, 20)
    alien_horiz = Alien_horiz(BROWN,20,20)

    # set a random location for the aliens
    alien_boss.rect.x = random.randrange(680)
    alien_boss.rect.y = random.randrange(-50,-20)

    # set a random location for the aliens
    alien_horiz.rect.x = random.randrange(0, 500)
    alien_horiz.rect.y = random.randrange(700,750)

    # Add the alien to the list of objects
    alien_boss_list.add(alien_boss)
    all_sprites_list.add(alien_boss)

    alien_horiz_list.add(alien_horiz)
    all_sprites_list.add(alien_horiz)

# Initiate the positions of objects
rect_x = 50  # position of rectangle
rect_y = 50  # position of rectangle

rect_change_x = 5  # vector direction and speed
rect_change_y = 3  # vector direction and speed



def draw_person(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [1 + x, 0 + y, 10, 10], 0)  # Head
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [10 + x, 27 + y], 2)  # Legs
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [0 + x, 27 + y], 2)  # Legs
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)  # Body
    pygame.draw.line(screen, RED, [5 + x, 10 + y], [9 + x, 17 + y], 2)  # Arms
    pygame.draw.line(screen, RED, [5 + x, 10 + y], [-3 + x, 10 + y], 2)  # Arms
    pygame.draw.line(screen, GREEN, [-3 + x, 10 + y], [-3 + x, -2 + y], 2)  # Arms

x_coord = 350
y_coord = 250

x_speed = 0
y_speed = 0

background_image = pygame.image.load("space_image.jpg").convert()
laser_sound = pygame.mixer.Sound("laser5.ogg")



player = Player(GREEN, 1, 1)
player.rect.x = 350
player.rect.y = 250
all_sprites_list.add(player)

pygame.display.set_caption("Alien Attack")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

life = 100
score = 0

life_list = []
score_list = []

font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 180
minutes = 1000
seconds = 1000
total_seconds = 1000


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or life <=0 or (minutes <= 0 and seconds <= 0):
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_coord > 5:
                x_speed = -3
            elif event.key == pygame.K_RIGHT and x_coord < 685:
                x_speed = 3
            else:
                x_speed = 0
            if event.key == pygame.K_UP and y_coord > 5:
                y_speed = -3
            elif event.key == pygame.K_DOWN and y_coord < 470:
                y_speed = 3
            else:
                y_speed = 0


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
            # Make a sound
            laser_sound.play()
            # Fire a bullet
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

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
    screen.blit(background_image, [0, 0])

    # Call the update() method on all the sprites
    all_sprites_list.update()

    if frame_count % 1 == 0:
        # set a random location for the aliens
        alien.rect.x = random.randrange(20,680)
        alien.rect.y = random.randrange(-50,-20)

        # Add the alien to the list of objects
        alien_list.add(alien)
        all_sprites_list.add(alien)




    # Call the mechanics of each bullet
    for bullet in bullet_list:

        # See if it hit an alien
        alien_hit_list = pygame.sprite.spritecollide(bullet, alien_list, True)

        # For each alien hit, remove the bullet and add to the score
        for alien in alien_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 100
            print("Score :", score)

        # See if it hit an alien
        alien_horiz_hit_list = pygame.sprite.spritecollide(bullet, alien_horiz_list, True)

        # For each alien hit, remove the bullet and add to the score
        for alien in alien_horiz_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 200
            print("Score :", score)

        # See if it hit an alien
        alien_boss_hit_list = pygame.sprite.spritecollide(bullet, alien_boss_list, True)

        # For each alien hit, remove the bullet and add to the score
        for alien in alien_boss_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 500
            print("Score :", score)

        # Remove the bullet if it flies off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # Collisions with the character
    alien_hit_list = pygame.sprite.spritecollide(player, alien_list, False)

    # Check the list of collisions
    for alien in alien_hit_list:
        life -= len(alien_hit_list) * 10
        print("Life: ", life)
        alien.reset_pos()


    alien_horiz_hit_list = pygame.sprite.spritecollide(player, alien_horiz_list, False)

    # Check the list of collisions
    for alien_horiz in alien_horiz_hit_list:
        life -= len(alien_horiz_hit_list) * 10
        print("Life: ", life)
        alien_horiz.reset_pos()

    alien_boss_hit_list = pygame.sprite.spritecollide(player, alien_boss_list, False)

    # Check the list of collisions
    for alien_boss in alien_boss_hit_list:
        life -= len(alien_boss_hit_list) * 10
        print("Life: ", life)
        alien_boss.reset_pos()


    # --- Drawing code
    # Draw the sprites
    all_sprites_list.draw(screen)


    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50], 2)

    # Draw character
    draw_person(screen, x_coord, y_coord)


    # --- Limit to 60 frames per second
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    level = (score // 1000) + 1

    # Use python string formatting to format in leading zeros
    output_string1 = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    output_string2 = "Score :" + str(score)
    output_string3 = "Life :" + str(life)
    output_string4 = "Level :" + str(level)

    # Blit to the screen
    text1 = font.render(output_string1, True, (255, 0, 0))
    text2 = font.render(output_string2, True, (255, 0, 0))
    text3 = font.render(output_string3, True, (255, 0, 0))
    text4 = font.render(output_string4, True, (255, 0, 0))

    screen.blit(text1, [550, 10])
    screen.blit(text2, [550, 30])
    screen.blit(text3, [550, 50])
    screen.blit(text4, [550, 70])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    clock.tick(frame_rate)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    life_list.append(life)
    score_list.append(score)
# Close the window and quit.
pygame.quit()

plt.plot(life_list)
plt.plot(score_list)
plt.show()

# score_list[len(score_list)-1]

