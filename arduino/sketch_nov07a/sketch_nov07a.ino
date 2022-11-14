#include "messaging.h"
#include "accelerator.h"

void setup() 
{
  Serial.begin(9600);
}

void loop()
{
  Accelerator Aobject;
  Messaging Mobject;

  Serial.println("Give number how many measurements");
  int NumberOfMeasurements = 0;
  while(NumberOfMeasurements == 0)
  {
    if(Serial.available()>0)
    {
       NumberOfMeasurements = Serial.parseInt();
                
       for (int i=0; i < NumberOfMeasurements; i++){
          Aobject.makeMeasurement();
          Measurement m = Aobject.getMeasurement();
          uint8_t id = i;
          uint8_t flags = 0xff;
          Mobject.createMessage(m);
          if(Mobject.sendMessage(id,flags))
          {
            Serial.println("Successfull transmission");
          }
          else
          {
            Serial.println("Transmission fails");
          }
          if(Mobject.receiveACK())
          {
            Serial.println("Receiver got message, going to next measurement");
          }
          else
          {
            Serial.println("Receiver didnt get the message, need to resend it");
            i--;
          }

          }      
    }
  }

}
