from Queue import PriorityQueue

#class for PriorityQueue
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


def left(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [0,3,6]:
		return -1
	temp = l[i-1]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i-1] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) #returns the tuple with state,path,cumulative cost
 	

def right(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [2,5,8]:
		return -1
	temp = l[i+1]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i+1] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) #returns the tuple with state,path,cumulative cost
 	


def up(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [0,1,2]:
		return -1
	temp = l[i-3]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i-3] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) #returns the tuple with state,path,cumulative cost
 	


def down(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [6,7,8]:
		return -1
	temp = l[i+3]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i+3] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) #returns the tuple with state,path,cumulative cost
 	


def ufs(s,e):
	visited = []
	start = (s,[],0) #(vertex,path to this vertex [])
	q = MyPriorityQueue()
	q.put(tuple(start),start[2])
	while q:
		current = tuple(q.get())
		current[1].append(current[0])
		if(current[0] == e):
			return current[1],current[2]
		if (left(list(current)) != -1) and (current[0] not in visited):
			t = tuple(left(tuple(current)))
			q.put(t,t[2])
		if (right(list(current)) != -1) and (current[0] not in visited):
			t = tuple(right(list(current)))
			q.put(t,t[2])
		if (up(list(current)) != -1) and (current[0] not in visited):
			t = tuple(up(list(current)))
			q.put(t,t[2])
		if (down(list(current)) != -1) and (current[0] not in visited):
			t = tuple(down(list(current)))
			q.put(t,t[2])
		if current[0] not in visited:
			visited.append(current[0])

#prints the output
def printPath(path,cost):
	print "----------------"
	print "cost :",cost
	print "----------------"

	for l in path:
		print l[0:3]
		print l[3:6]
		print l[6:9]
		print "###########"

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
start = readfile("input_ucs")

#End
end = [1,2,3,
	   4,5,6,
	   7,8,0]

path,cost =  ufs(list(start),list(end))
printPath(path,cost)
