def solution(A,D):
    # initialize the initial balance to zero
    
     # iterate through the array of transactions(A)
     
    # check for negative values(card transaction) :
    #    if present, deduct card fee(5*12) after summation
    #    if not present,return the summed balance
    
    #   split the date to obtain month
    
    # Create a dictionary to store the month as key and their corresponding amount as value-month_transaction
    
     # Create a dictionary to store the month as key and their corresponding occurence as value-total_month
     
    
    # iterate through dictionary to acces the value(transaction,month)
    
    
    
    #  If a card transaction worth more than 100 occurs more than three time in a month no fee is paid 
  
    balance = 0
    month_transaction = {}
    total_month = {}
    fee = 5 * 12
    
   
    for transaction in range(len(A)):
        # print(len(A))
        
      
        
       
        if A[transaction] >= 0:
           balance  += A[transaction]
        #    print(balance)
           
        else:
            
            
            month = int(D[transaction].split("-")[1])
            if month in month_transaction:
                month_transaction[month] += A[transaction]
            else:
                month_transaction[month] = A[transaction]
            if month in total_month:
                total_month[month] += 1
            else:
                total_month[month] = 1 
                
            for key,value in month_transaction.items():
                if value <= -100 and total_month[key] >= 3:
                     balance  += A[transaction] + 5
                else :
                    balance  += A[transaction] 
    balance -= fee
                       
                            
                
               
    print(month_transaction)
    print(total_month)
                      
                
                
        
            
                
            
                
            
            
            
            
    return balance
        
    
print(solution(  [180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"])) 