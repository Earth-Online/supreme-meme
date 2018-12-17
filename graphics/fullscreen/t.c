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
		MessageBox(NULL,"ע��ʧ�ܣ�","error",MB_OK);
		return 0;
	}

	BOOL fullscreen=true;

	if(MessageBox(NULL,"�Ƿ�ȫ����ʾ��","��ʾ",MB_YESNO|MB_ICONQUESTION)==IDNO)
	{
		fullscreen=false;
	}

	if(fullscreen)
	{
		DEVMODE dmScreenSettings;
		memset(&dmScreenSettings,0,sizeof(dmScreenSettings));
		dmScreenSettings.dmSize=sizeof(dmScreenSettings); //�ṹ��С
		dmScreenSettings.dmPelsHeight=600;  //��Ļ�ĸ�
		dmScreenSettings.dmPelsWidth=800;   //��Ļ�Ŀ�
		dmScreenSettings.dmBitsPerPel=16;  //�����ֽ�λ��
		dmScreenSettings.dmFields=DM_BITSPERPEL|DM_PELSWIDTH|DM_PELSHEIGHT;  //λ��ǣ�������Щ�ֽ�����Ч�ģ���Ӧǰ�����õ���������

		if(ChangeDisplaySettings(&dmScreenSettings,CDS_FULLSCREEN)!=DISP_CHANGE_SUCCESSFUL)
		{
			if (MessageBox(NULL,"�޸���ʾ�豸����ʧ�ܣ��Ƿ������һ��ģʽ��ʾ","��ʾ",MB_YESNO|MB_ICONEXCLAMATION)==IDYES)
			{
				fullscreen=FALSE;

			}
			else
			{
				MessageBox(NULL,"����رմ���","ERROR",MB_OK|MB_ICONSTOP);
				return FALSE;

			}
		}

		if(fullscreen)
		{
			dwExStyle=WS_EX_APPWINDOW; //���ض���Ĵ���
			dwStyle=WS_POPUP;   //û�б߿�Ĵ���
			ShowCursor(FALSE);  //����ʾ���ָ��
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

		AdjustWindowRectEx(&winRect, dwStyle,FALSE,dwExStyle);//��������ͻ����δ�С��������Ҫ�Ĵ��ھ��εĴ�С��

															 // ������Ĵ��ھ��������Դ��͸�CreateWindowEx������

															 //���ڴ���һ���ͻ��������С�Ĵ��ڡ�

	}

	HWND hwnd=CreateWindowEx(dwExStyle,"HelloWin","HelloWin",
	dwStyle|WS_CLIPSIBLINGS|WS_CLIPCHILDREN,  //WS_CLIPSIBLINGS|WS_CLIPCHILDREN�ο�����Ĳο�����
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