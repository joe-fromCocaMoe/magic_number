from tkinter import *
from random import shuffle, random, choice
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
from tkinter import ttk
import logging, sys


logging.basicConfig(level= logging.DEBUG)
#logging.disable(logging.CRITICAL)

class Guess_Your_Number(Frame):
    def __init__(self, parent=None):
        self.parent= parent
        Frame.__init__(self, self.parent)
        self.pack(expand=YES, fill=BOTH)

        font_1= ('arial',19,'bold')
        font_2= ('arial',16,'bold')
        self.canvas= Canvas(self)
        self.canvas.config(width= 1200, height= 1100, bg='gray90')
        self.canvas.pack(expand=YES, fill=BOTH)

        self.top_lbl= StringVar()
        self.tp_lbl= Label(self.canvas, textvariable=self.top_lbl,
                           font=font_1)
        self.tp_lbl.place(x=50,y=44)

        self.window= Text(self.canvas, relief='sunken',font=font_2,
                          height=35)
        self.window.place(x=75,y=150)

        self.multiplier= IntVar()
        self.drop_down= ttk.Combobox(self.canvas,textvariable=self.multiplier,
                                     width=18)
        self.drop_down.place(x=500,y=50)
        self.drop_down['values']=(63,127,255,511)
        self.multiplier.set(63)
        self.base_dict= {63:6,127:7,255:8,511:9}

        self.yes_btn= Button(self.canvas, text='begin', command=self.on_yes)
                
        self.btn= Button(self.canvas, text='submit', command= self.get_entry,
                         state='disabled')
        self.btn.place(x=600,y=100)
        
        self.radio= BooleanVar()
        self.rad_yes= Radiobutton(self.canvas,text='yes',value=True,
                                  variable=self.radio)
        self.rad_yes.place(x=200,y=100)
        self.rad_no= Radiobutton(self.canvas,text='no',value=False,
                                 variable=self.radio)
        self.rad_no.place(x=280,y=100)        
        
        self.bind_all('<Key>', self.key)
        self.g_count=0
        self.start_game()
        
    def display_chart(self,index: int, columns: int=8):
        self.window.delete('1.0','end')              
        UPPER_LIMIT= 2 ** self.base
        start = 1 << index
        chart = [str(x) for x in range(start, UPPER_LIMIT) if x % (start * 2) >= start]
        for i in range(len(chart) // columns):            
            text="\t".join(chart[i * columns : (i + 1) * columns])            
            self.window.insert("end",text,'\n')
            self.window.insert("end",'\n')
        answer= askyesno('queston', 'Is your number in this list?')
        if answer:
            self.guess += 1 << index
            
    def game(self):        
        for current in range(self.base):
            
            self.display_chart(current)
        final='Your number is {0}'.format(self.guess)
        self.top_lbl.set(final)
        replay= askyesno('Replay?', 'Play again?')
        if replay:
            self.window.delete('1.0','end')
            self.start_game()
        else:
            self.parent.destroy()
            
        
    def on_yes(self):
        if self.radio.get():
            self.yes_btn.place_forget()
            text='Is your number in this group below?'
            self.top_lbl.set(text)
            self.game()
        else:
            text= 'Think of a number between 1 and ->'
            self.top_lbl.set(text)
            self.yes_btn.place_forget()
            self.btn.config(state='normal')
        
    def start_game(self):
        self.guess= 0
        text= 'Think of a number between 1 and ->'
        self.top_lbl.set(text)
        self.btn.config(state='normal')
        
    def key(self, event):
        self.g_count +=1
        message= 'count:{0} key:{1} num:{2} state:{3}'.format(self.g_count,
                                                 event.keysym,event.keysym_num,
                                       event.state)
        logging.debug(message)
        
    def get_entry(self):
        self.btn.config(state='disabled')
        num= self.multiplier.get()        
        self.base= self.base_dict[num]        
        text= 'Your number is between 1 and {0}?'.format(num)
        self.top_lbl.set(text)
        self.yes_btn.place(x=350,y=100)
        
        
        
if __name__ == '__main__':
    root= Tk()
    Guess_Your_Number(root)
    root.mainloop()
      
