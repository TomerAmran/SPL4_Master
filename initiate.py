import os
os.remove('moncafe.db') # delete DataBase
from Repository import repo
from DAO import Coffee_stands, Activities, Employees, Suppliers
from DTO import Employee

if __name__ == '__main__':
    with open('config.txt') as inputFile:
        for line in inputFile:
            print(line)
    rep.employees.insert(Employee(1, 'Tomer', 35, 1))
    rep.conn.execute('SELECT * FROM employees')
    print(rep.conn.fetchAll())
