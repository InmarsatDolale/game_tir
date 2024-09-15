from turtledemo.nim import SCREENWIDTH

import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tir")
icon = pygame.image.load("img/shooting-target-png-1.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/img.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
score_area_width = 200
score_area_height = 50

hit_count = 0

color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
font = pygame.font.SysFont('Arial', 36)


def get_new_target_position():
    while True:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        if not (target_x > SCREEN_WIDTH - score_area_width - target_width and target_y < score_area_height):
            return target_x, target_y

target_x, target_y = get_new_target_position()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x, target_y = get_new_target_position()
                hit_count += 1
                print(f"Попаданий: {hit_count}")
                color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))


    screen.blit(target_img, (target_x, target_y))

    hit_text = font.render(f"Попаданий: {hit_count}", True, (255, 255, 255))
    text_width = hit_text.get_width()
    screen.blit(hit_text, (SCREEN_WIDTH - text_width - 10, 10))
    pygame.display.update()

pygame.quit()