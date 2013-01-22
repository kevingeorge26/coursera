'''
Created on Dec 28, 2012

@author: kevin

'''

weight = 0
no_items = 0
node_list = []
answers = {}

def load_file():
    global weight
    global no_items
    
    with open("knapsack2.txt") as files:
        line = files.next()
        weight = int(line.strip().split()[0])
        no_items = int(line.strip().split()[1])
        
        for line in files:
            node_list.append( ( int(line.strip().split()[0]),int(line.strip().split()[1] )) )
            
    node_list.sort( key=lambda x:x[1],reverse=True)
    

def rec(index,wt):
    
    if node_list[index][1] > wt:
        return 0
    
    if index < 0:
        return 0
    
    if str(index)+ "+" + str(wt) in answers:
        a = answers[str(index-1)+ "+" + str(wt)]
    else:
        a = rec(index-1,wt)
        answers[str(index-1)+ "+" + str(wt)] = a
        
        
    if str(index-1)+ "+" + str(wt- node_list[index][1]) in answers:
        b = answers[ str(index-1)+ "+" + str(wt- node_list[index][1]) ]
    else:
        b = rec(index-1,wt - node_list[index][1])
        answers[ str(index-1)+ "+" + str(wt- node_list[index][1]) ] = b        
        
    
    return max([ a, b + node_list[index][0]])


def py_pl():
    test = [(1,2),(3,3),(10,1)]
    test.sort( key=lambda x:x[1],reverse=True)
    print test

if __name__ == '__main__':
    
    load_file()
    
    print "start"
    print rec(no_items-1,weight)
    
    
    pass