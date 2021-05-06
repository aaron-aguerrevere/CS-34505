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
    desktop = dict()

    csvfile = open('gh.csv', newline='')

    reader = csv.reader(csvfile)

    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            desktop[row[0]] = row[7]

    print(desktop)
    



    
def generate_mobile_hash_table():
    '''
    var gannettHashTable = {
    'alicetx': 'tx-alice-mobile-C6683',
    };
    '''

    mobile = dict()

    csvfile = open('gh.csv', newline='')

    reader = csv.reader(csvfile)

    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            mobile[row[0]] = row[8]

    print(mobile)

############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # generate_desktop_hash_table()
    generate_mobile_hash_table()
