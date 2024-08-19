class Instructor:
    followers = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
   
    
    def display(self, subject_name):
        print(f"Hi, I am {self.name} and I teach {subject_name}")
    
    def update_followers(self, follower_name):
        self.followers +=1

Instructor_1= Instructor("Jenny", "Delhi")
print(Instructor_1.name)
Instructor_1.display("Python")
Instructor_1.update_followers("Payal")
print(Instructor_1.followers)
Instructor_2 = Instructor("Jiya", "Doha")

Instructor_2.update_followers("Jenny")
print(Instructor_2.followers)