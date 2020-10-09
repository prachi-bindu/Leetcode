def primeN(start,end):
    #start = start
    #end = end
    prime = ""
      
    for i in range(start,end): 
        for j in range(2,i): 
            if(i % j==0): 
                break
        else: 
            #print(i) 
            prime = prime+str(i)        
    #print(prime)
    return prime
    
def solution(n):
    idN = ""
    pStr = primeN(2,10000)
    return(pStr[n:n+5])

print(solution(3))