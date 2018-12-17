#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// 因为是使用折线绘画，所以当折线的顶点数量非常多的时候，我们就可以看到一条近似完美的曲线了！
#define        NUM                1000                // 将 x 轴分成 1000 等份
#define        TWOPI        (2 * 3.14159)        // 一个周期等于 2π

LRESULT WINAPI MainWndProc(HWND, UINT, WPARAM, LPARAM);

LRESULT CALLBACK MainWndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    HDC hdc;
    PAINTSTRUCT ps;
    RECT rect;
    static int cxClient, cyClient;

        switch (message)
        {
        /* 首先，我们需要让窗口在改变大小的时候，sin 函数的图形会跟着实时改变，所以我们这里需要响应 WM_SIZE 消息，
            lParam 的低 16 位是客户区的宽，高 16 位是客户区的高。
        */
        case WM_SIZE:
                cxClient = LOWORD(lParam);
                cyClient = HIWORD(lParam);
                return 0;

        case WM_PAINT:
				hdc = BeginPaint(hwnd, &ps);

				// 绘制辅助线
				MoveToEx(hdc, 0, cyClient / 2, NULL);
				LineTo(hdc, cxClient, cyClient / 2);
				MoveToEx(hdc, cxClient / 2, 0, NULL);
				LineTo(hdc, cxClient / 2, cyClient);

				// 设置当前映射模式为 MM_LOMETRIC，即每个逻辑单位映射为0.1毫米，x轴向右，y轴向上
				// 这样将窗口的映射模式类同于数学中的坐标系模式
				SetMapMode(hdc, MM_LOMETRIC);
				// 指定映射到窗口原点(0, 0)的设备原点的坐标，即指定哪个设备原点将映射到逻辑原点(0, 0)
				// 这里是指定的窗口的最左侧居中的位置为我们的逻辑原点(0, 0)在实际的设备上的映射
				// 这里指定的是窗口中心为坐标系原点位置，符合数学习惯
				SetViewportOrgEx(hdc, cxClient / 2, cyClient / 2, NULL);
				// 这里从最左边居中的位置开始绘制正弦图像
				MoveToEx(hdc, -cxClient / 2, 0, NULL);
				for (double x = -cxClient / 2; x < cxClient / 2; x += 0.01) {
					// 这里的两个坐标都进行了一部分的放大，其中x += 0.01 是为了细分曲线
					LineTo(hdc, x * 200, sin(x) * 300);
				}

				EndPaint(hwnd, &ps);
				return 0;

        case WM_DESTROY:
                PostQuitMessage(0);
                return 0;
        }

        return DefWindowProc(hwnd, message, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)
{
	WNDCLASS wc;
	MSG msg;
	HWND hWnd;

	wc.lpszClassName = "DibTestClass";
	wc.lpfnWndProc = MainWndProc;
	wc.style = CS_VREDRAW | CS_HREDRAW;
	wc.hInstance = hInstance;
	wc.hIcon = LoadIcon(NULL, (LPCTSTR)IDI_APPLICATION);
	wc.hCursor = LoadCursor(NULL, (LPCTSTR)IDC_ARROW);
	wc.hbrBackground = (HBRUSH)GetStockObject(GRAY_BRUSH);
	wc.lpszMenuName = NULL;
	wc.cbClsExtra = 0;
	wc.cbWndExtra = 0;
	if (RegisterClass(&wc) == 0)
	{
	  fprintf(stderr, "RegisterClass failed (last error 0x%lX)\n",
		  GetLastError());
	  return(1);
	}

	hWnd = CreateWindow("DibTestClass",
			  "DIB Test",
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
	  fprintf(stderr, "CreateWindow failed (last error 0x%lX)\n",
		  GetLastError());
	  return(1);
	}

	ShowWindow(hWnd, nCmdShow);

	while(GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return msg.wParam;
}
