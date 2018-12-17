#include <stdio.h>
#include <windows.h>
//gcc -o core.dll -shared core.c
#define uint unsigned int

struct COORD
{
	short x;
	short y;
};

struct SMALL_RECT
{
	short Left;
	short Top;
	short Right;
	short Bottom;
};

struct csbi
{
	COORD dwSize;
	COORD dwCursorPosition;
	uint wAttributes;
	SMALL_RECT srWindow;
	COORD dwMaximumWindowSize;

};

int gotoxy(short x,short y)
{
	HWND hwnd = GetStdHandle(-11);
	COORD.x=x;
	COORD.y=y;
	SetConsoleCursorPosition(hwnd,COORD);
	return 0;
};

int getxy()
{
	HWND hwnd = GetStdHandle(-11);
	csbi cmd_info;
	GetConsoleScreenBufferInfo(hwnd, byref(cmd_info));
	return cmd_info.dwCursorPosition.X,cmd_info.dwCursorPosition.Y;
};

int drawline(short x,short y,short a,short b)
{
	HWND hconsole = GetConsoleWindow();
	HDC hDC = GetDC(hconsole);
	HPEN hPen = CreatePen(PS_SOLID, 2, RGB(255,255,255));
	SelectObject(hDC, hPen);

	MoveToEx(hDC,x, y, NULL);
	LineTo(hDC,a,b);

	DeleteObject(hPen);
	ReleaseDC(hConsole, hDC);
	return 0;
};

int drawrect(short t,short l,short r,short b,char name[10])
{
	HWND hconsole = GetConsoleWindow();
	HDC hDC = GetDC(hconsole);
	HBRUSH hbr = CreateSolidBrush(RGB(255,255,255));
	SelectObject(hDC, hbr);

	RECT rect={t,l,r,b};
	FrameRect(hDC,&rect,hbr);
	RECT rect={t+2,l+2,r-2,b-2};
	FrameRect(hDC,&rect,hbr);

	gotoxy(t+1,l+1);
	printf("%s",name);

	DeleteObject(hbr);
	ReleaseDC(hConsole, hDC);
	return 0;
};