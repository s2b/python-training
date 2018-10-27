name = raw_input("Wie heisst du? ")
sprache = raw_input("Welche Sprache sprichst du? ")
anzahl = input("Wie oft willst du begruesst werden? ")

for x in range(1, anzahl):
    if sprache == 'Deutsch':
        print("Guten Tag " + name)
    else:
        print("Good afternoon " + name)
