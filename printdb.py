from Repository import repo


def print_Activities():
    print('Activities')
    for activitie in repo.activities.find_all():
        print(activitie)


def print_Employees():
    print('Employees')
    for employee in repo.employees.find_all():
        print(employee)


def print_Products():
    print('Product')
    for product in repo.products.find_all():
        print(product)


def print_Suppliers():
    print('Suppliers')
    for supplier in repo.suppliers.find_all():
        print(supplier)


def print_Employees_report():
    pass


def print_joined_Activities():
    pass


def printdb():
    print_Activities()
    print_Employees()
    print_Products()
    print_Suppliers()
    print_Employees_report()
    print_joined_Activities()


if __name__ == '__main__':
    printdb()
