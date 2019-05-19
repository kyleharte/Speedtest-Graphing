# Sources
# Big thanks to https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/ for helping me understand how to plot graphs
import matplotlib.pyplot as plt
import csv
import datetime

date = datetime.datetime.now()

time = []
download = []
upload = []

with open(date.strftime("%Y-%m-%d")+'.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        time.append(row[0])
        download.append(int(row[1]))
        upload.append(int(row[2]))

plt.plot(time,download, label='Download speeds')
plt.plot(time, upload, label='Upload speeds')
plt.xlabel("Time 24/HR")
plt.ylabel("Speed Mbit/s")
plt.title("Internet Speeds")
plt.legend()
plt.savefig(date.strftime("%Y-%m-%d") + '.pdf')
