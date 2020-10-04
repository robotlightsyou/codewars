import csv
from cs50 import SQL
from sys import argv, exit

db = SQL("sqlite:///students.db")

def main():
    check_args(argument=argv)
    get_people(peoplefile=argv[1])


#arg len check
def check_args(argument=[]):
    ''' incorrect len(argv) -> print error '''
    if len(argument) != 2:
        print('Please include the correct number of files')
        exit(1)


def split_names(namestring= ""):
    if namestring.count(" ") == 2:
        first, middle, last = namestring.split()
    else:
        middle = None
        first, last = namestring.split()
    return first, middle, last


def get_people(peoplefile=''):
    ''' first CLA -> CSV file open CSV and read contents into memory first row
    will be column names starting with 'name' and followed by str sequences '''
    with open(peoplefile, newline='') as f:
        fieldnames = ['name', 'house', 'birth']
        seq_reader = csv.DictReader(f, fieldnames=fieldnames)
        for index, row in enumerate(seq_reader):
            if index == 0: continue
            first, middle, last = split_names(row['name'])

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?,?,?,?,?)",
                       first, middle, last, row['house'], row['birth'])


if __name__ == '__main__':
    main()
