'''
Created on Jul 27, 2012

@author: kevin
'''


def load_file(file_name):
    
    numbers = [ int(line.strip()) for line in open(file_name) if int(line.strip()) <=4000 ]     
    
        
    number_set = sorted(set(numbers))    
    
    
    print len(number_set)
    return number_set
    
    
def count_t(numbers):
    
    set_result = {}
    
    for i in range(len(numbers)-1):
        a = numbers[i]
        for j in range(i+1,len(numbers)):
            b = numbers[j]
            temp = a+ b
            if temp <= 4000 and temp >= 2500:
                x = str(a)+ "+" +str(b)
                set_result[str(temp)] = "x"
                
    print len(set_result)
    #print set_result
    
    
def count_sum(numbers,start,end):
    
    count = 0
    for i in range( len(numbers)-1 ):
    
                
        a = binary_test_upper(numbers,start,end,i)
        b = binary_test_lower(numbers,start,end,i)
        
#        print a,b
        
        temp = a - b + 1
        count += temp
#        print count
        
    print count
    
    
def binary_test_upper(numbers,start,end,i):
    
    
    
    temp = numbers[i]
    if 1:
        a = i+1
        b = len(numbers) -1
        mid = 0
        
        
        while a <= b:
            
            mid = (a + b)/2
            
            if numbers[mid]+ temp < end :
                a = mid + 1
            elif numbers[mid] + temp > end :
                b = mid-1
            else:
                break
       
        if temp+numbers[mid]>end:
            return mid-1
        else:
            return mid
            

def binary_test_lower(numbers, start , end , i):
    
    temp = numbers[i]
    if 1:
        a = i+1
        b = len(numbers) -1
        mid = 0
        flag = False
        
        while a <= b:
            
            mid = (a + b)/2
            
            if numbers[mid]+ temp < start :
                a = mid + 1
            elif numbers[mid] + temp > start :
                b = mid-1
            else:
                break
            
            
        if temp + numbers[mid] < start:
            return mid+1
        else:
            return mid
        
        
            
    


if __name__ == '__main__':
    numbers = load_file("6.txt")
    count_t(numbers)
#    binary_test(numbers, 14, 20)
#    binary_test_lower(numbers,14 , 20)
#    count_sum(numbers, 2500, 4000)
#    print numbers

#    print "started"
#    count_sum(numbers, 2500, 4000)

    pass