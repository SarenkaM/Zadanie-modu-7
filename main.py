from faker import Faker
fake = Faker('pl_PL')

class Card:
   def __init__(self, name, firm, position, email):
       self.name = name
       self.firm = firm
       self.position = position
       self.email = email
       self._len_card = 0
   def __str__(self):
       return f'{self.name}, {self.firm}, {self.position}, {self.email}'
   def __repr__(self):
       return f"Card(name={self.name} firm={self.firm}position={self.position}email={self.email}"
   def contact(self):
       print(f"kontaktuj się z {self.name} {self.position} {self.email}")

""" @property
   def len_card(self):
       return (len(self.name))

   @len_card.setter
   def len_card(self, value):"""


cards_one = Card(name=fake.name(), firm=fake.company(), position=fake.job(), email=fake.email())
cards_two = Card(name=fake.name(), firm=fake.company(), position=fake.job(), email=fake.email())
cards_three = Card(name=fake.name(), firm=fake.company(), position=fake.job(), email=fake.email())
list_cards = [cards_one, cards_two, cards_three]
by_name = sorted(list_cards, key=lambda card:card.name)
print(by_name)
print(cards_one)
print(cards_two)
print(cards_three)
print(cards_one.contact())
#print(cards_one.len_card)


class BaseContact(Card):
   def __init__(self, phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.phone = phone
class BusinessContact(Card):
   def __init__(self, work_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.work_phone = work_phone

BaseContact_one = BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
BaseContact_two = BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
BaseContact_three = BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())

print(BaseContact_one)
print(BaseContact_two)
print(BaseContact_three)

class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

        self._current_speed = 0

    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'

    def __eq__(self, other):
        return all(
            (
                self.make == other.make,
                self.model_name == other.model_name,
                self.top_speed == other.top_speed,
                self.color == other.color
                 )
        )
    def accelarate(self, step=20):
        self._current_speed += step
    def decelerate(self, step=10):
        self._current_speed -= step

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")


car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_three = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")
print(car_one == car_two)
print(car_one == car_three)


car_one.current_speed = 25
print(car_one.current_speed)

class Truck(Car):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
print(truck)
truck.accelarate()
print(truck.current_speed)
