from DTO import Coffee_stand, Product, Activitie

from DTO import Employee, Supplier


class Activities:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, activitie):
        with self.conn:
            self.conn.execute("""
            INSERT INTO Activities(product_id, quantity, activator_id, date) VALUES (?,?,?,?)
            """, [activitie.product_id, activitie.quantity, activitie.activator_id, activitie.date])

    def find_all(self):
        cursor = self.conn.cursor()
        all = cursor.execute("""
                SELECT * FROM Activities ORDER BY date ASC""").fetchall()
        return [Activitie(*row) for row in all]


class Coffee_stands:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, coffee_stand):
        with self.conn:
            self.conn.execute("""
                INSERT INTO Coffee_stands VALUES(?,?,?)
                 """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM Coffee_stands WHERE id = ?
        """, ([id]))
        return Coffee_stand(*cursor.fetchone())

    def find_all(self):
        cursor = self.conn.cursor()
        all_stands = cursor.execute("""
                SELECT * FROM Coffee_stands ORDER BY id ASC""").fetchall()
        return [Coffee_stand(*row) for row in all_stands]

    def find_name_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
                SELECT name FROM Coffee_stands WHERE id = ?
                """, ([id]))
        return cursor.fetchone()


class Employees:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, employee):
        with self.conn:
            self.conn.execute("""INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)""",
                              [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, id):
        c = self.conn.cursor()
        c.execute("""
                SELECT * FROM Employees WHERE id = ?
            """, [id])
        return Employee(*c.fetchone())

    def find_all(self):
        c = self.conn.cursor()
        all = c.execute("""
            SELECT * FROM Employees ORDER BY id ASC
        """).fetchall()
        return [Employee(*row) for row in all]

    def find_all_sorted_by_name(self):
        c = self.conn.cursor()
        all = c.execute("""
                   SELECT * FROM Employees ORDER BY name ASC
               """).fetchall()
        return [Employee(*row) for row in all]


class Products:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, product):
        with self.conn:
            self.conn.execute("""
                INSERT INTO Products(id, description, price,quantity) VALUES (?,?,?,?)
                """, [product.id, product.description, product.price, product.quantity])

    def find(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM Products WHERE id = ?
        """, ([id]))
        return Product(*cursor.fetchone())

    def find_all(self):
        cursor = self.conn.cursor()
        all_stands = cursor.execute("""
                SELECT * FROM Products C""").fetchall()
        return [Product(*row) for row in all_stands]

    def getquantity(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
                SELECT quantity FROM Products WHERE id = ?
                 """, (id,))
        quantity = cursor.fetchone()[0]
        return quantity

    def updatequantity(self, id, quantity):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT quantity FROM Products WHERE id = ?
         """, (id,))
        originalquantity = self.getquantity(id)
        newquantity = originalquantity + int(quantity)
        self.conn.execute("""
        UPDATE Products SET quantity = ? WHERE id = ? """, [newquantity, id])

    def get_price(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
                SELECT price FROM Products WHERE id = ?
                 """, (id,))
        return cursor.fetchone()


class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, supplier):
        with self.conn:
            self.conn.execute("""INSERT INTO Suppliers VALUES (?, ?, ?)""",
                              [supplier.id, supplier.name, supplier.contact_information])

    def find(self, id):
        c = self.conn.cursor()
        c.execute("""
                SELECT * FROM Suppliers WHERE id = ?
            """, [id])
        return Employee(*c.fetchone())

    def find_all(self):
        c = self.conn.cursor()
        all = c.execute("""
            SELECT * FROM Suppliers ORDER BY id ASC
        """).fetchall()
        return [Supplier(*row) for row in all]
