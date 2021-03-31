class Roller_Coaster:
    def __init__(self):
        self.queue = []

    def start_ride(self):
        '''
        clears the queue as if the ride started and the cart has taken off
        and nobody else can board the car.
        '''
        for x in range(0,5):
            del self.queue[0]
        print('Enjoy the ride!')    


class Coaster_Car(Roller_Coaster):
    def __init__(self):
        self.maximum_capacity = 5
        super().__init__() #allows us to use the parent's class attributes and methods

    def add_rider(self, person):
        if len(self.queue) < self.maximum_capacity and len(self.queue) > 0:
            self.queue.append(person)
            print(f'Welcome abord!')
        else:
            print("Sorry, the ride is at maximum capacity, please wait for the next car.")
            self.start_ride()

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