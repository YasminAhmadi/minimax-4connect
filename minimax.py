import random
from game_logic import *

# In the beginning of every turn, minimax will scan the board’s remaining valid locations and calculate all possible moves, 
# before backtracking and choosing the optimal move for that turn. This will be either the best or worst move, depending on whether 
# it is the maximiser or minimiser’s turn. The assumption is that minimax (maximiser) can play optimally, as long as the human 
# player (minimiser) also plays optimally. This will not always be the case, but does not lead to significant gameplay problems.
def minimax(board, depth, alpha, beta, maximizingHUMAN, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE):
	valid_locations = []
	for col in range(colc):
		if board[rowc-1][col] == 0:
			valid_locations.append(col)
	is_terminal = False
	if (winact(board, HUMAN_PIECE, colc, rowc)):
		is_terminal = True
	if (winact(board, COMPUTER_PIECE, colc, rowc)):
		is_terminal = True
	if (len(valid_locations) == 0):
		is_terminal = True
	if depth == 0 or is_terminal:
		if is_terminal:
			# Weight of the computer winning should be high
			if winact(board, COMPUTER_PIECE, colc, rowc):
				return (None, 9999999)
			# Weight of the human winning should be low
			elif winact(board, HUMAN_PIECE, colc, rowc):
				return (None, -9999999)
			else: # no more valid moves so the game ends 
				return (None, 0)
		# Return the computer's score
		else: 
			return (None, loc_sc(board, COMPUTER_PIECE, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE))
	if maximizingHUMAN:
		value = -9999999
		# Randomise column to start
		column = random.choice(valid_locations)
		for col in valid_locations:

			stop_con = 0
			for r in range(rowc):
				if board[r][col] == 0 and stop_con ==0:
					row=r
					stop_con = 1
            # Create a copy of the board
			boardcop = board.copy()
			boardcop[row][col] = COMPUTER_PIECE
            # new_score = minimax(board, depth-1, alpha, beta, False, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE)[1]
			new_score = minimax(boardcop, depth-1, alpha, beta, False,colc,rowc,HUMAN_PIECE,COMPUTER_PIECE)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing HUMAN
		value = 9999999
		column = random.choice(valid_locations)
		for col in valid_locations:

			stop_con = 0
			for r in range(rowc):
				if board[r][col] == 0 and stop_con == 0:
					row=r
					stop_con = 1
					
			boardcop = board.copy()
			boardcop[row][col] = HUMAN_PIECE
            # new_score = minimax(board, depth-1, alpha, beta, False, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE)[1]
			new_score = minimax(boardcop, depth-1, alpha, beta, True, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE)[1]
			if new_score < value:
				value = new_score
				# Make 'column' the best scoring column we can get
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value