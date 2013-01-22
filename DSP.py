'''
Created on Jul 21, 2012

@author: kevin

Dijkstra's shortest-path

'''

import heapq
import logging


"""" edge list  , each element is array of tuple with node and distance """
edge_list = {}
result = {}
to_find = [7,37,59,82,99,115,133,165,188,197]
#to_find = [1,2,3,4,5,6]

logging.basicConfig(level=logging.DEBUG)

def load_file():
    """ load the file """
    
    global edge_list
    
#dijkstraData
    for f in open("dij.txt","r"):
        list = []
        f = f.strip()
        v_set = f.split("\t")
        for ele in range( 1 , len(v_set) ):
            
            temp =  int(v_set[ele].split(",")[0].strip()),int(v_set[ele].split(",")[1].strip())
            list.append(temp)
            
        edge_list[ int( v_set[0] ) ] = list
        
    print edge_list
    

def create_heap(visited_node):
    
    global edge_list
    min_heap = []
    global result
    
    for i in visited_node.iterkeys():
        
#        logging.info("node = %d", i )
        dist = visited_node[i]
        
        neighbours = edge_list[i]
        
        
        for v,e in neighbours:
            if v not in visited_node:
                new_entry = (dist + e,v)
                min_heap.append(new_entry)
                
    heapq.heapify(min_heap)
    #print min_heap
    next_ele = heapq.heappop(min_heap)
    
    if next_ele[1] in to_find:        
        result[next_ele[1]] = next_ele[0] 
    
    print "visited node = " , next_ele[1] , " total distance = ", next_ele[0]
    visited_node[next_ele[1]] = next_ele[0]
    

                 


if __name__ == '__main__':
    
    global to_find
    global result
    
    visited_node = {}
    visited_node[1] = 0
    
    load_file()
    for i in range(199):
        create_heap(visited_node)
        
    ans = []
    for i in to_find:
        if i in visited_node:
            ans.append(visited_node[i])
        else:
            ans.append(1000000)
            
    print ans
            

    
    pass