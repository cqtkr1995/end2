import gui
import test
import system 

def cho_win():
    #the main window
    choose_window = gui.main_window(test.sys1_test, test.sys2_test)
    choose_window.init_window()
    choose_window.make_layout()
    choose_window.create_window()

def sys1_win():
    #the system1's window
    system1_window = gui.main_window()
    system1_window.init_window()
    system1_window.make_layout()
    system1_window.create_window()

def sys2_win():
    #the system2's window
    system2_window = gui.main_window()
    system2_window.init_window()
    system2_window.make_layout()
    system2_window.create_window()
    
if __name__ == '__main__':
    cho_win()
    sys1_win()
    sys2_win()
