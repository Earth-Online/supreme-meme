#include <iostream>
#include <windows.h>

using namespace std;

void gotoxy(int x, int y)
{
	COORD pos = {x,y};
	HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleCursorPosition(hOut, pos);
};
int main() 
{
	HWND myconsole = GetConsoleWindow();
	HDC mydc = GetDC(myconsole);

	HBRUSH hbr = CreateSolidBrush(RGB(255,255,255));
	SelectObject(mydc, hbr);

	RECT rect={50,50,400,400};
	FrameRect(mydc,&rect,hbr);

	RECT rect1={54,54,396,396};
	FrameRect(mydc,&rect1,hbr);

	gotoxy(4,1);
	cout<<"form1";

	DeleteObject(hbr);
	ReleaseDC(myconsole, mydc);
	cin.ignore();
	return 0;
};