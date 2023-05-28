using namespace std;
#include <Arduino.h>
#include <Wire.h>
#define HAL1_ADDRESS 0x36
#define HAL_ANGLE_REGISTER 0x0E


void halInit()
{
    Wire.begin();
    Wire.setClock(100000);

}
double readAngle()
{
    Wire.beginTransmission(HAL1_ADDRESS);
    Wire.write(HAL_ANGLE_REGISTER);
    Wire.endTransmission();
    Wire.requestFrom(HAL1_ADDRESS, 2);

    if (Wire.available() == 2)
    {

        byte msb = Wire.read();
        byte lsb = Wire.read();

        int angleRaw = ((msb << 8) | lsb) & 0x0FFF;
        double angle = ((double)angleRaw / 0x0FFF) * 360;
        return angle;
    }

    return -1;
}