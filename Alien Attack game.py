############################################################################################################
                                    # "Alien Attack pygame"
############################################################################################################

############################################################################################################
                                        # Controls

#  Mouse - Shoot
#  Left arrow - move left
#  Right arrow - move right
#  Up arrow - move up
#  Down arrow - move down

############################################################################################################

############################################################################################################
                                        # Gameplay

# The aim of the game is to get as high of a score as you can within the 180 second time-limit
# (or until your life/health decreases to zero). You score points by shooting the aliens.

# There are 3 types of aliens:
# Blue aliens - these move down the screen at a regular speed. You get 100 points for each alien you hit.
# Green aliens - these move horizontally across the screen very quickly. You get 300 points for each green
#                alien you hit
# Pink aliens - these move down the screen twice as fast as the blue alien. You get 500 points for each pink
#               alien you hit.

# Life:
# Your health is 100 at the start of the game. Each time you collide with an alien your health/life
# decreases by 10. When your life falls to zero the game is over.

############################################################################################################


# Pygame code

# Import Packages required for the game
import random
import pandas as pd
import pygame
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pandas as pd


# Player Name
player_name = 'MC'  # required if you want to assign your initials to a high score leaderboard
now = datetime.now()  # required for the leaderboard

# Define colours which you want to use in your game, if you want to create any drawings or characters
# you will need to assign colours to the drawings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (150, 75, 0)


# Initialise the game
pygame.init()

# Set the width and height of the screen [width, height]
# You can make this larger if you would like.
size = (700, 500)
screen = pygame.display.set_mode(size)

# Load images and the laser sound (these are simply downloaded from the internet and re-sized)
background_image = pygame.image.load("space_image.jpg").convert()
blue_alien = pygame.image.load("blue_alien.png").convert()
green_alien = pygame.image.load("green_alien.png").convert()
pink_alien = pygame.image.load("pink_alien.png").convert()
laser_sound = pygame.mixer.Sound("laser5.ogg")


# Create a class called Alien, this will be used to define our blue aliens
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # we want these sprites to be our blue aliens
        self.image = blue_alien

        # Create a rectangle - set it to whatever the image is
        self.rect = self.image.get_rect()

    # The below function resets the position of the blue aliens once they collide with our
    # character or move below the screen (we need to set out where they should re-spawn essentially)
    # The position we want them to re-spawn is just above the top of the screen
    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(680)

    # function for updating the position of the alien. On every frame (60 frames per second) the alien will
    # move 1 pixel down the screen and will move either left or right by between 0 and 8 pixels.
    def update(self):
        self.rect.y += 1
        self.rect.x += random.randrange(-8,9,1)

        # re-spawn if it falls below the screen (500)
        if self.rect.y > 550:
            self.reset_pos()


# Create a class called Alien_horiz, this will be used to define our green aliens and these aliens
# will move from right to left across the screen
class Alien_horiz(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # we want these sprites to be our green aliens
        self.image = green_alien

        # Create a rectangle - set it to whatever the image is
        self.rect = self.image.get_rect()

    # The green aliens will re-spawn just off the right hand side of the screen
    def reset_pos(self):
        self.rect.y = random.randrange(0,500)
        self.rect.x = random.randrange(700,750)

    # The green alien moves from right to left across the screen
    def update(self):
        self.rect.y += 0
        self.rect.x += -3

        # The green alien re-spawns when it moves off the left hand side of the screen
        if self.rect.x < -25:
            self.reset_pos()

# The pink alien moves down the screen twice as fast as the blue alien and the movements on the x plain are also
# greater
class Alien_boss(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # we want these sprites to be our pink aliens
        self.image = pink_alien

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

# The above 3 classes are the three aliens we need to try and hit.
# The below player class sets out our player including its position and how
# it will move
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # call the parent
        pygame.sprite.Sprite.__init__(self)

        # Blank surface to draw on
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Create a rectangle - set it to whatever the image is
        self.rect = self.image.get_rect()

    # We define the x_speed and y_speed down further but essentially what we say
    # is that our player starts off at one point on the screen and moves based
    # on the value of x_speed and y_speed (x_speed and y_speed are equal to the
    # what the player presses)
    def update(self):
        self.rect.x = self.rect.x + x_speed
        self.rect.y = self.rect.y + y_speed

# The bullets which are fired from the gun/lightsaber is also defined via a class.
# The bullets are defined with a size of 2*5 pixels and move up the screen at a rate of
# 5 pixels
class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([2, 5])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

    def update(self):
        # move the bullet up 5 pixels
        self.rect.y -= 5


# List of aliens
alien_list = pygame.sprite.Group()
# List of green aliens
alien_horiz_list = pygame.sprite.Group()
# List of alien bosses (pink aliens)
alien_boss_list = pygame.sprite.Group()
# List of each bullet
bullet_list = pygame.sprite.Group()

# List of all aliens, bullets and the player are defined in the all_sprites_list
all_sprites_list = pygame.sprite.Group()



# Above we defined what the aliens look like and how they move we now have to define how many
# of them there are and where they originate
# We create 50 blue aliens which originate just above the screen
for i in range(50):
    alien = Alien()

    # set a random location for the aliens
    alien.rect.x = random.randrange(680)
    alien.rect.y = random.randrange(-50,-20)

    # Add the alien to the list of objects
    alien_list.add(alien)
    all_sprites_list.add(alien)

# We create 8 green and pink aliens
for i in range(8):
    alien_boss = Alien_boss()
    alien_horiz = Alien_horiz()

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


# We could import an image as our character but I decided to stick with the character provided in the tutorial
# http://programarcadegames.com/index.php?chapter=foreword&lang=en#section_0
# including a gun/lightsaber
def draw_person(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [1 + x, 0 + y, 10, 10], 0)  # Head
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [10 + x, 27 + y], 2)  # Legs
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [0 + x, 27 + y], 2)  # Legs
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)  # Body
    pygame.draw.line(screen, RED, [5 + x, 10 + y], [9 + x, 17 + y], 2)  # Arms
    pygame.draw.line(screen, RED, [5 + x, 10 + y], [-3 + x, 10 + y], 2)  # Arms
    pygame.draw.line(screen, GREEN, [-3 + x, 10 + y], [-3 + x, -2 + y], 2)  # gun/lightsaber

