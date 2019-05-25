# exceltocsvpy

Para usar a aplicação basta copiar a pasta app para dentro de sua própria aplicação, da um import nos requirements, e no seu código importar o seguinte

`from app.exceltocsv import convert`

A função convert recebe o nome do arquivo excel e o nome do arquivo csv que será gerado.
O arquivo excel deve está na mesma pasta.

Se você não passar nada ele vai ler o arquivo test.xlsx e retorna um arquivo csvfile.csv

Funciona para as versões 2.x e 3.x do Python!
