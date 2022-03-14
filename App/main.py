import pygame, sys
import os
from starBattle import *

# WIDTH = 600
# HEIGHT = 600

# # Colours
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# LIGHTBLUE = (96, 216, 232)
# LOCKEDCELLCOLOUR = (189,189,189)
# INCORRECTCELLCOLOUR = (195,121,121)

# assets_path = os.getcwd() + "\\..\\Assets"
# os.chdir(assets_path)


# # Positions and sizes
# gridPos = (75,100)
# cellSize = 50
# gridSize = cellSize*9

# # Test board
# map = [
#     [0,0,5,5],
#     [0,3,2,3],
#     [2,3,2,5],
#     [2,4,4,4],
#     [3,0,3,4],
#     [3,1,4,1],
#     [3,4,4,4],
#     [4,1,4,4],
#     [4,2,5,1]
# ]

# pygame.init()

# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Hello world!')
# star = pygame.image.load(os.getcwd() + '\\star.png')

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     window.fill(WHITE)
#     gridSize = cellSize*map[0][3]
#     cellSize = 450/map[0][3]
#     intdent = 10
#     star = pygame.transform.scale(star, (cellSize-2*intdent, cellSize-2*intdent))
#     # print(type(cellSize))
#     pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], cellSize*map[0][3], cellSize*map[0][3]), 4)
#     for x in range(map[0][3]):
#         pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450), 1)
#         pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+450, gridPos[1]++(x*cellSize)), 1)
#     for x in map[1:]:
#         if x[0] == x[2]:
#             pygame.draw.line(window, BLACK, (gridPos[0]+(x[1]*cellSize), gridPos[1]+(x[0]*cellSize)), (gridPos[0]+(x[3]*cellSize), gridPos[1]+(x[0]*cellSize)), 4)
#         else:
#             pygame.draw.line(window, BLACK, (gridPos[0]+(x[1]*cellSize), gridPos[1]+(x[0]*cellSize)), (gridPos[0]+(x[1]*cellSize), gridPos[1]+(x[2]*cellSize)), 4)

#     # place star
#     window.blit(star,(gridPos[0]+intdent,gridPos[1]+intdent))
#     window.blit(star,(gridPos[0]+3*cellSize+intdent,gridPos[1]+intdent))





#     pygame.display.update()
def main():
    app = StarBattle()
    app.run()

if __name__ == "__main__":
	main()