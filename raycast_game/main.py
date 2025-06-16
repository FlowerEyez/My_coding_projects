import pygame
from settings import WIDTH, HEIGHT, FPS, BACKGROUND_COLOR, TILE_SIZE, MINIMAP_SCALE
from map import game_map
from player import Player
from raycasting import cast_rays

# Minimap scale
MINIMAP_SCALE = 0.2

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raycast Game")
clock = pygame.time.Clock()

# Create the Player
player = Player(100, 100) # stating postion (x, y)

# capture mouse for rotation
mouse_locked = True
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

# Draw the minimap
def draw_minimap(screen, player, map_data):
	for y, row in enumerate(map_data):
		for x, tile in enumerate(row):
			color = (255, 255, 255) if tile else (30, 30, 30)
			rect = pygame.Rect(
				x * TILE_SIZE * MINIMAP_SCALE,
				y * TILE_SIZE * MINIMAP_SCALE,
				TILE_SIZE * MINIMAP_SCALE,
				TILE_SIZE * MINIMAP_SCALE
			)
			pygame.draw.rect(screen, color, rect)

	# Draw player on minimap
	pygame.draw.circle(
	screen,
	(255, 0, 0),
	(
		int(player.x * MINIMAP_SCALE),
		int(player.y * MINIMAP_SCALE)
		),
		3
	)

running = True
while running:
	dt = clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running= False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				mouse_locked = not mouse_locked
				pygame.event.set_grab(mouse_locked)
				pygame.mouse.set_visible(not mouse_locked)

	keys = pygame.key.get_pressed()
	player.update(keys, game_map)
	if mouse_locked:
		player.mouse_rotation()

	screen.fill(BACKGROUND_COLOR)

	cast_rays(screen, player, game_map)
	draw_minimap(screen, player, game_map)

	pygame.display.flip()

pygame.quit()
