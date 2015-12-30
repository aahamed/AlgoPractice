"""
monochromatic_board.py: topcoder problem
Author: Aadil Ahamed
"""

class MonoChromaticBoard(object):
	
	def theMin(self, board):
		row = []
		col = []
		H = len(board)	# height
		W = len(board[0])	# width
		for i in range(H):
			row.append(True)
		for j in range(W):
			col.append(True)
		for i in range(H):
			for j in range(W):
				if board[i][j] == 'W':
					row[i] = False
					col[j] = False
		num = 0
		for elem in col:
			if elem == True:
				num += 1
		for elem in row:
			if elem == True:
				num += 1
		if num == H + W:		# special case: entire board is black
			return min(H, W)
		else:
			return num

			
def test_the_min():
	mcb = MonoChromaticBoard()
	board = ["WBWBW", "BBBBB", "WBWBW", "WBWBW"]
	print(mcb.theMin(board))
	mcb = MonoChromaticBoard()
	board = ["BBBBB", "BBBBB", "BBBBB", "BBBBB", "BBBBB", "BBBBB", "BBBBB", "BBBBB"]
	print(mcb.theMin(board))	
	mcb = MonoChromaticBoard()
	board = ["WW", "WW"]
	print(mcb.theMin(board))

def main():
	test_the_min()

if __name__ == '__main__':
	main()
	