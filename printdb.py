from Repository import repo


def print_Activities():
    print('Activities')
    for activitie in repo.activities.find_all():
        print(activitie)

def print_Coffee_stands():
    print('Coffee stands')
    for stand in repo.coffee_stands.find_all():
        print(stand)

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
    report = repo.create_employees_report()
    print()
    print('Employees Report')
    for line in report:
      print(*line)


def print_joined_Activities():
    report = repo.create_activity_report()
    if report.__len__() > 0:
        print()
        print('Activities')
        for line in report:
            print(line)


def printdb():
    print_Activities()
    print_Coffee_stands()
    print_Employees()
    print_Products()
    print_Suppliers()
    print_Employees_report()
    print_joined_Activities()


if __name__ == '__main__':
    printdb()
