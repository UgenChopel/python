import time
import csv
from time import time, sleep

while (1):  # for continuously fetching the data

    ## reading the values
    with open( '/media/ugyen/Drive/ACS/libiec61850/01Practice_with_1Device/client_app1/value1.csv', 'r' ) as values:
        data = csv.reader( values, delimiter=" " )
        for row in data:
            print( row[0], row[1], row[2], row[3], row[4])  # To print the values read

    ## writing the values
    with open( 'file1.csv', 'a' ) as file:
        csv.writer( file, delimiter=',', quoting=csv.QUOTE_MINIMAL )
        file.write( row[0]+ row[1] + row[2] + row[3] + row[4] + "\n" )  # reading the floating value of 'y' and giving new line

    ## checking the limit violations of voltage and taking necessary decisions
    if float( row[0] ) <= 0.95:

        if float( row[1] ) == 0:
            print( "Put ON ESS" )
            sleep( 1 )

        elif float( row[2] ) != 0:
            print( 'Suspend EV1' )
            sleep( 1 )

        elif float( row[3] ) != 0:
            print( 'Suspend EV2' )
            sleep( 1 )

        elif float( row[4] ) != 0:
            print( 'Suspend EV3' )
            sleep( 1 )

    else:
        print( "wonderful" )

    sleep( 1 )
