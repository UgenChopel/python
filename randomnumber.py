import random
import csv
import time
while True:
    x = round(random.uniform(0.9, 1.09), 2)
    print(x)

    with open('/media/ugyen/Drive/ACS/libiec61850/01Practice_with_1Device/server_app/randomnumber.csv', 'w') as file:
        csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        file.write(str(x) + '\n')
    time.sleep(1)
