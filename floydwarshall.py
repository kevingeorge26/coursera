'''
Created on Jan 19, 2013

@author: kevin

all pair shortest path
'''

from numpy import *

node_number = 0
  

class loop(Exception):
    pass

def load_file(filename):
    global node_number
    with open(filename) as file:
        
        node_number = int(file.next().split()[0])
        edge_list = [ [ float("inf") for i in xrange(node_number)] for j in xrange(node_number) ]
        
        for line in file:
            line_value = line.split()
            edge_list[int(line_value[0])-1][int(line_value[1])-1] = int(line_value[2])
            
        return edge_list


def init_matrix(edge_list):
    
    #matrix =     [ [ float("1e10") for i in xrange(node_number)] for j in xrange(node_number) ]
    
    matrix = zeros((node_number,node_number))
    matrix.fill(float("1e10"))
    
    for i in xrange(node_number):
        for j in xrange(node_number):
            if i == j:
                matrix[i][j] = 0
            elif edge_list[i][j] < float("1e10"):
                matrix[i][j] = edge_list[i][j]
                           
    return matrix

        
def find_path(matrix):
    
    for k in xrange(1,node_number):
        for i in xrange(node_number):
            for j in xrange(node_number):
                matrix[i][j] = min( [ matrix[i][j] , matrix[i][k] + matrix[k][j] ]  )
    
    """ print value"""
    min_value = float("inf")
    try:            
        for i in xrange(node_number):
            for j in xrange(node_number):
                
                if i == j and matrix[i][j] < 0:
                    raise loop
                
                if min_value > matrix[i][j]:
                    min_value = matrix[i][j]
    except loop:
        print "cycle detected"
        
    print min_value

def play_py():
    a = zeros((2,2))
    a.fill(5)
    a[1][1] = 10
    print a
                     

if __name__ == '__main__':
    
#    print play_py()
    
    edge_list = load_file(filename = "graph3.txt")
    
    print "init matrix "
    
    matrix = init_matrix(edge_list)
    
    print "going to find the path"
    find_path(matrix)
    pass