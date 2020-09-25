# named dna.py

from sys import argv, exit
import csv

# incorrect len(aegv) -> print error
if len(argv) != 2:
    print('Please include the correct files')
    exit(1)

# first CLA -> CSV file
# open CSV and read contents into memory
# first row will be column names starting with 'name' and followed by str sequences
with open(argv[1], newline='') as f:
    # seq_reader = csv.Reader(f, delimiter=',', quotechar='|')
    # seq_reader = csv.DictReader(f)
    fieldnames = ['name']
    seq_reader = csv.DictReader(f, fieldnames=fieldnames, restkey='SRTs')
    CSV = {}
    for index, row in enumerate(seq_reader):
        if index == 0:
            dna_list = row
        else:
            print(row['name'], row['SRTs'])
            # print(', '.join(row))
            # print(row)
    if dna_list:
        print(dna_list)
# second CLA -> text file of DNA sequence
# open DNA file and read contents into memory

# compute longest run of eact STR in DNA

# if count(STR) == person from CSV -> print person.name

# if no match print 'No match'
