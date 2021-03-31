'''
This program allows riders to board the coaster car, then
when the car is full (max capacity of 5 people) it leaves 
the dock and begins the ride. Upon return, the car is emptied and
5 more people are allowed to board for another run.
'''
class Roller_Coaster:
    def __init__(self):
        self.queue = []

    def start_ride(self):
        '''
        Clears the queue as if the ride started and the cart has taken off
        and nobody else can board the car.
        '''
        pass    #put code here   


class Coaster_Car(Roller_Coaster):
    def __init__(self):
        self.maximum_capacity = 5
        super().__init__() #allows us to use the parent's class attributes and methods

    def add_rider(self, person):
        if len(self.queue) < self.maximum_capacity and len(self.queue) > 0:
            pass    #put code here
            print(f'Welcome abord!')
        else:
            print("Sorry, the ride is at maximum capacity, please wait for the next car.")


print('Test Case #1\n-------------------------')
car = Coaster_Car()
car.add_rider('Bob')
car.add_rider('Tim')
car.add_rider('Sue')
car.add_rider('Joe')
car.add_rider('Sally')
car.add_rider('Bill')
#should result in 5 'Welcome aboard!'s followed by a ride at capacity.
print('-------------------------')
print('Test Case #2\n-------------------------')
car.start_ride()
car.add_rider('Bill')
for x in range(0, len(car.queue)):
    print(car.queue[x])
#Should result in 'Enjoy the ride' meaning the car has left then 'welcome aboard' and who boarded the car.