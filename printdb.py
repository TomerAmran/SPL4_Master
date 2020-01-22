from Repository import repo


def print_Activities():
    output = 'Activities' + '\n'
    for activity in repo.activities.find_all():
        output += activity.__str__() + '\n'
    return output


def print_Coffee_stands():
    output = 'Coffee stands' + '\n'
    for stand in repo.coffee_stands.find_all():
        output += stand.__str__() + '\n'
    return output


def print_Employees():
    output = 'Employees' + '\n'
    for employee in repo.employees.find_all():
        output += employee.__str__() + '\n'
    return output


def print_Products():
    output = 'Products' + '\n'
    for product in repo.products.find_all():
        output += product.__str__() + '\n'
    return output


def print_Suppliers():
    output = 'Suppliers' + '\n'
    for supplier in repo.suppliers.find_all():
        output += supplier.__str__() + '\n'
    return output


def print_Employees_report():
    report = repo.create_employees_report()
    output = 'Employees report' + '\n'
    for line in report:
        for cell in line:
            output += cell.__str__() + ' '
        output = output.rstrip()
        output += '\n'
    return output.rstrip()


def print_joined_Activities():
    report = repo.create_activity_report()
    if report.__len__() > 0:
        output = '\n' + 'Activities' + '\n'
        for line in report:
            output += line.__str__() + '\n'
        return output.rstrip()
    return ''


def printdb():
    output = print_Activities()
    output += print_Coffee_stands()
    output += print_Employees()
    output += print_Products()
    output += print_Suppliers()
    output += '\n' + print_Employees_report()
    output += '\n' + print_joined_Activities()
    return output


if __name__ == '__main__':
    print(printdb())
