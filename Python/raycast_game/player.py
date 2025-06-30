import math
import pygame
from settings import TILE_SIZE, PLAYER_SPEED, PLAYER_ROT_SPEED

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = PLAYER_SPEED
        self.rot_speed = PLAYER_ROT_SPEED

    def update(self, keys, map_data):
        self.move(keys, map_data)
        self.rotate(keys)

    def move(self, keys, map_data):
        dx, dy = 0, 0
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dx += cos_a * self.speed
            dy += sin_a * self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dx -= cos_a * self.speed
            dy -= sin_a * self.speed
        if keys[pygame.K_a]:
            dx += sin_a * self.speed
            dy -= cos_a * self.speed
        if keys[pygame.K_d]:
            dx -= sin_a * self.speed
            dy += cos_a * self.speed

        new_x = self.x + dx
        new_y = self.y + dy

        # Collision detection
        if map_data[int(self.y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            self.x = new_x
        if map_data[int(new_y / TILE_SIZE)][int(self.x / TILE_SIZE)] == 0:
            self.y = new_y

    def rotate(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle -= self.rot_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.rot_speed

    def mouse_rotation(self):
        rel_x = pygame.mouse.get_rel()[0]
        self.angle += rel_x * 0.002 # mouse sensitivity

    def update(self, keys, map_data):
        self.move(keys, map_data)
        self.rotate(keys)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 5)
