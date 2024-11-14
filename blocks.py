import pygame

class Blocks:
    

    def __init__(self, screen, scale):
        
        global sc
        sc = scale
        
        self.screen = screen

        self.blocks = {}
        # for x in range(12):
        #     self.blocks[0, x] = Block(0, x)
        #     self.blocks[10, x] = Block(10, x)


        for x in range(90):
            #screen is (48, 27)
            self.blocks[x, 0] = Block(x, 0)
            self.blocks[x + 90, 0] = Block(x + 90, 0)
            self.blocks[x + 180, 0] = Block(x + 180, 0)
            self.blocks[0, x] = Block(0, x)
            self.blocks[x, 26] = Block(x, 26)
        
        self.blocks[20, 15] = Block(20, 15, color="red")
        self.blocks[21, 15] = Block(21, 15, color="green")
    
    def render(self, camera):

        onscreen_blocks = [key for key in self.blocks if -1 < key[0]+ (camera[0]/(10*sc)) < 49 and -1 < key[1] +(camera[1]/(10*sc)) < 28]

        for block in onscreen_blocks:
            self.blocks[block].render(self.screen, camera)

    def update_settings(self, scale):

        global sc
        sc = scale
        new_blocks = {}
        for i in self.blocks:
            new_blocks[i] = Block(i[0], i[1])
        
        self.blocks = new_blocks


class Block:
    def __init__(self, x, y, type="block", color=("grey")):
        self.rect = pygame.Rect(x *10*sc, y *10*sc, 10 *sc, 10 *sc)
        self.type = type
        self.color = color

    def render(self, screen, camera):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.left + camera[0],
                                                            self.rect.top + camera[1],
                                                            self.rect.width,
                                                            self.rect.height))
