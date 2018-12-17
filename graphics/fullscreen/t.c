#include<windows.h>
//gcc t.c -o t.exe -lgdi32 -luser32
#define true 1;
#define false 0;

LRESULT CALLBACK WndProc(HWND,UINT,WPARAM,LPARAM);

int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance,LPSTR lpCmdLine,int iCmdShow)
{
	DWORD dwExStyle;
	DWORD dwStyle;
	WNDCLASS wndclass;
	
	wndclass.cbClsExtra=0;
	wndclass.cbWndExtra=0;
	wndclass.hbrBackground=(HBRUSH)GetStockObject(GRAY_BRUSH);
	wndclass.hInstance=hInstance;
	wndclass.hCursor=LoadCursor(NULL,IDC_ARROW);
	wndclass.hIcon=LoadIcon(NULL,IDI_APPLICATION);
	wndclass.lpfnWndProc=WndProc;
	wndclass.lpszClassName="HelloWin";
	wndclass.lpszMenuName=NULL;
	wndclass.style=CS_HREDRAW|CS_VREDRAW;

	if(!RegisterClass(&wndclass))
	{
		MessageBox(NULL,"注册失败！","error",MB_OK);
		return 0;
	}

	BOOL fullscreen=true;

	if(MessageBox(NULL,"是否全屏显示？","提示",MB_YESNO|MB_ICONQUESTION)==IDNO)
	{
		fullscreen=false;
	}

	if(fullscreen)
	{
		DEVMODE dmScreenSettings;
		memset(&dmScreenSettings,0,sizeof(dmScreenSettings));
		dmScreenSettings.dmSize=sizeof(dmScreenSettings); //结构大小
		dmScreenSettings.dmPelsHeight=600;  //屏幕的高
		dmScreenSettings.dmPelsWidth=800;   //屏幕的宽
		dmScreenSettings.dmBitsPerPel=16;  //像素字节位数
		dmScreenSettings.dmFields=DM_BITSPERPEL|DM_PELSWIDTH|DM_PELSHEIGHT;  //位标记，标明哪些字节是有效的，对应前面设置的三个参数

		if(ChangeDisplaySettings(&dmScreenSettings,CDS_FULLSCREEN)!=DISP_CHANGE_SUCCESSFUL)
		{
			if (MessageBox(NULL,"修改显示设备属性失败！是否继续用一般模式显示","提示",MB_YESNO|MB_ICONEXCLAMATION)==IDYES)
			{
				fullscreen=FALSE;

			}
			else
			{
				MessageBox(NULL,"点击关闭窗口","ERROR",MB_OK|MB_ICONSTOP);
				return FALSE;

			}
		}

		if(fullscreen)
		{
			dwExStyle=WS_EX_APPWINDOW; //隐藏顶层的窗口
			dwStyle=WS_POPUP;   //没有边框的窗口
			ShowCursor(FALSE);  //不显示鼠标指针
		}
		else
		{
			dwExStyle=WS_EX_APPWINDOW|WS_EX_WINDOWEDGE;
			dwStyle=WS_OVERLAPPEDWINDOW;
		}
		RECT  winRect;
		winRect.left=0;
		winRect.right=800;
		winRect.top=0;
		winRect.bottom=600;

		AdjustWindowRectEx(&winRect, dwStyle,FALSE,dwExStyle);//依据所需客户矩形大小，计算需要的窗口矩形的大小。

															 // 计算出的窗口矩形随后可以传送给CreateWindowEx函数，

															 //用于创建一个客户区所需大小的窗口。

	}

	HWND hwnd=CreateWindowEx(dwExStyle,"HelloWin","HelloWin",
	dwStyle|WS_CLIPSIBLINGS|WS_CLIPCHILDREN,  //WS_CLIPSIBLINGS|WS_CLIPCHILDREN参考后面的参考资料
	0,0,800,600,NULL,NULL,hInstance,NULL);
	
	ShowWindow(hwnd,iCmdShow);
	UpdateWindow(hwnd);
	MSG msg;
	while(GetMessage(&msg,NULL,0,0))
	{
		if(msg.message==WM_CLOSE)
		{
			break;
		}
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return msg.wParam;
}

LRESULT CALLBACK WndProc(HWND hWnd,UINT msg,WPARAM wParam,LPARAM lParam)
{
	PAINTSTRUCT ps;
	switch(msg)
	{
		case WM_CREATE:
			return 0;
		case WM_PAINT:
		{
			HDC hdc=BeginPaint(hWnd,&ps);
			EndPaint(hWnd,&ps);
			return 0;
		}
		case WM_KEYDOWN:
			switch(wParam)
			{
				case VK_ESCAPE:
				PostMessage(hWnd,WM_CLOSE,0,0);
				break;
			}
			return 0;
		case WM_CLOSE:
			DestroyWindow(hWnd);
			return 0;
		case WM_DESTROY:
			PostQuitMessage(0);
			return 0;

	}
	return DefWindowProc(hWnd,msg,wParam,lParam);
}