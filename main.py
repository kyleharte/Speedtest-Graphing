#*                    Imports                          *#
import speedtest
import datetime
import csv
import pprint
import csv
#*                    Date                             *#
date = datetime.datetime.now()
#*                    Speedtest                        *#
s = speedtest.Speedtest()
download = round(s.download() / 1e+6)
upload = round(s.upload() / 1e+6)
results = [date.strftime("%Y-%m-%d"), download, upload]

#*                    Prints                           *#

pprint.pprint(results)
#*                    CSV                              *#
with open(date.strftime("%Y-%m-%d") + '.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(results)

csvFile.close()
