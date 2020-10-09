class BinArraySorting:
    def __init__(self):
        self.arr = []
        
    def showArray(self):
        print(self.arr)
        
    def fillArray(self):
        n = int( input("Enter the size of the array-") )
        print("Enter the elements in the array-")
        for i in range(n):
            elem = int( input() )
            self.arr.append(elem)
            
    def sortArray(self):
        print("2")
        self.arr.sort()
        self.showArray()

a = BinArraySorting()
#n = int( input("Enter the number of elements in array-") )
a.fillArray()
a.showArray()
a.sortArray()
#a.showArray()