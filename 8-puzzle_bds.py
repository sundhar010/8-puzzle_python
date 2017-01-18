
def left(l):
	i = l.index(0)
	if i  in [0,3,6]:
		return -1
	temp = l[i-1]
	l[i-1] = l[i]
	l[i] = temp 
	return l


def right(l):
	i = l.index(0)
	if i  in [2,5,8]:
		return -1
	temp = l[i+1]
	l[i+1] = l[i]
	l[i] = temp 
	return l


def up(l):
	i = l.index(0)
	if i in [0,1,2]:
		return -1
	temp = l[i]
	l[i] = l[i-3]
	l[i-3] = temp
	return l

def down(l):
	i = l.index(0)
	if i in [6,7,8]:
		return -1
	temp = l[i]
	l[i] = l[i+3]
	l[i+3] = temp
	return l

def bfs(s,e):
	visited_strt = []
	visited_end =[]
	start = []
	end = []
	q_strt = [(s,[])] #[(vertex,path to this vertex [])]
	q_end = [(e,[])]
	while ( q_end or q_strt ):
		#print "$"
		
		flag_strt=0
		flag_end=0

		if(q_strt):
			flag_strt=1
			current_strt = tuple(q_strt.pop(0))
			current_strt[1].append(current_strt[0])
	
		if(q_end):
			flag_end=1
			current_end = tuple(q_end.pop(0))
			current_end[1].append(current_end[0])



		j=0
		for i in visited_strt:

			if (i in visited_end):
			
				
				temp=[]
				for k in start[j][1]:
					temp.append(k)
				for k in end[j][1][::-1]:
					temp.append(k)
				return  temp
			j=j+1
		
		#print "crossed retur"	
		if(flag_strt):
		#	print "&&"
			if (left(list(current_strt[0])) != -1) and (current_strt[0] not in visited_strt):
				t = tuple((left(list(current_strt[0])),list(current_strt[1])))
				q_strt.append(t)
			if (right(list(current_strt[0])) != -1) and (current_strt[0] not in visited_strt):
				t = tuple((right(list(current_strt[0])),list(current_strt[1])))
				q_strt.append(t)
			if (up(list(current_strt[0])) != -1) and (current_strt[0] not in visited_strt):
				t = tuple((up(list(current_strt[0])),list(current_strt[1])))
				q_strt.append(t)
			if (down(list(current_strt[0])) != -1) and (current_strt[0] not in visited_strt):
				t = tuple((down(list(current_strt[0])),list(current_strt[1])))
				q_strt.append(t)
			if (current_strt[0] not in visited_strt):
				visited_strt.append(current_strt[0])
				start.append(current_strt)

		#print "crossed first haif"
		if(flag_end):	
		#	print "@@"	
			if (left(list(current_end[0])) != -1) and (current_end[0] not in visited_end):
				t = tuple((left(list(current_end[0])),list(current_end[1])))
				q_end.append(t)
			if (right(list(current_end[0])) != -1) and (current_end[0] not in visited_end):
				t = tuple((right(list(current_end[0])),list(current_end[1])))
				q_end.append(t)
			if (up(list(current_end[0])) != -1) and (current_end[0] not in visited_end):
				t = tuple((up(list(current_end[0])),list(current_end[1])))
				q_end.append(t)
			if (down(list(current_end[0])) != -1) and (current_end[0] not in visited_end):
				t = tuple((down(list(current_end[0])),list(current_end[1])))
				q_end.append(t)
			if (current_end[0] not in visited_end):
				visited_end.append(current_end[0])
				end.append(current_end)

#		print q_strt , q_end


#start
start = [1,0,2,
		4,5,3,
		7,8,6]

#End
end = [1,2,3,
	   4,5,6,
	   7,8,0]
path =  bfs(list(start),list(end))

#print path

for l in path:
	print l[0:3]
	print l[3:6]
	print l[6:9]
	print "###########"