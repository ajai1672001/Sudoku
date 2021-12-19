import random
def start():
	global mode
	global wh
	global rcib	
wh=1
view=[[8,4,7,9,3,1,2,6,5],
	[3,1,9,5,6,2,8,7,4],
	[5,2,6,7,8,4,1,9,3],
	[4,5,8,2,7,3,6,1,9],
	[1,6,3,8,5,9,4,2,7],
	[9,7,2,1,4,6,3,5,8],
	[7,9,1,4,2,8,5,3,6],
	[2,3,4,6,9,5,7,8,1],
	[6,8,5,3,1,7,9,4,2],]
check=[[8,4,7,9,3,1,2,6,5],
	[3,1,9,5,6,2,8,7,4],
	[5,2,6,7,8,4,1,9,3],
	[4,5,8,2,7,3,6,1,9],
	[1,6,3,8,5,9,4,2,7],
	[9,7,2,1,4,6,3,5,8],
	[7,9,1,4,2,8,5,3,6],
	[2,3,4,6,9,5,7,8,1],
	[6,8,5,3,1,7,9,4,2],]
#Hide and creat puzzle
def hide():
	li=0
	while li<=wh:
		for i in range(0,9):
			for j in range(0,4):
				k=random.randint(0,8)
				# print(k)
				view[i][k]=' '
				li=li+1
hide()
#puzzle board outer look
def board():
	print()
	print('        i   ii iii iv   v   vi vii viii ix')
	print('        |   |   |   |   |   |   |   |   |    ')
	print()
	print("   i -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- i".format( view[0][0], view[0][1], view[0][2] , view[0][3] , view[0][4] , view[0][5] , view[0][6] , view[0][7] , view[0][8]))
	print()
	print("  ii -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- ii".format( view[1][0], view[1][1], view[1][2] , view[1][3] , view[1][4] , view[1][5] , view[1][6] , view[1][7] , view[1][8]))
	print()
	print(" iii -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- iii".format( view[2][0], view[2][1], view[2][2] , view[2][3] , view[2][4] , view[2][5] , view[2][6] , view[2][7] , view[2][8]))
	print('        ----------------------------------')
	print("  iv -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- iv".format( view[3][0], view[3][1], view[3][2] , view[3][3] , view[3][4] , view[3][5] , view[3][6] , view[3][7] , view[3][8]))
	print()
	print("   v -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- v".format( view[4][0], view[4][1], view[4][2] , view[4][3] , view[4][4] , view[4][5] , view[4][6] , view[4][7] , view[4][8]))
	print()
	print("  vi -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- vi".format( view[5][0], view[5][1], view[5][2] , view[5][3] , view[5][4] , view[5][5] , view[5][6] , view[5][7] , view[5][8]))
	print('        ----------------------------------')
	print(" vii -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- vii".format( view[6][0], view[6][1], view[6][2] , view[6][3] , view[6][4] , view[6][5] , view[6][6] , view[6][7] , view[6][8]))
	print()
	print("viii -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- viii".format( view[7][0], view[7][1], view[7][2] , view[7][3] , view[7][4] , view[7][5] , view[7][6] , view[7][7] , view[7][8]))
	print()
	print("  ix -- {}   {}   {} | {}   {}   {} | {}   {}   {} -- ix".format( view[8][0], view[8][1], view[8][2] , view[8][3] , view[8][4] , view[8][5] , view[8][6] , view[8][7] , view[8][8]))
	print()
	print('        |   |   |   |   |   |   |   |   |    ')
	print('        i   ii iii iv   v   vi vii viii ix')
	print()
	start()
board()

#For exit the game
def complete():
	global wh
	if  wh=="s" or wh=="y" or wh=="yes":
		exit()
#To check the game is winning
def winner():
	global a
	a=0
	for x in range(0,9):
		for y in range(0,9):
			if view[x][y]!=' ':
				a=a+1
			else:
				continue
	if a==81 and ' ' not in view :
		print("you win the game")
		wh=input("If you want play Again")
		if wh=="s" or wh=="y" or wh=="yes":
			start()
		elif wh=='no' or wh=='n':
			complete()
	elif rcip=="res" or rcip=="restart" or rcip=="r":	
		wh=input("If you want play Again")
		if wh=="s" or wh=="y" or wh=="yes":
			start()
	board()
#playing conntent
while True:
	rcip=input("enter row , column , input number  = > = > = > ")
	if rcip=="restart" or rcip=="res" or rcip=="r":
		winner()
	if rcip.isdigit():
		rci=int(rcip)
		ip=rci%10
		col=int((rci/10)%10)
		row=int(rci/100)
	else:
		print()
		print("Enter Numbers Only")
		print()
		continue
	if rci<=999 and rci>=111:
		a=1
	else:
		print()
		print("Limit of row , column , input number are 1 to 9 ")
		print("Give inputs like this format \" 111 or 999\"")
		print()
		continue
	if view[row-1][col-1]==' ':
		b=2
	else:
		print("This place was Already Takken")
		continue
	if  check[row-1][col-1]==ip:
		view[row-1][col-1]=ip
	else:
		print("It\'s not a right number ")
	winner()
start()
