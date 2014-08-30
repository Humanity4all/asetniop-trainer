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
        self.a=gui.Checkbutton(master, text=_("a"), variable=self.chars['a'])
        self.a.grid(row=2,column=2, sticky=gui.W)
        self.b=gui.Checkbutton(master, text=_("b"), variable=self.chars['b'])       
        self.b.grid(row=3,column=2, sticky=gui.W)
        self.c=gui.Checkbutton(master, text=_("c"), variable=self.chars['c'])
        self.c.grid(row=4,column=2, sticky=gui.W)
        self.d=gui.Checkbutton(master, text=_("d"), variable=self.chars['d'])
        self.d.grid(row=5,column=2, sticky=gui.W)
        self.e=gui.Checkbutton(master, text=_("e"), variable=self.chars['e'])
        self.e.grid(row=6,column=2, sticky=gui.W)
        self.f=gui.Checkbutton(master, text=_("f"), variable=self.chars['f'])
        self.f.grid(row=7,column=2, sticky=gui.W)
        self.g=gui.Checkbutton(master, text=_("g"), variable=self.chars['g'])
        self.g.grid(row=8,column=2, sticky=gui.W)
        self.h=gui.Checkbutton(master, text=_("h"), variable=self.chars['h'])
        self.h.grid(row=9,column=2, sticky=gui.W)
        self.i=gui.Checkbutton(master, text=_("i"), variable=self.chars['i'])
        self.i.grid(row=10,column=2, sticky=gui.W)
        self.j=gui.Checkbutton(master, text=_("j"), variable=self.chars['j'])
        self.j.grid(row=11,column=2, sticky=gui.W)
        self.k=gui.Checkbutton(master, text=_("k"), variable=self.chars['k'])
        self.k.grid(row=12,column=2, sticky=gui.W)
        self.l=gui.Checkbutton(master, text=_("l"), variable=self.chars['l'])
        self.l.grid(row=13,column=2, sticky=gui.W)
        self.m=gui.Checkbutton(master, text=_("m"), variable=self.chars['m'])
        self.m.grid(row=14,column=2, sticky=gui.W)
        self.n=gui.Checkbutton(master, text=_("n"), variable=self.chars['n'])
        self.n.grid(row=15,column=2, sticky=gui.W)
        self.o=gui.Checkbutton(master, text=_("o"), variable=self.chars['o'])
        self.o.grid(row=16,column=2, sticky=gui.W)
        self.p=gui.Checkbutton(master, text=_("p"), variable=self.chars['p'])
        self.p.grid(row=17,column=2, sticky=gui.W)
        self.q=gui.Checkbutton(master, text=_("q"), variable=self.chars['q'])
        self.q.grid(row=18,column=2, sticky=gui.W)
        self.r=gui.Checkbutton(master, text=_("r"), variable=self.chars['r'])
        self.r.grid(row=19,column=2, sticky=gui.W)
        self.s=gui.Checkbutton(master, text=_("s"), variable=self.chars['s'])
        self.s.grid(row=20,column=2, sticky=gui.W)
        self.t=gui.Checkbutton(master, text=_("t"), variable=self.chars['t'])
        self.t.grid(row=21,column=2, sticky=gui.W)
        self.u=gui.Checkbutton(master, text=_("u"), variable=self.chars['u'])
        self.u.grid(row=22,column=2, sticky=gui.W)
        self.v=gui.Checkbutton(master, text=_("v"), variable=self.chars['v'])
        self.v.grid(row=23,column=2, sticky=gui.W)
        self.w=gui.Checkbutton(master, text=_("w"), variable=self.chars['w'])
        self.w.grid(row=24,column=2, sticky=gui.W)
        self.x=gui.Checkbutton(master, text=_("x"), variable=self.chars['x'])
        self.x.grid(row=25,column=2, sticky=gui.W)
        self.y=gui.Checkbutton(master, text=_("y"), variable=self.chars['y'])
        self.y.grid(row=26,column=2, sticky=gui.W)
        self.z=gui.Checkbutton(master, text=_("z"), variable=self.chars['z'])
        self.z.grid(row=27,column=2, sticky=gui.W)
        self.bnumeric=gui.Checkbutton(master, text=_("Numeric"), variable=self.numeric, command=lambda: self.toggle('numeric'))
        self.bnumeric.grid(row=28,column=1, sticky=gui.W)
        self.n1=gui.Checkbutton(master, text=_("1"), variable=self.chars['1'])
        self.n1.grid(row=28,column=2, sticky=gui.W)
        self.n2=gui.Checkbutton(master, text=_("2"), variable=self.chars['2'])
        self.n2.grid(row=29,column=2, sticky=gui.W)
        self.n3=gui.Checkbutton(master, text=_("3"), variable=self.chars['3'])
        self.n3.grid(row=30,column=2, sticky=gui.W)
        self.n4=gui.Checkbutton(master, text=_("4"), variable=self.chars['4'])
        self.n4.grid(row=31,column=2, sticky=gui.W)
        self.n5=gui.Checkbutton(master, text=_("5"), variable=self.chars['5'])
        self.n5.grid(row=32,column=2, sticky=gui.W)
        self.n6=gui.Checkbutton(master, text=_("6"), variable=self.chars['6'])
        self.n6.grid(row=33,column=2, sticky=gui.W)
        self.n7=gui.Checkbutton(master, text=_("7"), variable=self.chars['7'])
        self.n7.grid(row=34,column=2, sticky=gui.W)
        self.n8=gui.Checkbutton(master, text=_("8"), variable=self.chars['8'])
        self.n8.grid(row=35,column=2, sticky=gui.W)
        self.n9=gui.Checkbutton(master, text=_("9"), variable=self.chars['9'])
        self.n9.grid(row=36,column=2, sticky=gui.W)
        self.n0=gui.Checkbutton(master, text=_("0"), variable=self.chars['0'])
        self.n0.grid(row=37,column=2, sticky=gui.W)
        self.bspecial=gui.Checkbutton(master, text=_("Special"), variable=self.special, command=lambda: self.toggle('special'))
        self.bspecial.grid(row=2,column=3, sticky=gui.W)
        self.bperiod=gui.Checkbutton(master, text=_("."), variable=self.chars['.'])
        self.bperiod.grid(row=2,column=4, sticky=gui.W)
        self.bcomma=gui.Checkbutton(master, text=_(","), variable=self.chars[','])
        self.bcomma.grid(row=3,column=4, sticky=gui.W)
        self.bexclamation=gui.Checkbutton(master, text=_("!"), variable=self.chars['!'])
        self.bexclamation.grid(row=4,column=4, sticky=gui.W)
        self.bquestion=gui.Checkbutton(master, text=_("?"), variable=self.chars['?'])
        self.bquestion.grid(row=5,column=4, sticky=gui.W)
        self.bcolon=gui.Checkbutton(master, text=_(":"), variable=self.chars[':'])
        self.bcolon.grid(row=6,column=4, sticky=gui.W)
        self.bsemicolon=gui.Checkbutton(master, text=_(";"), variable=self.chars[';'])
        self.bsemicolon.grid(row=7,column=4, sticky=gui.W)
        self.bsq=gui.Checkbutton(master, text=_("'"), variable=self.chars['\''])
        self.bsq.grid(row=8,column=4, sticky=gui.W)
        self.bdq=gui.Checkbutton(master, text=_("\""), variable=self.chars['"'])
        self.bdq.grid(row=9,column=4, sticky=gui.W)
        self.blsb=gui.Checkbutton(master, text=_("["), variable=self.chars['['])
        self.blsb.grid(row=10,column=4, sticky=gui.W)
        self.brsb=gui.Checkbutton(master, text=_("]"), variable=self.chars[']'])
        self.brsb.grid(row=11,column=4, sticky=gui.W)
        self.blcb=gui.Checkbutton(master, text=_("{"), variable=self.chars['{'])
        self.blcb.grid(row=12,column=4, sticky=gui.W)
        self.brcb=gui.Checkbutton(master, text=_("}"), variable=self.chars['}'])
        self.brcb.grid(row=13,column=4, sticky=gui.W)
        self.beq=gui.Checkbutton(master, text=_("="), variable=self.chars['='])
        self.beq.grid(row=14,column=4, sticky=gui.W)
        self.bplus=gui.Checkbutton(master, text=_("+"), variable=self.chars['+'])
        self.bplus.grid(row=15,column=4, sticky=gui.W)
        self.bat=gui.Checkbutton(master, text=_("@"), variable=self.chars['@'])
        self.bat.grid(row=16,column=4, sticky=gui.W)
        self.bpound=gui.Checkbutton(master, text=_("#"), variable=self.chars['#'])
        self.bpound.grid(row=17,column=4, sticky=gui.W)
        self.bdollar=gui.Checkbutton(master, text=_("$"), variable=self.chars['$'])
        self.bdollar.grid(row=18,column=4, sticky=gui.W)
        self.bperc=gui.Checkbutton(master, text=_("%"), variable=self.chars['%'])
        self.bperc.grid(row=19,column=4, sticky=gui.W)
        self.bacc=gui.Checkbutton(master, text=_("^"), variable=self.chars['^'])
        self.bacc.grid(row=20,column=4, sticky=gui.W)
        self.bamp=gui.Checkbutton(master, text=_("&"), variable=self.chars['&'])
        self.bamp.grid(row=21,column=4, sticky=gui.W)
        self.bast=gui.Checkbutton(master, text=_("*"), variable=self.chars['*'])
        self.bast.grid(row=22,column=4, sticky=gui.W)
        self.blb=gui.Checkbutton(master, text=_("("), variable=self.chars['('])
        self.blb.grid(row=23,column=4, sticky=gui.W)
        self.brb=gui.Checkbutton(master, text=_(")"), variable=self.chars[')'])
        self.brb.grid(row=24,column=4, sticky=gui.W)
        self.bunder=gui.Checkbutton(master, text=_("_"), variable=self.chars['_'])
        self.bunder.grid(row=25,column=4, sticky=gui.W)
        self.bmin=gui.Checkbutton(master, text=_("-"), variable=self.chars['-'])
        self.bmin.grid(row=26,column=4, sticky=gui.W)
        self.bback=gui.Checkbutton(master, text=_("\\"), variable=self.chars['\\'])
        self.bback.grid(row=27,column=4, sticky=gui.W)
        self.bforw=gui.Checkbutton(master, text=_("/"), variable=self.chars['/'])
        self.bforw.grid(row=28,column=4, sticky=gui.W)
        self.bpipe=gui.Checkbutton(master, text=_("|"), variable=self.chars['|'])
        self.bpipe.grid(row=29,column=4, sticky=gui.W)
        self.bgreat=gui.Checkbutton(master, text=_(">"), variable=self.chars['>'])
        self.bgreat.grid(row=30,column=4, sticky=gui.W)
        self.bless=gui.Checkbutton(master, text=_("<"), variable=self.chars['<'])
        self.bless.grid(row=31,column=4, sticky=gui.W)
        self.btick=gui.Checkbutton(master, text=_("`"), variable=self.chars['`'])
        self.btick.grid(row=32,column=4, sticky=gui.W)
        self.btilde=gui.Checkbutton(master, text=_("~"), variable=self.chars['~'])
        self.btilde.grid(row=33,column=4, sticky=gui.W)
        self.bspace=gui.Checkbutton(master, text=_(" "), variable=self.chars[' '])
        self.bspace.grid(row=34,column=4, sticky=gui.W)


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

        # bind all keys
        element.bind('a', lambda: self.key('a'))
        element.bind('b', lambda: self.key('b'))       
        element.bind('c', lambda: self.key('c'))
        element.bind('d', lambda: self.key('d'))
        element.bind('e', lambda: self.key('e'))
        element.bind('f', lambda: self.key('f'))
        element.bind('g', lambda: self.key('g'))
        element.bind('h', lambda: self.key('h'))
        element.bind('i', lambda: self.key('i'))
        element.bind('j', lambda: self.key('j'))
        element.bind('k', lambda: self.key('k'))
        element.bind('l', lambda: self.key('l'))
        element.bind('m', lambda: self.key('m'))
        element.bind('n', lambda: self.key('n'))
        element.bind('o', lambda: self.key('o'))
        element.bind('p', lambda: self.key('p'))
        element.bind('q', lambda: self.key('q'))
        element.bind('r', lambda: self.key('r'))
        element.bind('s', lambda: self.key('s'))
        element.bind('t', lambda: self.key('t'))
        element.bind('u', lambda: self.key('u'))
        element.bind('v', lambda: self.key('v'))
        element.bind('w', lambda: self.key('w'))
        element.bind('x', lambda: self.key('x'))
        element.bind('y', lambda: self.key('y'))
        element.bind('z', lambda: self.key('z'))
        element.bind('1', lambda: self.key('1'))   
        element.bind('2', lambda: self.key('2'))
        element.bind('3', lambda: self.key('3'))
        element.bind('4', lambda: self.key('4'))
        element.bind('5', lambda: self.key('5'))
        element.bind('6', lambda: self.key('6'))
        element.bind('7', lambda: self.key('7'))
        element.bind('8', lambda: self.key('8'))
        element.bind('9', lambda: self.key('9'))
        element.bind('0', lambda: self.key('0'))

    def key(self, k):
        print('detected keypress:', k)
        self.target(k)

root = gui.Tk()

typetrainer = TypeTrainer(root)

root.mainloop()
root.destroy()
