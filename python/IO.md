# Input/Output
- python não precisa importar lib para manipular arquivos (nativo)
- Utiliza cursores para ler arquivos (percorre o arquivo uma vez, ao chegar ao fim, precisa ser inicializado novamente)

## open()
```python
file = open("file.txt")

#criando um novo arquivo
file = open("new.txt", "w")
```

## with()
- utilizando with() os recursos são dispensados automaticamente. (é a mesma coisa que o using do C#)
- por trás dos panos, ele utiliza os dunders __enter()__ e __exit()__ para executar as operações de abertura e fechamento

## With Statement Usage
Opening a file using with is as simple as: with open(filename) as file:

```python
with open("welcome.txt") as file: # Use file to refer to the file object
   data = file.read()
   # ...do something with data
```

## Métodos
|Nome|Função|
|----|------|
|**file.read()**|retorna o arquivo como uma única string (\n para quebra de linhas)|
|**file.seek()**|movimenta o cursor (o argumento é um caracter)|
|**file.read()**|Traz uma única linha|
|**file.realines()**|Retorna todas as linhas como uma lista|
|**file.closed**|Retorna True se o arquivo estiver aberto|
|**file.close()**|fecha o arquivo, liberando recursos do computador|
|**file.write(<string>)**|Adiciona texto à um arquivo|

## Reading CSV
### read normal
```python
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
 ```
 
 ### read as dict
 - The first line of the CSV file is assumed to contain the keys to use to build the dictionary. If you don’t have these in your CSV file, you should specify your own keys by setting the fieldnames optional parameter to a list containing them.
```python
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
```
### writting csv
```python
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```
