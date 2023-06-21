import turtle
import math
import random

#초기화 및 화면 설정
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Collision Detection by @TokyoEdtech")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

shapes = ["pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]

for shape in shapes:
    wn.register_shape(shape)


class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def is_distance_collision(self, other):
        distance = (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width) / 2.0:
            return True
        else:
            return False


class Character(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)

    def move_up(self):
        self.y += 24

    def move_down(self):
        self.y -= 24

    def move_left(self):
        self.x -= 24

    def move_right(self):
        self.x += 24


class Cherry(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)

    def reset_position(self):
        self.x = random.randint(-200, 200)
        self.y = random.randint(-200, 200)

#팩맨 캐릭터 위치 지정 및 체리 생성
pacman = Character(-128, 0, 128, 128, "pacman.gif")
cherry1 = Cherry(random.randint(-200, 200), random.randint(-200, 200), 128, 128, "cherry.gif")
cherry2 = Cherry(random.randint(-200, 200), random.randint(-200, 200), 128, 128, "cherry.gif")
cherry3 = Cherry(random.randint(-200, 200), random.randint(-200, 200), 128, 128, "cherry.gif")
cherry4 = Cherry(random.randint(-200, 200), random.randint(-200, 200), 128, 128, "cherry.gif")
cherry5 = Cherry(random.randint(-200, 200), random.randint(-200, 200), 128, 128, "cherry.gif")

sprites = [pacman, cherry1, cherry2, cherry3, cherry4, cherry5]


def move_pacman_up():
    pacman.move_up()


def move_pacman_down():
    pacman.move_down()


def move_pacman_left():
    pacman.move_left()


def move_pacman_right():
    pacman.move_right()


def update_score(score):
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


wn.listen()
wn.onkeypress(move_pacman_up, "w")
wn.onkeypress(move_pacman_down, "s")
wn.onkeypress(move_pacman_left, "a")
wn.onkeypress(move_pacman_right, "d")

score = 0
game_over = False

while not game_over:
    for sprite in sprites:
        sprite.render(pen)

    if pacman.is_distance_collision(cherry1):
        cherry1.reset_position()
        score += 1
        update_score(score)

    if pacman.is_distance_collision(cherry2):
        cherry2.reset_position()
        score += 1
        update_score(score)

    if pacman.is_distance_collision(cherry3):
        cherry3.reset_position()
        score += 1
        update_score(score)

    if pacman.is_distance_collision(cherry4):
        cherry4.reset_position()
        score += 1
        update_score(score)

    if pacman.is_distance_collision(cherry5):
        cherry5.reset_position()
        score += 1
        update_score(score)

    wn.update()
    pen.clearstamps()