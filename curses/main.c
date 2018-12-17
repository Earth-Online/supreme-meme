#include<windows.h>
#include<curses.h>

int main(){
	system("chcp 437");
	
	initscr();
	noecho();
	curs_set(0);
	keypad(stdscr,TRUE);
	
	box(stdscr,0,0);
	WINDOW *win1 = derwin(stdscr,10,20,1,1);
	box(win1,0,0);
	char *str = "hello world!";
	mvwprintw(win1,2,3,str);
	
	refresh();
	getch();
	endwin();
	return 0;
}