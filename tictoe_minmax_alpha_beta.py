#tictaoe #x=1 ,0=-1, " "=0
import random
import math
from sets import Set
board=[[0 for i in range(0,3)]for i in range(0,3)]
my_move=-2
CPU_move=-2
game_state=3
row_sum=[0,0,0]
col_sum=[0,0,0]
diag_sum=[0,0]
states_set=Set()

def state_writer(board=[]):
	multipler=100000000
	sum_=0
	for i in range(0,3):
		for j in range(0,3):
			temp=board[i][j]
			if temp==-1:
				temp=2
			sum_=sum_+temp*multipler
			multipler=multipler/10

	if sum_ in states_set:
		return False

	else:
		states_set.add(sum_)

def symmetry_generator(board=[]):
	result=state_writer(board)

	if result==False:
		return False
	board_dup=[[0 for i in range(0,3)]for i in range(0,3)]


	for k in range(0,3):
		for i in range(0,3):
			for j in range(0,3):
				if i==1 and j==1:
					pass

					if board[i][j]!=0:
						if i==0 and j==0:
							board_dup[0][2]=board[0][0]

						elif i==0 and j==1:
							board_dup[1][2]=board[0][1]

						elif i==0 and j==1:
							board_dup[1][2]=board[0][1]

						elif i==0 and j==2:
							board_dup[2][2]=board[0][2]

						elif i==1 and j==0:
							board_dup[0][1]=board[1][0]

						elif i==1 and j==2:
							board_dup[2][1]=board[1][2]

						elif i==2 and j==0:
							board_dup[2][0]=board[0][0]

						elif i==2 and j==1:
							board_dup[2][1]=board[1][0]

						elif i==2 and j==2:
							board_dup[2][2]=board[2][0]
		board=board_dup
		state_writer(board)
	del board_dup[:]

def user_input():
	my_move=int(raw_input("Enter the your choice on the board "))

	if my_move==0:
		row_sum[0]+=1
		col_sum[0]+=1
		diag_sum[0]+=1
		board[0][0]=1

	elif my_move==1:
		row_sum[0]+=1
		col_sum[1]+=1
		board[0][1]=1

	elif my_move==2:
		row_sum[0]+=1
		col_sum[2]+=1
		diag_sum[1]+=1
		board[0][2]=1

	elif my_move==3:
		row_sum[1]+=1
		col_sum[0]+=1
		board[1][0]=1

	elif my_move==4:
		row_sum[1]+=1
		col_sum[1]+=1
		diag_sum[0]+=1
		diag_sum[1]+=1
		board[1][1]=1

	elif my_move==5:
		row_sum[1]+=1
		col_sum[2]+=1
		board[1][2]=1

	elif my_move==6:
		row_sum[2]+=1
		col_sum[0]+=1
		diag_sum[1]+=1
		board[2][0]=1

	elif my_move==7:
		row_sum[2]+=1
		col_sum[1]+=1
		board[2][1]=1

	elif my_move==8:
		row_sum[2]+=1
		col_sum[2]+=1
		diag_sum[0]+=1
		board[2][2]=1

	else:
		print("Invalid move")

def print_board():
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j]==0:
				print "   ",

			elif board[i][j]==1:
				print " x ",

			elif board[i][j]==-1:
				print " 0 ",

			if j!=2:
				print "|",

		print("\n")
		if i!=2:
			print("--------------------")			

def cpu_input(CPU_move):

	if CPU_move==0:
		row_sum[0]-=1
		col_sum[0]-=1
		diag_sum[0]-=1
		board[0][0]=-1

	elif CPU_move==1:
		row_sum[0]-=1
		col_sum[1]-=1
		board[0][1]=-1

	elif CPU_move==2:
		row_sum[0]-=1
		col_sum[2]-=1
		diag_sum[1]-=1
		board[0][2]=-1

	elif CPU_move==3:
		row_sum[1]-=1
		col_sum[0]-=1
		board[1][0]=-1

	elif CPU_move==4:
		row_sum[1]-=1
		col_sum[1]-=1
		diag_sum[0]-=1
		diag_sum[1]-=1
		board[1][1]=-1

	elif CPU_move==5:
		row_sum[1]-=1
		col_sum[2]-=1
		board[1][2]=-1

	elif CPU_move==6:
		row_sum[2]-=1
		col_sum[0]-=1
		diag_sum[1]-=1
		board[2][0]=-1

	elif CPU_move==7:
		row_sum[2]-=1
		col_sum[1]-=1
		board[2][1]=-1

	elif CPU_move==8:
		row_sum[2]-=1
		col_sum[2]-=1
		diag_sum[0]-=1
		board[2][2]=-1

def check_state():
		if 3 in row_sum or 3 in col_sum or 3 in diag_sum:
			return 1	#you win

		elif -3 in row_sum or -3 in col_sum or -3 in diag_sum:
			return 2	#CPU win
		
		else:
			return 3

def next_move():
	CPU_move=random.randrange(9)
	while board[int(math.floor(CPU_move/3))][CPU_move%3]!=0:
	 	CPU_move=random.randrange(9)
	cpu_input(CPU_move)

move=0
if random.randrange(2)==0:
	user_input()
	symmetry_generator(board)
	print_board()
	print states_set #
	++move

else:
	CPU_move=random.randrange(9)
	print(CPU_move)
	cpu_input(CPU_move)
	symmetry_generator(board)
	print_board()
	user_input()
	symmetry_generator(board)
	print_board()
	print states_set #
	move=2

while game_state==3:
	next_move()
	symmetry_generator(board)
	print_board()
	user_input()
	symmetry_generator(board)
	print_board()
	print states_set #
	game_state=check_state()

	++move

	if move>9:
		game_state=0


if game_state==0:
	print("DRAW")

if game_state==1:
	print("YOU WIN")

if game_state==2:
	print("YOU LOSE")

