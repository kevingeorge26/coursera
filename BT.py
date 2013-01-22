'''
Created on Dec 26, 2012

@author: kevin
'''
""" code for optimal binary search tree , where the frequency of each
key is given """



keys_freq = {1:.05,2:.4,3:.08,4:.04,5:.1,6:.1,7:.23}
val = [ [float(0) for y in range(7)]  for x in range(7) ]
n = 7 # no of elements
def tree():
    val[0][0] = .05
    keys = sorted(keys_freq.keys())
    print val
    
    for s in range(n-2):
        for i in range(n-1):
            print val
            sub = []
            
            sums = 0
            for item in range(i,i+s):                
                sums += keys_freq[keys[item]]                
            
            print i,i+s
            for r in range(i,i+s):
                sub.append( sums + 0 if r-1>i else val[i][r-1] + 0 if i+s>r+1 else val[r+1][i+s] )
                
            #print i,i+s
            if len(sub)>0:
                val[i][i+s] = min(sub)
                
    print val
            


if __name__ == '__main__':
    tree()
    pass