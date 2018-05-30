import tkinter as tk

class main_window(object):

    def __init__(self):
        #define main_window
        main_window = tk.Tk()

    def init_window(self):
        #write window's name
        main_window.title("Main")
        
        #main_window size
        main_window.minsize(800, 600)
        main_window.maxsize(800, 600)
        
        #define two enter button of systems
        button_sys1 = tk.Button(main_window, text = 'SYSTEM 1', bg = 'white', height = 50, width = 50).pack(side = tk.LEFT)
        button_sys2 = tk.Button(main_window, text = 'SYSTEM 2', bg = 'white', height = 50, width = 50).pack(side = tk.RIGHT)
        

    def create_window(self):
        main_window.mainloop()

    def make_layout(self):

    def bind_event(self):
  
    def destroy_window(self):

    def __del__(self):
        destroy_window()
 

class sys1_window(object):
    
    def __init__(self):
        #define main_window
        main_window = tk.Tk()

        #define button
        button1 = tk.Button(main_window1, text = 'OCR', bg = 'white', height = 50, width = 50)
        button2 = tk.Button(main_window1, text = 'face', bg = 'white', height = 50, width = 50)
        button3 = tk.Button(main_window1, text = 'exit', bg = 'white', height = 50, width = 50)
 
        #input path
        entry = tk.Entry(main_window1, text = 'input path: ', bg = 'white')

        #menu
        menu = tk.Menu(main_window)
 
    def init_window(self):
        #write window's name
        main_window.title("Main")
        
        #main_window size
        main_window1.minsize(800, 600)
        main_window1.maxsize(800, 600)

        #menu config
        menu.add_command(label='menu')
        main_window.config(menu = menu)
        
    def create_window(self):
        
        main_window.mainloop()
        
        #define frame
        frame_main_window1 = tk.Frame(main_window1)
    
    def make_layout(self):
        #button layout
        button1.grid(row = 0, colum = 0)
        button2.grid(row = 1, colum = 0)
        button3.grid(row = 2, colum = 0)

        #entry layout
        entry.pack()

    def bind_event(self):

    def destroy_window(self):

    def __del__(self):
        destroy_window()

class sys2_window(object):
    
    def __init__(self):
        #define main_window
        main_window = tk.Tk()

        #define button
        button1 = tk.Button(main_window1, text = 'OCR', bg = 'white', height = 50, width = 50)
        button2 = tk.Button(main_window1, text = 'face', bg = 'white', height = 50, width = 50)
        button3 = tk.Button(main_window1, text = 'exit', bg = 'white', height = 50, width = 50)
 
        #input path
        entry = tk.Entry(main_window1, text = 'input path: ', bg = 'white')

        #menu
        menu = tk.Menu(main_window)
        
        #define frame
        frame_main_window = tk.Frame(main_window)
 
    def init_window(self):
        #write window's name
        main_window.title("Main")
        
        #main_window size
        main_window1.minsize(800, 600)
        main_window1.maxsize(800, 600)

        #menu config
        menu.add_command(label='menu')
        main_window.config(menu = menu)
        
    def create_window(self):
        main_window.mainloop()
    
    def make_layout(self):
        #button layout
        button1.grid(row = 0, colum = 0)
        button2.grid(row = 1, colum = 0)
        button3.grid(row = 2, colum = 0)

        #entry layout
        entry.pack()

    def bind_event(self):

    def destroy_window(self):

    def __del__(self):
        destroy_window()
