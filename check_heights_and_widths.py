# script to create list of sitenames to check heights and withs in db

def clear_sitenames():
    #open sites.txt and read it
    f = open('sites.txt', 'r')
    reader = f.read().splitlines()

    # open/create list.txt and write on it
    clean = open('list.txt', 'w')

    for line in reader:
        clean.write(f"'{line}', ")



############------------ DRIVER CODE ------------############
clear_sitenames()