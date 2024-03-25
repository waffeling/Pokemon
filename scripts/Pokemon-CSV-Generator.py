import os
import csv

def get_pokemon():
   files = os.listdir()
   for i in files:
      period = i.find('.')
      if i[period+1::] == 'txt':
        return i

def open_file_with_getcwd(file_name):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   cwd = os.getcwd()

   if script_dir != cwd:
      print("Warning: The script is not running from its own directory.")
      print(f"Script Directory: {script_dir}")
      print(f"Current Working Directory: {cwd}")

   file_path = os.path.join(script_dir, file_name)
   
   with open(file_path, 'r') as file:
      content = file.read()

   return content

def table_maker(data):

    table = [['Set', 'No.', 'Name', 'Stage', 'Type', 'Rarity', 'Sale Status']]

    key = ['{G}', '{F}', '{E}', '{M}', '{N}', '{M}', '{P}', '{W}', '{L}', '{R}', '{D}', '{C}']

    newl = 0
    oldl = 0
    while newl != -1:
        entry = []
        for i in range(7):
            newl = data.find('\n', oldl+1)

            if i == 4 and data[oldl+1:oldl+4] not in key:
               entry.append('')

            else:
                entry.append(data[oldl+1:newl])
                oldl = newl

            
        table.append(entry) 

    return table

filename = get_pokemon()
data = open_file_with_getcwd(filename)
table = table_maker(data)

filename = filename.rstrip('.txt')
print(filename)

with open('{fname}.csv'.format(fname = filename), mode='w') as employee_file:
    entry_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in table:
        entry_writer.writerow(i)





