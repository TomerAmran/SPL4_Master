import atexit
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

    def create_employees_report(self):
        employees = self.employees.find_all_sorted_by_name()
        report = []
        for employee in employees:
            employeereport = [employee.name, employee.salary, self.coffee_stands.find(employee.coffee_stand).location]
            cursor = self.conn.cursor()
            employeereport.append(0)
            cursor.execute("""
            SELECT product_id, quantity  FROM activities where activator_id = ?
             """, (employee.id,))
            for tuple in cursor.fetchall():
                sales = (self.products.get_price(tuple[0]))
                employeereport[3] = employeereport[3] - (sales[0] * tuple[1])
            report.append(employeereport)
        return report

    def create_activity_report(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT a.date, p.description, a.quantity, e.name, s.name
        from Activities as a 
        JOIN Products as p on a.product_id = p.id
        LEFT JOIN Employees as e on a.activator_id = e.id
        LEFT JOIN Suppliers as s on a.activator_id = s.id 
        ORDER BY a.date ASC""")
        return cursor.fetchall()

    def _close(self):
        self.conn.commit()
        self.conn.close()


repo = Repository()
atexit.register(repo._close)
