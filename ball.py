import pygame

WIDTH, HEIGHT = 900, 570
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BABY_BLUE = (137, 207, 240)
BORDER = pygame.Rect((WIDTH//2) - 5,0,10,500)
TOP_BORDER = pygame.Rect(0,0, 900, 5)
BOTTOM_BORDER = pygame.Rect(0, 490, 900, 5)
VEL = 5

PLAYER_HEIGHT, PLAYER_WIDTH = 40, 10


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
    MAX_VEL = 5


    def __init__(self,x , y):
        self.x = x
        self.y = y

        self.x_velocity = self.MAX_VEL
        self.y_velocity = 0
        

    def draw_ball(self):
        BALL = pygame.Rect(self.x, self.y, 15, 15)
        pygame.draw.rect(WIN, RED, BALL)

    def move_ball(self, left_player, right_player, ball):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.handle_collision(left_player, right_player, ball)
        

    def handle_collision(self, left_player,right_player, ball):
        BALL = pygame.Rect(self.x, self.y, 15, 15)
        left_center = left_player.y + left_player.height // 2
        right_center = right_player.y + right_player.height // 2

        left_displacement = (left_center - ball.y)
        right_displacement = (right_center - ball.y) 

        if BALL.colliderect(left_player) and self.x == 50:
            self.y_velocity = (self.y_velocity + left_displacement//10) * -1
            self.x_velocity = (self.x_velocity) * -1
        if BALL.colliderect(right_player) and self.x == 850:
            self.y_velocity = (self.y_velocity + right_displacement//10) * -1 
            self.x_velocity = (self.x_velocity) * -1
        if BALL.colliderect(TOP_BORDER):
            self.y_velocity = self.y_velocity * -1 
        if BALL.colliderect(BOTTOM_BORDER):
            self.y_velocity = self.y_velocity * -1
        
        if self.y_velocity > 5 or self.x_velocity > 5:
            self.y_velocity = self.y_velocity - 1
            self.x_velocity = self.x_velocity - 1





