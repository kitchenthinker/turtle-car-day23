import game_screen_and_graphic, cars, player, math, time, turtle, random

GAP_BETWEEN_CELLS = 20
TIME_SLEEP = 0.07
TURTLE_STEPS = 10
OPPOSITE_ANGLE = 180


def check_collisions_2_obj(f_obj: turtle.Turtle, s_obj: turtle.Turtle):
    x_collision = (math.fabs(f_obj.xcor() - s_obj.xcor()) * 2) < (f_obj.pensize() + s_obj.pensize())
    y_collision = (math.fabs(f_obj.ycor() - s_obj.ycor()) * 2) < (f_obj.pensize() + s_obj.pensize())
    return x_collision and y_collision


def check_collisions_2_obj_food(f_obj: turtle.Turtle, s_obj: turtle.Turtle):
    return f_obj.distance(s_obj) < s_obj.pensize()*2


class MainGame:

    def __init__(self):
        self.game_screen_and_graphic = game_screen_and_graphic.GameScreen()
        self.game_screen = self.game_screen_and_graphic.screen
        self.scoreboard = self.game_screen_and_graphic.scoreboard
        self.player = None
        self.car_traffic = []
        self.create_player()
        self.create_car_traffic()
        # self.player = game_players.PlayerStick()
        # self.opponent = game_players.PlayerStick(False)
        self.game_is_on = True
        self.game_screen.update()

    def create_player(self):
        self.player = player.PlayerTurtle()
        self.player.set_default_position(ycor=-game_screen_and_graphic.DEFAULT_SCREEN_HEIGHT/2 + 20)

    def cross_the_line(self):
        if self.player.ycor() > game_screen_and_graphic.DEFAULT_SCREEN_HEIGHT/2 - 50:
            self.scoreboard.player_score.increase_level()
            self.player.set_default_position(ycor=-game_screen_and_graphic.DEFAULT_SCREEN_HEIGHT / 2 + 20)
            self.create_car_traffic()

    def create_car_traffic(self):
        if len(self.car_traffic) > 0:
            for x in self.car_traffic:
                x.reset()
            self.car_traffic.clear()
        for _ in range(random.randint(10, 100)):
            self.append_car_2_car_traffic()

    def car_traffic_movement(self):
        for car in self.car_traffic:
            car.move()
            if car.xcor() < -game_screen_and_graphic.DEFAULT_SCREEN_WIDTH/2 - 50:
                self.car_traffic.remove(car)
                self.append_car_2_car_traffic()

    def append_car_2_car_traffic(self):
        x_cor = int(game_screen_and_graphic.DEFAULT_SCREEN_WIDTH/2) + random.randrange(100, 1000, 10)
        ycor = int(game_screen_and_graphic.DEFAULT_SCREEN_HEIGHT/2) - game_screen_and_graphic.DEFAULT_ALIGNMENT*2
        new_car = cars.Car()
        new_car.set_up_default_position(x_cor, random.randrange(-ycor, ycor, 40))
        self.car_traffic.append(new_car)

    def start_game(self):
        self.game_screen.listen()
        self.game_screen.onkeypress(self.player.go_north, 'w')
        self.game_screen.onkey(self.reset_game, 'c')

        while self.game_is_on:

            time.sleep(TIME_SLEEP)
            self.scoreboard.write_scoreboard()
            self.game_screen.update()
            self.car_traffic_movement()
            self.cross_the_line()
            self.is_collision_with_car()
            # self.check_collision_with_walls()
            # self.check_collision_with_players()
            # self.ball.move()
            # self.opponent.ai_moving()
            # time.sleep(TIME_SLEEP)
            # self.write_game_score()
            # self.game_screen.update()
            # self.snake.move()
            # self.check_collisions_with_walls()
            # self.check_collisions_with_tail()
            # self.check_collision_with_apple()
            # self.check_game_is_over()

        self.game_screen.mainloop()

    def is_collision_with_car(self):
     #   print(self.check_collision_with_players())
        if self.check_collision_with_players():
            self.scoreboard.write_game_over()
            self.game_is_on = False

    def check_collision_with_players(self):
        for car in self.car_traffic:
            if self.player.distance(car) < 20:# and (abs(self.player.ycor() - car.ycor()) < 5):
                return True
        return False

    # def check_game_is_over(self):
    #     if not self.snake.moving:
    #         self.game_is_on = False
    #         self.graphics.setposition(0, 0)
    #         self.graphics.write(f"GAME OVER:", False, align="center",
    #                             font=("Small fonts", 18, "bold"))
    #         return True
    #     return False

    def reset_game(self):
        self.__init__()
        self.start_game()

    # def increase_game_point_counter(self):
    #     self.game_points += 1

    # def check_collisions_with_tail(self):
    #     snake = self.snake
    #     for segment in range(1, len(snake.body) - 1, 1):
    #         if check_collisions_2_obj(snake.head, snake.body[segment]):
    #             self.snake.set_moving_var(False)

    # def check_collisions_with_walls(self):
    #     x_cor = self.snake.head.xcor()
    #     y_cor = self.snake.head.ycor()
    #     w_width = self.game_screen.window_width()
    #     w_height = self.game_screen.window_height()
    #     ###
    #     left_wall = - (w_width/2)
    #     right_wall = (w_width/2)
    #     up_wall = (w_height/2)
    #     down_wall = - (w_height/2)
    #     ###
    #     if (x_cor >= right_wall) or (x_cor <= left_wall) or (y_cor >= up_wall) or (y_cor <= down_wall):
    #         self.snake.set_moving_var(False)