def IsCheckmate(self,board,color):
	#returns true if 'color' player is in checkmate
	#Call GetListOfValidMoves for each piece of current player
	#If there aren't any valid moves for any pieces, then return true
 
	if color == "black":
		myColor = 'b'
		enemyColor = 'w'
	else:
		myColor = 'w'
		enemyColor = 'b'
 
	myColorValidMoves = [];
	for row in range(8):
		for col in range(8):
			piece = board[row][col]
			if myColor in piece:
				myColorValidMoves.extend(self.GetListOfValidMoves(board,color,(row,col)))
 
	if len(myColorValidMoves) == 0:
		return True
	else:
		return False
