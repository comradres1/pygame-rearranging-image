"""
Game of re-arranging image of the tv cartoon tom and jerry.

group comrades1
group members
1.ADAUN MICHEAL REGNO: 16/U/1886
2.NYIVURU DIANA REGNO: 16/U/1856
3.AMAU MOSES    REGNO: 16/U/1808
4.RUKUNDO MUTANA PETER REGNO:16/U/1082
5.IRADUKUNDA SILVAN REGNO: 16/U/4938/PS

"""

import sys, pygame
import random
from pygame.locals import *

pygame.init()

# Initialize variables.

tile_size = 160
size = width, height = 480, 480
font = pygame.font.Font(None, 14)

screen = pygame.display.set_mode(size)
image = pygame.image.load('tom.jpg')

# These are the valid adjacent squares.

above, below = (0, -tile_size), (0, tile_size)
left, right = (-tile_size, 0), (tile_size, 0) 

# Create tiles.

tiles = []
for x_pos in range(width / tile_size):
    for y_pos in range(height / tile_size):
        area = pygame.Rect(x_pos * tile_size, y_pos * tile_size,
                           tile_size, tile_size)
        tile = pygame.Surface((tile_size, tile_size))
        tile.blit(image, (0, 0), area)
        tiles.append([area, tile])

# Replace last tile with black square.

tiles[-1][1] = pygame.Surface((tile_size, tile_size))
black_tile = tiles[-1]

# Mix up tile locations.

for rpt in range(1000):
    # Swap black tile with random adjacent tile.
    areas = map(black_tile[0].move, (above, below, left, right))
    adjacent_tiles = [tile for tile in tiles if tile[0] in areas]
    tile = random.choice(adjacent_tiles)
    tile[0], black_tile[0] = black_tile[0], tile[0]

while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
            # TODO: Respond to arrow keys.
            pass
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN:
        # Swap a clicked tile if it is adjacent.

        place = ((event.pos[0] / tile_size) * tile_size,
                 (event.pos[1] / tile_size) * tile_size)

        tile = [tile for tile in tiles if tile[0].topleft == place][0]

        diff = (tile[0][0] - black_tile[0][0],
                tile[0][1] - black_tile[0][1])

        if diff in (above, below, left, right):
            black_tile[0], tile[0] = tile[0], black_tile[0]

    for tile in tiles:
        screen.blit(tile[1], tile[0])

    pygame.display.flip()
