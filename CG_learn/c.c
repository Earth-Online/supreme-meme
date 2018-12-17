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
        static int cxClient, cyClient;
        POINT apt[NUM];        // 一千个点构成
        int i;

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

                // 先画一条 x 轴在客户区的 1/2 的位置
                MoveToEx(hdc, 0, cyClient / 2, NULL);
                LineTo(hdc, cxClient, cyClient / 2);

                // 接着我们用一个循环，分别求出每个 x 对应的 y 值，然后把它画出来即可。
                for (i = 0; i < NUM; i++)
                {
                        // 将 x 分为 1000 等份，然后将每一份的 x 坐标计算出来。
                        apt[i].x = i * cxClient / NUM;

                        /* 直接调用 sin 函数计算 y 值：api[i].y = (int)(sin(x))
                            这里我们要显示一个周期（2π）:api[i].y = (int)(sin(TWOPI * i / NUM))
                            接下来是难点了：
                            要把求得的 y 值显示在整个客户区内，正弦函数 y 值的取值范围是 -1 ~ 1，
                            而我们的客户区是木有负数的范围，而且数学函数原点的位置跟客户区原点的位置不同，
                            导致直接显示到客户区上的图像会倒过来。
                            所以我们应该做一些转化：1 - sin(TWOPI * i / NUM)
                            使得函数图像倒过来，并且 y 值的取值范围变成了 0 ~ 2，
                            所以这里我们再乘上 cyClient / 2 即可完美显示！
                        */
                        apt[i].y = (int)(cyClient / 2 * (1 - sin(TWOPI * i / NUM)));
                        //printf("(%d, %d)\n", apt[i].x, apt[i].y);
                }

                PolylineTo(hdc, apt, NUM);
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
