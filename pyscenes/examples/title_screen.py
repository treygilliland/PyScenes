# Self-contained example of using PyScenes for a simple title screen
# Step 1: Imports
from pyscenes import Game
from pyscenes import BaseScene


class TitleScene(BaseScene):
    """
    This class is a minimal implementation example.
    Feel free to use as a starting point for your scenes!
    """

    def __init__(self, game, test=False):
        self.test = test
        if self.test:
            self.render_count = 0

        super().__init__(game)

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
    # Step 2: Create a Game instance
    game = Game(width=800, height=600, fps=30)

    # Step 3: Create a Scene instance, passing in game instance
    scene = TitleScene(game)

    # Step 4: Run the game using the starting scene
    game.run(scene)


if __name__ == "__main__":
    main()
