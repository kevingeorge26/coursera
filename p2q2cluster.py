'''
Created on Dec 20, 2012

@author: kevin
'''
from collections import defaultdict

"9995,1641"
class edge:
  def __init__(self,u,v,weight):
    self.u=u
    self.v=v
    self.weight= weight
    
  def __repr__(self):
    return "u =" + self.u + " v " + self.v +\
             " weight " + str(self.weight)
    
    
node_to_cluster = {}
cluster_content = {}
edge_list  = []


def load_file():
  with open("test_output.txt") as file:
    file.next()
    for line in file:
    
      u=line.strip().split()[0]
      v=line.strip().split()[1]
      wt=line.strip().split()[2]
      
      edge_list.append( edge(u,v,int(wt)) )
      
      node_to_cluster[u] = u
      cluster_content[u] = set([u])
      
      node_to_cluster[v] = v
      cluster_content[v] = set([v])
     
    
    edge_list.sort(key=lambda x: x.weight)
  print len(node_to_cluster)
      
def cluster():
  global k
  
  while len(edge_list) > 0:
   
    valid_edge = edge_list.pop(0)
    
    
    if node_to_cluster[valid_edge.u] != node_to_cluster[valid_edge.v]:
      
      cluster1 = cluster_content[node_to_cluster[valid_edge.u]]
      cluster2 = cluster_content[node_to_cluster[valid_edge.v]]
      
      cluster_content.pop( node_to_cluster[valid_edge.v] )
      
      for x in cluster2:
        node_to_cluster[x] = node_to_cluster[valid_edge.u]
        
      cluster1.update(cluster2)
      



if __name__ == '__main__':
  load_file()
  cluster()
  print "cluster",len(cluster_content)
  
  pass