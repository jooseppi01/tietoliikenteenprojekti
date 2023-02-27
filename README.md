# Tietoliikenteenprojekti syksy 2022, Kaikkonen Joona TVT21SPL


Projektin aihe:
Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. Reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan. 

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen. 

Valmiin algoritmin on tarkoitus tunnistaa missä asennossa anturi on milloinkin.

Projektiin sisältyi myös hieman linux askarteluja -> php sriptin tekeminen ja firewall. Löytyy kansioista linux_jutut.


## Arkkitehtuurikuva
<picture>
  <img alt="Shows an picture of arkkitehtuuri." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/1483fb82f5a4360c1cb069b78ebe5500e72e1c45/pictures/arkkitehtuuri.png"
  width=50% height=50%>
</picture>

---
- Kytketään koekytkentälevyyn kiihtyvyysanturi, lähetin ja vastaanotin.
<picture>
  <img alt="Shows an picture of setup." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/841a0662e337c5b6c53a49d1fb09349b78cb665e/pictures/setupkuva.jpg"
  width=50% height=50%>
</picture>

- luetaan anturin data ja lähetetään se tietokantaan käyttäen highbyteä ja lowbyteä: 
```
void Accelerator::makeMeasurement()
{ 
  m.x = analogRead(A1); 
  m.y = analogRead(A2); 
  m.z = analogRead(A3);
}
```
```
void Messaging::createMessage(Measurement m)
{
  data[0]=highByte(m.x);
  data[1]=lowByte(m.x);

  data[2]=highByte(m.y);
  data[3]=lowByte(m.y);

  data[4]=highByte(m.z);
  data[5]=lowByte(m.z);
  messageLength = 6;
}
```


---

k-means algoritmi pythonilla. Algoritmia opetetaan niin kauan, kunnes keskipisteet eivät enää muutu.
 
 Aluksi arvottiin satunnaiset keskipisteet. Tässä tapaksessa 4. 
1. lasketaan jokaisen datapisteen etäisyys jokaiseen keskipisteeseen.
2. Jokaiselle datapisteelle annetaan oma keskipiste, sen perusteella mihin sillä on lyhin matka. Tässä vaiheessa on muodostunut ensimmäiset klusterit.
3. Sitten jokaiselle klusterille lasketaan uudet keskipisteet.
```
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
```



---
- Seuraavaksi haetaan oman kiihtyvyysanturin mittaukset mysql tietokannasta ja luokitellaaan se kmeans algoritmilla 4 luokkaan. Jokaisella luokalla on oma värinsä. 


<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/41f3a2663d1027b56d87ff6eff95de8e1c77ced4/pictures/kmeans_vareilla.png"
  width=60% height=60%>
</picture>


---

- Tehdään confusion matrix. Jokaisesta kiihtyvyys anturin asennosta on tehty 100 mittausta eli yhteensä 400 mittausta. Aika tarkasti saadaan oikeat arvot vaikka anturia vähän heiluttelikin mittausten aikana. 
```
#data tallennettu arduinolta putty3.log nimiseen tiedostoon.
data = np.loadtxt("putty3.log")

y_test = data[:, 0]
y_pred = data[:, 1]

kk = confusion_matrix(y_test, y_pred)
display3 = metrics.ConfusionMatrixDisplay(confusion_matrix = kk, display_labels = ['p1', 'p2', 'p3', 'p4'])
display3.plot()
```

<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/27a32628d76fc6075fb20d3f9df9cdb4ae9cbeb3/pictures/confusionmatrix2.png"
  width=50% height=50%>
</picture>

<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/27a32628d76fc6075fb20d3f9df9cdb4ae9cbeb3/pictures/score.png"
  width=50% height=50%>
</picture>
