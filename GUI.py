import numpy as np
import math
import random
import sys
import pygame
from game_logic import *
from minimax import *

def GUI(rowc, colc, HUMAN, COMPUTER, BLACK,RED,BLUE,YELLOW, HUMAN_PIECE, COMPUTER_PIECE,depth, alpha, beta, maximizingHUMAN):
    board=np.zeros((rowc,colc))

    pygame.init()

    screen = pygame.display.set_mode((colc * 100, (rowc+1) * 100))
    draw_board(board, colc, rowc, screen, YELLOW, BLACK, RED, BLUE, HUMAN_PIECE, COMPUTER_PIECE)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(HUMAN, COMPUTER)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, colc * 100, 100))
                posx = event.pos[0]
                if turn == HUMAN:
                    pygame.draw.circle(screen, RED, (posx, int(100 / 2)), int(100 / 2 - 5))

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, colc * 100, 100))
                if turn == HUMAN:
                    posx = event.pos[0]
                    col = int(math.floor(posx / 100))

                    if board[rowc-1][col] == 0:
                        not_found = 0
                        for r in range(rowc):
                            if board[r][col] == 0 and not_found == 0:
                                row = r
                                not_found = 1

                        board[row][col] = HUMAN_PIECE

                        if  winact(board, HUMAN_PIECE, colc, rowc):
                            label = myfont.render("HUMAN 1 wins!!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_running = False

                        turn += 1
                        turn = turn % 2

                        print(board)
                        draw_board(board, colc, rowc, screen, YELLOW, BLACK, RED, BLUE, HUMAN_PIECE, COMPUTER_PIECE)

        if turn == COMPUTER and game_running:
            
            col, minimax_score = minimax(board, depth, alpha, beta, maximizingHUMAN, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE)

            if board[rowc-1][col] == 0:
                not_found = 0
                for r in range(rowc):
                    if board[r][col] == 0 and not_found == 0:
                        row = r
                        not_found = 1

                board[row][col] = COMPUTER_PIECE

                if winact(board, COMPUTER_PIECE, colc, rowc):
                    label = myfont.render("HUMAN 2 wins!!", 1, BLUE)
                    screen.blit(label, (40, 10))
                    game_running = False

                print(board)
                draw_board(board, colc, rowc, screen, YELLOW, BLACK, RED, BLUE, HUMAN_PIECE, COMPUTER_PIECE)

                turn += 1
                turn = turn % 2

    if not game_running:
        pygame.quit()
        sys.exit()

    if not game_running:
        pygame.time.wait(3000)