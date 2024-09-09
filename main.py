"""
Name: Syed Qadri
Date: January 9, 2023
Program: Mario Game
"""

#Imports
import pygame, random #Main Imports for Program
from game import Text, Mario, Goomba #Importing My Custom Created Classes
from tkinter import messagebox #Import Message Box

#Initiate PyGame
pygame.init()

#Create Game Variable
def game():

    # Initiate PyGame Mizer
    pygame.mixer.init()

    #Customize Game
    game_background = pygame.image.load('images/game_background.jpg') #Set Game Wallpaper
    game_title = pygame.image.load('images/game_title.png') #Set 'Mario Dodger' Title
    game_title = pygame.transform.smoothscale(game_title, (game_title.get_width() * 0.30, game_title.get_height() * 0.30)) #Set Size of Game Title

    #Create Surface
    surface = pygame.display.set_mode((game_background.get_width(), game_background.get_height())) #Main Surface
    pygame.display.set_caption("Mario Dodger - Syed's Version") #Window Caption
    pygame.display.set_icon(pygame.image.load('images/super_mario.png')) #Window Icon

    #Set Mouse Visibility
    pygame.mouse.set_visible(False) #Hide Mouse
    #pygame.mouse.set_visibility(True) - #Un-hide Mouse (only when needed)

    #Pre-game Prompt
    message = Text(surface, 'CLICK SPACEBAR TO BEGIN', pygame.font.Font('fonts/SuperMario256.ttf', 28), '#009cd9')

    #Bottom Border
    BOTTOM_BORDER = int(surface.get_height() * 0.76)

    #Create Goomba's List
    goombas = []
    goombas.clear()

    #Create Mario
    mario=Mario(surface, 'images/super_mario.png') #Main Mario Image
    mario.set_size(50,50) #Resize Mario Image
    mario.set_location((surface.get_width() - mario.get_width()) // 2, (surface.get_height() - mario.get_height()) // 2) #Set Spawn Location On Surface

    #Set Variables
    show_mario = False #Mario Visibility
    move = True #Mario and Goomba Movement
    play = True #Running the Game Loop

    #Show Game Graphics
    surface.blit(game_background, (0, 0)) #Bring background to surface, set visibile
    surface.blit(game_title, ((surface.get_width() - game_title.get_width()) // 2, 10)) #Bring title to surface, set visibile
    message.output(surface.get_width() // 2 - message.get_width() // 2, surface.get_height() * 0.4) #Bring message to surface, set visibile

    #Make Loops Live
    while True:
        if play==True: #Start Game Loop

            #Quitting the Program
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                #Start Game - Space Bar
                    if event.key==pygame.K_SPACE:
                        surface.blit(game_background, (0, 0)) #Re-blit Background
                        surface.blit(game_title, ((surface.get_width() - game_title.get_width()) // 2, 10)) #Re-blit Title
                        message = Text(surface, '', pygame.font.Font('fonts/SuperMario256.ttf', 28), '#009cd9') #Re-blit Empty Text
                        # pygame.mixer.music.load('mario_music.mp3') #Start Music
                        # pygame.mixer.music.play(-1) #Play Music Indefinetly

                        #Show Mario
                        show_mario = True

                        #Create Timers
                        pygame.time.set_timer(pygame.USEREVENT, 50)
                        pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

                #Moving Mario With The Mouse
                if move != False:
                    if event.type == pygame.MOUSEMOTION:
                        mario.set_x(pygame.mouse.get_pos()[0] - mario.get_width() // 2) #Set Mario's x-position to the Mouse's x-position
                        mario.set_y(pygame.mouse.get_pos()[1] - mario.get_height() // 2) #Set Mario's y-position to the Mouse's y-position

                        #Stop Mario from going below the ground
                        if mario.get_y() > 230:
                            mario.set_y(230)

                        #Stop Mario from exiting from the top of the screen
                        elif mario.get_y() < 0:
                            mario.set_y(0)

                        #Stop Mario from exiting from the right-side of the screen
                        elif mario.get_x() > 565:
                            mario.set_x(565)

                        # Stop Mario from exiting from the left-side of the screen
                        elif mario.get_x() < 0:
                            mario.set_x(0)

                #Creating Unique Goomba's
                if event.type == pygame.USEREVENT + 1: #Load Timer Event 1

                    #Customize Goomba
                    newgoo = Goomba(surface, 'images/goomba.png', 0, 0) #Create and Assign Goomba to Variable
                    newgoo.set_size(50, 50) #Set Goomba Size
                    newgoo.set_location(0, random.randint(0, 225)) #Set Goomba Spawn Location at Random (From Sides)
                    newgoo.set_xspeed(random.randint(4,12)) #Set Random x-speed from 4-12
                    newgoo.set_yspeed(random.randint(4,12)) #Set Random y-speed from 4-12

                    #Add The Newly Created Unique Goomba to the Goomba List
                    goombas.append(newgoo)

                #Spawning Individual Goomba's
                if event.type == pygame.USEREVENT: #Load Timer Event 2

                    #Start Goomba Spawn
                    for g in goombas:

                        #Move The Goomba
                        g.move(g.get_xspeed(), g.get_yspeed())

                        #Making the Goomba Bounce (if it hits the floor)
                        if g.get_bottom() >= 280:
                            g.set_yspeed(g.get_yspeed() * -1)

                        #Making the Goomba Bounce (if it hits the right side)
                        if g.get_right() >= surface.get_width():
                            g.set_xspeed(g.get_xspeed() * -1)

                        #Making the Goomba Bounce (if it hits the roof)
                        if g.get_top() <= 0:
                            g.set_yspeed(g.get_yspeed() * -1)

                        #Making the Goomba Bounce (if it hits the left)
                        if g.get_left() <= 0:
                            g.set_xspeed(g.get_xspeed() * -1)

                        #If Mario Colldies with a Goomba
                        if g.get_rect().colliderect(mario.get_rect()):

                            #Change Mario Image; Set Status Dead
                            mario = Mario(surface, 'images/mario_dead.png')

                            #Resize New Image
                            mario.set_size(50, 50)

                            #Stop Any Movement
                            move = False

                            #Set mario image spawns at last mouse x and y positions
                            mario.set_x(pygame.mouse.get_pos()[0] - mario.get_width() // 2)
                            mario.set_y(pygame.mouse.get_pos()[1] - mario.get_height() // 2)

                            #Assign The Positions
                            mario.set_location(mario.get_x(), mario.get_y())

                            #Stop The Timers
                            pygame.time.set_timer(pygame.USEREVENT, 0)
                            pygame.time.set_timer(pygame.USEREVENT + 1, 0)

                            #Stop The Music
                            pygame.mixer.quit()

                            #Stop the game entirely, run end screen
                            play = False

            #Reset in-game sprites
            surface.blit(game_background, (0, 0)) #Blit Background
            surface.blit(game_title, ((surface.get_width() - game_title.get_width()) // 2, 10)) #Blit Game Title
            message.output(surface.get_width() // 2 - message.get_width() // 2, surface.get_height() * 0.4) #Blit Message

            #When The Game Begins
            if show_mario != False:
                mario.output() #Blit Mario
                for g in goombas:
                    g.output() #Blit Goomba's

            #Update The Display Constantly
            pygame.display.update()

        #When Player Looses and the Game Ends
        if play != True:

            #Show Messagebox
            msg_box = messagebox.askyesno('Game Over!', f'You Lose.\nYour final score is {len(goombas)}.\nWould you like to play again?')

            #If player chooses to play again
            if msg_box == True:
                game()

            #If player chooses to leave
            else:
                pygame.quit()
                exit()

#Run The Entire Program
game()