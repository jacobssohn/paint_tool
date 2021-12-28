import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import cv2


class Window(tk.Tk):

    '''
    This class should create an object displaying a window with all the GUI of the application.
    It should be created either permanently, one object for all pictures, or
    one object per one image. Clicking on buttons of the window should trigger
    further functions.

    #TODO Main window with options to either open a file or make a screenshot (paint_ss)
    #TODO Open provided picture in a separate window
    '''

    def __init__(self):
        super().__init__()
        img = ImageTk.PhotoImage(Image.open('../pictures/main_screen.png').resize((300, 200)))
        homeScreen = ttk.Label(self, image=img, padding=5)
        #img['image'] = image
        homeScreen.image = img
        homeScreen.pack()
        self.title('Main window')
        self.geometry('300x300+300+200')
        #self.resizable(False, False)
        self.attributes('-topmost', 1)
        self.iconbitmap('../pictures/logo.ico')
        ttk.Button(self, text='Take a screenshot', command=self.button_clicked).pack()


    def button_clicked(self):
        print("Screenshot not taken, cause the function isn't implemented yet")

def main():
    root = Window()

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()

if __name__ == '__main__':
    main()