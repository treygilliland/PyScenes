# Centralized Scene Logic inspired by https://nerdparadise.com/programming/pygame/part7
# this is where the game itself comes to life
# the user should make their own scenes within this class
#   expecting that the runner will take care of the game loop itself
#   so the user can focus on making scenes using the methods available in
#   PyScenes

import pyscenes

# temp game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Abstract Base Scene class for all scene objects
# Essentially an implementation of the Model-View-Controller pattern
# setup, processInput, update, render, cleanup must be overridden
class BaseScene:
    def __init__(self):
        self.next = self

    def __repr__(self):
        return self.__class__.__name__

    # called once when a Scene is initiated
    # responsible for setting up the scene and loading data
    def setup(self):
        print("uh-oh, you didn't override this in the child class")

    # first part of the core loop
    # responsible for parsing input events
    def process_input(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    # second part of the core loop
    # responsible for handling the core game logic
    def update(self):
        print("uh-oh, you didn't override this in the child class")

    # third and final part of the core loop
    # responsible for updating graphics
    def render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    # called once when the scene is no longer used
    def cleanup(self):
        print("uh-oh, you didn't override this in the child class")

    # setter method for scene switching
    def switch_scene(self, next_scene):
        self.next = next_scene

    # this method is called when the user input event is to terminate
    def terminate(self):
        self.switch_scene(None)

# Title Scene
class TitleScene(BaseScene):
    def __init__(self):
        print("Initializing TitleScene...")
        self.setup()
        BaseScene.__init__(self)

    def setup(self):
        print("Setting up TitleScene...")
        pyscenes.setBackgroundImage("assets/title_screen.jpg")

    def process_input(self, events, pressed_keys):
        print("process")

    def update(self):
        print("update")

    def render(self, screen):
        print("render")

    def cleanup(self):
        print("cleanup")

def main():
    instance = pyscenes.Runner(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    instance.run_game(TitleScene())  # pass a Scene object here to start the game

if __name__ == "__main__":
    main()