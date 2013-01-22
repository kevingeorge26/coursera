'''
Created on Jul 27, 2012

@author: kevin
'''


def load_file(file_name):
    
    numbers = [ int(line.strip()) for line in open(file_name)  ]     
        
    numbers.sort()
    return numbers
    
    
def count_sum(numbers,start,end):
    
    result = {}
    
    for i in range( len(numbers) ):
        a = numbers[i]
        
        for j in range( i+1 , len(numbers) ):
            temp = a + numbers[j]
            if temp <= end and temp >= start:
                result[str(a) + "+" + str(numbers[j]) ] = "x"
                
   # print result
    print len (result)


if __name__ == '__main__':
    numbers = load_file("6.txt")
   
    count_sum(numbers, 2500, 4000)
    pass