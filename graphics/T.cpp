#include<windows.h>
#include<iostream>
#include <cmath>

using namespace std;

#define PI 3.14

int main() 
{
    //Get a console handle
    HWND myconsole = GetConsoleWindow();
    //Get a handle to device context
    HDC mydc = GetDC(myconsole);

	Rectangle(mydc,50,50,200,200);

    ReleaseDC(myconsole, mydc);
    cin.ignore();
    return 0;
}