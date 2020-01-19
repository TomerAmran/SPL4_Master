import sqlite3
import DAOs.Employees
import DAOs.Activities
import DAOs.Coffee_stands
import DAOs.Products
import DAOs.Suppliers


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect('moncafe.db')
        self.employees = DAOs.Employees(self.conn)

    def create_tables(self):
        self.conn.executescript(""""
        CREATE TABLE employees (
            id      INTEGER         PRIMARY KEY,
            name    TEXT        NOT NULL,
            salary  REAL    NOT NULL,
            coffee_stand    INTEGER REFERENCE   coffee_stand(id)
        );""")
