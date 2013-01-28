'''
Created on Jan 26, 2013

@author: kevin
'''

from itertools import combinations
from collections import defaultdict
import math
import string


start = "a" # start node
distance = {}

class point:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "name " + str(self.name) + " x = " + str(self.x) + " y= " + str(self.y)

def load_file():
    node_lst = {}
    with open("tsp.txt") as f:
        f.next()     
        
        counter = 0
        for row in f:
            name = string.lowercase[counter]
            x = float(row.split()[0][:8])
            y = float(row.split()[1][:8])
            counter+=1
            
            node_lst[name] = point(name,x,y)
            
            
        return node_lst
    
def init_matrix():
    matrix  =  {}
    sub = {}
    sub[start] = 0
    
    matrix[start] = sub
    return matrix


def calculate_distance(node_lst,p1,p2):
    
    key =  "".join( sorted([node_lst[p1].name, node_lst[p2].name] ))
    
    if key in distance:
        return distance[key]
    else:   
        val = math.sqrt((node_lst[p1].x-node_lst[p2].x) ** 2 + (node_lst[p1].y-node_lst[p2].y) ** 2)
        distance[key] = float("{0:.3f}".format( val ))
        return distance[key]
    
    
def cal_tsp(node_lst,matrix):
   
    no_nodes = len(node_lst)
    
    all_nodes = [ key for key in node_lst.iterkeys() ]
    all_nodes.remove(start)
    
    for set_size in range(1,no_nodes):        
        for s in combinations( all_nodes ,set_size):
            
          
            lst = "".join(sorted(s + (start,)))
            
            if lst not in matrix:
                sub_m =  defaultdict(lambda: float("inf"))
                matrix[lst] = sub_m
            
            for j in lst:
                
               
                min_value = float("1e10")
                
                if j == start:
                    continue
                else:
                  
                    for k in lst:
                        
                        if k != j: 
                            temp_cal = matrix[lst.replace(j,"")][k] + calculate_distance(node_lst, k, j)                           
                            if temp_cal< min_value:
                                min_value = temp_cal
                            
                    #print min(min_lst)
                    matrix[lst][j] = temp_cal
        
        # clean up
        clean_up = set_size-1            
        if ( clean_up > 0):
#            print matrix
            for ki in matrix.keys():
                if len(ki) < clean_up:
                    del matrix[ki]
            
        
        

if __name__ == '__main__':
    matrix = init_matrix()
    node_lst =  load_file()
    cal_tsp(node_lst,matrix)
    
    min_lst = []
    ans = matrix[ "".join(sorted( [ key for key in node_lst.iterkeys() ] )) ]
   
    for x in ans.iterkeys():
        min_lst.append(ans[x] + calculate_distance(node_lst, x, start))
    
    print min(min_lst)

    

    pass