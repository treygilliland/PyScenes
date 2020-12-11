"""
This file acts as a 5 Step template for all pyscenes games!
"""

# Step 1: Import the Game class
from pyscenes import Game

# Step 2: Import your starting scene
from template_scenes import TitleScene

# Step 3: Create a Game instance
game = Game(width=800, height=600, fps=30)

# Step 4: Create a Scene instance, passing in game instance
scene = TitleScene(game)

# Step 5: Run the game using the starting scene
game.run(scene)
