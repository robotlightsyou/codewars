# named dna.py

from sys import argv, exit
import csv


def main():
    check_args(argv)
    dna_list, people_list = get_people(argv[1])
    dna_string = get_dna_string(argv[2])
    print(dna_string.rstrip())
    print(dna_list)
    print(people_list)

# incorrect len(aegv) -> print error


def check_args(argument):
    if len(argument) != 3:
        print('Please include the correct files')
        exit(1)

# first CLA -> CSV file
# open CSV and read contents into memory
# first row will be column names starting with 'name' and followed by str sequences


def get_people(peoplefile):
    with open(peoplefile, newline='') as f:
        fieldnames = ['name']
        seq_reader = csv.DictReader(f, fieldnames=fieldnames, restkey='SRTs')
        CSV = {}
        for index, row in enumerate(seq_reader):
            if index == 0:
                dna_list = row
            else:
                print(row['name'], row['SRTs'])
                CSV[row['name']] = row['SRTs']
        return dna_list, CSV

        if dna_list:
            # print(dna_list)
            return dna_list
# second CLA -> text file of DNA sequence
# open DNA file and read contents into memory


def get_dna_string(dnafile):
    with open(dnafile, newline='') as dnaf:
        dna_string = dnaf.read()
        return dna_string

# compute longest run of eact STR in DNA

# if count(STR) == person from CSV -> print person.name


# if no match print 'No match'
if __name__ == '__main__':
    main()
