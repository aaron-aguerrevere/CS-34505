# script to generate hashtable that will populate desktop & mobile ads
############------------ IMPORTS ------------############
import csv

############------------ FUNCTIONS ------------############
def generate_desktop_hash_table():
    '''
    var gannettHashTable = {
    'alicetx': 'tx-alice-C6683',
    };
    '''

    csvfile = open('gh.csv', newline='')

    reader = csv.reader(csvfile)

    desktop_hash_table = open('desktop.txt', 'w')

    desktop_hash_table.write('var gannettHashTable = {\n')

    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            desktop_hash_table.write(f'{row[0]}: {row[7]},\n')

    desktop_hash_table.write('};')
    



    
def generate_mobile_hash_table():
    '''
    var gannettHashTable = {
    'alicetx': 'tx-alice-mobile-C6683',
    };
    '''

    csvfile = open('gh.csv', newline='')

    reader = csv.reader(csvfile)

    mobile_hash_table = open('mobile.txt', 'w')

    mobile_hash_table.write('var gannettHashTable = {\n')

    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            mobile_hash_table.write(f'{row[0]}: {row[8]},\n')

    mobile_hash_table.write('};')


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # generate_desktop_hash_table()
    generate_mobile_hash_table()
