'''print('You rock!')
import random
random_choice = random.randint(0, 2)
print("MAC chooses", random_choice)


ferari_cost = 2500
bank_balance =int(input("Input your amount! "))


if bank_balance >= ferari_cost:
    print('Sure, you can buy it')
else:
    print('Sorry, insufficient balance')
names =['kweku','jon','ase','killer']
names.append('banku')
#append is for adding new values
names.sort()
#sort is for arranging in alphabetical order
print(names)

#sets
s= set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.remove(4)
print(len(s))

name="killer"
for f in name:
    print(f)
for q in range(1000):
    print(q)

phones ={"Ase": "Techno", "nsuo":"Infinix", "banku":"Nokia"}
phones['kweku']='Infinix'
print(phones["nsuo"])

def square(x):
    return x*x
for i in range(5):
    print(f'the square of {i} is {square(i)}') 

#creates a new flight
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers =[]
#adds passengers to flight
    def passenger_add(self, name):
#means if there are no open seats available, return false        
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
#number of seats available        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight= Flight(3)        
people =['Kofi','Kweku','Ase','Killa']
for person in people:
    success = flight.passenger_add(person)
    
    if success:
        print(f'we added {person} to flight successfully.')
    else:
        print(f'better luck next time,{person}')
        '''
import random
def announce(f):
    def wrapper():
        print('Starting with the function')
        f()
        print('Done running the function')
    return wrapper

@announce
def sum():
    random_choice = random.randint(0, 2)
    print("MAC chooses", random_choice)
sum()    
    
