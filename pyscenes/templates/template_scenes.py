"""
This file contains scenes used in the template example!
"""

# Step 1: Import BaseScene
from pyscenes import BaseScene

# Step 2: Define all of your game scenes


class TemplateScene(BaseScene):
    """
    This class is a contains the minimum code for a scene.
    Feel free to use as a starting point for your scenes!
    """

    def __init__(self, game):
        """
        Constructor can be overridden to take in more variables for state.
        NOTE: If overridden, the user must make game the first variable and pass to super init call.
        """
        super().__init__(game)

    def setup(self):
        """
        Method responsible for setting up scene and loading necessary data.

        Called once when a Scene is initiated.
        """
        pass

    def process_input(self, events, pressed_keys):
        """
        Responsible for processing user inputs into game functionality.

        First part of core loop. Called once each clock tick.
        """
        pass

    def update(self):
        """
        Responsible for updating game model, sprites, and data.

        Second part of game loop. Called once each clock tick.
        """
        pass

    def render(self, display):
        """
        Responsible for processing user inputs into game functionality.

        Third and final part of game loop. Called once each clock tick.
        """
        pass

    def cleanup(self):
        """
        Responsible for saving state and destroying scene objects.

        Called once when scene is switched/terminated.
        """
        pass


class TitleScene(BaseScene):
    """
    This class is another minimal implementation example.
    Feel free to use as a starting point for your scenes!
    """

    def __init__(self, game):
        """
        Constructor can be overridden to take in more variables for state.
        NOTE: If overridden, the user must make game the first variable and pass to super init call.
        """
        super().__init__(game)

    def setup(self):
        """
        Method responsible for setting up scene and loading necessary data.

        Called once when a Scene is initiated.
        """
        print("Setting up TitleScene...")
        self.game.display.background.setImage("assets/title_screen.jpg")

    def process_input(self, events, pressed_keys):
        """
        Responsible for processing user inputs into game functionality.

        First part of core loop. Called once each clock tick.
        """
        pass

    def update(self):
        """
        Responsible for updating game model, sprites, and data.

        Second part of game loop. Called once each clock tick.
        """
        pass

    def render(self, display):
        """
        Responsible for processing user inputs into game functionality.

        Third and final part of game loop. Called once each clock tick.
        """
        pass

    def cleanup(self):
        """
        Responsible for saving state and destroying scene objects.

        Called once when scene is switched/terminated.
        """
        print("Cleaning up TitleScene...")
