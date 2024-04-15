import os
import csv 

def get_pokemon_list(file_path:str):
    files = os.listdir(file_path)
    csv_list = []
    for i in files:
        period = i.find('.')
        if i[period+1::] == 'csv':
            csv_list.append(i)
   
    return csv_list


def extract_csv_content(file_path:str):
   content = []

   with open(file_path, 'r') as file:
      csvreader = csv.reader(file)

      for row in csvreader:
         content.append(row)

   return content


def extract_name_set(images):

    names = [[], []]
    for i in range(len(images)):
        for j in range(len(images[i])):
            if j == 1 and 'paf' in images[i][j]:
                names[0].append('paf')
            if j == 2:
                names[1].append(images[i][j][41::])

    return names
    

def write_csv_file(file_dir, content):
    with open(file_dir, mode='w') as file:
        entry_writer = csv.writer(file)

        for i in content:
            entry_writer.writerow(i)


def generate_master_table(csv_list, parent_dir):
    master_table = []

    for i in csv_list:
        master_table.append(extract_csv_content(parent_dir + "\\" + i))

    return master_table


#dir where original csv's are found
cards_dir = "C:\\Users\\cock\\Desktop\\Pokemon-main\\Pokemon Card CSV's"

#dir where image names are found
image_dir = "C:\\Users\\cock\\Desktop\\Pkmn Card Image Names\\set_astral-radiance ‹ PkmnCards.csv"

#dir to put new csv's
target_dir = "C:\\Users\\cock\\Desktop\\Pokemon-main\\New Pokemon CSV's"

#get image names, pokemon csv names, and create master table of csv's
image_content = extract_csv_content(image_dir)
names = extract_name_set(image_content)
csv_list = get_pokemon_list(cards_dir)
master_table = generate_master_table(csv_list, cards_dir)
namecounter = 1

print(len(names[1]))
for i in csv_list:
    
    card_content = extract_csv_content(cards_dir + "\\" + i)

    #add '1' to filenames to make them different
    idx = i.find(".")
    i = i[:idx] + "1" + i[idx:]
    
    #insert names
    for j in card_content:
        if j:
            if j[0] != '' and j[0] != "Set":
                j.append(names[1][namecounter])
                namecounter+=1
    
    #open new csv file
    with open(target_dir + "\\" + i, mode='w') as target_file:
        entry_writer = csv.writer(target_file)

        #put new card content into new csv
        for j in card_content:
            entry_writer.writerow(j)

    #closer current writer and file
    target_file.close()
    
    
                

    