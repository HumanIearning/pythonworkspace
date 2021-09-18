# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:43:10 2021

@author: user
"""

import tkinter as tk
import numpy as np

# run main gui(graphical user interface)
gui = tk.Tk()


def my_click():
    my_label = tk.Label(gui,
        text='Button Clicked!'
        )
    my_label.pack()





# create button
my_button = tk.Button(gui,
                      text='Click!',     # 버튼 텍스트
                      #state=tk.DISABLED, # 버튼 비활성화
                      padx=30,           # 버튼 크기
                      pady=20,
                      command=my_click   # 함수 이름만 알려주면됨 괄호 안씀
                      )

# place in gui
my_button.pack()



# run mainloop
gui.mainloop()
