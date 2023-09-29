from Config import app,db 

def create_authors():
    authors = [
            {"id" : 0,"last_name": "Tolkien", "first_name": "J.R.R.", "nationality": "British", "famous_work": "The Lord of the Rings"},
            {"id" : 1, "last_name": "Rowling", "first_name": "J.K.", "nationality": "British", "famous_work": "Harry Potter"},
            {"id" : 2, "last_name": "Hemingway", "first_name": "Ernest", "nationality": "American", "famous_work": "The Old Man and the Sea"},
            {"id" : 3, "last_name": "Austen", "first_name": "Jane", "nationality": "British", "famous_work": "Pride and Prejudice"},
        ]

    for a in authors:
        newA = Author(last_name = a['last_name'], first_name  = a['first_name'], nationality = a['nationality'], famous_work = a['famous_work'] )
    
        db.session.add(newA)

    db.session.commit()


class Author(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    last_name =  db.Column(db.String, nullable=False)
    first_name =  db.Column(db.String, nullable=False)
    nationality =  db.Column(db.String, nullable=False)
    famous_work = db.Column(db.Text, nullable=True)

    
    def __init__(self, last_name, first_name, nationality, famous_work):
        self.last_name = last_name
        self.first_name = first_name
        self.nationality = nationality
        self.famous_work = famous_work



try:
    
    Authors = Author.query.all()
    countAuthors = len( Authors )
    print(f"already created with posts ...NB posts {countAuthors}")

    
    if  len( Authors ) == 0 :
        create_authors()

except:
    db.create_all() 
    create_authors()