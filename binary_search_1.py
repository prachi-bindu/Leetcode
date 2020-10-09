def binarySearch(low,high,item):
    mid = int( low + (high - low)/2 )
    
    if(item == array[mid]):
        print("found at - ", array.index(item))
        
    elif(item > array[mid]):
        low = mid + 1
        binarySearch(low,high,item)
        
    elif(item < array[mid]):
        high = mid
        binarySearch(low,high,item)


array = []        

numOfElem = input("Enter the number of elements in array:- ")
for i in range(int(numOfElem)):
    array.append( int( input("Enter element in the array in increasing order:- ") ) )

low = 0
high = len(array)

item = int(input("Element to be searched - "))
binarySearch(low,high,item)
#print("Item found at ",foundIndex," location in array!")    
