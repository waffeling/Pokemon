import psycopg2
import os
import sys
import csv
from unicodedata import normalize



def execute_insert_update(query:str, conn):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()


def get_pokemon_list(file_path:str):
    files = os.listdir(file_path)
    csv_list = []
    for i in files:
        period = i.find('.')
        if i[period+1::] == 'csv':
            csv_list.append(i)
   
    return csv_list
        

def open_file(file_path:str):
   content = []

   with open(file_path, 'r') as file:
      csvreader = csv.reader(file)

      for row in csvreader:
         content.append(row)

   return content

def content_to_data(content):


    mapp = {'{G}':"Grass", "{R}":"Fire", "{F}":"Fighting",
            "{L}":"Electric", "{W}":"Water", "{M}":"Metal",
            "{D}":"Dark", "{C}":"Normal", "{N}":"Dragon",
            "{P}": "Psychic"}
    content[0] = []


    for i in content:
        
        if not i:
            continue
        
        
        string_encode = i[2].encode('ascii','ignore')
        i[2] = string_encode.decode()

        if i[4] != '':
            i[4] = mapp[i[4]]

        words = i[3].split(" ")

        i[3] = words[0] + " " + words[2]

        print("Adding Card {cardname}...".format(cardname = i[2]))

    return content
    


def create_entry(entry, conn):

    if entry:
        if entry[4]:
            query = "INSERT INTO cards(card_name, pokemon_type, card_type, release, price, card_number, pokemon_stage, rarity) VALUES('{card_name}', '{pokemon_type}', '{card_type}', '{release}', '{price}', '{card_number}', '{pokemon_stage}', '{rarity}')"
            execute_insert_update(query.format(release = entry[0], card_number=entry[1], card_name = entry[2], pokemon_stage = entry[3], pokemon_type = entry[4], rarity = entry[5], price = entry[6], card_type = "Pokemon"), conn)

        else:
            query = "INSERT INTO cards(card_name, card_type, release, price, card_number, rarity) VALUES('{card_name}', '{card_type}', '{release}', '{price}', '{card_number}', '{rarity}')"
            execute_insert_update(query.format(release = entry[0], card_number=entry[1], card_name = entry[2], rarity = entry[5], price = entry[6], card_type = entry[3]), conn)

def __main__():
    print("ZOOOOOOMMMM")
    file_path = sys.argv[1]
    files = get_pokemon_list(file_path)
    conn = psycopg2.connect("dbname=postgres user=postgres password=pass123 host=localhost")
    for i in files:
        content = open_file(file_path + "\\" + i)
        data = content_to_data(content)
        for i in data:
            create_entry(i, conn)
    conn.close()


if __name__ == "__main__":
   __main__()

