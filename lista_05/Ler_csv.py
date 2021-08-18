import csv

arquivo = csv.reader(open("leitura.csv"))
for line in arquivo:
    print(line)
