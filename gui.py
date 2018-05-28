import tkinter as tk

class main_window(object):

    def __init__(self, command1, command2):
        #define window
        self.window = tk.Tk()

        #define two enter button of systems
        self.button_sys1 = tk.Button(self.window, text = 'SYSTEM 1', bg = 'white', height = 3, width = 9)
        self.button_sys2 = tk.Button(self.window, text = 'SYSTEM 2', bg = 'white', height = 3, width = 9)

        #define enter system button function
        self.enter_sys1 = command1
        self.enter_sys2 = command2

        #define label
        self.school_label = tk.Label(self.window, text = 'SWJTU')

    def init_window(self):
        #write window's name
        self.window.title("Main")
        
        #window size
        self.window.minsize(400, 300)
        self.window.maxsize(400, 300)

    def create_window(self):
        #prepare create window
        self.init_window()
        self.make_layout()

        #run window
        self.window.mainloop()

    def make_layout(self):
        #button layout
        self.button_sys1.grid(row = 0, column = 0, padx = 50, pady = 100)
        self.button_sys2.grid(row = 0, column = 1, padx = 50, pady = 100)
        
        #SWJTU Label 
        self.school_label.grid(row = 1, column = 1, padx = 0, pady = 0) 

    def bind_event(self):
        #configure enter system function
        self.button_sys1.configure(command = enter_sys1)
        self.button_sys2.configure(command = enter_sys2)
        print("ok")
  
    def destroy_window(self):
        print("Destroy")
"""
    def __del__(self):
        destroy_window()
"""

class sys1_window(object):
    
    def __init__(self):
        #define sys1_window
        self.sys1_window = tk.Tk()

        #define button
        self.button1 = tk.Button(sys1_window, text = 'OCR', bg = 'white', height = 50, width = 50)
        self.button2 = tk.Button(sys1_window, text = 'face', bg = 'white', height = 50, width = 50)
        self.button3 = tk.Button(sys1_window, text = 'exit', bg = 'white', height = 50, width = 50)
 
        #input path
        self.entry = tk.Entry(sys1_window, text = 'input path: ', bg = 'white')

        #menu
        self.menu = tk.Menu(sys1_window)

        #define label
        self.school_label = tk.Label(sys1_window, text = 'SWJTU', bg = 'gold')
        
        #define frame
        self.frame_sys1_window = tk.Frame(sys1_window)
 
    def init_window(self):
        #write window's name
        self.sys1_window.title("Main")
        
        #sys1_window size
        self.sys1_window.minsize(800, 600)
        self.sys1_window.maxsize(800, 600)

        #menu config
        self.menu.add_command(label='menu')
        self.sys1_window.config(menu = menu)

        #SWJTU Label 
        self.school_label.pack() 
        
    def create_window(self):
        self.sys1_window.mainloop()
    
    def make_layout(self):
        #button layout
        self.button1.grid(row = 0, colum = 0)
        self.button2.grid(row = 1, colum = 0)
        self.button3.grid(row = 2, colum = 0)

        #entry layout
        self.entry.pack()

    def bind_event(self):
        #configure enter system function
        self.button_sys1.configure(command = enter_sys1)
        self.button_sys2.configure(command = enter_sys2)

    def destroy_window(self):
        print("Destroy")

"""
    def __del__(self):
        destroy_window()
"""

class sys2_window(object):
    
    def __init__(self):
        #define sys2_window
        self.sys2_window = tk.Tk()

        #define button
        self.button1 = tk.Button(sys2_window, text = 'OCR', bg = 'white', height = 40, width = 50)
        self.button2 = tk.Button(sys2_window, text = 'face', bg = 'white', height = 50, width = 50)
        self.button3 = tk.Button(sys2_window, text = 'exit', bg = 'white', height = 50, width = 50)
 
        #input path
        self.entry = tk.Entry(sys2_window, text = 'input path: ', bg = 'white')

        #define text
        self.text =  tk.Text(sys2_windoW, height = 10)

        #menu
        self.menu = tk.Menu(sys2_window)
        
        #define frame
        self.frame_sys2_window = tk.Frame(sys2_window)

        #define label
        self.entry_label = tk.Label(sys2_window, text = 'entry', bg = 'black')
        self.text_label = tk.Label(sys2_window, text = 'text', bg = 'black')
        self.school_label = tk.Label(sys2_window, text = 'SWJTU', bg = 'black')
 
    def init_window(self):
        #write window's name
        self.sys2_window.title("Main")
        
        #sys2_window size
        self.sys2_window.minsize(800, 600)
        self.sys2_window.maxsize(800, 600)


        #menu config
        self.menu.grid()
        self.menu.add_command(label='menu')
        self.sys2_window.config(menu = menu)
        
    def create_window(self):
        self.sys2_window.mainloop()
    
    def make_layout(self):
        #button layout
        self.button1.grid(row = 2, column = 0, padx = 50, pady = 100)
        self.button2.grid(row = 2, column = 1, padx = 50, pady = 100)
        self.button3.grid(row = 2, column = 2, padx = 50, pady = 100)

        #entry layout
        self.entry_label.grid(row = 1, column = 0)
        self.entry.grid(row 1, column = 1)

        #text entry
        self.text_label.grid(row = 0, column = 0)
        self.text.grid(row = 0, column = 1)

        #SWJTU Label 
        self.school_label.grid(row = 3, column = 2) 

    def bind_event(self):
        #configure enter system function
        self.button_sys2.configure(command = enter_sys1)
        self.button_sys2.configure(command = enter_sys2)

    def destroy_window(self):
        print("Destroy")

"""
    def __del__(self):
        destroy_window()
"""
