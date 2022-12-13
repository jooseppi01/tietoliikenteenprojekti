#include "C:\TVT21SPL-2-VUOSI\Tietoliikenteen projekti\tietoliikenteenprojekti\keskipisteet.h"

int x; //X-akselin lukema
int y; //Y-akselin lukema
int z; //Z-akselin lukema

//Keskipisteet

//ylös
int x1 = kp[0][0];
int y1 = kp[0][1];
int z1 = kp[0][2];

//alas
int x2 = kp[1][0];
int y2 = kp[1][1];
int z2 = kp[1][2];

//vasen
int x3 = kp[2][0];
int y3 = kp[2][1];
int z3 = kp[2][2];

//oikee
int x4 = kp[3][0];
int y4 = kp[3][1];
int z4 = kp[3][2];

double distances(int p1x, int p1y, int p1z, int p2x, int p2y, int p2z){
  int xdist = pow(p2x - p1x, 2);  // pow = (luku, potenssi)
  int ydist = pow(p2y - p1y, 2);
  int zdist = pow(p2z - p1z, 2);
  double distance = sqrt(xdist + ydist + zdist);    
  return distance;
}

void setup() {
  Serial.begin (9600);
}

void loop() {

  Serial.println("asento 1, 2, 3 vai 4?");
  while (Serial.available() == 0) {
  }
  int asento = Serial.parseInt();

  Serial.println("kuinka monta mittausta?");
  while (Serial.available() == 0) {
  }
  int luku = Serial.parseInt(); 
  
   for (int i = 0; i < luku; i++) {
    //Lue akselit
    x = analogRead(A1);
    y = analogRead(A2);
    z = analogRead(A3);
    
    //Lasketaan etäisyydet keskipisteisiin
    int d1 = distances(x, y, z, x1, y1, z1);
    int d2 = distances(x, y, z, x2, y2, z2);
    int d3 = distances(x, y, z, x3, y3, z3);
    int d4 = distances(x, y, z, x4, y4, z4);
    
    //Vertaa etäisyyksiä ja määritä luokka 
    if (d1 < d2 && d1 < d3 && d1 < d4) {
      Serial.print (asento);
      Serial.print (" 1");
      Serial.print("\n");
    }
    else if (d2 < d1 && d2 < d3 && d2 < d4) {
      Serial.print (asento);
      Serial.print (" 2");
      Serial.print("\n");
    }
    else if (d3 < d1 && d3 < d2 && d3 < d4) {
      Serial.print (asento);
      Serial.print (" 3");
      Serial.print("\n");
    }
    else if (d4 < d1 && d4 < d2 && d4 < d3) {
      Serial.print (asento);
      Serial.print (" 4");
      Serial.print("\n");    }
      delay(250);
  }
  
 }


  /*
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 3; j++) {
      // print the value of kp[i][j] followed by a tab
      Serial.print(kp[i][j]);
      Serial.print("\t");
    }
    // after printing the values in the inner loop, print a newline
    Serial.println();
  }
  delay(1000);  // delay for 1 second
  */ 
