#include <stdlib.h>
#include "SDL.h"

// If you're going to render widgets to the same
// UI from different source files, you can avoid
// ID collisions by defining IMGUI_SRC_ID before
// this define block:
#ifdef IMGUI_SRC_ID
#define GEN_ID ((IMGUI_SRC_ID) + (__LINE__))
#else
#define GEN_ID (__LINE__)
#endif

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


// Check whether current mouse position is within a rectangle
int regionhit(int x, int y, int w, int h)
{
  if (uistate.mousex < x ||
    uistate.mousey < y ||
    uistate.mousex >= x + w ||
    uistate.mousey >= y + h)
    return 0;
  return 1;
}

// Simple button IMGUI widget
int button(int id, int x, int y)
{
  // Check whether the button should be hot
  if (regionhit(x, y, 64, 48))
  {
    uistate.hotitem = id;
    if (uistate.activeitem == 0 && uistate.mousedown)
      uistate.activeitem = id;
  }

  // Render button 
  drawrect(x+8, y+8, 64, 48, 0);
  if (uistate.hotitem == id)
  {
    if (uistate.activeitem == id)
    {
      // Button is both 'hot' and 'active'
      drawrect(x+2, y+2, 64, 48, 0xffffff);
    }
    else
    {
      // Button is merely 'hot'
      drawrect(x, y, 64, 48, 0xffffff);
    }
  }
  else
  {
    // button is not hot, but it may be active    
    drawrect(x, y, 64, 48, 0xaaaaaa);
  }

  // If button is hot and active, but mouse button is not
  // down, the user must have clicked the button.
  if (uistate.mousedown == 0 && 
    uistate.hotitem == id && 
    uistate.activeitem == id)
    return 1;

  // Otherwise, no clicky.
  return 0;
}

void imgui_prepare()
{
  uistate.hotitem = 0;
}

void imgui_finish()
{
  if (uistate.mousedown == 0)
  {
    uistate.activeitem = 0;
  }
  else
  {
    if (uistate.activeitem == 0)
      uistate.activeitem = -1;
  }
}

// Rendering function
void render()
{   
  static int bgcolor = 0x77;

  // clear screen
  drawrect(0,0,640,480,bgcolor);

  imgui_prepare();

  button(GEN_ID,50,50);
  
  button(GEN_ID,150,50);
  
  if (button(GEN_ID,50,150))
    bgcolor = (SDL_GetTicks() * 0xc0cac01a) | 0x77;
  
  if (button(GEN_ID,150,150))
    exit(0);

  imgui_finish();

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
