import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import csv

##z = []
##p = []
##k = []
sos = []


##with open('z.csv', newline='') as csvfilea:
##    spamreader = csv.reader(csvfilea, delimiter=',', quotechar='|')
##    for row in spamreader:
##        z = row
##
##with open('p.csv', newline='') as csvfileb:
##    spamreader = csv.reader(csvfileb, delimiter=',', quotechar='|')
##    for row in spamreader:
##        p = row
##
##with open('k.csv', newline='') as csvfileb:
##    spamreader = csv.reader(csvfileb, delimiter=',', quotechar='|')
##    for row in spamreader:
##        k = row

##with open('sos.csv', newline='') as csvfileb:
##    spamreader = csv.reader(csvfileb, delimiter=',', quotechar='|')
##    for row in spamreader:
##        sos = row
sos = signal.iirfilter(13, 0.0006875, btype='lowpass', ftype='butter', output = 'sos')
##sosM = np.loadtxt(open("sos.csv", "rb"), delimiter=",")
        
##print(sos)
##print(sosM)
##z_float = list(map(float, z))
##p_float = list(map(float, p))
##k_float = list(map(float, k))

t = np.linspace(0, 1, 160000)
fifty = np.sin(50*2*np.pi*t)
y = np.sin(50*2*np.pi*t) + 0.5*np.sin(100*2*np.pi*t)+0.25*np.sin(150*2*np.pi*t) + 0.125*np.sin(200*2*np.pi*t) + 0.1*np.sin(2*np.pi*20000*t)

##print(type(sos))

yf = signal.sosfiltfilt(sos, y)
print(yf)

plt.plot(t,y)
plt.plot(t,fifty)
plt.plot(t,yf)
plt.show()

##w, h = signal.sosfreqz(sos, worN=1500)
##
##plt.subplot(2, 1, 1)
##db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
##plt.plot(w/np.pi, db)
##plt.ylim(-75, 5)
##plt.grid(True)
##plt.yticks([0, -20, -40, -60])
##plt.ylabel('Gain [dB]')
##plt.title('Frequency Response')
##plt.subplot(2, 1, 2)
##plt.plot(w/np.pi, np.angle(h))
##plt.grid(True)
##plt.yticks([-np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi],
##           [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
##plt.ylabel('Phase [rad]')
##plt.xlabel('Normalized frequency (1.0 = Nyquist)')
##plt.show()

