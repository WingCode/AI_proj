from sets import Set

goal_state=[[1,2,3],[8,0,4],[7,6,5]]
depth=3
states_set=Set()
goal_set=Set([123804765])

def no_moves(i,j):
	move=[]
	if i==0 and j==0:
		move.append(1)
		move.append(2)

	elif i==0 and j==1:
		move.append(1)
		move.append(2)
		move.append(3)

	elif i==0 and j==2:
		move.append(2)
		move.append(3)

	elif i==1 and j==0:
		move.append(0)
		move.append(1)
		move.append(2)

	elif i==1 and j==1:
		move.append(0)
		move.append(1)
		move.append(2)
		move.append(3)

	elif i==1 and j==2:
		move.append(0)
		move.append(2)
		move.append(3)

	elif i==2 and j==0:
		move.append(0)
		move.append(1)

	elif i==2 and j==1:
		move.append(0)
		move.append(1)
		move.append(3)

	elif i==2 and j==2:
		move.append(0)
		move.append(3)

	return move

def find_blank(current_state=[]):
	i_=0
	j_=0
	for i in range(0,3):
		for j in range(0,3):
			if current_state[i][j]==0:
				i_=i
				j_=j
				break
	return i_,j_

def heu(current_state=[]):
	out_place=0
	for i in range(0,3):
		for j in range(0,3):
			if goal_state[i][j]!=current_state[i][j] and not(i==1 and j==1):
				#print goal_state[i][j],current_state[i][j]
				out_place+=1
	return out_place

def swap(one,two):
	return two,one

def mover2(i_,j_,movement,current_state=[]):
	#print movement,"crst"
	#print_board(current_state)
	current_state2_=current_state[:]
	if movement==0:
		current_state2_[i_][j_],current_state2_[i_-1][j_]=swap(current_state2_[i_][j_],current_state2_[i_-1][j_])

	elif movement==1:
		current_state2_[i_][j_],current_state2_[i_][j_+1]=swap(current_state2_[i_][j_],current_state2_[i_][j_+1])

	elif movement==2:
		current_state2_[i_][j_],current_state2_[i_+1][j_]=swap(current_state2_[i_][j_],current_state2_[i_+1][j_])

	elif movement==3:
		current_state2_[i_][j_],current_state2_[i_][j_-1]=swap(current_state2_[i_][j_],current_state2_[i_][j_-1])

	print_board(current_state2_)

	multipler=100000000
	sum_=0
	for i in range(0,3):
		for j in range(0,3):
			sum_=sum_+current_state2_[i][j]*multipler
			multipler=multipler/10

	if sum_ in states_set:
		return None

	else:
		states_set.add(sum_)

	print("The recorded states are:",states_set)
	value=heu(current_state2_)
	return value,current_state2_

def mover(i_,j_,iterator,move_list=[],current_state=[]):

	h_x=('Inf')
	best_state=[]
	for i in range(0,len(move_list)):
		#print "IN LOOP"
		#print_board(current_state)
		value,matrix=mover2(i_,j_,move_list[i],current_state)
		
		if value<h_x:
			h_x=value
			best_state=matrix

	print("The current depth level %d and heurestic value %d"%(iterator,h_x))
	return best_state

def print_board(current_state=[]):
	for i in range(0,3):
		for j in range(0,3):
			if current_state[i][j]==0:
				print "   ","|",

			else:
				print current_state[i][j],"|",

		print("\n")
		if i!=2:
			print("---------------")
	print("\n\n")

current_state=[[2,8,3],[1,6,4],[7,0,5]]
iterator=0
print "The intial configuration"
print_board(current_state)
while iterator<depth:
	i_,j_=find_blank(current_state)
	move_list=no_moves(i_,j_)
	current_state=mover(i_,j_,iterator,move_list,current_state)

	iterator+=1