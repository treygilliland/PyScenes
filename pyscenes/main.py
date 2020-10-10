import pyscenes
from base_scene import BaseScene

# Game constants should be defined in class with scenes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Example implementation of the base scene class


class TitleScene(BaseScene):
    def setup(self):
        print("setup")

    def process_input(self, events, pressed_keys):
        print("process")

    def update(self):
        print("update")

    def render(self, display):
        print("render")

    def cleanup(self):
        print("cleanup")


def main():
    instance = pyscenes.Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    # pass the initial Scene object here to start the game
    instance.run_game(TitleScene())


if __name__ == "__main__":
    main()
