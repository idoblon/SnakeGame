SnakeGame
Description

A classic Snake Game implemented in Python using the turtle graphics library. The goal is to control a snake, eat food to grow longer, and avoid colliding with the walls or itself.

Features

-Player-controlled snake using arrow keys

-Food that appears at random positions

-Growing snake body when food is eaten

-Score tracking

-Game over when the snake hits the wall or itself

-Basic speed control / delay to adjust difficulty


Installation

1. Clone the repository:
   git clone https://github.com/idoblon/SnakeGame.git
2. Go into the project directory:
   cd SnakeGame
3. Install dependencies:
   pip install -r requirements.txt  
If there isn’t a requirements.txt, make sure Python is installed (3.x) and you have the turtle module (standard in Python).

Usage

Run the game with:
- python main.py

Then use the arrow keys to control the snake’s movement:

-Up Arrow → move up

-Down Arrow → move down

-Left Arrow → move left

-Right Arrow → move right

-The snake moves continuously. Each time it eats the food, the snake grows, and your score increases. If the snake collides with the wall or its own body, the game ends.


Technologies

-Python 3 — main programming language

-Turtle — for graphics and rendering the game


Why This Project Matters / Use Cases

-Learning Tool: Great for beginners to learn Python basics, event handling, and game loops.

-Fun Project: A nostalgic throwback to the classic Snake game from early mobile phones.

-Extendable: You can enhance it with:

Sound effects

-Speed levels or difficulty settings

-High-score persistence (e.g., saving to a file)

-Better graphics / UI
