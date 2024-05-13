from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_distance = 5

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.color(random.choice(COLORS))
        new_car.pu()
        new_car.shapesize(1, 2)
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT



