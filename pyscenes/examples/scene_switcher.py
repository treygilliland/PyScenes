# Self-contained example of using PyScenes for a simple title screen
# Step 1: Imports
from pyscenes import Game
from pyscenes import BaseScene
import pygame

# Step 2: Scene Definitions


class PrimaryScene(BaseScene):
    """
    TitleScene example class.
    """

    def __init__(self, game, test=False):
        """
        Standard initialization method. Check to see if example was ran by testing class.
        """
        print(f"Initializing {self.__repr__()}...")
        self.test = test
        if self.test:
            self.render_count = 0

        # required super call
        super().__init__(game)

    def __repr__(self):
        """
        Representation used for command line output for scene switch.
        """
        return "PrimaryScene"

    def setup(self):
        """
        Output the scene name and change the background display.
        """
        print(f"Setting up {self.__repr__()}...")
        self.game.display.background.setImage("assets/primary.png")

    def process_input(self, events, pressed_keys):
        """
        If the user presses the space bar, switch to the SecondaryScene.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.switch_scene(SecondaryScene(self.game))

    def update(self):
        """
        Scenes are static.
        """
        pass

    def render(self, display):
        """
        Scenes are static. Render count is used for PyScenes testing.
        """
        if self.test:
            self.render_count += 1
            if self.render_count > 60:
                super().terminate()

    def cleanup(self):
        """
        Output to show where in process cleanup occurs.
        """
        print(f"Cleaning up {self.__repr__()}...")


class SecondaryScene(BaseScene):
    """
    TitleScene example class.
    """

    def __init__(self, game, test=False):
        """
        Standard initialization method. Check to see if example was ran by testing class.
        """
        print(f"Initializing {self.__repr__()}...")
        self.test = test
        if self.test:
            self.render_count = 0

        # required super call
        super().__init__(game)

    def __repr__(self):
        """
        Representation used for command line output for scene switch.
        """
        return "SecondaryScene"

    def setup(self):
        """
        Output the scene name and change the background display.
        """
        print(f"Setting up {self.__repr__()}...")
        self.game.display.background.setImage("assets/secondary.png")

    def process_input(self, events, pressed_keys):
        """
        If the user presses the space bar, switch to the SecondaryScene.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.switch_scene(PrimaryScene(self.game))

    def update(self):
        """
        Scenes are static.
        """
        pass

    def render(self, display):
        """
        Scenes are static. Render count is used for PyScenes testing.
        """
        if self.test:
            self.render_count += 1
            if self.render_count > 60:
                super().terminate()

    def cleanup(self):
        """
        Output to show where in process cleanup occurs.
        """
        print(f"Cleaning up {self.__repr__()}...")


# Step 2: Create a Game instance
game = Game(width=800, height=600, fps=30)

# Step 3: Create a Scene instance, passing in game instance
scene = PrimaryScene(game)

# Step 4: Run the game using the starting scene
game.run(scene)
