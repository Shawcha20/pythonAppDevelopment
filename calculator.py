# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 16:56:25 2025

@author: shawcha
"""
import tkinter as tk
from tkinter import ttk
class calculatorApp:
    def __init__(self, root):
        self.root= root
        self.root.title("calculator")
        self.root.geometry("400x400")
        self.root.resizable(True, True)
        self.expression=""
        self.display_txt= tk.StringVar()
       
        display_frame=ttk.Frame(self.root)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        display_label=ttk.Label(
            display_frame,
            textvariable=self.display_txt,
            font=("Arial",25),
            anchor="e",
            background="white",
            foreground='black',
            padding=6
            )
        
        display_label.pack(fill=tk.BOTH,expand=True)
        button_frame=ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)
        self.create_button(button_frame)
    def create_button(self,frame):
        buttons=[
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3)
            ,('4',2,0),('5',2,1),('6',2,2),('*',2,3)
            ,('1',3,0),('2',3,1),('3',3,2),('-',3,3)
            ,('c',4,0),('0',4,1),('=',4,2),('+',4,3)
            ]
        for (text,row, col) in buttons:
            button=ttk.Button(frame,text=text,command=lambda t=text:self.on_button_click(t))
            button.grid(row=row,column=col, sticky="nsew",padx=2,pady=2)
        for i in range (5):
            frame.rowconfigure(i,weight=1)
            frame.columnconfigure(i,weight=1)
            
    def on_button_click(self,button_text)    :
        if button_text=='c':
            self.expression=""
        elif button_text=='=':
            try:
                self.expression=str(eval(self.expression))
                print(self.expression)
            except Exception as e:
                self.expression="error"
        else:
            self.expression+=button_text
            
        self.display_txt.set(self.expression);    



if __name__=="__main__":
    root=tk.Tk()
    app=calculatorApp(root)
    root.mainloop()
        