# PyScenes

![GitHub](https://img.shields.io/github/license/treygilliland/PyScenes?style=plastic)

PyScenes is [PyGame 2](https://www.pygame.org/wiki/about) library designed to provide the high-level functionality used in games and multi-media programs so that users can focus on creating rather than debugging. PyScenes aims to provide classes and functions related to sprites, backgrounds, sounds, images, text, and more!

## Installation and Usage

There are 2 main ways to use PyScenes:

1. PyScenes with Runner Class

> This is the intended way to use PyScenes for beginners and for starting a new project.
> To create your own game, all you need to do is create subclasses of the BaseScene class 
> that contain your code for each "scene" of your game.

2. PyScenes standalone

> PyScene methods can be used on existing projects with some integration work. 
> PyScene contains static functions that operate at higher levels than PyGame itself offers
> so feel free to import these functions for use in your own project.

To see an example of using PyScenes, navigate to the examples directory 
and run any of the self-contained examples there. More coming soon!

## Contributing

Coming Soon.

See CONTRIBUTING.md for more.

## License
Distributed under the GPLv3 license. See LICENSE.md for more.

## Acknowledgements

PyScenes is heavily inspired by and contains code from 
[Pygame_functions](https://github.com/StevePaget/Pygame_Functions) by Steve Paget.
This library was very useful when I first started learning to make games with Python and 
its simplicity and ease of use is a great motivation for the project.

The code for the scene-based OOP implementation comes from the Nerd Paradise blog pygame tutorial.
See more [here](https://nerdparadise.com/programming/pygame/part7).