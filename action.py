import sys

from DTO import Activitie


def main(args):
    from Repository import repo
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            words = line.split(",")
            if repo.products.getquantity(words[0]) + int(words[1]) >= 0:
                repo.activities.insert(Activitie(words[0], words[1], words[2], words[3]))
                repo.products.find(words[0])
                repo.products.updatequantity(words[0], words[1])
        repo.conn.commit()
    import printdb
    print(printdb.printdb())


if __name__ == '__main__':
    main(sys.argv)
