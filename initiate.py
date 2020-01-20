if __name__ == '__main__':
    import os
    # delete DataBase if exists
    if os.path.exists('moncafe.db'):
        os.remove('moncafe.db')
    # imports
    from Repository import repo
    from DAO import Coffee_stands, Activities, Employees, Suppliers
    from DTO import Employee, Activitie, Coffee_stand, Product, Supplier

    # with open('config.txt') as inputFile:
    #     for line in inputFile:
    #         print(line)
    repo.employees.insert(Employee(1, 'Tomer', 35, 1))
    repo.employees.insert(Employee(2, 'Niva', 40, 1))
    repo.activities.insert(Activitie(5, -100, 1, '20200121'))
    repo.activities.insert(Activitie(4, -400, 1, '20200121'))
    repo.activities.insert(Activitie(4, -400, 2, '20200121'))
    repo.coffee_stands.insert(Coffee_stand(1, 'location1', 0))
    repo.coffee_stands.insert(Coffee_stand(2, 'location2', 0))
    repo.products.insert(Product(1,'prod1', 1, 0))
    repo.products.insert(Product(2,'prod2', 2, 0))
    repo.products.insert(Product(3,'prod3', 3, 0))
    repo.suppliers.insert(Supplier(66, 'sup1', 'contact1'))
    repo.suppliers.insert(Supplier(67, 'sup2', 'contact2'))
    repo.suppliers.insert(Supplier(68, 'sup3', 'contact3'))
    import printdb
    printdb.printdb()


    # print(repo.conn.execute("""
    # SELECT
    # Activities.date, Activities.product_id, Activities.quantity, Employees.name
    # FROM Activities JOIN Employees on activator_id=id
    # """).fetchall())
    # print(repo.conn.execute('SELECT * FROM Employees').fetchall())
    # print(repo.conn.cursor().execute('SELECT * FROM Activities').fetchall())
