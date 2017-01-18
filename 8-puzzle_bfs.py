#team sundhar,hima,preethi
#python

#does left move by swaping 0 with the respective element
def left(l):
	i = l.index(0)
	if i  in [0,3,6]:
		return -1
	temp = l[i-1]
	l[i-1] = l[i]
	l[i] = temp 
	return l #returns new state


#does right move by swaping 0 with the respective element
def right(l):
	i = l.index(0)
	if i  in [2,5,8]:
		return -1
	temp = l[i+1]
	l[i+1] = l[i]
	l[i] = temp 
	return l #returns new state


#does up move by swaping 0 with the respective element
def up(l):
	i = l.index(0)
	if i in [0,1,2]:
		return -1
	temp = l[i]
	l[i] = l[i-3]
	l[i-3] = temp
	return l  #returns new state

#does down move by swaping 0 with the respective element
def down(l):
	i = l.index(0)
	if i in [6,7,8]:
		return -1
	temp = l[i]
	l[i] = l[i+3]
	l[i+3] = temp
	return l   #returns new state
	
#this function cal the path from start to end 
def bfs(s,e):
	visited = []  #this list is used to store all the visited states
	q = [(s,[])] #[(vertex,path to this vertex [])] this list is used as a queue and the queue contains tuples with (state and path)
	while q:
		current = tuple(q.pop(0))
		current[1].append(current[0])
		if(current[0] == e):
			return current[1]
		if (left(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((left(list(current[0])),list(current[1])))
			q.append(t)
		if (right(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((right(list(current[0])),list(current[1])))
			q.append(t)
		if (up(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((up(list(current[0])),list(current[1])))
			q.append(t)
		if (down(list(current[0])) != -1) and (current[0] not in visited):
			t = tuple((down(list(current[0])),list(current[1])))
			q.append(t)
		if current[0] not in visited:
			visited.append(current[0])
#prints the output
def printPath(path):
	for l in path:
		print l[0:3]
		print l[3:6]
		print l[6:9]
		print "###########"
	print "cost is:",len(path)

def readfile( filename ):
    f = open( filename )
    data = f.read()
    # Get rid of the newlines
    data = data.strip( "\n" )
    #Break the string into a list using a space as a seperator.
    data = data.split( " " )
    state = []
    for element in data:
        state.append( int( element ) )
    return state


#start
start = readfile("input_bfs")

#End
end = [1,2,3,
	   4,5,6,
	   7,8,0]

path =  bfs(list(start),list(end))  

printPath(path)
