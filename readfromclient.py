import csv
from time import time, sleep

while True:  # for continuously fetching the data

    def readLines():
        with open('/media/ugyen/Drive/ACS/libiec61850/01Practice_with_1Device/client_app1/value.csv', 'r') as data:
            reader = csv.reader(data)
            row = list(reader)
            for x in row:
                for y in x:
                    print("the value of 'y' is", y)

                    if float(y) <= 0.95:
                        print("Put ON ESS")
                        sleep(5)

                        if float(y) <= 0.95:
                            print("suspend EV1")
                            print('wait...')
                            sleep(2)
                            break

                    if float(y) >= 1.05:
                        print('Suspend ESS\n')

                    else:
                        print('wonderful! continue\n')

            with open('file1.csv', 'a') as file:
                csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                file.write(y + "\n")  # reading the floating value of 'y' and giving new line


    sleep(2)  # in seconds
    readLines()
