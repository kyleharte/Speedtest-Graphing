# Sources
# Big thanks to https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/ for helping me understand how to plot graphs
import matplotlib.pyplot as plt
import csv
import datetime

time = []
download = []
upload = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        time.append(int(row[0]))
        download.append(int(row[1]))
        upload.append(int(row[2]))

plt.plot(time,download, label='Download speeds')
plt.plot(time, upload, label='Upload speeds')
plt.xlabel("Time 24/HR")
plt.ylabel("Speed Mbit/s")
plt.title("Internet Speeds")
plt.legend()
plt.show()
