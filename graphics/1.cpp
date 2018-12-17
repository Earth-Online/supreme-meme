#include <iostream>
#include <math.h>
#include <windows.h>

int main()
{
	HWND hConsole = GetConsoleWindow();
	HDC hDC = GetDC(hConsole);

	HPEN hPen = CreatePen(PS_SOLID, 1, RGB(200, 256,256));
	HBRUSH hbr =  CreateSolidBrush(RGB(255,255,255));

	SelectObject(hDC, hPen);
	MoveToEx(hDC,250, 250, NULL);
	LineTo(hDC,10,20);
	LineTo(hDC,10,200);

	SelectObject(hDC, hbr);
	RECT rect={10,10,100,100};
	FillRect(hDC,&rect,hbr);

	DeleteObject(hPen);
	DeleteObject(hbr);

	ReleaseDC(hConsole, hDC);
	cin.ignore();
	return 0;
}