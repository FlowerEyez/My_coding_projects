import pygame
import pygame_menu
import pygame_menu.events
import pygame_menu.themes
from settings import WIDTH, HEIGHT, FPS, BACKGROUND_COLOR, TILE_SIZE, MINIMAP_SCALE
from map import game_map
from player import Player
from raycasting import cast_rays

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raycast Game")
clock = pygame.time.Clock()

# Game state flags
game_active = False
paused = False
show_main_menu = True

# Create the Player
player = Player(100, 100) # stating postion (x, y)

# capture mouse for rotation
mouse_locked = True

# Draw the minimap
def draw_minimap(screen, player, map_data):
	for y, row in enumerate(map_data):
		for x, tile in enumerate(row):
			color = (255, 255, 255) if tile else (30, 30, 30)
			rect = pygame.Rect(
				x * TILE_SIZE * MINIMAP_SCALE + 5,
				y * TILE_SIZE * MINIMAP_SCALE + 5,
				TILE_SIZE * MINIMAP_SCALE,
				TILE_SIZE * MINIMAP_SCALE
			)
			pygame.draw.rect(screen, color, rect)

	# Draw player on minimap
	pygame.draw.circle(
	screen,
	(255, 0, 0),
	(
		int(player.x * MINIMAP_SCALE) + 5,
		int(player.y * MINIMAP_SCALE) + 5
		),
		3
	)
# Menu callbacks
def start_game():
	global game_active, paused, show_main_menu, mouse_locked
	game_active = True
	paused = False
	show_main_menu = False
	mouse_locked = True
	pygame.mouse.set_visible(False)
	pygame.event.set_grab(True)

def back_to_main_menu():
	global game_active, paused, show_main_menu, mouse_locked
	game_active = False
	paused = False
	show_main_menu = True
	mouse_locked = False
	pygame.mouse.set_visible(True)
	pygame.event.set_grab(False)

def resume_game():
	global paused, mouse_locked
	paused = False
	mouse_locked = True
	pygame.mouse.set_visible(False)
	pygame.event.set_grab(True)

def quit_game():
	pygame.quit()
	exit()

# Main menu
main_menu = pygame_menu.Menu('Raycaster Game', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
main_menu.add.button('Start Game', start_game)
main_menu.add.button('Quit', quit_game)

# Pause menu
pause_menu = pygame_menu.Menu('Paused', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
pause_menu.add.button('Resume', resume_game)
pause_menu.add.button('Main menu', back_to_main_menu)
pause_menu.add.button('Quit', quit_game)

# Game loop
running = True

while running:
	dt = clock.tick(FPS)
	screen.fill(BACKGROUND_COLOR)
	events = pygame.event.get()

	for event in events:
		if event.type == pygame.QUIT:
			running= False

		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			print("Escape pressed")  # DEBUG
			if game_active and not paused:
				print("Pausing game")  # DEBUG
				paused = True
				mouse_locked = False
				pygame.mouse.set_visible(True)
				pygame.event.set_grab(False)
			elif paused:
				print("Resuming game")  # DEBUG
				resume_game()

	if show_main_menu:
		main_menu.update(events)
		main_menu.draw(screen)
	
	elif paused:
		pause_menu.update(events)
		pause_menu.draw(screen)

	elif game_active and not paused:
		keys = pygame.key.get_pressed()
		player.update(keys, game_map)
		player.mouse_rotation()
		cast_rays(screen, player, game_map)
		draw_minimap(screen, player, game_map)

	pygame.display.flip()

pygame.quit()