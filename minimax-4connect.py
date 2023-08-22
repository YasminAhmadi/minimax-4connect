import numpy as np
import math
import random
import sys
import pygame
from GUI import *

# Number of rows and columns in the game board
rowc = int(input("Enter number of rows:"))
colc = int(input("Enter numbeer of columns:"))

# Defining colors and parameters
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
HUMAN = 0
HUMAN_PIECE = 1
COMPUTER = 1
COMPUTER_PIECE = 2
depth = 5
alpha = -9999999
beta = 9999999
maximizingHUMAN = True

# run the game and play with computer
GUI(rowc, colc, HUMAN, COMPUTER, BLACK,RED,BLUE,YELLOW, HUMAN_PIECE, COMPUTER_PIECE, depth, alpha, beta, maximizingHUMAN)


