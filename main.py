
import pygame
from ball import Ball

pygame.font.init()

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

SCORE_TEXT = pygame.font.SysFont('Default Pixilart Text', 46)

SCORE_TEXT_RENDER = SCORE_TEXT.render("Score", True, WHITE)
SCORE_TEXT_CENTER = SCORE_TEXT_RENDER.get_rect(center=(WIDTH // 2, 525))

LEFT_PLAYER_SCORE_TEXT = pygame.font.SysFont('Default Pixilart Text', 44)
RIGHT_PLAYER_SCORE_TEXT = pygame.font.SysFont('Default Pixilart Text', 44) 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

left_player_score = 0
right_player_score = 0



ball = Ball(WIDTH // 2 - 10, HEIGHT // 2)


def check_left_goal(ball):
    if ball.x <  0:
        reset_ball(ball)
        return True
    else:
        return False
def check_right_goal(ball):
    if ball.x > WIDTH:
        reset_ball(ball)
        return True
    else:
        return False

def reset_ball(ball):
    # build 5 second count
    goal_text = pygame.font.SysFont('Default Pixilart Text', 46)
    goal_text_render = SCORE_TEXT.render("GOAL!", True, WHITE)
    goal_text_center = SCORE_TEXT_RENDER.get_rect(center=(WIDTH // 2, 250))
    WIN.blit(goal_text_render, goal_text_center)
    
    ball.x = WIDTH // 2 - 10
    ball.y = HEIGHT // 2

    ball.x_velocity = 5
    ball.y_velocity = 0

    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.display.flip()
    pygame.time.wait(1000)

def draw_dashed_line(surface, start_pos, end_pos):
    LINE_WIDTH = 5
    DASH_LENGTH = 20
    GAP_LENGTH = 10

    x1, y1 = start_pos
    x2, y2 = end_pos
    total_length = abs(y2 - y1)

    for i in range(0, total_length, DASH_LENGTH + GAP_LENGTH):
        pygame.draw.line(surface, WHITE, (x1, y1 + i), (x1, y1 + i + DASH_LENGTH), LINE_WIDTH)

def left_player_move(keys_pressed, left_player):
    if keys_pressed[pygame.K_w] and left_player.y - VEL > 0:
        left_player.y -= VEL
    if keys_pressed[pygame.K_s] and left_player.y + VEL + left_player.height + 5 < 500:
        left_player.y += VEL



def right_player_move(keys_pressed, right_player):
    if keys_pressed[pygame.K_UP] and right_player.y - VEL > 0:
        right_player.y -= VEL
    if keys_pressed[pygame.K_DOWN] and right_player.y + VEL + right_player.height + 5 < 500:
        right_player.y += VEL



        
def draw_window(left_player, right_player, ball):
    global left_player_score, right_player_score
    WIN.fill(BLACK)
    draw_dashed_line(WIN,(WIDTH // 2, 0), (WIDTH // 2, 500))
    pygame.draw.rect(WIN, WHITE, left_player)
    pygame.draw.rect(WIN, WHITE, right_player)
    pygame.draw.rect(WIN, WHITE, TOP_BORDER)
    pygame.draw.rect(WIN, WHITE, BOTTOM_BORDER)
    is_goal_right = check_right_goal(ball)
    if  is_goal_right:
        left_player_score += 1
    is_goal_left = check_left_goal(ball)
    if is_goal_left:
        right_player_score += 1
    left_player_score_string = str(left_player_score)
    right_player_score_string = str(right_player_score)
    WIN.blit(LEFT_PLAYER_SCORE_TEXT.render(left_player_score_string, 1, WHITE), (WIDTH // 4, 470))
    WIN.blit(SCORE_TEXT_RENDER, SCORE_TEXT_CENTER)
    WIN.blit(RIGHT_PLAYER_SCORE_TEXT.render(right_player_score_string, 1, WHITE), (WIDTH // 4 * 3, 470))
    ball.draw_ball()
    ball.move_ball(left_player, right_player, ball)
    pygame.display.flip()



def main():

    left_player = pygame.Rect(50,(HEIGHT // 2 - 15), PLAYER_WIDTH, PLAYER_HEIGHT)
    right_player = pygame.Rect(850, (HEIGHT // 2 - 15), PLAYER_WIDTH, PLAYER_HEIGHT)
    
    ball = Ball(WIDTH // 2 - 10, HEIGHT // 2)   #pygame.Rect(WIDTH// 2 - 10, HEIGHT // 2, 15, 15)
    
    
    
    
    pygame.init()

    clock = pygame.time.Clock()
    running = True
    # gmaeloop with 60 fps
    while running:
        clock.tick(60)
        draw_window(left_player, right_player, ball)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        left_player_move(keys_pressed, left_player)
        right_player_move(keys_pressed, right_player)


if __name__ == "__main__":
    main()