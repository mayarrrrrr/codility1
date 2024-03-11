def solution(A,D):
    # Initialize the balance
    # iterate through the array A
    # iterate through array D ,split the string  on meeting an hyphen
    # negative value < 3 && num > 100(sum - (5*11))
    # 
    initial_balance = 0
    for transaction in range (0,len(A)):
        
        
        if A[transaction] < initial_balance:
           total_balance  = sum(A) - (5*12)
           
        elif A[transaction] > initial_balance:
            total_balance = sum(A)
            return total_balance
            
    return total_balance
        
    
            
        
       
    
            
            
        
        
    
        
        
        
    
            
    
print(solution([10,-20,30],["2020-1-20","1210","12901"]))    
        
        