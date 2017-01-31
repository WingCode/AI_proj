import sys

depth=5	
no_cities=5
start_city='a'
cities = map(chr,range(97,97+no_cities))
print(cities)
dist=[[ sys.maxint,1,6,8,4],
	  [7, sys.maxint,8,5,6],
	  [6,8, sys.maxint,9,7],
	  [8,5,9, sys.maxint,8],
	  [4,6,7,8, sys.maxint]]

def getKey(item):
	return item[0]

print("Nearest neighbor heurestics")
selected=[False for i in range(0,no_cities)]
start_city_index=cities.index(start_city)

try:
	selected[start_city_index]=True
except:
	print("Enter a valid city")


tuple_city=[[ sys.maxint for i in range(0,3)] for j in range(0,no_cities)]
path=[]
cost=0

for i in range(0,no_cities):
	tuple_city[i][0]=dist[start_city_index][i]
	tuple_city[i][1]=i
	tuple_city[i][2]=False

for i in range(0,no_cities):
	if i==0:
		temp=sorted(tuple_city,key=getKey)


	else:
		for i in range(0,no_cities):
			tuple_city[i][0]=dist[start_city_index][i]
			temp=sorted(tuple_city,key=getKey)
		

	print("DEPTH %d : %s"%(i,temp))
	for j in range(0,no_cities):
		if(temp[j][2]==False):
			temp[j][2]=True
			path.append(temp[j][1])
			cost+=int(temp[j][0])
			start_city_index=temp[j][1]
			break

print cost
for i in range(0,no_cities):
	path[i]+=97
print map(chr,path)
#print tuple_city