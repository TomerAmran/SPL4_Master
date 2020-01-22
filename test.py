import os

import action
import initiate
from printdb import printdb


def main():
    initiate_print = printdb()
    open('initiate_print.txt', 'w').write(printdb())
    action_print = printdb()
    print(open('initiate-out.txt').read())
    if initiate_print == open('initiate-out.txt'):
        print('initiate print SUCCEEDED')
    else:
        print('initiate print FAILED')

    if action_print == open('action-out1.txt'):
        print('action print SUCCEEDED')
    else:
        print('action print FAILED')


if __name__ == '__main__':
    main()
