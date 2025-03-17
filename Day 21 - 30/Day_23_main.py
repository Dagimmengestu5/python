from turtle import Turtle, Screen
import random
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-220,260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))
    def increas_lavel(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

color = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_move_distance = 5
moving_instrument = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = starting_move_distance
    def creat_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(color))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(moving_instrument)
    def level_up(self):
        self.car_speed += move_distance_1


starting_position = (0, -280)
move_distance_1 = 10
move_distance_2 = -10
finish_line_y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(starting_position) # keyet endemetnesa
        self.setheading(90)  # turtelwan lemazor
    def go_up(self):
        self.forward(move_distance_1)

    def go_down(self):
        self.forward(move_distance_2)
    def is_at_finish_line(self):
        if self.ycor() > finish_line_y:
            return True
        else:
            return False

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car_manager.creat_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
       if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.goto(starting_position)
        car_manager.level_up()
        scoreboard.increas_lavel()
screen.exitonclick()