import sqlite3
from DAOs.Employees import Employees
from DAOs.Suppliers import Suppliers
from DAOs.Products import Products
from DAOs.Activities import Activities
from DAOs.Coffee_stands import Coffee_stands


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect('moncafe.db')
        self.employees = Employees(self.conn)

    def create_tables(self):
        self.conn.execute('CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary TEXT NOT NULL, coffee_stand INTEGER REFERENCE coffee_stand(id))')
        # self.conn.execute('CREATE TABLE employees(id INTEGER PRIMARY KEY,name TEXT NOT NULL, salary REAL NOT NULL, coffee_stand INTEGER REFERENCE coffee_stand(id))')
