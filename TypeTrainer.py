#!/usr/bin/python


import Tkinter as gui
import tkFont
import gettext
import os
import sqlite3

class TypeTrainer:
    def __init__(self, master):
         
        #TODO fetch persistant settings from database
        self.debug=True
        self.lang="nl"
        self.localepath=os.path.join(os.getcwd(), "locale")
        
        #set up gettext for internationalization
        t=gettext.translation(self.lang, self.localepath, fallback=True)
        _=t.ugettext
        
        #some fonts to use
        self.xxlFont = tkFont.Font(family="Arial", size=300)
        
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
        
        self.bhome = gui.Button(master, text=_("Home"), command=self.home)
        self.bhome.grid(row=1, column=1)

        self.bkeyreview = gui.Button(master, text=_("Key review"), command=self.keyreview)
        self.bkeyreview.grid(row=1, column=2)

        self.btypingexercise = gui.Button(master, text=_("Typing exercize"), command=self.typingexercise)
        self.btypingexercise.grid(row=1, column=3)

        self.bcustomexercise = gui.Button(master, text=_("Custom exercize"), command=self.customexercise)
        self.bcustomexercise.grid(row=1, column=4)

        self.bprogress = gui.Button(master, text=_("Progress"), command=self.progress)
        self.bprogress.grid(row=1, column=5)

        self.bsettings = gui.Button(master, text=_("Settings"), command=self.settings)
        self.bsettings.grid(row=1, column=6)

        self.bhelp = gui.Button(master, text=_("Help"), command=self.help_)
        self.bhelp.grid(row=1, column=7)

        self.bquit = gui.Button(master, text=_("Exit"), command=master.quit)
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
            self.fhomeltitle = gui.Label(self.fhome, text="Welcome to the asetniop type trainer!", font=self.xxlFont)
            self.fhomeltitle.grid(row=1, column=1, sticky=gui.W, columnspan=3)
            
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
            self.hkeyreviewltitle = gui.Label(self.fkeyreview, text="Key review", font=self.xxlFont)
            self.hkeyreviewltitle.grid(row=1, column=1, columnspan=3)
            
            #show hands to indicate fingerpress
            self.hkeyreviewhands = Hands(self.fkeyreview,2,2)
            
            #Label for key to press
            self.hkeyreviewassignment = gui.Label(self.fkeyreview, text="A", bg="white", font=self.xxlFont)
            self.hkeyreviewassignment.grid(row=5, column=11)

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
    def __init__(self, db):
        #fetch from database which boxes should be ticked
        


root = gui.Tk()

typetrainer = TypeTrainer(root)

root.mainloop()
root.destroy()
