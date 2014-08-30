#!/usr/bin/python


import Tkinter as gui
import tkFont
import gettext
import os
import sqlite3

#initialize gettext
lang="nl"
localepath=os.path.join(os.getcwd(), "locale")
t=gettext.translation(lang, localepath, fallback=True)
_=t.ugettext

class TypeTrainer:
    def __init__(self, master):
         
        #TODO fetch persistant settings from database
        self.debug=True
        #self.lang="nl"
        #self.localepath=os.path.join(os.getcwd(), "locale")
        
        #set up gettext for internationalization
        #t=gettext.translation(self.lang, self.localepath, fallback=True)
        #_=t.ugettext
        
        #some fonts to use
        self.lFont = tkFont.Font(family="Arial", size=30)
        self.xxlFont = tkFont.Font(family="Arial", size=100)
        
        # frames that make up the main part of the application
        self.fhome = gui.Frame(master, bd=1)
        self.fsettings = gui.Frame(master, bd=1)
        self.fhelp = gui.Frame(master, bd=1)
        self.fkeyreview = gui.Frame(master, bd=1)
        self.ftypingexercise = gui.Frame(master, bd=1)
        self.fcustomexercise = gui.Frame(master, bd=1)
        self.fprogress = gui.Frame(master, bd=1)
        
        # frame states, these tell the frames what to do on return
        self.shome = 0
        self.ssettings = 0
        self.shelp = 0
        self.skeyreview = 0
        self.stypingexercise = 0
        self.scustomexercise = 0
        self.sprogress = 0

        # buttons that make up the menu row - these aren't subject to change
        self.fmenu = gui.Frame(master, bd=1)
        self.fmenu.grid(row=1,column=1, columnspan=30, sticky=gui.W)

        self.bhome = gui.Button(self.fmenu, text=_("Home"), command=self.home)
        self.bhome.grid(row=1, column=1)

        self.bkeyreview = gui.Button(self.fmenu, text=_("Key review"), command=self.keyreview)
        self.bkeyreview.grid(row=1, column=2)

        self.btypingexercise = gui.Button(self.fmenu, text=_("Typing exercize"), command=self.typingexercise)
        self.btypingexercise.grid(row=1, column=3)

        self.bcustomexercise = gui.Button(self.fmenu, text=_("Custom exercize"), command=self.customexercise)
        self.bcustomexercise.grid(row=1, column=4)

        self.bprogress = gui.Button(self.fmenu, text=_("Progress"), command=self.progress)
        self.bprogress.grid(row=1, column=5)

        self.bsettings = gui.Button(self.fmenu, text=_("Settings"), command=self.settings)
        self.bsettings.grid(row=1, column=6)

        self.bhelp = gui.Button(self.fmenu, text=_("Help"), command=self.help_)
        self.bhelp.grid(row=1, column=7)

        self.bquit = gui.Button(self.fmenu, text=_("Exit"), command=self.fmenu.quit)
        self.bquit.grid(row=1, column=8)

        self.home(True)
    def removeFrame(self):
        """ Clear the path for a new frame"""
        self.currentframe.grid_remove()
    def home(self, first=False):
        """ Home frame
        Here you can find some statistics and a welcome message."""
        if(first==False): # only remove the current frame if there actually is one
            self.removeFrame()
        
        # check frame state
        if (self.shome==0): # uninitialized
            #TODO initialize the frame
            self.fhomeltitle = gui.Label(self.fhome, text=_("Welcome to the asetniop type trainer!"), font=self.lFont)
            self.fhomeltitle.grid(row=1, column=5, sticky=gui.W, columnspan=10)
            
            #update frame state
            self.shome=1
        
        #TODO make frame visible
        self.fhome.grid(row=2, column=1, rowspan=15, columnspan=9)
        
        #set current frame variable so other frames know what to remove when switching
        self.currentframe=self.fhome
        

    def keyreview(self):
        """ Key review frame
        This frame helps learn where all the different keys are in the asetniop layout. Training is done one letter at the time."""
        
        # remove past frame
        self.removeFrame()
        
        # check frame state
        if (self.skeyreview==0) : # uninitialized
            #TODO initialize the frame
            self.hkeyreviewltitle = gui.Label(self.fkeyreview, text=_("Key review"), font=self.lFont)
            self.hkeyreviewltitle.grid(row=1, column=7, columnspan=8)
            
            #show hands to indicate fingerpress
            self.hkeyreviewhands = Hands(self.fkeyreview,2,2)
            
            #Label for key to press
            self.hkeyreviewassignment = gui.Label(self.fkeyreview, text="A", bg="white", font=self.xxlFont)
            self.hkeyreviewassignment.grid(row=7, column=11)
            
            #Character selection window
            #self.hkeyreviewcsframe = VerticalScrolledFrame(self.fkeyreview)
            
            self.hkeyreviewcsframe = gui.Frame(self.fkeyreview)
            self.hkeyreviewcsframe.grid(row=2, column=25, rowspan=30)

            #hack to get a scrollbar
            canvas = gui.Canvas(self.hkeyreviewcsframe)
            innerframe = gui.Frame(canvas)
            scrollbar= gui.Scrollbar(self.hkeyreviewcsframe, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both")
            canvas.create_window((0,0),window=innerframe,anchor='nw')
            def tmpfun(event):
                canvas.configure(scrollregion=canvas.bbox("all"),width=250,height=800)
                
            innerframe.bind("<Configure>", tmpfun)

            self.hkeyreviewselection=t = CharacterSelection(innerframe, self.lFont)
            
            #Scrollbar


            #update framestate
            self.skeyreview=1
        
        #TODO make frame visible
        self.fkeyreview.grid(row=2, column=1, rowspan=15, columnspan=9)
        #set current frame variable so other frames know what to remove when switching
        self.currentframe=self.fkeyreview
        
        #testing
        self.hkeyreviewhands.showfinger("l1")
        self.hkeyreviewhands.showfinger("r5")
    def typingexercise(self):
        """ Type exercise frame
        This frame is dedicated to typing more coherently. It trains typing real world sentences, and builds speed and accuracy."""


    def customexercise(self):
        """ Custom typing exercise frame
        One might get bored by the built-in exercises, or find them less than useful.
        In that case the user can provide their own exercises here. It will subsequently be shown in the typing exercizes screen."""


    def progress(self):
        """ Progress frame
        Here the user can view some statistics about their progress."""

    def settings(self):
        """ Settings frame 
        Here you can configure some persistent settings about the application behavior."""
    
    def help_(self):
        """ Help frame
        Here you can find some basic information on how this application works."""
    
    def debug(self, message):
        """ Debug function
        If debug functionality is turned on, debug messages will be printed on the commandline."""
        if self.debug==True:
            print message


class Hands:
    def __init__(self, master, x, y):
        """ Initiates the hand graphics that indicate which fingers to use.
        master indicates the parent widget, x is the left top table column, y is the left to table row."""
        self.l5 = gui.Frame(master, bg="white", height=200, width=50)
        self.l4 = gui.Frame(master, bg="white", height=200, width=50)
        self.l3 = gui.Frame(master, bg="white", height=200, width=50)
        self.l2 = gui.Frame(master, bg="white", height=200, width=50)
        self.l1 = gui.Frame(master, bg="white", height=50, width=100)
        self.r1 = gui.Frame(master, bg="white", height=50, width=100)
        self.r2 = gui.Frame(master, bg="white", height=200, width=50)
        self.r3 = gui.Frame(master, bg="white", height=200, width=50)
        self.r4 = gui.Frame(master, bg="white", height=200, width=50)
        self.r5 = gui.Frame(master, bg="white", height=200, width=50)
        self.lp = gui.Frame(master, bg="white", height=150, width=275)
        self.rp = gui.Frame(master, bg="white", height=150, width=275)

        # place the fields on the grid
        
        #left hand
        self.l5.grid(row=y, column=x)
        self.l4.grid(row=y, column=x+2)
        self.l3.grid(row=y, column=x+4)
        self.l2.grid(row=y, column=x+6)
        self.lp.grid(row=y+1, column=x, rowspan=2, columnspan=7)
        self.l1.grid(row=y+2, column=x+8)
        
        #right hand
        self.r1.grid(row=y+2, column=x+10)
        self.rp.grid(row=y+1, column=x+11, rowspan=2, columnspan=7)
        self.r2.grid(row=y, column=x+11)
        self.r3.grid(row=y, column=x+13)
        self.r4.grid(row=y, column=x+15)
        self.r5.grid(row=y, column=x+17)

    def reset(self):
        self.l5["bg"]="white"
        self.l4["bg"]="white"
        self.l3["bg"]="white"
        self.l2["bg"]="white"
        self.l1["bg"]="white"
        self.lp["bg"]="white"
        self.rp["bg"]="white"
        self.r1["bg"]="white"
        self.r2["bg"]="white"
        self.r3["bg"]="white"
        self.r4["bg"]="white"
        self.r5["bg"]="white"
    
    def showfinger(self, finger):
        if(finger=="l5"):
            self.l5["bg"]="red"
        elif(finger=="l4"):
            self.l4["bg"]="red"
        elif(finger=="l3"):
            self.l3["bg"]="red"
        elif(finger=="l2"):
            self.l2["bg"]="red"
        elif(finger=="l1"):
            self.l1["bg"]="red"
        elif(finger=="r1"):
            self.r1["bg"]="red"
        elif(finger=="r2"):
            self.r2["bg"]="red"
        elif(finger=="r3"):
            self.r3["bg"]="red"
        elif(finger=="r4"):
            self.r4["bg"]="red"
        elif(finger=="r5"):
            self.r5["bg"]="red"


class CharacterSelection:
    def __init__(self, master, lFont):
        #TODO fetch from database which boxes should be ticked
        #initiate character states
        self.chars={}
        for c in "abcdefghijklmnopqrstuvwxyz":
            self.chars[c]=gui.IntVar()
            self.chars[c].set(1)
        for c in "1234567890":
            self.chars[c]=gui.IntVar()
            self.chars[c].set(1)
        for c in ".,!?\'\";:[]{}=+@#$%^&*()_-\\|/<>`~ ":
            self.chars[c]=gui.IntVar()
            self.chars[c].set(0)
        self.alpha=gui.IntVar()
        self.alpha.set(1)
        self.numeric=gui.IntVar()
        self.numeric.set(1)
        self.special=gui.IntVar()
        self.special.set(0)
        
        self.title=gui.Label(master, text=_("Characters to practice"),font=tkFont.Font(family="Arial", size=15))
        self.title.grid(row=1,column=1, columnspan=4)

        self.balpha=gui.Checkbutton(master, text=_("Alphabetic"), variable=self.alpha, command=lambda: self.toggle('alpha'))
        self.balpha.grid(row=2,column=1, sticky=gui.W)

        self.buttons={}
        r=2
        for c in "abcdefghijklmnopqrstuvwxyz1234567890":
            self.buttons[c]=gui.Checkbutton(master, text=c, variable=self.chars[c])
            self.buttons[c].grid(row=r, column=2, sticky=gui.W)
            r+=1

        self.bnumeric=gui.Checkbutton(master, text=_("Numeric"), variable=self.numeric, command=lambda: self.toggle('numeric'))
        self.bnumeric.grid(row=28,column=1, sticky=gui.W)
        
        r=2
        for c in ".,!?\'\";:[]{}=+@#$%^&*()_-\\|/<>`~ ":
            self.buttons[c]=gui.Checkbutton(master, text=c, variable=self.chars[c])   
            self.buttons[c].grid(row=r, column=4, sticky=gui.W)
            r+=1
        self.bspecial=gui.Checkbutton(master, text=_("Special"), variable=self.special, command=lambda: self.toggle('special'))
        self.bspecial.grid(row=2,column=3, sticky=gui.W) 


    def toggle(self, button):
        if(button=="alpha"):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if(self.alpha.get()==1):
                    self.chars[c].set(1)
                else:
                    self.chars[c].set(0)
        elif(button=="numeric"):
            for c in "1234567890":
                if(self.numeric.get()==1):
                    self.chars[c].set(1)
                else:
                    self.chars[c].set(0)
        if(button=="special"):
            for c in ".,!?\'\";:[]{}=+@#$%^&*()_-\\|/<>`~ ":
                if(self.special.get()==1):
                    self.chars[c].set(1)
                else:
                    self.chars[c].set(0)

    def pick(self):
        choice=self.characters.keys()[int(random.random()*len(d.keys()))]
        return choice

class KeyEvents:
    def __init__(self, element, target):
        """ Listen for keybindings and act accordingly with them """
        self.target=target

        for c in "abcdefghijklmnopqrstuvwxyz01234567890.,!?\'\";:[]{}=+@#$%^&*()_-\\|/<>`~ ":
            if(c=="<"):
                element.bind('<<>', lambda: self.key('<'))
            elif(c==" "):
                element.bind('<space>', lambda: self.key(' '))
            else:
                element.bind(c, lambda: self.key(c))

    def key(self, k):
        print('detected keypress:', k)
        self.target(k)

root = gui.Tk()

typetrainer = TypeTrainer(root)

root.mainloop()
root.destroy()
