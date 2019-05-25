# Teste da aplicação pra ler excel e converter para csv.

from app.exceltocsv import convert

'''
A função convert() recebe o nome do arquivo excel e o nome do arquivo csv a ser criado,
ela não retorna nada, mas cria um arquivo no mesmo diretório com o nome desejado.

Caso nenhum nome seja enviado como no exemplo abaixo, ele lê exatamente um arquivo chamado
test.xlsx e exporta um outro arquivo chamado csvfile.csv
'''
convert()