# Tietoliikenteenprojekti syksy 2022, Kaikkonen Joona TVT21SPL


Projektin aihe:
Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. Reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan. 

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen.


## Arkkitehtuurikuva
<picture>
  <img alt="Shows an picture of arkkitehtuuri." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/1483fb82f5a4360c1cb069b78ebe5500e72e1c45/pictures/arkkitehtuuri.png"
  width=50% height=50%>
</picture>

---------------------------------------------------------------------------------------------------------
 ##### Aluksi testailua testidatalla, jossa data näkyy sinisinä palloina ja algortimin laskemat keskipisteet näkyy punaisina * merkkeinä. Algoritmi on toteutettu siten että k-means = 4, eli data luokitellaa neljään eri joukkoon. 
<picture>
  <img alt="Shows an picture of kmeans_testidata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/main/pictures/testidata_kmeans.png?raw=true"
     width=50% height=50%>
</picture>

----------------------------------------------------------------------------------------------------------
##### Tässä sama homma, mutta omalla datalla. Siniset pallot ovat dataa kiihtyvyysanturilta, punaiset * ovat algoritmin laskemat keskipisteet. 
<picture>
  <img alt="Shows an picture of kmeans_omadata." src="https://github.com/jooseppi01/tietoliikenteenprojekti/blob/main/pictures/omadata_kmeans.png?raw=true"
  width=50% height=50%>
</picture>


