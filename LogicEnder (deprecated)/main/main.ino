#include <AccelStepper.h>
#include <MultiStepper.h>


#include "pins_arduino.h"
#define acceleration 2000
#define deceleration 1000
#define max_speed 6000
#define full_rotation 3200
#define first_delay 80
int actual_speed = 1000;
int target_speed = 80000;

void setup() 
{
    float acc_dec_ratio = (acceleration/deceleration);

    Serial.begin(9600);
    pinMode(XYEENABLE, OUTPUT);
    pinMode(X_DIR, OUTPUT);
    pinMode(X_STEP, OUTPUT);
    pinMode(Y_DIR, OUTPUT);
    pinMode(Y_STEP, OUTPUT);

    digitalWrite(XYEENABLE, LOW);   
    digitalWrite(X_DIR, LOW);
    digitalWrite(X_STEP, HIGH);
    digitalWrite(Y_DIR, LOW);
    digitalWrite(Y_STEP, HIGH);
    ramp(1,80000);

}

void loop() 
{
    // delay();
    // PORTD |= B10000000;
    // PORTC |= B01000000;
    // // digitalWrite(X_STEP, LOW);
    // // digitalWrite(Y_STEP, LOW);
    // delayMicroseconds(15);
    // PORTD &= B01111111;
    // PORTC &= B10000000;
    delayMicroseconds(15);

    // digitalWrite(X_STEP, HIGH);
    // digitalWrite(Y_STEP, HIGH);
}


void ramp(int actual_speed, int target_speed){

    int ramp_count = abs(target_speed - actual_speed)/10;
    int final_delay = 1000000 / target_speed;
    int actual_delay = 1000000  / actual_speed;
    const int target_spedded = 80000;
    const int start = 80;
    const int end = 1000000 / 80000;
    const int diff = (first_delay - end);

    for(float i = 0; i < 1; i+=0.00001)
    {
        delayMicroseconds(first_delay - i * diff);
        PORTD |= B10000000;
        PORTC |= B01000000;
        delayMicroseconds(first_delay - i * diff);
        PORTD &= B01111111;
        PORTC &= B10000000;
    }

}