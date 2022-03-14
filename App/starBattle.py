import pygame, sys
import os
from settings import *
import numpy as np

assets_path = os.getcwd() + "\\..\\Assets"
os.chdir(assets_path)
star = pygame.image.load(os.getcwd() + '\\star.png')
star = pygame.transform.scale(star, (cellSize-2*intdent, cellSize-2*intdent))
leftArrow = pygame.image.load(os.getcwd() + '\\leftArrow.png')
leftArrow = pygame.transform.scale(leftArrow, (50, 50))
rightArrow = pygame.image.load(os.getcwd() + '\\rightArrow.png')
rightArrow = pygame.transform.scale(rightArrow, (50, 50))
upArrow = pygame.image.load(os.getcwd() + '\\upArrow.png')
upArrow = pygame.transform.scale(upArrow, (15, 15))
downArrow = pygame.image.load(os.getcwd() + '\\downArrow.png')
downArrow = pygame.transform.scale(downArrow, (15, 15))
background = pygame.image.load(os.getcwd() + '\\background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

class StarBattle:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Star Battle Puzzle')
        self.running = True
        self.state = "init"
        self.mapIdx = 0
        self.algorithm = "Breadth First Search"
        self.maps = self.getMaps()
        

    def run(self):
        while self.running:
            self.window.blit(background,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.state == "init":
                        if self.mapIdx < len(self.maps) - 1:
                            self.mapIdx += 1
                        else: self.mapIdx = 0
                    if event.key == pygame.K_LEFT and self.state == "init":
                        if self.mapIdx > 0:
                            self.mapIdx -= 1
                        else: self.mapIdx = len(self.maps) - 1
                    if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and self.state == "init":
                        self.algorithm = "Breadth First Search" if self.algorithm  == "Hill Climbing" else "Hill Climbing"
            if self.state == "init":
                print("run")
                self.startScreen()
            pygame.display.update()
        pygame.quit()
    
    def getMaps(self):
        path = os.getcwd() + '\\..\\Maps'
        os.chdir(path)
        list_maps = []
        for file in os.listdir():
            if file.endswith(".txt"):
                file_path = f"{path}\{file}"
                map = np.loadtxt(f"{file_path}", dtype=int, delimiter=',')
                list_maps.append(map)
        return list_maps
    
    def draw_board(self,map,size,pos):
        mapSize= map[0][0]
        cellSize = size/mapSize
        pygame.draw.rect(self.window, BLACK, (pos[0], pos[1], cellSize*mapSize, cellSize*mapSize), 4)
        for x in range(mapSize):
            pygame.draw.line(self.window, BLACK, (pos[0]+(x*cellSize), pos[1]), (pos[0]+(x*cellSize), pos[1]+size), 1)
            pygame.draw.line(self.window, BLACK, (pos[0], pos[1]+(x*cellSize)), (pos[0]+size, pos[1]++(x*cellSize)), 1)
        for x in map[1:]:
            if x[0] == x[2]:
                pygame.draw.line(self.window, BLACK, (pos[0]+(x[1]*cellSize), pos[1]+(x[0]*cellSize)), (pos[0]+(x[3]*cellSize), pos[1]+(x[0]*cellSize)), 4)
            else:
                pygame.draw.line(self.window, BLACK, (pos[0]+(x[1]*cellSize), pos[1]+(x[0]*cellSize)), (pos[0]+(x[1]*cellSize), pos[1]+(x[2]*cellSize)), 4)

    def startScreen(self):
        os.chdir(assets_path)
        titleSize = pygame.font.Font('gameFont.ttf', 60)
        titleText = titleSize.render('Star Battle', True, BLACK)
        titleRect = titleText.get_rect(center=(300, 50))
        self.window.blit(titleText, titleRect)

        desSize = pygame.font.Font('gameFont.ttf', 20)
        desText = desSize.render('Choose the Map and Algorithm.', True, BLACK)
        desRect = desText.get_rect(center=(300, 115))
        self.window.blit(desText, desRect)
        desText = desSize.render('Then press Enter to start.', True, BLACK)
        desRect = desText.get_rect(center=(300, 140))
        self.window.blit(desText, desRect)

        mapSize = pygame.font.Font('gameFont.ttf', 30)
        mapText = mapSize.render("Map." + str(self.mapIdx + 1), True, BLACK)
        mapRect = mapText.get_rect(center=(300, 180))
        self.window.blit(mapText, mapRect)

        self.window.blit(leftArrow,(80,320))
        self.window.blit(rightArrow,(470,320))

        algorithmSize = pygame.font.Font('gameFont.ttf', 24)
        algorithmDes = algorithmSize.render('Algorithm', True, BLACK)
        algorithmRect = algorithmDes.get_rect(center=(300, 510))
        self.window.blit(algorithmDes, algorithmRect)

        self.window.blit(upArrow,(370,500))
        self.window.blit(downArrow,(370,512))

        algorithmSize = pygame.font.Font('gameFont.ttf', 28)
        algorithmText = algorithmSize.render(str(self.algorithm), True, BLACK)
        algorithmRect = algorithmText.get_rect(center=(300, 540))
        self.window.blit(algorithmText, algorithmRect)
        
        self.draw_board(self.maps[self.mapIdx],BOARD_SELECT_SIZE,gridSelectPos)

        

    
