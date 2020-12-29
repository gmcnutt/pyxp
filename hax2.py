import atexit
import sdl2
from sdl2 import sdlttf
import sys
import time


class MainWindow(object):

    def __init__(self):
        window = sdl2.SDL_CreateWindow(
            bytes("haxima2", "utf-8"),
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            640 * 2,
            480 * 2,
            sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_OPENGL,
        )
        self._renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

    def clear(self):
        sdl2.SDL_SetRenderDrawColor(self._renderer, 0, 0, 0, sdl2.SDL_ALPHA_OPAQUE)
        sdl2.SDL_RenderClear(self._renderer)
        sdl2.SDL_RenderPresent(self._renderer)

def splash():
    clear_screen()
    ttf = sdlttf.open("avatar.ttf", 128)


if __name__ == "__main__":
    # setup sdl
    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
    atexit.register(sdl2.SDL_Quit)

    # create main window
    window = MainWindow()
    window.clear()
    time.sleep(3)
