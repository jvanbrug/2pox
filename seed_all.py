"""Write seed node choices for all graph files

.. moduleauthor:: Jan Van Bruggen <jancvanbruggen@gmail.com>
"""
from __future__ import print_function
from os import listdir
from os import system
from sys import executable


def run():
    for graph_file_name in listdir('graphs'):
        print('seeding', graph_file_name)
        system(executable + ' seed.py graphs/' + graph_file_name)


if __name__ == '__main__':
    run()
