class Employee:
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Supplier:
    def __init__(self, id, name, contact_information):
        self.contact_information = contact_information
        self.name = name
        self.id = id


class Product:
    def __init__(self,id,description, price, quantity):
        self.quantity = quantity
        self.price = price
        self.description = description
        self.id = id


class Coffee_stand:
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activitie:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date