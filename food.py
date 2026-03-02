from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self, snake_segments=None):
        while True:
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            self.goto(random_x, random_y)
            
            if snake_segments is None:
                break
            
            collision = False
            for segment in snake_segments:
                if self.distance(segment) < 20:
                    collision = True
                    break
            
            if not collision:
                break