import sqlite3
from DAO import Coffee_stands, Activities, Employees, Suppliers, Products
from DTO import Employee


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect('moncafe.db')
        self.employees = Employees(self.conn)
        self.activities = Activities(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.products = Products(self.conn)
        self.coffee_stands = Coffee_stands(self.conn)

    def create_tables(self):
        # Coffee_stands
        self.conn.execute(
            'CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY, location TEXT NOT NULL, number_of_employees INTEGER)')
        # Employees
        self.conn.execute(
            'CREATE TABLE Employees(id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary TEXT NOT NULL, coffee_stand '
            'INTEGER REFERENCES Coffee_stands(id))')
        # Suppliers
        self.conn.execute(
            'CREATE TABLE Suppliers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, contact_information TEXT)')
        # Products
        self.conn.execute('CREATE TABLE Products(id INTEGER PRIMARY KEY, description TEXT NOT NULL, price REAL NOT '
                          'NULL, quantity INTEGER NOT NULL)')
        # Activities
        self.conn.execute("""
        CREATE TABLE Activities(
        product_id INTEGER INTEGER REFERENCES Product(id),
        quantity INTEGER NOT NULL,
        activator_id INTEGER NOT NULL,
        date DATE NOT NULL)
        """)

        

    def create_activity_report(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT a.date, p.description, a.quantity, e.name, s.name
        from Activities as a
        JOIN Products as p
        on a.product_id = p.id
        LEFT JOIN Employees as e
        on a.activator_id = e.id
        LEFT JOIN Suppliers as s
        on a.activator_id = s.id """)
        return cursor.fetchall()


repo = Repository()
