items = ['a', 'b', 'c','d','e']
dist=[[0,1,6,8,4],
	  [7,0,8,5,6],
	  [6,8,0,9,7],
	  [8,5,9,0,8],
	  [4,6,7,8,0]]
all_perm=[]
from itertools import permutations
for p in permutations(items):
	all_perm.append(p)

index_min=-1
to_city=-1
minim=100
for i in range(0,len(all_perm)):
	val=0
	from_city=items.index(all_perm[i][0])
	for j in range(0,4):
		to_city=items.index(all_perm[i][j+1])		
		val=val+dist[from_city][to_city]
		from_city=to_city

	val=val+dist[from_city][items.index(all_perm[i][0])]
	print(all_perm[i],val)
	if val<minim:
		index_min=i
		minim=val
	print("\n")
minim=minim-5

print("MINIMUM INDEX",index_min,minim)
print(all_perm[index_min])
