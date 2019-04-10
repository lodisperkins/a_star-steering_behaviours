from game import Game
import pygame
from pygame import *
'''create a gameObject class to be given to the instance of the Game class. The instances of this class will have their update and draw methods invoked by the Game class.

draw and update should take in the screen from the game, so that it can blit it's "surface" to that screen.
we pass the background in and the gameOBject will then use that argument to add it's surface to it. ex: draw(background) background.blit(mysurface)
draw 4 squares'''
def main():
    pygame.init()
    '''main execution func'''    
    game = Game("game")
    #add the gameObjects here
    if game._startup():#if the game starts up correctly 
        while game._update():#update the game if the game updates then 
            game._draw()#draw elements from the game
        game._shutdown()
if __name__ == "__main__":
    main()




