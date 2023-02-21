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
       return(f"kontaktuj się z {self.name} {self.position} {self.email}")


cards_one = Card(name=fake.name(), firm=fake.company(), position=fake.job(), email=fake.email())
cards_two = Card(name=fake.name(), firm=fake.company(), position=fake.job(), email=fake.email())
cards_three = Card(name=fake.name(), firm=fake.company(), position=fake.job(), email=fake.email())
list_cards = [cards_one, cards_two, cards_three]
by_name = sorted(list_cards, key=lambda card:card.name)

#print(cards_one.len_card)



class BaseContact:
   def __init__(self, name, phone, email):
       self.name = name
       self.phone = phone
       self.email = email
       self._len_card = 0
   def __str__(self):
       return f'{self.name}, {self.phone}, {self.email}'
   def base_contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name}")
   @property
   def len_card(self):
       return self._len_card
   @len_card.setter
   def len_card(self, value):
       value = (len(self.name))
       self._len_card = value

class BusinessContact(BaseContact):
   def __init__(self, work_phone, firm, position, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.work_phone = work_phone
       self.firm = firm
       self.position = position
   def __str__(self):
       return f'{self.name}, {self.phone}, {self.email},{self.firm}, {self.work_phone}, {self.position}'
   def business_contact(self):
       print(f"Wybieram numer {self.work_phone} i dzwonię do {self.name} ")
BaseContact_one = BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
BaseContact_two = BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
BaseContact_three = BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
BusinessContact_one = BusinessContact(name=fake.name(), phone=fake.phone_number(), email=fake.email(), firm=fake.company(), position=fake.job(), work_phone=fake.phone_number())
BusinessContact_two = BusinessContact(name=fake.name(), phone=fake.phone_number(), email=fake.email(), firm=fake.company(), position=fake.job(),  work_phone=fake.phone_number())
BusinessContact_three = BusinessContact(name=fake.name(), phone=fake.phone_number(), email=fake.email(), firm=fake.company(), position=fake.job(), work_phone=fake.phone_number())

print(BaseContact_one)
print(BaseContact_two)
print(BaseContact_three)
print(BusinessContact_one)
print(BusinessContact_two)
print(BusinessContact_three)
print(BaseContact_two.len_card)

