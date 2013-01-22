'''
Created on Dec 27, 2012

@author: kevin
'''

""" iterative version of knapscak
"""

node_list = []
weight = 0
no_items = 0


def load_file():
    global weight
    global no_items
    
    with open("knapsack2.txt") as files:
        line = files.next()
        weight = int(line.strip().split()[0])
        no_items = int(line.strip().split()[1])
        
        for line in files:
            node_list.append( ( int(line.strip().split()[0]),int(line.strip().split()[1] )) )

def init():
    global answers
    answers = [[0 for x in range(weight+1)] for y in range(len(node_list))]

def knap():
    
    for i in range(no_items):
        for w in range(1,weight+1):
            if i == 0 and node_list[i][1] < w:
                answers[i][w] = node_list[i][0]
                
            elif w >= node_list[i][1]:
                answers[i][w] = max([ answers[i-1][w],node_list[i][0] + answers[i-1][w - node_list[i][1]] ])
                
            else:
                answers[i][w] = answers[i-1][w]

if __name__ == '__main__':
    load_file()
    init()
   
    
    knap()
    #print answers
    print answers[no_items-1][weight]
    print 
    pass