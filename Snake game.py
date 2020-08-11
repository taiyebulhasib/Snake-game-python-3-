import pygame
import sys
import random
import time

display_size = (1080, 480)
snakehead = [360, 240]
snakebody = []
direction = 'RIGHT'
food = [random.randrange(1, display_size[0] // 10) * 10, random.randrange(1, display_size[1] // 10 - 20) * 10]
score = 0
game_over = False
pygame_error = pygame.init()
if pygame_error[1] > 0:
    print('{} error while initializing pygame. exiting!!'.format(pygame_error[1]))
    sys.exit(1)
else:
    print('PyGame initialized')
window = pygame.display.set_mode(display_size)
pygame.display.set_caption('Snake Game by T.Hasib')
# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)
sky_blue = pygame.Color(0, 255, 255)
window.fill(black)
pygame.display.flip()
fpsController = pygame.time.Clock()
blocksize = 10
snakebody = [[snakehead[0], snakehead[1]]]
for i in range(4):
    snakebody.append([snakebody[i][0] - blocksize, snakebody[i][1]])

def update():
    global snakehead, snakebody, direction, food, score, game_over
    if direction == 'RIGHT':
        snakehead = [snakehead[0] + blocksize, snakehead[1]]
    if direction == 'LEFT':
        snakehead = [snakehead[0] - blocksize, snakehead[1]]
    if direction == 'UP':
        snakehead = [snakehead[0], snakehead[1] - blocksize]
    if direction == 'DOWN':
        snakehead = [snakehead[0], snakehead[1] + blocksize]
    snakebody.insert(0, list(snakehead))
    if snakehead[0] == food[0] and snakehead[1] == food[1]:
        food = [random.randrange(1, display_size[0] // 10) * 10, random.randrange(1, display_size[1] // 10 - 20) * 10]
        score += 1
    else:
        snakebody.pop()
    if snakehead[0] <= 0 or snakehead[0] >= display_size[0]:
        game_over = True
    if snakehead[1] <= 0 or snakehead[1] >= display_size[1]:
        game_over = True
    for block in snakebody[1:]:
        if snakehead[0] == block[0] and snakehead[1] == block[1]:
            game_over = True

def render():
    global snakebody, fpsController, window, score
    window.fill(sky_blue)
    for bit in snakebody:
        pygame.draw.rect(window, red, pygame.Rect(bit[0], bit[1], 10, 10))
    pygame.draw.rect(window, blue, pygame.Rect(food[0], food[1], blocksize, blocksize))
    hudfont = pygame.font.SysFont('monaco', 24)
    hud_score = hudfont.render('Score: {}'.format(score), True, red)
    hud_score_rect = hud_score.get_rect()
    hud_score_rect.midtop = (360, 20)
    hud_game_state = hudfont.render('{}'.format('Playing'), True, black)
    hud_game_state_rect = hud_game_state.get_rect()
    hud_game_state_rect.midtop = (660, 20)
    window.blit(hud_score, hud_score_rect)
    window.blit(hud_game_state, hud_game_state_rect)
    pygame.display.flip()
    fpsController.tick(15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keypressed = event.key
            if keypressed == pygame.K_RIGHT:
                direction = 'RIGHT'
            if keypressed == pygame.K_LEFT:
                direction = 'LEFT'
            if keypressed == pygame.K_UP:
                direction = 'UP'
            if keypressed == pygame.K_DOWN:
                direction = 'DOWN'
    if not game_over:
        update()
        render()
    else:
        hudfont = pygame.font.SysFont('monaco', 24)
        hud_score = hudfont.render('Score: {}'.format(score), True, red)
        hud_score_rect = hud_score.get_rect()
        hud_score_rect.midtop = (360, 20)
        gg_text = hudfont.render('GG WP. Press any key to continue', True, black)
        gg_rect = gg_text.get_rect()
        gg_rect.midtop = (360, 260)
        window.fill(white)
        window.blit(gg_text, gg_rect)
        window.blit(hud_score, hud_score_rect)
        pygame.display.flip()
        fpsController.tick(15)
        time.sleep(3)
        sys.exit(1)
