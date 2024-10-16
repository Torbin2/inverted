import pygame
from player import Player
from blocks import Blocks
from menu import Menu
pygame.init()

open_menu = True
menu = Menu()

class Game:
    def __init__(self):


        self.apply_setting()


        pygame.display.set_caption('game')
        self.clock = pygame.time.Clock()
        
    def apply_setting(self):
        self.settings = menu.main()

        self.scale = self.settings["window_size"]
        self.screen = pygame.display.set_mode((400 * self.scale, 300* self.scale))
        self.fps = 60 + (60 * self.settings["high_fps"])
        print(self.fps)

        self.player = Player(self.screen, self.scale)
        self.blocks = Blocks(self.screen, self.scale)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill("black")

            self.blocks.render()
            self.player.update(self.blocks.blocks)

            self.clock.tick(self.fps)
            pygame.display.update()

    
        


    
Game().run()
