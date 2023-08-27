class Agegroup:
    def __init__(self, age, color):
        self.age = age
        self.color = color
        # print(self.__class__.__name__)

def announce(f):
    def wrapper(a,b):
        print("Checking for seats")
        f(a,b)
    return wrapper


Shola = Agegroup(18, 'Red')
Tinubu = Agegroup(25, 'Blue')
Folabi = Agegroup(26, "Yellow")

students = {"Shola": Shola, "Tinubu": Tinubu, "Folabi": Folabi}

for name, details in students.items():
    print(f"My Name is {name}, i am {details.age} years old, My favourite color is {details.color}")

class Seatscheck:
    def __init__(self, seats):
        self.seats = seats
        self.passengers = []
    
    def available_seats(self):
        available = self.seats - len(self.passengers)
        return available
    
    def checker (self, name):
        if not self.available_seats():
            return False
        self.passengers.append(name)
        return True
            
@announce
def seatchecking(checker, list):
    for passenger in list:
        success = checker.checker(passenger)

        if success:
            print(f"{passenger} has been added to the Flight.")
            print(f"There are {checker.available_seats()}seats left")
        else:
            print("No More Seats")

Passengerlist = ["Dayo", "Kunle", "Dolapo", "Segun", "Ayo"]
checker = Seatscheck(25)
seatchecking(checker, Passengerlist)