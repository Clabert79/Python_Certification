import csv

import argparse
parser = argparse.ArgumentParser(description="Un esempio di script con parametri opzionali")

# Aggiungere argomenti opzionali
parser.add_argument('--name', type=str, help='Il nome dell\'utente')
parser.add_argument('--age', type=int, help='L\'età dell\'utente')
parser.add_argument('--city', type=str, help='La città dell\'utente')

# Analizzare gli argomenti della linea di comando
args = parser.parse_args()

# Utilizzare gli argomenti
if args.name:
    print(f"Nome: {args.name}")
else:
    print("Nome non fornito")

if args.age:
    print(f"Età: {args.age}")
else:
    print("Età non fornita")

if args.city:
    print(f"Città: {args.city}")
else:
    print("Città non fornita")

# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/

rows = []
with open("accounts_deploy.csv", 'r') as file:
    type(file)

    csvreader = csv.reader(file)

    for row in csvreader:
        account = row[0]
        if(len(account) < 12):
           print("short account: ", account)
           account = account.zfill(12)
        
        rows.append(account)

print(rows)

print(len(rows))