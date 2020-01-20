if __name__ == '__main__':
    import os
    # delete DataBase if exists
    if os.path.exists('moncafe.db'):
        os.remove('moncafe.db')
    # imports
    from Repository import repo
    from DAO import Coffee_stands, Activities, Employees, Suppliers
    from DTO import Employee
    with open('config.txt') as inputFile:
        for line in inputFile:
            print(line)
    repo.employees.insert(Employee(1, 'Tomer', 35, 1))
    repo.conn.execute('SELECT * FROM employees')
    print(rep.conn.fetchAll())
