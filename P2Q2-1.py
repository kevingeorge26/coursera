'''
Created on Dec 22, 2012

@author: kevin
'''
from collections import defaultdict
import sys

class mynode:
  def __init__(self,string,line_no):
    self.string = string
    self.node = line_no
    self.one_count = string.count("1")
    
  def __repr__(self):
    return "string " + self.string + " node name " + self.line_no + " count " + self.one_count
    
  def __index__(self):
    return int(self.string,2)

one_count = {}

def load_file():
  
  with open("clustering2.txt") as file:
    file.next()
    count = 0
    for x in file:
      count+=1
      node = mynode(x.strip().replace(" ",""),str(count))
      one_count[node.string.count("1")].append(node)
      
def create_file():
  with open("test_output.txt",'w') as file:
    file.write("i made this \n")
    
    print sorted(one_count.keys(),reverse=False)
    for x in sorted(one_count.keys(),reverse=False):
      lst = one_count[x]
      
      for i in range(0,4):
        new_x = x+i
        if new_x in one_count:
          print new_x
          lst2 = one_count[new_x]
          
          for node1 in lst:
            for node2 in lst2:
              dist = get_hamming_distance(node1.string, node2.string)
             
              if node1.node != node2.node and dist <= 2:
                file.write(node1.node + " " + node2.node + " " + str(dist) +"\n")
      
    


def get_hamming_distance(string1,string2):
  """ count is the hamming distance we are looking for """
  
  return bin(int(string1,2) ^  int(string2,2))[2:].count("1")
  

  
  
def play_py():
  for i in range(1,4):
    print i   


if __name__ == '__main__':
  one_count = defaultdict(lambda:[])
  load_file()
  create_file()
  pass