#Create a fixed-size array class to store DVDs
class DVDArray:
    def __init__(self, capacity):
        #Max number of DVDs that can be stored - simulates fixed memory allocation
        self.capacity = capacity
        #Pre-fill the array with None (empty slots)
        self.storage = [None] * capacity
        #Tracks how many DVDs are actually stored (not how many slots exist)
        self.size = 0

    def insert(self, index, dvd):
        #This function places a DVD at a specific index

        #If the index is out of range, we simulate a memory overflow/block
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of bounds!")
        
        #Place the DVD at the specified index
        self.storage[index] = dvd
        