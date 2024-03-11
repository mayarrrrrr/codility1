def solution(A,D):
  
    initial_balance = 0
    for transaction in range (len(A)):
        
        
        if A[transaction] < 0:
           initial_balance  += A[transaction]-(5*12)
           
        elif A[transaction] > 0:
            initial_balance += A[transaction]
            
            
    return initial_balance
        
    
print(solution([-10,-20,-30],["2020-1-20","1210","12901"])) 