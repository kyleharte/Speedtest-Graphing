import speedtest
import datetime
import csv
import pprint

results = {}
#*                                                     *#
date = datetime.datetime.now()
#*                    Speedtest                        *#
s = speedtest.Speedtest()
download = s.download()
upload = s.upload()
ping = s.get_best_server()
downmbits = download / 1e+6
results["download"] = download
results["ping"] = ping
results["upload"] = upload

#*                    Prints                           *#

pprint.pprint(results)
print(date.strftime("%Y-%m-%d"))

print(downmbits)
print(round(downmbits))
