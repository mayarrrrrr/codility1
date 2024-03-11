def solution(A,D):
    # initialize the initial balance to zero
    
     # iterate through the array of transactions(A)
     
    # check for negative values(card transaction) :
    #    if present, deduct card fee(5*12) after summation
    #    if not present,return the summed balance
    
    #  iterate through the D array(dates) and split the date to obtain month
    
    #  If a card transaction worth more than 100 occurs more than three time in a month no fee is paid 
  
    initial_balance = 0
    
   
    for transaction in range (len(A)):
        
       
        if A[transaction] < 0:
           initial_balance  += A[transaction]-(5*12)
           
        elif A[transaction] > 0:
            initial_balance += A[transaction]
            
            
    return initial_balance
        
    
print(solution(  [-60, 60, -40, -20] ,["2020-1-20","1210","12901"])) 