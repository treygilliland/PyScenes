# Centralized Scene Logic inspired by https://nerdparadise.com/programming/pygame/part7
# this is where the game itself comes to life
# the user should make their own scenes within this class
#   expecting that the runner will take care of the game loop itself
#   so the user can focus on making scenes using the methods available in
#   PyScenes

from abc import ABC, abstractmethod

# Abstract Base Scene class for all scene objects
# Essentially an implementation of the Model-View-Controller pattern
# setup, processInput, update, render, cleanup must be overridden


class BaseScene(ABC):
    # if init is overrided by the base class, super must be called
    @abstractmethod
    def __init__(self):
        self.next = self

    def __repr__(self):
        return self.__class__.__name__

    # called once when a Scene is initiated
    # responsible for setting up the scene and loading data
    @abstractmethod
    def setup(self):
        pass

    # first part of the core loop
    # responsible for parsing input events CONTROLLER
    @abstractmethod
    def process_input(self, events, pressed_keys):
        pass

    # second part of the core loop
    # responsible for handling the core game logic MODEL
    @abstractmethod
    def update(self):
        pass

    # third and final part of the core loop
    # responsible for updating the VIEW
    @abstractmethod
    def render(self, display):
        pass

    # called once when the scene is no longer used
    @abstractmethod
    def cleanup(self):
        pass

    # setter method for scene switching
    # do NOT override
    def switch_scene(self, next_scene):
        self.next = next_scene

    # this method is called when the user input event is to terminate
    # do NOT override
    def terminate(self):
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
