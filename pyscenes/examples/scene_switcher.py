# Self-contained example of using PyScenes for a simple title screen
import pyscenes.pyscenes as pyscenes
import pygame
from pyscenes.base_scene import BaseScene

# temp game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30


class PrimaryScene(BaseScene):
    """
    TitleScene example class.
    """

    def __init__(self, game, test=False):
        print(f"Initializing {self.__repr__()}...")
        self.game = game
        self.test = test
        if self.test:
            self.render_count = 0

        BaseScene.__init__(self)

    def __repr__(self):
        return "PrimaryScene"

    def setup(self):
        print(f"Setting up {self.__repr__()}...")
        self.game.display.background.setImage("assets/title_screen.jpg")

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.switch_scene(SecondaryScene(self.game))

    def update(self):
        pass

    def render(self, display):
        if self.test:
            self.render_count += 1
            if self.render_count > 60:
                super().terminate()

    def cleanup(self):
        print(f"Cleaning up {self.__repr__()}...")

class SecondaryScene(BaseScene):
    """
    TitleScene example class.
    """

    def __init__(self, game, test=False):
        print(f"Initializing {self.__repr__()}...")
        self.game = game
        self.test = test
        if self.test:
            self.render_count = 0

        BaseScene.__init__(self)

    def __repr__(self):
        return "SecondaryScene"

    def setup(self):
        print(f"Setting up {self.__repr__()}...")
        self.game.display.background.setImage("assets/sky.png")

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.switch_scene(PrimaryScene(self.game))

    def update(self):
        pass

    def render(self, display):
        if self.test:
            self.render_count += 1
            if self.render_count > 60:
                super().terminate()

    def cleanup(self):
        print(f"Cleaning up {self.__repr__()}...")

def main():
    instance = pyscenes.Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    # pass a Scene object here to start the game
    instance.run_game(PrimaryScene(instance))


if __name__ == "__main__":
    main()
