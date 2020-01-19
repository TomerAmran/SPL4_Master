class Employees:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, employee):
        self.conn.execute("""INSERT INTO employees (id, name, salary, coffee_stand) VALUES (?, ?)""", [employee.id, employee.name, employee.salary, employee.coffee_stand])

    # def find(self, student_id):
    #     c = self.conn.cursor()
    #     c.execute("""
    #         SELECT id, name FROM students WHERE id = ?
    #     """, [student_id])
    #     return Student(*c.fetchone())