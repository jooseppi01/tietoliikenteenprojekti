import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import random

#haetaan data tietokannasta.
connection = mysql.connector.connect(host='172.20.241.9',
                                         database='measurements',
                                         user='dbaccess_ro',
                                         password='vsdjkvwselkvwe234wv234vsdfas')
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM rawdata WHERE groupid = 61")    
        data = mycursor.fetchall()

data = np.array(data)
data = data[::-1]
data = data[0:86, 5:8]
data = np.array(data, dtype=int)

#siivotaan dataa hieman.
data = data[(data[:, 0] <= 400) & (data[:, 1] <= 450) & (data[:, 2] <= 450)] 

maxValue = np.max(data)
minValue = np.min(data)


#luodaan 4 satunnaista keskikeskipistettä
keskipiste = []
for i in range(12):
        n = random.randint(minValue, maxValue)
        keskipiste.append(n)
keskipiste = np.reshape(keskipiste, (4, 3))


#luodaan aliohjelma joka laskee pisteiden euklidisen etäisyyden.
def distance(p1, p2):
        xdist = (p2[0] - p1[0])**2
        ydist = (p2[1] - p1[1])**2
        zdist = (p2[2] - p1[2])**2
        xyzdist = np.sqrt(xdist + ydist + zdist)    
        return xyzdist

#arvoja joita tarvitaan siihen että looppi kiertää kunnes counts arvo pysyy samana kerrasta toiseen.
counter = 0
iterations_without_change = 10 
iterations = True
whileloopcounter = 0
counts = np.zeros(4)         

#luodaan kmeans algoritmi.
while iterations == True:
        prev_counts = counts 
        counts = np.zeros(4)         
        centerPoinCumulativeSum = np.zeros((4, 3))
        distances = np.zeros(4)
        whileloopcounter += 1                    
   
        for i in range(len(data)):
                for a in range(4):
                        distances[a] = distance(data[i], keskipiste[a])
                counts[np.argmin(distances)] = counts[np.argmin(distances)] + 1
                centerPoinCumulativeSum[np.argmin(distances)] = centerPoinCumulativeSum[np.argmin(distances)] + data[i]

        for i in range(4):
                if(counts[i] == 0):
                        keskipiste[i] = random.randint(minValue, maxValue)
                else:
                        keskipiste[i] = centerPoinCumulativeSum[i] / counts[i]

        if counts[0] == prev_counts[0] and counts[1] == prev_counts[1] and counts[2] == prev_counts[2]:
                counter += 1
        else:
                counter = 0

        if counter == iterations_without_change:
                iterations = False
        
print('luupit:', whileloopcounter - 10)

#tallennetaan keskipisteet plottausta varten.
x = keskipiste[:, 0]
y = keskipiste[:, 1]
z = keskipiste[:, 2]

np.savetxt(r'C:\Users\Joona\Desktop\keskipisteet.h', keskipiste, fmt='%d', delimiter=',')

#alkuperäisen data pisteiden arvot plottausta varten.
x2 = data[0:, 0]
y2 = data[0:, 1]
z2 = data[0:, 2]

#luodaan 3d plottaus lopputuloksesta.
plt.figure(1)
plt.subplot(1,1,1, projection= '3d')
plt.plot(x, y, z, 'r*')
plt.plot(x2, y2, z2, 'b.')
#plt.pause(0.03)
plt.show()
