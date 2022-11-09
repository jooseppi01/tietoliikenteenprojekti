#include "accelerator.h"
#include <arduino.h>

Accelerator::Accelerator()
{
   Serial.println("Accelerator created!");
}


Accelerator::~Accelerator()
{
   Serial.println("Accelerator deleted!");
}


void Accelerator::makeMeasurement()
{
  m.x = analogRead(A1); 
  m.y = analogRead(A2); 
  m.z = analogRead(A3);

/*
  Serial.print(analogRead(x));
  
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(y));
  
  Serial.print("\t");
  Serial.print(analogRead(z));

  // new line
  Serial.println();

  // delay before next reading:
  delay(10);
  */
}


Measurement Accelerator::getMeasurement()
{
  return m;
}

void Accelerator::tulostus()
{
            Serial.println(m.x);
            Serial.println(m.y);
            Serial.println(m.z);
}
