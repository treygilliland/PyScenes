#Self-contained test scene ensuring Game.run_game() works properly
import pyscenes.pyscenes as pyscenes
from pyscenes.base_scene import BaseScene

class CounterScene(BaseScene):
    '''
    CounterScene is a minimum implementation of a Scene Object
    This scene is setup to make sure each method inside the scene is run the appropriate amount of time according to the FPS.
    '''

    def __init__(self, game, test_duration):
        self.game = game
        self.test_duration = test_duration * game.fps
        self.setup_count = 0
        self.process_input_count = 0
        self.update_count = 0
        self.render_count = 0
        self.cleanup_count = 0
        super().__init__()

    def setup(self):
        self.setup_count += 1
        print("setup called", self.setup_count, "times")

    def process_input(self, events, pressed_keys):
        self.process_input_count += 1

    def update(self):
        self.update_count += 1

    def render(self, screen):
        self.render_count += 1

        if self.render_count == self.test_duration:
            super().terminate()

    def cleanup(self):
        self.cleanup_count += 1
        print("setup called", self.cleanup_count, "times")

        print("setup test")
        assert self.setup_count == 1
        assert self.process_input_count == self.test_duration
        assert self.update_count == self.test_duration
        assert self.render_count == self.test_duration
        print("cleanup test")
        assert self.cleanup_count == 1
