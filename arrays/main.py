#Script to run and test your DVD array 
from DVD_definition import DVD
from DVD_Array_File import DVDArray 

#Here we create some DVDS 
dvd1 = DVD("The Matrix", "Sci-Fi", 1999)
dvd2 = DVD("Friday Night Lights", "Drama", 2004)
dvd3 = DVD("Straw", "Drama", 2025)
dvd4 = DVD("Hackers", "Thriller", 1995)

#Create a DvD array (shelf) with a capacity of 5
shelf = DVDArray(5)

# Insert the DvDs
shelf.insert(0, dvd1)
shelf.insert(1, dvd2)
shelf.insert(2, dvd3)
shelf.insert(3, dvd4)

#Print the full shelf
print(shelf)

#Get and print a specific DVD
print ("\nGet index 1:")
print(shelf.get(1))
