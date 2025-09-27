# Person class with age calculation
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or \
           (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age

# Test the Person class
person = Person("John Doe", "USA", "1990-05-15")
print(f"Name: {person.name}")
print(f"Country: {person.country}")
print(f"Age: {person.calculate_age()} years")