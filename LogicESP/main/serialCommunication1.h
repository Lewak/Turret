#include <Arduino.h>
#include <vector>
#include <string>
#include "utils.h"
#include <functional>
void serial1Init();
void serial1Read(function<void(string, vector<int> )>callback);
