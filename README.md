# Tietoliikenteenprojekti syksy 2022, Kaikkonen Joona TVT21SPL


Projektin aihe:
Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. Reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan. 

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen.

Projektiin sisältyi myös hieman linux askarteluja esim. php sriptin tekeminen ymsyms. Löytyy kansioista linux_jutut.


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
- Kuva tietokannasta joka sisältää:
id,
timestamp,
groupid,
from_mac,
to_mac,
sensorvalue_a,
sensorvalue_b,
sensorvalue_c,
sensorvalue_d,
sensorvalue_e,
sensorvalue_f 

<picture>
  <img alt="Shows an picture of setup." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/b24c597ebce4b326edac50f16f48a4f7d9c43837/pictures/tietokanta.png"
  width=50% height=50%>
</picture>

---

k-means algoritmi pythonilla. Algoritmia opetetaan niin kauan, kunnes keskipisteet eivät enää muutu.
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


- Aluksi testailua testidatalla, jotta voidaan varmistua algoritmin toimivuudesta. Vaaleat ympyrät kuvaavat 40 pisteen testidataa, mustat rastit kuvaava opetetun algoritmin lopulliset clusterit. 4-means ->
<picture>
  <img alt="Shows an picture of kmeans_testidata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/main/pictures/testidata_kmeans.png?raw=true"
     width=50% height=50%>
</picture>

---
- Seuraavaksi haetaan oman kiihtyvyysanturin mittaukset mysql tietokannasta ja luokitellaaan se kmeans algoritmilla 4 luokkaan. Jokaisella luokalla on oma värinsä. 
```
import mysql.connector
connection = mysql.connector.connect(host='172.20.241.9',
                                         database='measurements',
                                         user='dbaccess_ro',
                                         password='vsdjkvwselkvwe234wv234vsdfas')
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM rawdata WHERE groupid = 61")       
        myresult = mycursor.fetchall()
```

<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/41f3a2663d1027b56d87ff6eff95de8e1c77ced4/pictures/kmeans_vareilla.png"
  width=50% height=50%>
</picture>

Python ohjelman lopuksi tallennetaan keskipisteet tiedostoon keskipisteet.h ja tämä tiedosto sitten incluudataan arduinolle.

---


```
void loop() {

  Serial.println("asento 1, 2, 3 vai 4?");
  while (Serial.available() == 0) {
  }
  int asento = Serial.parseInt();

  Serial.println("kuinka monta mittausta?");
  while (Serial.available() == 0) {
  }
  int luku = Serial.parseInt(); 
```

- Vasemmat arvo on se asento missä kiihtyvyysanturi on ja oikeat arvot ovat algortimin antamat. Tehdään 20 mittausta jokaisesta asennosta.  
<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/b24c597ebce4b326edac50f16f48a4f7d9c43837/pictures/arduinoserialport.png"
  width=30% height=30%>
</picture>

---

- Tehdään confusion matrix, jokaisesta kiihtyvyys anturin asennosta on tehty 20 mittausta eli yhteensä 80 mittausta. Aika tarkasti saadaan oikeat arvot vaikka anturia vähän heiluttelikin mittausten aikana. 
```
#data tallennettu arduinolta putty2.log nimiseen tiedostoon.
data = np.loadtxt("putty2.log")
y_test = data[:, 0]
y_pred = data[:, 1]

kk = confusion_matrix(y_test, y_pred)
display3 = metrics.ConfusionMatrixDisplay(confusion_matrix = kk, display_labels = ['p1', 'p2', 'p3', 'p4'])
display3.plot()
```

<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/b24c597ebce4b326edac50f16f48a4f7d9c43837/pictures/cofusionmatrix.png"
  width=50% height=50%>
</picture>
