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
k = 4

def load_file():
  with open("cluster.txt") as file:
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
      
def cluster():
  global k
  
  while len(cluster_content) > k:
   
    valid_edge = edge_list.pop(0)
    
    
    if node_to_cluster[valid_edge.u] != node_to_cluster[valid_edge.v]:
      
      cluster1 = cluster_content[node_to_cluster[valid_edge.u]]
      cluster2 = cluster_content[node_to_cluster[valid_edge.v]]
      
      cluster_content.pop( node_to_cluster[valid_edge.v] )
      
      for x in cluster2:
        node_to_cluster[x] = node_to_cluster[valid_edge.u]
        
      cluster1.update(cluster2)
      
  print cluster_content
      
def get_max_spacing():
  
  cluster_distance = defaultdict( lambda : 9999999 )
  
  for x in edge_list:
    if node_to_cluster[x.u] != node_to_cluster[x.v]:
      
      cluster_pair = ""
      if node_to_cluster[x.u] > node_to_cluster[x.v]:
        cluster_pair = node_to_cluster[x.u]+","+node_to_cluster[x.v]
      else:
        cluster_pair = node_to_cluster[x.v]+","+node_to_cluster[x.u]
        
      print cluster_distance[cluster_pair]
      if cluster_distance[cluster_pair] > x.weight:
        print "here"
        cluster_distance[cluster_pair] = x.weight  
      
  print cluster_distance
    
    
    
      
  


if __name__ == '__main__':
  load_file()
  cluster()
  get_max_spacing()
  pass