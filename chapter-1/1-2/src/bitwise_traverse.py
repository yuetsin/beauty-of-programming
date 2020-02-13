#!/usr/bin/env python

chessboard = 0

while True:
	# 清零「帅」位置
	chessboard &= ~0xf
	while True:
		if (chessboard & 0xf) % 3 != ((chessboard >> 4) & 0xf) % 3:
			print('將：(%s, %s)，帥：(%s, %s)' % (
				['d', 'e', 'f'][(chessboard & 0xf) % 3],
				['8', '9', '10'][(chessboard & 0xf) // 3],
				['d', 'e', 'f'][((chessboard >> 4) & 0xf) % 3], 
				['1', '2', '3'][((chessboard >> 4) & 0xf) // 3]))

		# 递增「帅」的位置
		if chessboard & 0xf >= 8:
			break
            
		chessboard += 1

	if (chessboard >> 4) >= 8:
		break
    
	# 递增「将」的位置
	chessboard += 0x10