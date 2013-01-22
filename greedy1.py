'''
Created on Dec 16, 2012

@author: kevin
'''
from collections import defaultdict

class job:
    def __init__(self,weight,length):
        self.weight = weight
        self.length = length
    
    def __repr__(self):
        return "w " + str(self.weight) + " l " + str(self.length)
        
dict = {}

def load_file1():
    time_elapsed = 0
    sum_m = 0
    
    for line in open("jobs.txt"):
        if len( line.strip().split() ) > 1:
            w = int(line.strip().split()[0])
            l = int(line.strip().split()[1])
            dict[w-l].append(job(w,l))
    
    order =  sorted(dict.keys(),reverse=True)
    print order
    
    for i in order:
        job_w = dict[ int(i) ]
        job_w.sort(reverse=True,key = lambda x : x.weight)
        
        for job_o in job_w:
            time_elapsed +=job_o.length
            sum_m += time_elapsed*job_o.weight
            
    print sum_m
    
def load_file2():
    time_elapsed = 0
    sum_m = 0
    
    for line in open("jobs.txt"):
        if len( line.strip().split() ) > 1:
            w = int(line.strip().split()[0])
            l = int(line.strip().split()[1])
           
            dict[w/float(l)].append(job(w,l))
    
    order =  sorted(dict.keys(),reverse=True)
    
    
    for i in order:
        job_w = dict[ float(i) ]
        job_w.sort(reverse=True,key = lambda x : x.weight)
        
        for job_o in job_w:
            time_elapsed +=job_o.length
            sum_m += time_elapsed*job_o.weight
            
    print sum_m


def play():
    st = [i for i in "abcdaeeeee"]
    print st
    i =1
    tail=0
    j =0
    
    for i in range(1,len(st)):
        
        for j in range(tail+1):
            if st[i] == st[j]:
                break
        
        if j == tail:
            st[tail] = st[i]
            tail+=1
            
    st[tail] = "9"
    print st
        
    

if __name__ == '__main__':
    #dict = defaultdict(lambda:[])
    #load_file1()
    #load_file2()
    play()
    pass