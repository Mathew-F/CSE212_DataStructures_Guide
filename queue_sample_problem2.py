'''
In keeping with the roller coaster example, imagine that the park allows guests 
to buy a priority pass that allows them to enter at the front of the ride lines. Lame right?
In this case, the park manager allows 3 pass holders to board the ride before allowing 2 non pass holders to 
board. 
'''

class Roller_Coaster:
    def __init__(self):
        self.norm_queue = []
        self.pass_queue = []

    def start_ride(self):
        '''
        clears the queue as if the ride started and the cart has taken off
        and nobody else can board the car. 
        '''
        if len(self.pass_queue) == 0:
            for x in range(0, 5):
                print(f'Boarding {self.norm_queue[0]}')
                pass #code goes here
        elif len(self.pass_queue) < 3 and len(self.pass_queue) > 0:
            for x in range(0, len(self.pass_queue)):
                print(f'Boarding {self.pass_queue[0]}')
                del self.pass_queue[0]
            remainder = abs(len(self.pass_queue) - len(self.norm_queue))
            for x in range(0, remainder):
                print(f'Boarding {self.norm_queue[0]}')
                del self.norm_queue[0]
        elif len(self.pass_queue) > 3 and len(self.pass_queue) < 6:
            for x in range(0,3):
                print(f'Boarding {self.pass_queue[0]}')
                del self.pass_queue[0]
            for x in range(0, len(self.norm_queue)):
                print(f'Boarding {self.norm_queue[0]}')
                del self.norm_queue[0]
            remainder = abs(len(self.pass_queue) - len(self.norm_queue))
            for x in range(0, remainder):
                print(f'Boarding {self.pass_queue[0]}')
                del self.pass_queue[0]
        else:
            for x in range(0, 3):
                print(f'Boarding {self.pass_queue[0]}')
                pass #Code goes here
            for x in range(0, 2):
                print(f'Boarding {self.norm_queue[0]}')
                pass #code goes here
        print('Enjoy the ride!')  

class Coaster_Car(Roller_Coaster):
    def __init__(self):
        self.maximum_capacity = 5
        super().__init__() #allows us to use the parent's class attributes and methods

    def add_rider(self, name, pass_holder):
        if ((len(self.norm_queue) + len(self.pass_queue)) < self.maximum_capacity and len(self.norm_queue) >= 0 and len(self.pass_queue) >= 0):
            if pass_holder == True:
                pass #Code goes here
            else:
                pass #Code goes here
            print(f'Welcome abord!')
        else:
            print("Sorry, the ride is at maximum capacity, please wait for the next car.")
            self.start_ride()

print('Test Case #1')
car = Coaster_Car()
car.add_rider('Bob', False)
car.add_rider('Bill', False)
car.add_rider('Pam', False)
car.add_rider('Jim', False)
car.add_rider('Samantha', False)
car.add_rider('Jill', False)
#Bob, Bill, Pam, Jim, Samantha
print("=================")

print('\nTest Case #2')
car.add_rider('Bob', False)
car.add_rider('Bill', False)
car.add_rider('Pam', True)
car.add_rider('Jim', False)
car.add_rider('Samantha', True)
car.add_rider('Jill', False)
#Pam, Samantha, Bob, Bill, Jim 
print("=================")

print('\nTest Case #3')
car.add_rider('Bob', True)
car.add_rider('Bill', True)
car.add_rider('Pam', True)
car.add_rider('Jim', True)
car.add_rider('Samantha', False)
car.add_rider('Jill', False)
#Bob, Bill, Pam, Samantha, Jim
print("=================")

print('\nTest Case #4')
car.add_rider('Bob', False)
car.add_rider('Bill', True)
car.add_rider('Pam', True)
car.add_rider('Jim', False)
car.add_rider('Samantha', True)
car.add_rider('Jill', False)
#Bill, Pam, Samantha, Bob, Jim

#uncomment and use these lines, if needed, for testing purposes.
# print(f'Pass Queue: {car.pass_queue}')
# print(f'Normal Queue: {car.norm_queue}')
