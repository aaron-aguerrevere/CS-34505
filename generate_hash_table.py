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

    reader = csv.reader(csvfile, skipinitialspace=True)

    pass

    
def generate_mobile_hash_table():
    '''
    var gannettHashTable = {
    'alicetx': 'tx-alice-mobile-C6683',
    };
    '''

    csvfile = open('gh.csv', newline='')

    reader = csv.reader(csvfile, skipinitialspace=True)

    pass

############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    generate_desktop_hash_table()
    generate_mobile_hash_table()
