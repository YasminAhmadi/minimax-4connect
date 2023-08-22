import pygame


# Exits the game loop if a winning move is found
def winact(board, piece, colc, rowc):
	# Looking for a possibility to win in horizontal entries
	for c in range(colc-3):
		for r in range(rowc):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Looking for a possibility to win invertical entries
	for c in range(colc):
		for r in range(rowc-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Looking for a possibility to win in diaganol entries
    # Both going up and down
	for c in range(colc-3):
		for r in range(rowc-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	for c in range(colc-3):
		for r in range(3, rowc):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

# In order to choose the best move to play, 
# it has to know the current board state. 
# the windows (horizontal, vertical, diagonal) are then used to scan all possible 4-piece sections of the board.
# they are all scored basd off the content
def winscore(window, piece, HUMAN_PIECE, COMPUTER_PIECE):
	score = 0
	opp_piece = HUMAN_PIECE
	if piece == HUMAN_PIECE:
		opp_piece = COMPUTER_PIECE
	piecesnum = window.count(piece)
	# The highest score should be given to connecting 4 pieces 
	if (piecesnum == 4):
		score += 150
	# The next best thing is to connect 3
	elif (piecesnum == 3) and window.count(0) == 1:
		score += 15
	# Next to connect 2
	elif (piecesnum == 2) and window.count(0) == 2:
		score += 5
    # Not more important than winning but the apponent's winning move also needs to be stopped
	if window.count(opp_piece) == 3 and window.count(0) == 1:
		score -= 10
	return score

def loc_sc(board, piece, colc, rowc, HUMAN_PIECE, COMPUTER_PIECE):
	score = 0

	# Score center column
	center_array = [int(i) for i in list(board[:, colc//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	# Score Horizontal
	for r in range(rowc):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(colc-3):
			window = row_array[c:c+4]
			score += winscore(window, piece, HUMAN_PIECE, COMPUTER_PIECE)

	# Score Vertical
	for c in range(colc):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(rowc-3):
			window = col_array[r:r+4]
			score += winscore(window, piece, HUMAN_PIECE, COMPUTER_PIECE)

	# Score posiive sloped diagonal
	for r in range(rowc-3):
		for c in range(colc-3):
			window = [board[r+i][c+i] for i in range(4)]
			score += winscore(window, piece, HUMAN_PIECE, COMPUTER_PIECE)

	for r in range(rowc-3):
		for c in range(colc-3):
			window = [board[r+3-i][c+i] for i in range(4)]
			score += winscore(window, piece, HUMAN_PIECE, COMPUTER_PIECE)

	return score



def draw_board(board, colc, rowc, screen, YELLOW, BLACK, RED, BLUE, HUMAN_PIECE, COMPUTER_PIECE):
	for c in range(colc):
		for r in range(rowc):
			pygame.draw.rect(screen, YELLOW, (c*100, r*100+100, 100, 100))
			pygame.draw.circle(screen, BLACK, (int(c*100+100/2), int(r*100+100+100/2)), int(100/2 - 5))
	
	for c in range(colc):
		for r in range(rowc):		

			if (board[r][c] == HUMAN_PIECE):
				pygame.draw.circle(screen, RED, (int(c*100+100/2), (rowc+1) * 100-int(r*100+100/2)), int(100/2 - 5))
			elif board[r][c] == COMPUTER_PIECE: 
				pygame.draw.circle(screen, BLUE, (int(c*100+100/2), (rowc+1) * 100-int(r*100+100/2)), int(100/2 - 5))
	pygame.display.update()