#include <Arduino.h>
#include <vector>
#include <string>
#include "utils.h"
#include <functional>
using namespace std;
void serial1Init() 
{
    Serial1.begin(115200, SERIAL_8N1, 16, 17);
}
void serial1Read(function<void(string, vector<int> )>callback)  
{
    //Serial.println("jajco1");
    if (Serial1.available() > 0)
    {

        String result = Serial1.readStringUntil('\n');

        vector<string> inputString = split(string(result.c_str()), ' ');

        vector<string> subvector(inputString.begin() + 1, inputString.end());

        vector<int> intSubvector;

        for (string &i:subvector)
        {

            intSubvector.push_back(atoi(i.c_str()));
        }
        callback (inputString[0], intSubvector);
    }
}

