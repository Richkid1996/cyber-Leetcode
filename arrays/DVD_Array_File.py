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

        #Increase the actual size count 
        self.size += 1
    
    def get(self, index):
        #Retrieve a DVD from a specific slot in the array

        #Protects against out-of-bounds access
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of Bounds!")
        
        #Return the DVD object (or None)
        return self.storage[index]
    
    def __str__(self):
        #Return a human-readble version of the shelf
        #Shows all slots: either a DVD or "Empty"
        return "\n".join(
            f"[{i}] {str(dvd) if dvd else 'Empty'}"
            for i, dvd in enumerate(self.storage)
        )
        