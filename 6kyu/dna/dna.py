from sys import argv, exit
import csv
from pprint import pprint
import re


def main():

    check_args(argument=argv)
    dna_string = get_dna_string(dnafile=argv[2]).rstrip()
    dna_dict, people_list = get_people(peoplefile=argv[1])
    totals = calc_STR(dna_string=dna_string, str_list=dna_dict['SRTs'])
    string_numbers = make_strings(totals)
    print(dna_match(people=people_list, numbers=string_numbers))


def check_args(argument=[]):
    ''' incorrect len(argv) -> print error '''
    if len(argument) != 3:
        print('Please include the correct number of files')
        exit(1)


def get_people(peoplefile=''):
    ''' first CLA -> CSV file open CSV and read contents into memory first row
    will be column names starting with 'name' and followed by str sequences '''
    with open(peoplefile, newline='') as f:
        fieldnames = ['name']
        seq_reader = csv.DictReader(f, fieldnames=fieldnames, restkey='SRTs')
        CSV = {}
        for index, row in enumerate(seq_reader):
            if index == 0:
                dna_list = row
            else:
                CSV[row['name']] = row['SRTs']
        return dna_list, CSV


def get_dna_string(dnafile=''):
    '''second CLA -> text file of DNA sequence open DNA file and read contents into memory'''
    with open(dnafile, newline='') as dnaf:
        dna_string = dnaf.read()
        return dna_string


def calc_STR(str_list=[], dna_string=''):
    count_total = []
    for STR in str_list:
        matches = re.findall(rf'((?:{STR})+)', dna_string)
        longest_match = max(matches, default='')
        count_total.append(longest_match.count(STR))
    return count_total


def make_strings(number_list=[]):
    ''' coerce data for comparison '''
    return [str(i) for i in number_list]


def dna_match(people={}, numbers=[]):
    # print(people)

    for person in people.keys():
        '''
        if count(STR) == person from CSV -> print person.name,
        if no match print 'No match'
        '''
        test = people[person]
        if test == numbers:
            return person
    return 'No match'


if __name__ == '__main__':
    main()
