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
            words = line.split(",")
            if words[0] == 'C':
                repo.coffee_stands.insert(Coffee_stand(words[1].strip(' '), words[2].strip(' '), words[3].strip(' ')))
            if words[0] == 'S':
                repo.suppliers.insert(Supplier(words[1].strip(' '), words[2].strip(' '), words[3][:-1].strip(' ')))
            if words[0] == 'E':
                repo.employees.insert(Employee(words[1].strip(' '), words[2].strip(' '), words[3].strip(' '), words[4].strip(' ')))
            if words[0] == 'P':
                repo.products.insert(Product(words[1].strip(' '), words[2].strip(' '), words[3].strip(' '), 0))
    # import printdb
    # print(printdb.printdb())


if __name__ == '__main__':
    main(sys.argv)
