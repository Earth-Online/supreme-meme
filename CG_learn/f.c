#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.1415926
#define SX 16//8
#define SY 32//16
#define DX PI / SX
#define DY PI * 2 / SY
#define X(a, b) (cx + v[a][b].x * r), (cy + v[a][b].y * r)
typedef struct { double x, y; } Vec;

void calc(double i, double j, double rot, Vec* v) {
    double x = sin(i) * cos(j), y = sin(i) * sin(j), z = cos(i),
        s = sin(rot), c = cos(rot), c1 = 1 - c, u = 1 / sqrt(3), u2 = u * u;
    v->x = x * (c + u2 * c1) + y * (u2 * c1 - u * s) + z * (u2 * c1 + u * s);
    v->y = x * (u2 * c1 + u * s) + y * (c + u2 * c1) + z * (u2 * c1 - u * s);
}

LRESULT WINAPI MainWndProc(HWND, UINT, WPARAM, LPARAM);

LRESULT CALLBACK MainWndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
        HDC hdc1;
        PAINTSTRUCT ps;
        static int cxClient, cyClient;
		static double rot = 0;
		static int fps = 0;

        switch (message)
        {
		case WM_CREATE:
			SetTimer(hwnd,1,30,NULL);//定时器
			SetTimer(hwnd,2,1000,NULL);//fps定时器
			return 0;

        case WM_SIZE:
			cxClient = LOWORD(lParam);
			cyClient = HIWORD(lParam);
			return 0;

		case WM_PAINT:
			hdc1 = BeginPaint(hwnd, &ps);
			
			int w = cxClient, h = cyClient, cx = w / 2, cy = h / 2, r = h * 0.375;
			HDC hdc2 = CreateCompatibleDC(hdc1); HBITMAP bmp = CreateCompatibleBitmap(hdc1, w, h); SelectObject(hdc2, bmp);
			SelectObject(hdc2, GetStockObject(WHITE_PEN));
			Vec v[SX + 1][SY + 1];
			for(int i = 0; i <= SX; ++i) for(int j = 0; j <= SY; ++j) calc(i * DX, j * DY, rot, &v[i][j]);
			for(int i = 0; i < SX; ++i) for(int j = 0; j < SY; ++j) {
				MoveToEx(hdc2, X(i, j), NULL); LineTo(hdc2, X(i + 1, j));
				MoveToEx(hdc2, X(i, j), NULL); LineTo(hdc2, X(i, j + 1));
			}
			BitBlt(hdc1, 0, 0, w, h, hdc2, 0, 0, SRCCOPY); DeleteObject(bmp); DeleteDC(hdc2);
			
			
			EndPaint(hwnd, &ps);
			return 0;

		case WM_DESTROY:
			PostQuitMessage(0);
			return 0;
		case WM_TIMER:
			switch (wParam)
			{
			case 1:
				InvalidateRect(hwnd,NULL,TRUE);//ms刷新一次窗口
				rot += 0.02;
				fps++;
				return 0;
			case 2:
				printf("fps: %d\n", fps);
				fps = 0;
				return 0;
			}
		 	
		 	return 0;
		}

		return DefWindowProc(hwnd, message, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)
{
	WNDCLASS wc;
	MSG msg;
	HWND hWnd;

	wc.lpszClassName = "DrawerClass";
	wc.lpfnWndProc = MainWndProc;
	wc.style = CS_VREDRAW | CS_HREDRAW;
	wc.hInstance = hInstance;
	wc.hIcon = LoadIcon(NULL, (LPCTSTR)IDI_APPLICATION);
	wc.hCursor = LoadCursor(NULL, (LPCTSTR)IDC_ARROW);
	//wc.hbrBackground = (HBRUSH)GetStockObject(GRAY_BRUSH);
	wc.hbrBackground = NULL;
	wc.lpszMenuName = NULL;
	wc.cbClsExtra = 0;
	wc.cbWndExtra = 0;

	if (RegisterClass(&wc) == 0)
	{
		MessageBox(NULL, TEXT("注册失败"), wc.lpszClassName, MB_ICONERROR);
		return 1;
	}

	hWnd = CreateWindow("DrawerClass",
			  "Draw Test",
			  WS_OVERLAPPEDWINDOW,
			  CW_USEDEFAULT,
			  CW_USEDEFAULT,
					  800,
					  600,
			  NULL,
			  NULL,
			  hInstance,
			  NULL);
	if (hWnd == NULL)
	{
		MessageBox(NULL, TEXT("窗口句柄创建失败"), wc.lpszClassName, MB_ICONERROR);
		return 1;
	}

	ShowWindow(hWnd, nCmdShow);

	while(GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return msg.wParam;
}
