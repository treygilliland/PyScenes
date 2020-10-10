import pyscenes.pyscenes as pyscenes
from pyscenes.base_scene import BaseScene
from pyscenes.examples import title_screen
import os
import pytest
import time

# Game constants should be defined in scenes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30


class CounterScene(BaseScene):
    '''
    CounterScene is a minimum implementation of a Scene Object
    This scene is setup to make sure each method inside the scene is run the appropriate amount of time according to the FPS.
    '''

    def __init__(self, test_duration):
        self.test_duration = test_duration * FPS
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


@pytest.fixture
def game_instance():
    instance = pyscenes.Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    return instance


def test_game_instance_vars(game_instance):
    '''
    Tests to ensure the game variables were initalized correctly.
    '''
    assert game_instance.display.width == SCREEN_WIDTH
    assert game_instance.display.height == SCREEN_HEIGHT
    assert game_instance.fps == FPS


def test_mixer(game_instance):
    '''
    Tests to ensure music can be loaded, played, paused, and stopped.
    Note: Music will be played on your device.
    '''
    wd = os.getcwd()
    os.chdir("pyscenes/examples/")

    game_instance.mixer.loadMusic("assets/title_theme.ogg")
    game_instance.mixer.play()
    time.sleep(1)
    assert game_instance.mixer.paused == False
    game_instance.mixer.pause()
    assert game_instance.mixer.paused == True
    game_instance.mixer.stop()

    os.chdir(wd)


def test_load_image(game_instance):
    '''
    Tests to see if pyscenes can load an image properly.
    game_instance must be passed in to use pygame message.
    '''
    pyscenes.loadImage("pyscenes/examples/assets/title_screen.jpg")


def test_title_scene(game_instance):
    '''
    This tests to see if the title scene example is working correctly.
    Title scene example must be closed manually using x button, esc, or alt+f4.
    '''
    wd = os.getcwd()
    os.chdir("pyscenes/examples/")
    game_instance.run_game(title_screen.TitleScene(game_instance.display))
    os.chdir(wd)


def test_counter_scene(game_instance):
    '''
    See CounterScene above.
    '''
    game_instance.run_game(CounterScene(2))
