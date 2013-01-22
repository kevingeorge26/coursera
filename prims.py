'''
Created on Dec 16, 2012

@author: kevin
'''
from collections import defaultdict

adj_list = {}
un_visited = set([])
visited = set([])
valid_edges = []

class edge:
    def __init__(self,u,v,weight):
        self.u = u
        self.v= v
        self.weight = weight
        
    def __repr__(self):
        return "u =" + self.u + " v " + self.v +\
             " weight " + str(self.weight)

def load_file():
   
    global valid_edges
    with open("edges.txt") as file:
        file.next()
        for line in file:
            row = line.strip().split()
            print row
            e = edge(row[0], row[1], int(row[2]) )
            adj_list[row[0]].append(e)
            adj_list[row[1]].append(e)
            
            un_visited.add(row[0])
            un_visited.add(row[1])
            
    first_node = un_visited.pop()
    visited.add(first_node)
    
    print un_visited
    
def prims():
    
    total = 0
    
    while len(un_visited) > 0:
        valid_edges = []
        for x in visited:
        	nodes = adj_list[x]
    		for node in nodes:
    			if node.u not in visited or node.v not in visited:
    				valid_edges.append(node)
    
        valid_edges.sort(key  = lambda x :x.weight)
        if len(valid_edges) == 0:
        	print un_visited
        	
        nexte = valid_edges[0]
        total += nexte.weight
        print total
        
        visited.add(nexte.u)
        visited.add(nexte.v)
        
        un_visited.discard( nexte.u )
        un_visited.discard( nexte.v )
        
	
        
        
        

if __name__ == '__main__':
    adj_list = defaultdict(lambda : [] )
    load_file()
    prims()
    pass