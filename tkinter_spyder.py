# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:43:10 2021

@author: user
"""

import tkinter as tk
import numpy as np

# run main gui(graphical user interface)
gui = tk.Tk()

# create labels
my_label = tk.Label(gui, text='Hello, World!')
my_label1 = tk.Label(gui, text='Hello, Korea!')


# play in gui
# my_label.pack()
# my_label1.pack()
my_label.grid(row=0,column=0)
my_label1.grid(row=1,column=0)



# run mainloop
gui.mainloop()
