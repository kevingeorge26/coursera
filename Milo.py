'''
Created on Feb 7, 2013

@author: kevin
'''

import sys
from itertools import combinations
from collections import defaultdict
import string



vowels_count = {} # store vowel count
constants_count = {} #store constant count


vowels = set([ x for x in "aeiouAEIOU" ])
constants = set([ x for x in "aeiouAEIOU " ])
   
value_mat ={}

def cal_gcd(a,b):
    if a == b:
        return b
    
    if b > a:
        a,b = b,a
        
    while b != 0:
        temp = b
        b = a%b
        a=temp
        
    return a

def calculate_ss(product,person):
    
    if person not in vowels_count:
        vowels_count[person] = sum(letter in vowels for letter in person)
        constants_count[person] = sum(letter not in constants for letter in person)
    
    val = product + "+" + person
    
    if val not in value_mat:
        if len(product)%2 == 0:
            value_mat[val] = vowels_count[person] * 1.5
        else:
            value_mat[val] = constants_count[person]
            
        if cal_gcd(len(product),len(person)) > 1:
            value_mat[val] = value_mat[val] * 1.5
            
    return value_mat[val]
        

def solve(test):
    
    global vowels_count,constants_count
        
    vowels_count.clear()
    constants_count.clear()
        
    line = test.split(";")
    people = line[0].split(",")
    products = line[1].split(",")
    
    mat = defaultdict(lambda : defaultdict(lambda:0) ) # dict where we would find the answer
    
  
    mat_prod = {}  # char to product name mapping
    
    lowercase = string.ascii_letters
    
    for i in range(len(products)):
        mat_prod[lowercase[i]] = products[i] 
 
        
    for i in range(0,len(products)):  
        for s in combinations( mat_prod.iterkeys() ,i +1):
            
            s = "".join(sorted(s))
           
            for j in range(0,len(people)):
                max = 0
                
                for k in s:
                    temp = calculate_ss(mat_prod[k],people[j]) + mat[ s[:].replace(k,"") ][j]
                    if temp > max:
                        max = temp
                
                mat[s][j+1] = max
                
    print mat["abc"]
                
                
        
    
        
    

    

# start execution of the program

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if len(test) > 1:
        solve(test)
        
        
    
test_cases.close()
