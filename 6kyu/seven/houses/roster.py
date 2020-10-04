import csv
from cs50 import SQL
from sys import argv, exit


db = SQL("sqlite:///students.db")


def main():
    check_args(argument=argv)
    get_students()


def check_args(argument=[]):
    ''' incorrect len(argv) -> print error '''
    if len(argument) != 2:
        print('Please include the correct number of files')
        exit(1)


# query students table for all students in argv[1]
def get_students():
    # stoer query results to access for printing
    query = db.execute("SELECT first, middle, last, birth FROM students WHERE house = %s ORDER BY last, first", argv[1])
    for student in query:
        # print(student['first'])
        name = []
        name.append(student['first'])
        name.append(student['middle'])
        name.append(student['last'])
        # loop over name printing if not None
        print(f"{' '.join(nm for nm in name if nm)}, born {student['birth']}")


if __name__ == '__main__':
    main()

