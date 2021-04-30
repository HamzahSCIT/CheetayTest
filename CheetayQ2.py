def equilibriumPoint(A, n):
    total = sum(A) 
    lsum = 0
    
    for i, num in enumerate(A):  
        total -= num 
        if lsum == total: 
            return i+1
        lsum += num  
    return -1
    
    
A = [1,3,5,2,2]
n = len(A)
print(equilibriumPoint(A, n))
