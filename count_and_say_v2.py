def solution(n):
    str_ = "1"
    
    if n == 1:
        return str_
    
    for i in range(2,n+1):
        curr = ""
        temp = ""
        j = 0
        counter = 0
        while(j<len(str_)):
            #counter = 0
            if curr == "":
                curr = str_[j]
                counter += 1
                j += 1
                
                
            elif curr == str_[j]:
                counter += 1
                j += 1
                
            else:
                temp += str(counter)+curr
                curr = ""
                counter = 0
                #j += 1
                #print("tmp = ",temp)
        temp += str(counter)+curr
        str_ = temp
    #print("tmp = ",temp)
    #print(str_)
    return str_
print(solution(5))