# Define a class to represent each DVD
class DVD:
    def __init__(self, title, genre, year):
        #These are attributes of a DVD
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self):
        #This controls how the DVD is printed when we display it
        return f"{self.title} ({self.year}) - {self.genre}"
    


        