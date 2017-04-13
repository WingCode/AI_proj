import string

days=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
persons=["Sham","Ram","Ravi","Shiva"]
time=[8,10,13,17]
day_save=None
time_save=-1
flag=0

def meeting_planner():
	for day in days: #day loop
		for i in range(0,4): #time loop
			for j in range(0,4): #person loop
				print "%s, Are free on %s on %d hours?"%(persons[j],day,time[i])
				inp=str(raw_input())
				if inp not in ("y","Y","Yes","YES"):
					break

				if j==3:
					return(i,day)

time_save,day_save=meeting_planner()
if day_save==None or time_save==-1:
	print "Nobody is free on anyday and anytime. Meeting cannot be scheluded"

else:
	print "Meeting scheluded %s, %s hours"%(day_save,time[time_save])