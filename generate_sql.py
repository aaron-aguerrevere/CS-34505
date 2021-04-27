# script to generate sql that will update header and footer urls in db
############------------ IMPORTS ------------############
import csv

############------------ FUNCTIONS ------------############
def generate_sql():
    '''
    UPDATE dbo.tblaffiliatesettings
    SET headerurl = <headerurl>,
        footerurl = <footerurl>,
        artworkdeliveryoption = 3
    WHERE affiliatesitename = <sitename>
    '''
    # target_columns Domain, Paper, Header, Footer

    csvfile = open('gh.csv', newline='')

    reader = csv.reader(csvfile, skipinitialspace=True)

    with open('sql_scripts.cvs', 'w', newline='', encoding='utf-8') as result:
    
        writer = csv.writer(result, dialect='excel')

        for i, row in enumerate(reader):
            if i == 0:
                continue
            else:
                writer.writerow(
                    [f"UPDATE dbo.tblaffiliatesettings\n\
                    SET headerurl = '{row[5]}',\n\
                        footerurl = '{row[6]}',\n\
                        artworkdeliveryoption = 3\n\
                    WHERE affiliatesitename = '{row[0]}'"]
                )


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    generate_sql()
