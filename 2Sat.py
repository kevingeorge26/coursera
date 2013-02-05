'''
Created on Feb 3, 2013

@author: kevin

Solving 2 sat by find strongly connected component using
Kosaraju's algorithm

for a or b
there is a edge for !a->b and !b->a 

'''
from collections import defaultdict


edge_list = defaultdict(lambda:set([]))
finish_node = defaultdict(lambda : -1)

visited = set([])
all_nodes = set([])

finishing_time = 0
flag = True

class edge:
    def __init__(self,head,tail,ordering):
        self.head = head
        self.tail = tail
        self.ordering = ordering
        
        
def load_file_r(filename):
    """first step where we consider reverse edges
    text file is considered of the format TAIL HEAD"""
    with open(filename) as f:
        f.next()
        
        for line in f:
            data = map(lambda x: int(x),line.split())
            edge_list[data[0]].add(data[1])
            
            all_nodes.add(data[0])
            all_nodes.add(data[1])
            
def load_file(filename):
    
    edge_list.clear()
    visited.clear()
    
    with open(filename) as f:
        f.next()
        
        for line in f:
            data = map(lambda x: int(x),line.split())
            edge_list[data[1]].add(data[0])
            
            
def dfs_count( node ):
    " calculate the finishing times "
    global finishing_time
    visited.add(node)
    
    for child in edge_list[node]:
        if child not in visited:
            dfs_count(child)
            
    finishing_time+=1
    finish_node[finishing_time] = node
    
    
def dfs ( node,scc ):
    
    global flag
    visited.add(node)
    scc.add(node)
    
    temp = node * -1
    if temp in scc:
        print "nottttttttttttttttttttttttttt"
        flag = False
        
    for child in edge_list[node]:
        if child not in visited:
            dfs(child , scc )
            
def transform_file(test_file):
    with open("my_test.txt",'w') as opf:
        with open(test_file) as inf:
            inf.next()
            opf.write("this i made \n")
            
            for line in inf:
                data = map(lambda x: int(x),line.split())
                opf.write( str( (data[0]) * (-1) ) + " " + str(data[1]) + "\n" )
                opf.write( str( (data[1]) * (-1) ) + " " + str(data[0]) + "\n" )
        
        
    
        

if __name__ == '__main__':
    
    transform_file("2sat5.txt")
    
    global finishing_time
    global flag
    
    load_file_r("my_test.txt")  
    
    for i in all_nodes:
        if i not in visited:
            dfs_count(i)
   
    load_file("my_test.txt")
    for key in sorted(finish_node.keys(),reverse=True):
        i = finish_node[key]
        
        if i not in visited:
            scc = set([])
            dfs( i , scc )
            del(scc)
            
        if not flag:
            print "breaking cause nottttt"
            break        
    
   
    pass