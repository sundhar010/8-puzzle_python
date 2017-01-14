
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

def dfs(s,e):
	visited = []
	q = [(s,[])] #[(vertex,path to this vertex [])]
	while q:
		current = tuple(q.pop())
		current[1].append(current[0])
		if(current[0] == e):
			return current[1]
			
		if (left(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((left(list(current[0])),list(current[1])))
			q.append(t)
		if (up(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((up(list(current[0])),list(current[1])))
			q.append(t)
		if (down(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((down(list(current[0])),list(current[1])))
			q.append(t)
		if (right(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((right(list(current[0])),list(current[1])))
			q.append(t)
		visited.append(current)


#start
start = [0,1,2,
		4,5,3,
		7,8,6]

#End
end = [1,2,3,
	   4,5,6,
	   7,8,0]

path =  dfs(list(start),list(end))

for l in path:
	print l[0:3]
	print l[3:6]
	print l[6:9]
	print "###########"