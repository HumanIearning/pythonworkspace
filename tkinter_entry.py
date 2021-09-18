# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:09:55 2021

@author: user
"""


import tkinter as tk
import numpy as np

# run main gui(graphical user interface)
gui = tk.Tk()

# def
def my_click():
    user_msg = "typed : " + my_entry.get()
    my_label = tk.Label(gui,
        text = user_msg,
        )
    my_label.pack()

# creat an entry
my_entry = tk.Entry(gui,
                    width=50,  # 가로길이
                    )
my_entry.pack()
my_entry.insert(0,'Enter values')

# button
my_button = tk.Button(gui,
                      text='Click!',     # 버튼 텍스트
                      #state=tk.DISABLED, # 버튼 비활성화
                      padx=30,           # 버튼 크기
                      pady=20,
                      command=my_click   # 함수 이름만 알려주면됨 괄호 안씀
                      )
my_button.pack()



# run mainloop
gui.mainloop()
