import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import random
from numpy import linalg as LA

data = np.loadtxt("putty.log", dtype=int)
data = np.array([data])
data = data.reshape(40,3)

maxValue = np.max(data)
minValue = np.min(data)
print(data)

#luodaan 4 satunnaista keskikeskipistettä
keskipiste = []
for i in range(12):
        n = random.randint(minValue, maxValue)
        keskipiste.append(n)
keskipiste = np.reshape(keskipiste, (4, 3))
print(keskipiste)


#luodaan aliohjelma joka laskee pisteiden euklidisen etäisyyden.
def distance(p1, p2):
        xdist = (p2[0] - p1[0])**2
        ydist = (p2[1] - p1[1])**2
        zdist = (p2[2] - p1[2])**2
        xyzdist = np.sqrt(xdist + ydist + zdist)    
        return xyzdist

#alkuperäisen data pisteiden arvot.
x2 = data[0:, 0]
y2 = data[0:, 1]
z2 = data[0:, 2]

#def kmeans():
centerPoinCumulativeSum = np.zeros([4,3])
counts = np.zeros(4)

for m in range(50):   
        counts = np.zeros(4) 
        centerPoinCumulativeSum = np.zeros((4, 3))
        distances = np.zeros(4)    
        for i in range(40):               
                for a in range(4):
                        distances[a] = distance(data[i], keskipiste[a])
                counts[np.argmin(distances)] = counts[np.argmin(distances)] + 1
                centerPoinCumulativeSum[np.argmin(distances)] = centerPoinCumulativeSum[np.argmin(distances)] + data[i]

        for i in range(4):
                if(counts[i] == 0):
                        keskipiste[i] = random.randint(minValue, maxValue)
                else:
                        keskipiste[i] = centerPoinCumulativeSum[i] / counts[i]


        #pisteiden keskipisteet.
        x = keskipiste[:, 0]
        y = keskipiste[:, 1]
        z = keskipiste[:, 2]
        print('counts: ', counts)
        
        #luodaan 3d plottaus.
        plt.figure(1)
        plt.subplot(1,1,1, projection= '3d')
        plt.plot(x, y, z, 'r*')
        plt.plot(x2, y2, z2, 'b.')
        plt.pause(0.03)

plt.show()
