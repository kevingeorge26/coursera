'''
Created on Dec 21, 2012

@author: kevin
'''

from collections import defaultdict

class mynode:
  def __init__(self,string,line_no):
    self.string = string
    self.node = line_no
    self.parent = line_no
    self.one_count = string.count("1")
    
  def __repr__(self):
  	return "parent = " + self.parent
  
  def set_parent(self,parent):
    self.parent = parent
      
  def __index__(self):
    return int(self.string,2)
  

one_node = {} # hash map where key is the number of one in the string
cluster_list = {} # key parent that is line number in string

def file_something():
  
  with open("test.txt") as file:
    file.next()
    count = 0
    for x in file:
      count+=1
      node = mynode(x.strip().replace(" ",""),str(count))  
      one_node[node.string.count("1")].append(node)
      cluster_list[str(count)].append(node)
      
      
def cluster():
  for x in cluster_list:
    cluster_node_list = cluster_list[x]
    for node in cluster_node_list:
      dist = node.one_count
      
      # same one  count
      for neigh in one_node[dist]:
        if node.parent != neigh.parent and check_hamming_distance(node.string, neigh.string, 1):
          to_join = cluster_list[neigh.parent]
          cluster_list.pop[neigh.parent]
          for temp in to_join:
            temp.parent = node.parent
            cluster_node_list.append(temp)

			# same one	count
      for neigh in one_node[dist-1]:
        if node.parent != neigh.parent and check_hamming_distance(node.string, neigh.string, 1):
          to_join = cluster_list[neigh.parent]
          cluster_list.pop[neigh.parent]
          for temp in to_join:
          	temp.parent = node.parent
          	cluster_node_list.append(temp)
          	
			# same one	count
      for neigh in one_node[dist+1]:
        if node.parent != neigh.parent and check_hamming_distance(node.string, neigh.string, 1):
          to_join = cluster_list[neigh.parent]
          cluster_list.pop(neigh.parent)
          for temp in to_join:
          	temp.parent = node.parent
          	cluster_node_list.append(temp)


                  
def check_hamming_distance(string1,string2,count):
  """ count is the hamming distance we are looking for """
  if bin(int(string1,2)+int(string2,2))[-3:].count("1") <= count:
    return True
  else:
    return False

def play_py():
	mydict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
	
	for x in mydict.keys():
		print x
		if "three" in mydict:
			mydict.pop("three")

if __name__ == '__main__':
  
  one_node = defaultdict(lambda : [] )
  cluster_list = defaultdict(lambda : [] )
  
#  file_something()
#  cluster()

  play_py()
  print cluster_list
  
  #print bin(int("101",2)+int("101",2))[-3:].count("1")
  

  
