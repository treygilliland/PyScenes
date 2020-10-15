# this is the main "engine" of the project
# the user shouldn't need to modify ANYTHING within this file to create a game
# this contains classes related to the game itself, objects are interfaced through Scene objects
#   made by the user in scenes.py

# this code is a modification of pygame_functions by Steve Paget
# https://github.com/StevePaget/Pygame_Functions

import pygame
import sys
import os

spriteGroup = pygame.sprite.OrderedUpdates()
textboxGroup = pygame.sprite.OrderedUpdates()
hiddenSprites = pygame.sprite.OrderedUpdates()
screenRefresh = True


class Mixer:
    def __init__(self):
        self.paused = False
        self.initialize()

    def initialize(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def play(self, loops=0):
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play(loops)
        self.paused = False

    def stop(self):
        pygame.mixer.music.stop()

    def loadMusic(self, path):
        pygame.mixer.music.load(path)


class Display:
    # screen is a pygame object
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen, self.background = self.createScreen()

    # see screenSize function
    def createScreen(self):
        screen = pygame.display.set_mode([self.width, self.height])
        background = Background(screen)

        screen.fill(background.colour)
        background.surface = screen.copy()
        pygame.display.update()
        return screen, background

    def update(self):
        spriteRects = spriteGroup.draw(self.screen)
        textboxRects = textboxGroup.draw(self.screen)
        pygame.display.update()
        spriteGroup.clear(self.screen, self.background.surface)
        textboxGroup.clear(self.screen, self.background.surface)


# contains methods related to managing game
# should be self contained, no need to access anything anything in here
# inputs are only processed for quit events here
#   all other input processing should be done through the scene itself


class Game:
    def __init__(self, width, height, fps):
        self.fps = fps
        self.initialize()
        self.clock = pygame.time.Clock()
        self.display = Display(width, height)
        self.mixer = Mixer()

    def initialize(self):
        pygame.init()

    # see tick method

    def tick(self):
        self.clock.tick(self.fps)
        return self.clock.get_fps()

    # "main" method for running game, controlling system level
    def run_game(self, starting_scene):
        self.current_scene = starting_scene
        self.current_scene.setup()

        # Game Loop
        while self.current_scene is not None:
            pressed_keys = pygame.key.get_pressed()
            filtered_events = self.filter_events(pressed_keys)

            self.current_scene.process_input(filtered_events, pressed_keys)
            self.current_scene.update()
            self.current_scene.render(self.display.screen)
            self.current_scene = self.next_scene()
            self.display.update()
            self.tick()

        print("Game made with PyScenes.")

    def next_scene(self):
        # if scene called switch, clean it up, then set it to old scene state
        if self.current_scene.next is not self.current_scene:
            self.current_scene.cleanup()

            # if game is not terminating, setup next scene
            if self.current_scene.next is not None:
                print(
                    "Switching from {} to {}...".format(
                        self.current_scene, self.current_scene.next
                    )
                )
                self.current_scene.next.setup()

        return self.current_scene.next

    # define external game events here
    # all other event handling should be done in scene class
    def filter_events(self, pressed_keys):
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                self.current_scene.terminate()
            else:
                filtered_events.append(event)

        return filtered_events


keydict = {
    "space": pygame.K_SPACE,
    "esc": pygame.K_ESCAPE,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "return": pygame.K_RETURN,
    "a": pygame.K_a,
    "b": pygame.K_b,
    "c": pygame.K_c,
    "d": pygame.K_d,
    "e": pygame.K_e,
    "f": pygame.K_f,
    "g": pygame.K_g,
    "h": pygame.K_h,
    "i": pygame.K_i,
    "j": pygame.K_j,
    "k": pygame.K_k,
    "l": pygame.K_l,
    "m": pygame.K_m,
    "n": pygame.K_n,
    "o": pygame.K_o,
    "p": pygame.K_p,
    "q": pygame.K_q,
    "r": pygame.K_r,
    "s": pygame.K_s,
    "t": pygame.K_t,
    "u": pygame.K_u,
    "v": pygame.K_v,
    "w": pygame.K_w,
    "x": pygame.K_x,
    "y": pygame.K_y,
    "z": pygame.K_z,
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9,
    "0": pygame.K_0,
    "num0": pygame.K_KP0,
    "num1": pygame.K_KP1,
    "num2": pygame.K_KP2,
    "num3": pygame.K_KP3,
    "num4": pygame.K_KP4,
    "num5": pygame.K_KP5,
    "num6": pygame.K_KP6,
    "num7": pygame.K_KP7,
    "num8": pygame.K_KP8,
    "num9": pygame.K_KP9,
}


class Background:
    def __init__(self, screen):
        self.colour = pygame.Color("black")
        self.screen = screen

    def setTiles(self, tiles):
        if type(tiles) is str:
            self.tiles = [[loadImage(tiles)]]
        elif type(tiles[0]) is str:
            self.tiles = [[loadImage(i) for i in tiles]]
        else:
            self.tiles = [[loadImage(i) for i in row] for row in tiles]
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileWidth = self.tiles[0][0].get_width()
        self.tileHeight = self.tiles[0][0].get_height()
        self.screen.blit(self.tiles[0][0], [0, 0])
        self.surface = self.screen.copy()

    def setBackgroundImage(self, img):
        self.setTiles(img)

    def scroll(self, x, y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = 0 - self.stagePosX % self.tileWidth
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = 0 - self.stagePosY % self.tileHeight

        col2 = (
            (self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))
        ) // self.tileWidth
        row2 = (
            (self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))
        ) // self.tileHeight
        screen.blit(self.tiles[row][col], [xOff, yOff])
        screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
        screen.blit(
            self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight]
        )

        self.surface = screen.copy()

    def setColour(self, colour):
        self.colour = parseColour(colour)
        screen.fill(self.colour)
        pygame.display.update()
        self.surface = screen.copy()


def loadImage(fileName, useColorKey=False):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception(
            "Error loading image: " + fileName + " - Check filename and path?"
        )


if __name__ == "__main__":
    print("""PyScenes is not designed to be run directly.""")
