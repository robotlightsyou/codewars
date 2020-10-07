import cs50
import csv
from sys import argv

if len(argv) != 2: # Checking arguments
    print("Necesito más argumentos")
    exit(0)
if str(argv[1]) != "characters.csv": # Check for correct input file
    print("Archivo equivocado")
    exit(0)
db = cs50.SQL("sqlite:///students.db") # opens data base
db.execute("DELETE FROM students") # deletes other data
db.execute("DELETE FROM sqlite_sequence")
with open(argv[1], "r") as characters: # Opens and read file
    reader = csv.DictReader(characters)
    for row in reader:
        house = row["house"]
        name = row["name"]
        names = name.split()
        if len(names) == 2:
            first = names[0]
            middle = None
            last = names[1]
        else:
            first = names[0]
            middle = names[1]
            last = names[2]
        birth = int(row["birth"])
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?,?,?,?,?)", first, middle, last, house, birth)
