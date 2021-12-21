#include <wiringPi.h>
#define LED_PIN 4
int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_PIN, OUTPUT) ;
  for (int i=0; i<5; i++)
  {
    digitalWrite (LED_PIN, HIGH) ; delay (500) ;
    digitalWrite (LED_PIN,  LOW) ; delay (500) ;
  }
  return 0 ;
}