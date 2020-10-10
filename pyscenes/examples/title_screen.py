# Centralized Scene Logic inspired by https://nerdparadise.com/programming/pygame/part7
# this is where the game itself comes to life
# the user should make their own scenes within this class
#   expecting that the runner will take care of the game loop itself
#   so the user can focus on making scenes using the methods available in
#   PyScenes

import pyscenes.pyscenes as pyscenes
from pyscenes.base_scene import BaseScene

# temp game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Title Scene


class TitleScene(BaseScene):
    def __init__(self, display, test=False):
        print("Initializing TitleScene...")
        self.display = display
        if test:
            self.test = test
            self.render_count = 0

        self.setup()
        BaseScene.__init__(self)

    def setup(self):
        print("Setting up TitleScene...")
        self.display.background.setBackgroundImage("assets/title_screen.jpg")

    def process_input(self, events, pressed_keys):
        print("process")

    def update(self):
        print("update")

    def render(self, display):
        print("render")

        if self.test:
            self.render_count += 1
            if self.render_count > 60:
                super().terminate()

    def cleanup(self):
        print("cleanup")


def main():
    instance = pyscenes.Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    # pass a Scene object here to start the game
    instance.run_game(TitleScene(instance.display))


if __name__ == "__main__":
    main()
