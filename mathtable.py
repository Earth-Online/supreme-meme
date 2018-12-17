import math
from colorconsole import terminal

screen = terminal.get_terminal(conEmu=False)
screen.set_title("mathtable")
screen.clear()

PI = math.pi
step = (2.0*PI)/screen.columns()

for x in range(screen.columns()):

    screen.print_at(x, 11, "-")
    screen.print_at(screen.columns()/2, 25-x, "|")

    screen.print_at(x, 11+math.sin(x*step)*10, ".")

    screen.print_at(x, 11+math.cos(x*step)*10, ".")

screen.reset_colors()
screen.cprint(13,0,'f(x)=sin x\n')
screen.cprint(13,0,'f(x)=cos x\n')
screen.getch()
