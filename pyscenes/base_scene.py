# Centralized Scene Logic inspired by https://nerdparadise.com/programming/pygame/part7
# this is where the game itself comes to life
# the user should make their own scenes within this class
#   expecting that the runner will take care of the game loop itself
#   so the user can focus on making scenes using the methods available in
#   PyScenes

from abc import ABC, abstractmethod

class BaseScene(ABC):
    """
    Abstract Scene template class that allows PyScenes to manage the scene context switching.

    All user-defined scenes should inherit from this class.
    All scenes MUST override the setup, processInput, update, render, cleanup methods.
    Functionality can be minimal, but it is safe practice to require each of them.
    """
    #Note: if init is overrided by the base class, super must be called

    @abstractmethod
    def __init__(self):
        self.next = self

    def __repr__(self):
        return self.__class__.__name__


    @abstractmethod
    def setup(self):
        """
        Method responsible for setting up scene and loading necessary data.

        Called once when a Scene is initiated.
        """
        pass

    # first part of the core loop
    # responsible for parsing input events CONTROLLER
    @abstractmethod
    def process_input(self, events, pressed_keys):
        """
        Responsible for processing user inputs into game functionality.

        Called once each clock tick.
        """
        pass

    # second part of the core loop
    # responsible for handling the core game logic MODEL
    @abstractmethod
    def update(self):
        """
        Responsible for updating game model, sprites, and data.

        Called once each clock tick.
        """
        pass

    # third and final part of the core loop
    # responsible for updating the VIEW
    @abstractmethod
    def render(self, display):
        """
        Responsible for processing user inputs into game functionality.

        Called once each clock tick.
        """
        pass

    # called once when the scene is no longer used
    @abstractmethod
    def cleanup(self):
        """
        Responsible for saving state and destroying scene objects.

        Called once when scene is switched/terminated.
        """
        pass

    # setter method for scene switching
    # do NOT override
    def switch_scene(self, next_scene):
        """
        Takes in a scene to switch to.

        This method should be called in above methods when user wants to switch scenes.

        :param next_scene: Scene to switch to
        :type next_scene: Scene object inherting from BaseScene abstract class
        """
        self.next = next_scene

    # this method is called when the user input event is to terminate
    # do NOT override
    def terminate(self):
        """
        Terminates the game.
        """
        self.switch_scene(None)


# example implementation of the base scene
# class TitleScene(BaseScene):
#     def setup(self):
#         print("setup")

#     def process_input(self, events, pressed_keys):
#         print("process")

#     def update(self):
#         print("update")

#     def render(self, screen):
#         print("render")

#     def cleanup(self):
#         print("cleanup")
