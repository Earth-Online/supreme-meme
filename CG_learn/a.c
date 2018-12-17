#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#define SPEED 2

RECT rect;
POINT p;

int cursor_in_rect()
{
	return (p.x < rect.right && p.x > rect.left && p.y < rect.bottom && p.y > rect.top);
}

int main (void)
{
	HWND hwnd = GetConsoleWindow();
	puts("�ѻ�ȡ���ھ��"); 
	HDC hdc = GetDC(hwnd);
	puts("�ѻ�ȡ����DC"); 

	GetWindowRect(hwnd, &rect);
	puts("�ѻ�ȡ���ڿ��"); 
	HBITMAP hbitmap = LoadImage(NULL, "huaji.bmp", IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);
	puts("�����뻬��"); 
	HDC comp_hdc = CreateCompatibleDC(hdc);
	puts("�Ѵ����ڴ�DC"); 
	SelectObject(comp_hdc, hbitmap);
	puts("��ѡ�񻬻�"); 

	int i=0,j = 0;
	int height = rect.bottom - rect.top;
	int width = rect.right - rect.left;
	int move_right = 1;
	int move_down = 1;
	RECT image_rect;

	image_rect.bottom = 0;
	image_rect.left = 0;
	image_rect.right = 0;
	image_rect.top = 0;
	puts("���س���ʼ����");
	getchar();
	BitBlt(hdc, i, j, 64, 64, comp_hdc, 0, 0, SRCCOPY);
	HBRUSH brush = CreateSolidBrush(RGB(0,0,0));

	for (;;) {
		GetWindowRect(hwnd, &rect);
		GetCursorPos(&p);
		if(!cursor_in_rect()){
			continue;
		} else {
			if (p.x > rect.left + i) {
				move_right = 1;
			} else {
				move_right = 0;
			}
			if (p.y > rect.top + j) {
				move_down = 1;
			} else {
				move_down = 0;
			}
			FillRect(hdc, &image_rect, brush);
		}
		image_rect.left = i;
		image_rect.right = i + 64;
		image_rect.top = j;
		image_rect.bottom = j + 64;
		BitBlt(hdc, i, j, 64, 64, comp_hdc, 0, 0, SRCCOPY);
		if (move_right) {
			i += SPEED;
		} else {
			i -= SPEED;
		}
		if (move_down) {
			if (j < height - 64) {
				j += SPEED;
			} else {
				move_down = !move_down;
			}
		} else {
			if (j > 0) {
				j -= SPEED;
			} else {
				move_down = !move_down;
			}
		}
		Sleep(10);

	}

	ReleaseDC(hwnd, hdc);
	puts("test");
	getchar();
	return 0;
}