import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
run_time = 1
while game_is_on:
    time.sleep(0.1)
    if run_time % 6 == 0:
        car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    if car_manager.check_collision(player):
        game_is_on = False
        new_scoreboard = Scoreboard()
        new_scoreboard.game_over()

    if player.check_finish():
        scoreboard.increase_level()
        car_manager.increase_speed()

    screen.update()
    run_time += 1

screen.exitonclick()
