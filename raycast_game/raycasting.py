import math
import pygame
from settings import WIDTH, HEIGHT, FOV, NUM_RAYS, MAX_DEPTH, WALL_COLOR
from map import game_map, TILE_SIZE

def cast_rays(screen, player, map_data):
	ray_angle = player.angle - math.radians(FOV / 2)
	angle_step = math.radians(FOV) / NUM_RAYS

	for ray in range(NUM_RAYS):
		for depth in range(0, MAX_DEPTH * TILE_SIZE, 5): # Step every 5 pixels
			target_x = player.x + math.cos(ray_angle) * depth
			target_y = player.y + math.sin(ray_angle) * depth

			map_x = int(target_x / TILE_SIZE)
			map_y = int(target_y / TILE_SIZE)

			if 0 <= map_y < len(map_data) and 0 <= map_x < len(map_data[0]):
				if map_data[map_y][map_x] == 1:
					# Correct fish-eye
					corrected_depth = depth * math.cos(ray_angle - player.angle)
					wall_height = 30000 / (corrected_depth + 0.0001)
					screen_x = int(ray * (WIDTH / NUM_RAYS))
					pygame.draw.line(screen, WALL_COLOR, (screen_x, y1), (screen_x, y2))
					break
		ray_angle += angle_step
