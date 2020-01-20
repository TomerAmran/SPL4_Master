import sys
from DAO import Coffee_stands, Activities, Employees, Suppliers


def main(args):
    # imports
    import os

    # delete DataBase if exists
    if os.path.exists('moncafe.db'):
        os.remove('moncafe.db')
    from Repository import repo
    repo.create_tables()
    from DTO import Employee, Coffee_stand, Product, Supplier

    # with open('config.txt') as inputFile:
    #     for line in inputFile:
    #         print(line)
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            line = line[:-1]
            words = line.split(",")
            if words[0] == 'C':
                repo.coffee_stands.insert(Coffee_stand(words[1], words[2], words[3]))
            if words[0] == 'S':
                repo.suppliers.insert(Supplier(words[1], words[2], words[3]))
            if words[0] == 'E':
                repo.employees.insert(Employee(words[1], words[2], words[3], words[4]))
            if words[0] == 'P':
                repo.products.insert(Product(words[1], words[2], words[3], 0))
    import printdb
    printdb.printdb()

    # print(repo.conn.execute("""
    # SELECT
    # Activities.date, Activities.product_id, Activities.quantity, Employees.name
    # FROM Activities JOIN Employees on activator_id=id
    # """).fetchall())
    # print(repo.conn.execute('SELECT * FROM Employees').fetchall())
    # print(repo.conn.cursor().execute('SELECT * FROM Activities').fetchall())


if __name__ == '__main__':
    main(sys.argv)
