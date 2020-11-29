# reading from value.csv, compare with the set limits, and then writing it to writefile.csv as well

import csv
from time import time, sleep

while True:     #for continuously fetching the data

    def readLines():
        with open('value.csv', 'r') as data:
            reader = csv.reader(data)
            row = list(reader)
            for x in row:
                for y in x:
                    print("the value of 'y' is", y)
                    if (float(y)<=0.95):
                        print("suspend EV")
                        print('wait...')
                        break

                    if (float(y)>=1.05):
                        print('Suspend ESS')

                    else:
                        print('continue')

            with open('writefile.csv', 'a') as file:
                csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                file.write(y + "\n")    #reading the float value of 'y' with newline

    sleep(2)    #in seconds
    readLines()
