import turtle
import math

wn = turtle.Screen() #스크린 객체 생성
wn.bgcolor("black") # 배경 검정
wn.title("Collision Detection")
wn.tracer(0) #tracer 를 사용하여 애니메이션 효과를 줄수 있으며 0이면 애니메이션이 꺼진다.

pen = turtle.Turtle() # 그리기 객체생성
pen.speed(0) #그리기 속도는 0
pen.hideturtle() # 그리는 객체를 숨기기 위한 메소드

#사용할 그림을 배열로 선언
shapes = ["wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]

#shapes에 선언된 이미지를 TurtleScreen의 shapelist에 추가
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

    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def is_distance_collision(self, other):
        distance = (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width) / 2.0:
            return True
        else:
            return False

    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)


class Character(Sprite):
    def __init__(self, x, y, width, height, image, jump=False):
        super().__init__(x, y, width, height, image)
        self.jump = jump
        self.jump_height = 50  # 점프 높이
        self.jump_speed = 1   # 스피드
        self.jump_angle = 70  # 추가: 점프 각도 설정

    def hop(self, distance=1):
        if self.jump:
            for _ in range(self.jump_height):
                # x 좌표에 대한 이동
                self.x += self.jump_speed
                # 추가: y 좌표에 대한 하늘 이동
                self.y += self.jump_speed * math.sin(math.radians(self.jump_angle))
                self.render(pen)
                wn.update()
            for _ in range(self.jump_height):
                # x 좌표에 대한 이동
                self.x += self.jump_speed
                # 추가: y 좌표에 대한 아래 이동
                self.y -= self.jump_speed * math.sin(math.radians(self.jump_angle))
                self.render(pen)
                wn.update()
            self.x += distance


wizard = Character(-128, 200, 128, 128, "wizard.gif")
goblin = Sprite(128, 200, 108, 128, "goblin.gif")

pacman = Character(-128, 0, 128, 128, "pacman.gif", jump=True)
cherry = Sprite(128, 0, 128, 128, "cherry.gif")

bar = Sprite(0, -400, 128, 24, "bar.gif")
ball = Sprite(0, -200, 32, 32, "ball.gif")

sprites = [wizard, goblin, pacman, cherry, bar, ball]


def move_goblin():
    goblin.x -= 64


def move_pacman():
    pacman.x += 30


def jump_pacman(distance=1):
    pacman.hop(distance)


def move_ball():
    ball.y -= 24


wn.listen()
wn.onkeypress(move_goblin, "Left")
wn.onkeypress(move_pacman, "Right")
wn.onkeypress(jump_pacman, "space")
wn.onkeypress(move_ball, "Down")

while True:
    for sprite in sprites:
        sprite.render(pen)

    if wizard.is_overlapping_collision(goblin):
        wizard.image = "x.gif"

    if pacman.is_distance_collision(cherry):
        cherry.image = "x.gif"

    if bar.is_aabb_collision(ball):
        ball.image = "x.gif"

    wn.update()
    pen.clearstamps()