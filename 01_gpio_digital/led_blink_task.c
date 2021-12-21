#include <wiringPi.h>
#define LED_PIN1 3
#define LED_PIN2 4
#define LED_PIN3 17
int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_PIN1, OUTPUT) ;
  pinMode (LED_PIN2, OUTPUT) ;
  pinMode (LED_PIN3, OUTPUT) ;
  for (int i=0; i<5; i++)
  {
    digitalWrite (LED_PIN1, HIGH) ; delay (500) ;
    digitalWrite (LED_PIN1,  LOW) ;
     digitalWrite (LED_PIN2, HIGH) ; delay (500) ;
    digitalWrite (LED_PIN2,  LOW) ;
    digitalWrite (LED_PIN3, HIGH) ; delay (500) ;
    digitalWrite (LED_PIN3,  LOW) ;
  }
  return 0 ;
}