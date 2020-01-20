import sqlite3
from DAO import Coffee_stands, Activities, Employees, Suppliers
from DTO import Employee


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect('moncafe.db')
        self.employees = Employees(self.conn)

    def create_tables(self):
        self.conn.execute(
            'CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY, location TEXT NOT NULL, number_of_employees INTEGER)')
        self.conn.execute(
            'CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary TEXT NOT NULL, coffee_stand INTEGER REFERENCE Coffee_stands(id))')
        # self.conn.execute('CREATE TABLE employees(id INTEGER PRIMARY KEY,name TEXT NOT NULL, salary REAL NOT NULL,
        # coffee_stand INTEGER REFERENCE coffee_stand(id))')


repo = Repository()
repo.create_tables()
