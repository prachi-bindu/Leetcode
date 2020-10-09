def first_non_repeating_letter(string):
    #your code here
    str1 = string
    print(str1)
    char_order = []
    ctr = {}
    for c in str1:
        if c.lower() in ctr:
            ctr[c.lower()] += 1
        else:
            ctr[c.lower()] = 1 
            char_order.append(c)
    for c in char_order:
        if ctr[c.lower()] == 1:
            return c
    return ""
    
first_non_repeating_letter("sTTreg")
    