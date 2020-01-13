import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import csv

a = np.array([])
b = np.array([])

with open('a.csv', newline='') as csvfilea:
    spamreader = csv.reader(csvfilea, delimiter=' ', quotechar='|')
    for row in spamreader:
        a = np.append(a, row)

with open('b.csv', newline='') as csvfileb:
    spamreader = csv.reader(csvfileb, delimiter=' ', quotechar='|')
    for row in spamreader:
        b = np.append(b, row)


t = np.linspace(0, 1, 160000)
y = np.sin(50*2*np.pi*t) + 0.5*np.sin(100*2*np.pi*t)+0.25*np.sin(150*2*np.pi*t) + 0.125*np.sin(200*2*np.pi*t) + 0.1*np.sin(2*np.pi*20000*t)

##print(a,b)

yf = signal.filtfilt(b,a,t)
##
##plt.plot(t,y)
##plt.show()
