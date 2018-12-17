#include <stdlib.h>
#include "SDL.h"

// Screen surface
SDL_Surface *gScreen;

struct UIState
{
  int mousex;
  int mousey;
  int mousedown;

  int hotitem;
  int activeitem;
} 
uistate = {0,0,0,0,0};

// Simplified interface to SDL's fillrect call
void drawrect(int x, int y, int w, int h, int color)
{
  SDL_Rect r;
  r.x = x;
  r.y = y;
  r.w = w;
  r.h = h;
  SDL_FillRect(gScreen, &r, color);
}

// Rendering function
void render()
{   
  // clear screen
  drawrect(0,0,640,480,0);

  // test that the uistate is working
  drawrect(uistate.mousex - 32,uistate.mousey - 24,
         64,48,0xff << (uistate.mousedown * 8));

  // update the screen
    SDL_UpdateRect(gScreen, 0, 0, 640, 480);    

  // don't take all the cpu time
  SDL_Delay(10); 
}


// Entry point
int main(int argc, char *argv[])
{
  // Initialize SDL's subsystems - in this case, only video.
    if (SDL_Init(SDL_INIT_VIDEO) < 0) 
  {
        fprintf(stderr, "Unable to init SDL: %s\n", SDL_GetError());
        exit(1);
    }

  // Register SDL_Quit to be called at exit; makes sure things are
  // cleaned up when we quit.
    atexit(SDL_Quit);
    
  // Attempt to create a 640x480 window with 32bit pixels.
    gScreen = SDL_SetVideoMode(640, 480, 32, SDL_SWSURFACE);
  
  // If we fail, return error.
    if (gScreen == NULL) 
  {
        fprintf(stderr, "Unable to set up video: %s\n", SDL_GetError());
        exit(1);
    }

  // Main loop: loop forever.
    while (1)
    {
    // Render stuff
        render();

    // Poll for events, and handle the ones we care about.
        SDL_Event event;
        while (SDL_PollEvent(&event)) 
        {
            switch (event.type) 
            {
      case SDL_MOUSEMOTION:
        // update mouse position
        uistate.mousex = event.motion.x;
        uistate.mousey = event.motion.y;
        break;
      case SDL_MOUSEBUTTONDOWN:
        // update button down state if left-clicking
        if (event.button.button == 1)
          uistate.mousedown = 1;
        break;
      case SDL_MOUSEBUTTONUP:
        // update button down state if left-clicking
        if (event.button.button == 1)
          uistate.mousedown = 0;
        break;
            case SDL_KEYUP:                  
        switch (event.key.keysym.sym)
        {
        case SDLK_ESCAPE:
          // If escape is pressed, return (and thus, quit)
          return 0;
        }
                break;
            case SDL_QUIT:
                return(0);
            }
        }
    }
    return 0;
}
