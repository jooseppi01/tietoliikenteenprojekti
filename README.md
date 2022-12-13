# Tietoliikenteenprojekti syksy 2022, Kaikkonen Joona TVT21SPL


Projektin aihe:
Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. Reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan. 

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen.


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
- Seuraavaksi haetaan oman kiihtyvyysanturin mittaukset mysql tietokannasta ja opetetaan se kmeans algoritmilla. Vihreät ympyrät ovat dataa, rastit ovat algoritmin laskemat clusterit. 4-means->
<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/main/pictures/omadata_kmeans.png?raw=true"
  width=50% height=50%>
</picture>


