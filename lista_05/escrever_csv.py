import csv

arquivo = open("leitura.csv", "w", newline="", encoding="utf-8")
write = csv.writer(arquivo, delimiter=";")
cabecalho = ["Nome", "Idade", "Situacao"]
write.writerow(cabecalho)

funcionario1 = ["Jose", "25", "Ativo"]
write.writerow(funcionario1)
funcionario2 = ["Jose", "25", "Ativo"]
write.writerow(funcionario1)
funcionario3 = ["Jose", "25", "Ativo"]
write.writerow(funcionario1)
funcionario4 = ["Jose", "25", "Ativo"]
write.writerow(funcionario1)
