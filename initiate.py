if __name__ == '__main__':
    import os

    # delete DataBase if exists
    if os.path.exists('moncafe.db'):
        os.remove('moncafe.db')
    # imports
    from Repository import repo
    from DAO import Coffee_stands, Activities, Employees, Suppliers
    from DTO import Employee, Activitie

    # with open('config.txt') as inputFile:
    #     for line in inputFile:
    #         print(line)
    repo.employees.insert(Employee(1, 'Tomer', 35, 1))
    repo.employees.insert(Employee(2, 'Niva', 40, 1))
    repo.activities.insert(Activitie(5, -100, 1, '20200121'))
    repo.activities.insert(Activitie(4, -400, 1, '20200121'))
    repo.activities.insert(Activitie(4, -400, 2, '20200121'))
    print(repo.employees.find(1))

    # print(repo.conn.execute("""
    # SELECT
    # Activities.date, Activities.product_id, Activities.quantity, Employees.name
    # FROM Activities JOIN Employees on activator_id=id
    # """).fetchall())
    # print(repo.conn.execute('SELECT * FROM Employees').fetchall())
    # print(repo.conn.cursor().execute('SELECT * FROM Activities').fetchall())
