
#include <vector>
#include <string>
#include <sstream>
using namespace std;

std::vector<string> split(const string &s, char delim)
{
    vector<string> tokens;
    stringstream ss(s);
    string item;
    while (std::getline(ss, item, delim))
    {
        tokens.push_back(item);
    }
    return tokens;
}
int clampValue (int value, int min, int max)
{  
    return value>max ? max : value<min ? min : value;
}