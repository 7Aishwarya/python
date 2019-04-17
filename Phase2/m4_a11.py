class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
 
    def __str__(self):
        return self.title + ' by ' + self.author + '\nPublisher: ' + self.publisher
 
b = Book('Science for Class 10','Lakhmir Singh', 'S. Chand')
print(b)
