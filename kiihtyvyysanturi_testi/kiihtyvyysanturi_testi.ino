const int x_out = A1; /* connect x_out of module to A1 of UNO board */
const int y_out = A2; /* connect y_out of module to A2 of UNO board */
const int z_out = A3; /* connect z_out of module to A3 of UNO board */

void setup() {
  Serial.begin(9600); 
}

void loop() {
  int x_value, y_value, z_value, xyz_value; 

  x_value = analogRead(x_out); /* Digital value of voltage on x_out pin */ 
  y_value = analogRead(y_out); /* Digital value of voltage on y_out pin */ 
  z_value = analogRead(z_out); /* Digital value of voltage on z_out pin */
  //xyz_value = x_value + y_value + z_value;


  // print the sensor values:
  Serial.print(analogRead(x_value));
  
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(y_value));
  
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(z_value));

  // new line
  Serial.println();

  // delay before next reading:
  delay(10);
}
