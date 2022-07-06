import csv

myData = [["first_name", "second_name", "Grade"], 
        ["Alex", "Brian", "A"],
        ["Tom", "Smith", "B"]]

import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')

with myFile:

    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")

# Prueba 2 Archivos CSV 07/07/2022