from Repository import Repository
from DTOs.Employee import Employee
if __name__ == '__main__':

    with open('config.txt') as inputFile:
        for line in inputFile:
            print(line)
    rep = Repository()
    rep.create_tables()
    rep.employees.insert(Employee(1, 'Tomer', 35, 1))
    rep.conn.execute('SELECT * FROM employees')
    print(rep.conn.fetchAll())
