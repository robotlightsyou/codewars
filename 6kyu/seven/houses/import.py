import csv
from cs50 import SQL
from sys import argv, exit


db = SQL("sqlite:///students.db")


def main():
    check_args(argument=argv)
    get_people(peoplefile=argv[1])


def check_args(argument=[]):
    ''' incorrect len(argv) -> print error '''
    if len(argument) != 2:
        print('Please include the correct number of files')
        exit(1)


def split_names(namestring=""):
    ''' check if namestring has 2 or 3 names, fill middle with None if missing '''
    if namestring.count(" ") == 2:
        first, middle, last = namestring.split()
    else:
        middle = None
        first, last = namestring.split()
    return first, middle, last


def get_people(peoplefile=''):
    ''' read from a csv to dictionary, then insert into SQL table.'''
    with open(peoplefile, newline='') as f:
        fieldnames = ['name', 'house', 'birth']
        seq_reader = csv.DictReader(f, fieldnames=fieldnames)
        for index, row in enumerate(seq_reader):
            #skip the column titles
            if index == 0:
                continue
            first, middle, last = split_names(row['name'])

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?,?,?,?,?)",
                       first, middle, last, row['house'], row['birth'])


if __name__ == '__main__':
    main()
