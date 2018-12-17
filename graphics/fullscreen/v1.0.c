void viewport(short a,short b);

void viewport(short a,short b)
{
	DEVMODE dmScreenSettings;
	memset(&dmScreenSettings,0,sizeof(dmScreenSettings));
	dmScreenSettings.dmSize=sizeof(dmScreenSettings); //结构大小
	dmScreenSettings.dmPelsHeight=b;  //屏幕的高
	dmScreenSettings.dmPelsWidth=a;   //屏幕的宽
	dmScreenSettings.dmBitsPerPel=16;  //像素字节位数
	dmScreenSettings.dmFields=DM_BITSPERPEL|DM_PELSWIDTH|DM_PELSHEIGHT;  //位标记，标明哪些字节是有效的，对应前面设置的三个参数

	if(ChangeDisplaySettings(&dmScreenSettings,CDS_FULLSCREEN)!=DISP_CHANGE_SUCCESSFUL)
	{
		if (MessageBox(NULL,"修改显示设备属性失败！是否继续用一般模式显示","提示",MB_YESNO|MB_ICONEXCLAMATION)==IDYES)
		{
			return false;
		}
		else
		{
			MessageBox(NULL,"点击关闭窗口","ERROR",MB_OK|MB_ICONSTOP);
			return false;
		}
	}
}
int main()
{
	BOOL fullscreen=true;
	if(MessageBox(NULL,"是否全屏显示？","提示",MB_YESNO|MB_ICONQUESTION)==IDNO)
	{
		fullscreen=false;
	}
	if(fullscreen)
	{
		void change_attr()
		void init()
		void move_to(0,0)
		int get_size()
		if(viewport(a,b))
		{
			void run()
		}
		else
		{
			return 1;
		}	
	}
}