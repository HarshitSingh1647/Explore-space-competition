from tkinter import*
from pygame import mixer
from PIL import ImageTk, Image
from tkinter import ttk
import random
import sys
import pyperclip



def ask():
    asktk=Tk()
    asktk.title(" ")
    
    asktk.resizable(0,0)
    asktk.attributes('-topmost',True)
    ASKl=Label(asktk,text="Quit application ?",font=("Calibri 20"))
    buttonno=Button(asktk,text="No",command=asktk.destroy,font=("Calibri 12"))
    YESBU=Button(asktk,text="Yes",command=sys.exit,font=("Calibri 12"))
    ASKl.grid(row=1,column=1)
    buttonno.grid(row=2,column=2)
    YESBU.grid(row=2,column=3)
    asktk.mainloop()

start = Tk()

start.protocol('WM_DELETE_WINDOW',ask)



start.attributes('-topmost',True)
screen_width = start.winfo_screenwidth()
screen_height = start.winfo_screenheight()
x = (screen_width//2)-(853//2)
y = (screen_height//2)-(480//2)-15
print(x," ",y,screen_height)




start.resizable(0,0)
start.geometry(f"853x480+{x}+{y}")
start.title("")
mylp=PhotoImage(file = "yo/universe.png")
myl=Label(start,image=mylp)

myl.pack(side="top")
mixer.init()
start.after(3000,start.destroy)
start.mainloop()
root2 = Tk()


root2.title("Explore Space")
root2.geometry("1000x600")
root2.resizable(0,0)
error=Tk()
error.withdraw()

try:
    import wikipedia
    
    import pywhatkit as kit
except:
    root2.destroy()
    with open("staror.py","w") as yo:
        yo.write("start=False")
    
    error.deiconify()
    error.title("Connection Error")
    def ok():
        
        error.destroy() 
    def quit():
        
        error.destroy()

  
    error.resizable(0,0)
    lable = Label(error,text="The application (Explore Space) needs active internet \n please close the application and restart after connecting the Computer to an active internet.",font=("Calibri 12"))
    cblah = Canvas(error)
    ex=Button(cblah,text="Quite",font=("Calibri 10"),command=quit)
    ok=Button(cblah,text="Okay",font=("Calibri 10"),command=ok)
    lable.pack(side="top")
    cblah.pack(side="top")
    ok.grid(row=1,column=1,sticky=E)
    ex.grid(row=1,column=2,sticky=E)
    error.mainloop()

from staror import start

if start == True:
    yoframe=Frame(root2)
    root2.protocol('WM_DELETE_WINDOW',sys.exit)
    main_frame=Frame(yoframe)
    

    canvas=Canvas(main_frame)
    canvas.pack(side="left",fill="both" , expand =1)
    
    sby=ttk.Scrollbar(root2, orient=VERTICAL,command=canvas.yview)
    sby.pack(side="right",fill=Y)

    sbx=ttk.Scrollbar(root2, orient=HORIZONTAL,command=canvas.xview)
    sbx.pack(side="bottom",fill=X)
    main_frame.pack(fill=BOTH,expand=1)
    yoframe.pack(fill=BOTH,expand=1,side="top")
    canvas.configure(yscrollcommand=sby.set,xscrollcommand=sbx.set)
    canvas.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    yoframe.configure(bg="light grey")
    root2.configure(bg="light grey")
    root=Frame(canvas)
    root.configure(bg="light grey")
    main_frame.configure(bg="light grey",border=0)
    canvas.configure(bg="light grey",border=0)
    blahframe=Canvas(canvas,bg="light grey",border=0)

    canvas.create_window((0,0),window=blahframe,anchor=NW)





    def dothis():
        
        root2.resizable(1,1)
        
        canvas.delete("all")
        canvas.create_window((0,0),window=root,anchor=NW)
    main_frame.configure(bg="grey")
    
    mylist=[2,1,3]
    yoran=random.choice(mylist)
    cil=PhotoImage(file= f"speakers/{yoran}.png" )

    mywe=["welcome to the world of giants!  ","welcome let's explore the mysterious space!  ","welcome let's have a astronomical tour!  "]
    welcomel=random.choice(mywe)
    firstl=Label(blahframe,border=0,image=cil,text=f"Hello!\n {welcomel}",font=("Arial 25"),compound="left",bg="white")
    firstb=Button(blahframe,border=0,text="  x  ",font=("Arial 15"),command=dothis)
    canclel=Label(blahframe,text="<- Click to proceed",border=0,font=("Calibri 15"),bg="light grey")
    canclel.grid(row=1,column=2,sticky="w")
    firstl.grid(row=2,column=2)
    firstb.grid(row=1,column=1)
    
    def wiki2():
        r1123=entry.get()
        if text["state"] == "disable":
            text.configure(state="normal")
        try:


                results = wikipedia.summary(f"({entry.get()})", sentences=5)

                text.insert(1.0,results)
                pyperclip.copy(results)
        except:
            kit.search(r1123)      

    def wiki(self):
        r1245=entry.get()
        if text["state"] == "disable":
            text.configure(state="normal")
        try:


                results = wikipedia.summary(f"({entry.get()})", sentences=5)
                
                text.delete(1.0,END)
                text.insert(1.0,results)
                pyperclip.copy(results)
        except:
            kit.search(r1245)      






    def pause():
        mixer.music.stop()
        plyab.grid_forget()
    def yout():
        kit.playonyt("facts on space")
    def goo():
        kit.search("facts on space")
    
    
    def play(no):
        mixer.music.load(f"audio/{no}.mp3")
        mixer.music.play()
        plyab.grid(row=1,column=0)
    def sho(yo):
        sby.pack_forget()
        sbx.pack_forget()
        main_frame.pack_forget()
        c56.pack(expand=1,fill=BOTH)
        cb.pack(side="top")
        
        
        sby1.pack(side="right",fill=Y)
        sbx1.pack(side="bottom",fill=X)
        canvas1.pack(side="left",fill="both" , expand =1)


        if yo==1:
            phl123.configure(image=i)

        if yo==2:
            phl123.configure(image=i2)
        if yo==3:
            phl123.configure(image=i3)
        if yo==4:
            phl123.configure(image=i4)
        if yo==5:
            phl123.configure(image=i5)
        if yo ==6:
            phl123.configure(image=i6)
        phl123.pack()
        
        main_frame1.pack(fill=BOTH,expand=1)
        yoframe1.pack(fill=BOTH,expand=1,side="top")

    c4=Canvas(root)

    scrollbar = Scrollbar(c4)
    scrollbar.pack(fill=Y,side="left")
    c=Canvas(root)
    text = Text(c4,yscrollcommand=scrollbar.set,font=("Arial",15),height=10,width=50,wrap=WORD)

    text.pack(side="right")


    scrollbar.config(command =text.yview )
    search = PhotoImage(file="se.png")
    sl = Button(c, image=search,border=0,command=wiki2)
    unilp = PhotoImage(file="yo/my.png")
    unil = Label(root, image=unilp,text="* How the universe was formed ?\t\n", compound="right",font=("Arial 30 underline"))
    unil.grid(row=11, column=1,columnspan=20,sticky="w")

    entry = Entry(c,width=40,border=0,font=("Calibri",20))
    c.configure(bg="black")



    c.grid(row=1,column=1,sticky="nw")
    sl.grid(row=1,column=1)
    entry.grid(row=1,column=2)

    label=Label(root,text="Listen to Audio books:   Click on the fact you want to listen.",font=("Calibri 20 underline"))
    label.grid(row=3,column=1,columnspan=3,sticky="w")

    c2=Canvas(root,bg="white")
    c3=Canvas(root,bg="white")
    web=Label(c3,text="web help? - ",font=("Calibri 20 underline"))
    you=PhotoImage(file="yo/youtube.png")
    youtube=Button(c3, image=you,command=yout)
    google=PhotoImage(file="yo/GOOGLE.png")
    g=Button(c3,image=google,command=goo)

    cs=Canvas(root,bg=None,height=20,width=10)
    cs.grid(row=6,column=1,sticky=W)
    pas=Label(root,text="Solar System and MilkyWay  :     Click on the fact you want to see." ,  font=("Calibri 20 underline"))
    pas.grid(row=7 ,column=1,sticky="ws",columnspan=5)
    cs2=Canvas(root,height=15,width=10)
    cs2.grid(row=8,column=1,sticky=W,columnspan=20)
    cp=Canvas(root,border=0,bg="white")
    cp.grid(row=9,column=1,sticky=W,columnspan=8)

    ph1=PhotoImage(file="solarfacts/1.png")
    ph2=PhotoImage(file="solarfacts/2.png")
    ph3=PhotoImage(file="solarfacts/3.png")
    ph4=PhotoImage(file="solarfacts/4.png")
    ph5=PhotoImage(file="solarfacts/5.png")
    ph6=PhotoImage(file="solarfacts/6.png")
    


    p1=Button(cp,image=ph1,command=lambda: sho(1))
    p2=Button(cp,image=ph2,command=lambda: sho(2))
    p3=Button(cp,image=ph3,command=lambda: sho(3))
    p4=Button(cp,image=ph4,command=lambda: sho(4))
    p5=Button(cp,image=ph5,command=lambda: sho(5))
    p6=Button(cp,image=ph6,command=lambda: sho(6))
    



    p1.grid(row=1,column=1)
    p2.grid(row=1,column=2)
    p3.grid(row=1,column=3)
    p4.grid(row=1,column=4)
    p5.grid(row=1,column=5)
    p6.grid(row=1,column=6)
    

    def disable():
        c56.pack_forget()
        cb.pack_forget()
        sby1.pack_forget()
        canvas1.pack_forget()
        phl123.pack_forget()
        sbx1.pack_forget()
        main_frame1.pack_forget()
        yoframe.pack_forget()
        sby.pack(side="right",fill=Y)


        sbx.pack(side="bottom",fill=X)

        yoframe.pack(fill=BOTH,expand=1,side="top")
        main_frame.pack(fill=BOTH,expand=1)


    mp1=Button(c2,text="facts1.mp3",font=("Calibri",15),border=0,bg="white",command=lambda :play(1))
    mp2=Button(c2,text="facts2.mp3",font=("Calibri",15),border=0,bg="white",command=lambda :play(2))
    mp3=Button(c2,text="facts3.mp3",font=("Calibri",15),border=0,bg="white",command=lambda :play(3))
    mp4=Button(c2,text="facts4.mp3",font=("Calibri",15),border=0,bg="white",command=lambda :play(4))
    mp5=Button(c2,text="facts5.mp3",font=("Calibri",15),border=0,bg="white",command=lambda :play(5))
    mp6=Button(c2,text="facts6.mp3",font=("Calibri",15),border=0,bg="white",command=lambda :play(6))

    c4.grid(row=1,column=2,rowspan=2,sticky="nw")
    c2.grid(row=4,column=1,columnspan=10,sticky="W")
    c3.grid(row=5,column=1,sticky="w")
    web.grid(row=1,column=1,columnspan=1,sticky="W")
    youtube.grid(row=1,column=2)
    g.grid(row=1,column=3)
    mp1.grid(row=1,column=1)
    mp2.grid(row=1,column=2)
    mp3.grid(row=1,column=3)
    mp4.grid(row=1,column=4)
    mp5.grid(row=1,column=5)
    mp6.grid(row=1,column=6)
    
    i=PhotoImage(file='yo/1.png')
    i2=PhotoImage(file="yo/2.png")
    i3=PhotoImage(file="yo/3.png")
    i4=PhotoImage(file="yo/4.png")
    i5=PhotoImage(file="yo/5.png")
    i6=PhotoImage(file="yo/6.png")
    
    c56=Canvas(yoframe,bg="white",width=3000,height=3000)
    cb=Button(c56,text="  X  ",bg= "red",fg="white",command=disable,border=0)
    yoframe1=Frame(c56)
    main_frame1=Frame(yoframe1)
            
            
    canvas1=Canvas(main_frame1)
    sbx1=ttk.Scrollbar(main_frame1, orient=HORIZONTAL,command=canvas1.xview)

    sby1=ttk.Scrollbar(main_frame1, orient=VERTICAL,command=canvas1.yview)
        
    canvas1.configure(yscrollcommand=sby1.set,xscrollcommand=sbx1.set)
    canvas1.bind("<Configure>",lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
    root3=Frame(canvas1)
    canvas1.create_window((0,0),window=root3,anchor=NE)
    hunil=Label(root,text="""Our universe began with an explosion of space itself - the Big Bang. 
    Starting from extremely high density and temperature, space expanded, the universe cooled, and the simplest elements formed. 
    Gravity gradually drew matter together to form the first stars and the first galaxies. 
    Galaxies collected into groups, clusters, and superclusters. 
    Some stars died in supernova explosions, whose chemical remnants seeded new generations of stars and enabled the formation of rocky planets.""",font=("Calibri 16"))
    hunil.grid(row=12,column=1,columnspan=50,sticky="w")
    phl123=Label(root3,image=i)
    bli=PhotoImage(file="yo/black hole.png")
    cs4=Canvas(root,width=10,height=20)
    cs4.grid(row=13,column=1)
    wabh=Label(root,text="*Do you know about Black Holes ?\t",font=("Calibri 30 underline"),image=bli,compound="right")
    wabh.grid(row=14,column=1,columnspan=10,sticky="w")
    cc=Canvas(root,bg=None,width=10,height=20)
    cc.grid(row=10,column=1)
    entry.bind("<Return>",wiki)
    plyab=Button(c2,text="  ||  ",command=pause,bg="white",border=0,font="Calibri 20")

    blcl = Label(root,text="""A black hole is a region of spacetime where gravity is so strong that nothing—no particles or even electromagnetic radiation such as light—can escape from it.
    The theory of general relativity predicts that a sufficiently compact mass can deform spacetime to form a black hole. The boundary of no escape is called the event horizon. 
    Although it has an enormous effect on the fate and circumstances of an object crossing it,
    according to general relativity it has no locally detectable features. 
    In many ways, a black hole acts like an ideal black body, as it reflects no light.
    This temperature is on the order of billionths of a kelvin for black holes of stellar mass, making it essentially impossible to observe directly""",font=("Calibri 13"))
    blcl.grid(row=15,column=1,columnspan=50,sticky="w")
    cs6=Canvas(root,height=20,width=10)
    cs6.grid(row=16,column=1)


    marsp = PhotoImage(file="yo/mars.png")
    marsl = Label(root,text="* Is life possible on Mars ? \t",font=("Calibri 30 underline"),image=marsp,compound="right")
    marsl.grid(row=17,column=1,columnspan=20,sticky="w")
    marslc = Label(root,text="""The possibility of life on Mars is a subject of interest in astrobiology due to its proximity and similarities to Earth. 
    To date, no proof of past or present life has been found on Mars.
    Cumulative evidence suggests that during the ancient Noachian time period, the surface environment of Mars had liquid water and may have been habitable for microorganisms, 
    but habitable conditions do not necessarily indicate life""", font=("Calibri 13"))
    marslc.grid(row=18,column=1,columnspan=20,sticky="w")
    c7=Canvas(root,width=10,height=25)
    c7.grid(row=19,column=1)


    moonp = PhotoImage(file="yo/moon.png")
    moonl=Label(root,text="* The earth's natural satellite!\t",image=moonp,compound="right",font=("Calibri 30 underline"))
    moonl.grid(row=20,column=1,columnspan=20,sticky="w")


    moonlc=Label(root,text="""The Moon is Earth's only natural satellite. 
    At about one-quarter the diameter of Earth (comparable to the width of Australia), 
    it is the largest natural satellite in the Solar System relative to the size of its planet, 
    the fifth largest satellite in the Solar System overall, and is larger than any known dwarf planet. 
    Orbiting Earth at an average distance of 384,400 km (238,900 mi), or about 30 times Earth's diameter, 
    its gravitational influence slightly lengthens Earth's day and is the main driver of Earth's tides.""",font=("Calibri 14"))
    moonlc.grid(row=21,column=1,columnspan=20,sticky="w")

    cs9=Canvas(root,height=25,width=10)
    cs9.grid(row=22,column=1)


    solarli=PhotoImage(file="yo/solar.png")
    solarlh=Label(root,text="*The great Solar system.\t",font=("Calibri 30 underline"),image=solarli,compound="right")
    solarlh.grid(row=23,column=1,columnspan=20,sticky="w")


    solarhc=Label(root,text="""The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly. 
    Of the objects that orbit the Sun directly, the largest are the eight planets, with the remainder being smaller objects, the dwarf planets and small Solar System bodies. 
    Of the objects that orbit the Sun indirectly—the natural satellites—two are larger than the smallest planet, Mercury.
    The Solar System formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. 
    The vast majority of the system's mass is in the Sun, with the majority of the remaining mass contained in Jupiter. 
    The four smaller inner system planets, Mercury, Venus, Earth and Mars, are terrestrial planets, being primarily composed of rock and metal.""",font=("Calibri 13"))
    solarhc.grid(row=24,column=1,sticky="w",columnspan=25)
    cs11=Canvas(root,width=10,height=20)
    cs11.grid(row=25,column=1)
    rakeshp=PhotoImage(file="yo/rakesh.png")
    rakeshl=Label(root,text="*Our pride , Rakesh Sharma. \t",font=("Calibri 30 underline"),image=rakeshp,compound="right")
    rakeshlc=Label(root,text="""An alumnus of the 35th National Defence Academy, Rakesh joined the Indian Air Force as a test pilot in 1970 and 
    progressed through numerous levels where in 1984 he was promoted to the rank of squadron leader.
    He was selected on 20 September 1982 to become a cosmonaut and go into space as part of a joint programme between the Indian Air Force and the Soviet Interkosmos space programme.
    Cosmonaut Rakesh Sharma and his suit at Nehru Planetarium
    In 1984, Sharma became the first Indian citizen to enter space.
    when he flew aboard the Soviet rocket Soyuz T-11 launched from Baikonur Cosmodrome in the Kazakh Soviet Socialist Republic on 3 April 1984.""",font=("Calibri 13"))
    rakeshl.grid(row=26,column=1,columnspan=20,sticky="w")
    rakeshlc.grid(row=27,column=1,columnspan=20,sticky="w")
    cs132=Canvas(root,width=10,height=20)
    cs132.grid(row=28,column=1)
    aslp=PhotoImage(file="yo/astroid.png")
    asl=Label(root,text="*The astroid belt.\t",font=("Calibri 30 underline"),image=aslp,compound="right")
    aslc=Label(root,text="""The asteroid belt is a torus-shaped region in the Solar System, located roughly between the orbits of the planets Jupiter and Mars. 
    It contains a great many solid, irregularly shaped bodies, of many sizes but much smaller than planets, called asteroids or minor planets. 
    This asteroid belt is also called the main asteroid belt or main belt to distinguish it from other asteroid populations in the Solar System such as near-Earth asteroids and trojan asteroids.
    The asteroid belt is the smallest and innermost known circumstellar disc in the Solar System. 
    About half its mass is contained in the four largest asteroids: Ceres, Vesta, Pallas, and Hygiea. 
    The total mass of the asteroid belt is approximately 4% that of the Moon.""",font=("Calibri 13"))
    asl.grid(row=29,column=1,columnspan=20,sticky="w")
    aslc.grid(row=30,column=1,columnspan=30,sticky="w")
    root2.mainloop()


if start==False:
    with open("staror.py","w") as yo:
            yo.write("start=True")
    sys.exit()