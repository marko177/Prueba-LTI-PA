import csv
with open("example4.csv", "w") as csvfile:
    fieldnames = ["first_name", "last_name", "Grade"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Grade": "B", "first_name": "Alex", "last_name": "Brian"})
    writer.writerow({"Grade": "A", "first_name": "Rachael", "last_name": "Rodriguez"})
    writer.writerow({"Grade": "B", "first_name": "Jane", "last_name": "Oscar"})
    writer.writerow({"Grade": "B", "first_name": "Jane", "last_name": "Loive"})
    
    print("Writing complete")

# Prueba 3 Archivos CSV 07/07/2022