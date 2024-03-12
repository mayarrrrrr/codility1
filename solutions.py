def solution(A,D):
    # initialize the initial balance to zero
    
     # iterate through the array of transactions(A)
     
    # check for negative values(card transaction) :
    #    if present, deduct card fee(5*12) after summation
    #    if not present,return the summed balance
    
    #  iterate through the D array(dates) and split the date to obtain month
    
    # Create a dictionary to store the dates as keys and their corresponding amount as value 
    
    #  If a card transaction worth more than 100 occurs more than three time in a month no fee is paid 
  
    initial_balance = 0
    month_transaction = {}
    
   
    for transaction in A:
        print(transaction)
      
        
       
        if transaction >= 0:
           initial_balance  += transaction
        #    print(initial_balance)
           
        else:
            initial_balance += transaction - (5*12)
            
            
        for date in D:
            month = int(date.split("-")[1])
            print(month)
            
                
            
            
            
            
    return initial_balance
        
    
print(solution(  [1, -1, 0, -105, 1] ,["2020-1-20","2020-2-20","2020-1-20"])) 