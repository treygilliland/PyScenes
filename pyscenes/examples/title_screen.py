# Self-contained example of using PyScenes for a simple title screen
import pyscenes.pyscenes as pyscenes
from pyscenes.base_scene import BaseScene

# temp game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30


class TitleScene(BaseScene):
    """
    TitleScene example class.
    """

    def __init__(self, game, test=False):
        print("Initializing TitleScene...")
        self.game = game
        self.test = test
        if self.test:
            self.render_count = 0

        BaseScene.__init__(self)

    def setup(self):
        print("Setting up TitleScene...")
        self.game.display.background.setImage("assets/title_screen.jpg")

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render(self, display):
        if self.test:
            self.render_count += 1
            if self.render_count > 60:
                super().terminate()

    def cleanup(self):
        print("Cleaning up TitleScene...")


def main():
    instance = pyscenes.Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    # pass a Scene object here to start the game
    instance.run_game(TitleScene(instance))


if __name__ == "__main__":
    main()
