# positional arguments: *

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3)

# Many keyword arguments: **
# arguments become dictionary


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # no error if argument is missing in call
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)