# The below coordinates set out where above object will originate when we start the game and the person
# will move based on x_coord and y_coord ---- draw_person(screen, x_coord, y_coord)
x_coord = 350
y_coord = 450

# initialise x_speed and y_speed, we will use this later in the code
x_speed = 0
y_speed = 0


# We have a character which has head, legs and body. We want to create a sprite which sits behind the
# character as this is actually what we shoot from.
player = Player(BLACK, 20, 20)
player.rect.x = 350
player.rect.y = 450
all_sprites_list.add(player)

pygame.display.set_caption("Alien Attack")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Initialise a number of variables/lists used in the game
life = 100
score = 0

life_list = []
score_list = []

font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 180
minutes = 1000   # initialised at a very high value to avoid any issues, re-defined later in the code
seconds = 1000   # initialised at a very high value to avoid any issues, re-defined later in the code
total_seconds = 1000 # initialised at a very high value to avoid any issues, re-defined later in the code


# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        # The game quits if the user quits or life falls to zero or the time falls to zero
        if event.type == pygame.QUIT or life <=0 or (minutes <= 0 and seconds <= 0):
            done = True

        if event.type == pygame.KEYDOWN:
            # If the user presses left he/she will move left on the screen unless they are already
            # to the far left of the screen, this is to stop the character going off the screen
            # Please note it does not work if we hold the key down
            if event.key == pygame.K_LEFT and x_coord > 15:
                x_speed = -3
            elif event.key == pygame.K_RIGHT and x_coord < 670:
                x_speed = 3
            else:
                x_speed = 0
            if event.key == pygame.K_UP and y_coord > 15:
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

        # If the user presses the mouse the bullet will fire and the laser sound goes off.
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

    # We constantly have to update the x and y co-ordinates based on the keys which are pressed
    x_coord += x_speed
    y_coord += y_speed


    # --- Screen-clearing code goes here

    # We insert the background image for the game
    screen.blit(background_image, [0, 0])

    # Call the update() method on all the sprites, this moves the sprites based on
    all_sprites_list.update()

    # At present we only have a limited number of sprites which we would be able to shoot very quickly
    # We introduce more aliens every 2 frames
    if frame_count % 2 == 0:
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
        # 100 points for hitting the blue alien
        for alien in alien_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 100
            print("Score :", score)

        # See if it hit a green alien
        alien_horiz_hit_list = pygame.sprite.spritecollide(bullet, alien_horiz_list, True)

        # 300 points for hitting a green alien
        for alien in alien_horiz_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 300
            print("Score :", score)

        # See if it hit a pink alien
        alien_boss_hit_list = pygame.sprite.spritecollide(bullet, alien_boss_list, True)

        # For each alien hit, remove the bullet and add to the score
        # 500 points for hitting a pink alien
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

    # We move up a level after each 1000 points scored
    level = (score // 1000) + 1

    # Use python string formatting to format in leading zeros
    output_string1 = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    output_string2 = "Score :" + str(score)
    output_string3 = "Life :" + str(life)
    output_string4 = "Level :" + str(level)

    # Blit to the screen - We put it in red
    text1 = font.render(output_string1, True, (255, 0, 0))
    text2 = font.render(output_string2, True, (255, 0, 0))
    text3 = font.render(output_string3, True, (255, 0, 0))
    text4 = font.render(output_string4, True, (255, 0, 0))

    # Define the location of the text (the top left of the screen)
    screen.blit(text1, [550, 10])
    screen.blit(text2, [550, 30])
    screen.blit(text3, [550, 50])
    screen.blit(text4, [550, 70])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    clock.tick(frame_rate)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # We update the score to the score_list in order to assess how much the score increased by time
    # The purpose of this will be for when we train our neural network to solve the game will we see the score
    # flatten at certain times when it is deciding what to do?
    score_list.append(score)
# Close the window and quit.
pygame.quit()


##############################################################################################################
                                    # Outside the game
##############################################################################################################

# Plot the score by time, we will use this to track the performance of our Neural Network
sns.set()
_= plt.plot(score_list)
_= plt.xlabel('Time')
_= plt.ylabel('Score')
_= plt.title('Score', fontsize=20)
plt.show()

# Create a list including the player's name, score and the current time
# Useful if you want to track your high score each time
lst = [[now.strftime("%d/%m/%Y %H:%M:%S"), player_name, score]]
new_score_df = pd.DataFrame(lst, columns=['time', 'player_name', 'score'])


# top_score = pd.read_csv(r'top_score.csv',index_col=0)
# top_score_upd = pd.concat([top_score, new_score_df],ignore_index=True)
# top_score_upd.sort_values(by='score', ascending=False, inplace=True)
# top_score_upd.to_csv(r'top_score.csv', index=True, header=True)

