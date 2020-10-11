import pyscenes.pyscenes as pyscenes
from pyscenes.examples.title_screen import TitleScene
from counter_scene import CounterScene
import os
import pytest
import time

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"


# Define Game constants here for same size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30


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
    game_instance.run_game(
        TitleScene(game_instance.display, True))
    os.chdir(wd)


def test_counter_scene(game_instance):
    '''
    See CounterScene above.
    '''
    game_instance.run_game(CounterScene(game_instance, 2))
