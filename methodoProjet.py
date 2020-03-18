from tkinter import *
from random import *

# variables globales 

c=35 # dimension d'une case supposée carrée
x0,y0=50,50  #coordonnées du point en haut à gauche

#fonctions sur la grille

def creegrille(n, x):
    res=[0]*n
    for i in range(n):
        res[i]= [x]*n
    return res


def taille(grille):
    return len(grille)

# creation aléatoire de grilles avec tresors

def aleagrille(n,p):  # n taile de la grille p nombre d'objets
    m=creegrille(n,'_')
    cases=[(x,y) for x in range(n) for y in range(n) if x!=0 or y!=0]
    objets=sample (cases, p)
    for (i,j) in objets:
        m[i][j]=randint(0,1)
        
    for i in range (2):
        m[0][i]='b'
        m[1] [i]='b'

        m[i] [5]='w'
        m[i] [6]='w'

        
    for i in range (5,7,1):
        m[i] [5]='b'
        m[i] [6]='b'

        m[5] [i]='b'
        m[6] [i]='b'

        m[i][0]='w'
        m[i] [1]='w'

    for i in range (2,5,1):
        for y in range (2,5,1):
            m[i] [y] = 'r'

    m[5][3]='r'
    m[1][3]='r'
    m[3][5]='r'
    m[3][1]='r'
        
        
        
        
    
    return m


# fonctions sur les déplacements

##def deplacement(m,d, i,j):# deplacement de d à partir de la position i j
##    n=taille(m)
##    x,y,p=i,j,0
##    if d=="H":
##        x=i-1
##    elif d=='B':
##        x+=1
##    elif d=='G':
##        y-=1
##    else:
##        y+=1
##    if x in range(0,n) and y in range(0,n):
##        m[i][j]='_'
##        if m[x][y]==0:
##            p=5
##            changeScore(p)
##        elif m[x][y]==1:
##            p=-10
##            changeScore(p)
##        m[x][y]='*'
##        return (x,y,p)
##    else:
##        changeScore(-2)
##        return (i,j,-2)

def monquitter():
    dessin.quit()
    dessin.destroy()
    
def H():
    global pos
    res=deplacement(m, 'H', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
    
def D():
    global pos
    res=deplacement(m, 'D', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
    
def G():
    global pos
    res=deplacement(m, 'G', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)
def B():
    global pos
    res=deplacement(m, 'B', pos[0], pos[1])
    pos=res[0:2]
    dessineGrille(m)

def dessineGrille(m):
    can.delete(ALL)
    n=len(m)
    for i in range(n+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + n*c)
        can.create_line(x0, y0+c*i,x0+n*c ,y0+c*i)

    for i in range(n):
        for j in range(n):
            x=m[i][j]
            if x=='w':
                col="orange"
                can.create_oval(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=col)

            elif x=='b':
                col="black"
                can.create_oval(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=col)
            elif x=='r':
                col="red"
                can.create_oval(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=col)
m=""
pos=0,0
def new():
    global m
    global pos
    m=aleagrille(7,15)
    pos=0,0
    dessineGrille(m)
    cadre.pack(side=TOP)


            
## et les widgets

dessin=Tk()
Label(dessin,text="Jeu ",font=("Ubuntu",20,"bold")).pack()


can= Canvas(dessin,height=600,width=600,bg="white")
can.pack(side=LEFT)


bdem=Button(dessin,text="départ",command=new,font=("Ubuntu",20,"bold"))
bdem.pack(side=TOP)

cadre=Frame(dessin, pady=50, width=160)

BH=Button(cadre, command=H, text='H',font=("Ubuntu",20,"bold"))
BH.pack()
cadremilieu=Frame(cadre)
cadremilieu.pack()
BG=Button(cadremilieu, command=G, text='G',font=("Ubuntu",20,"bold"))
BD=Button(cadremilieu, command=D, text='D',font=("Ubuntu",20,"bold"))
BB=Button(cadre, command=B, text='B',font=("Ubuntu",20,"bold"))


BG.pack(side=LEFT)
BD.pack(side=LEFT)
BB.pack()

bq=Button(dessin,text="Quitter",command=monquitter,font=("Ubuntu",20,"bold"))
bq.pack(side=BOTTOM)  

cadreScore=Frame(dessin, pady=50, padx=20)
cadreScore.pack(side=BOTTOM)
lab=Label(cadreScore, text= "votre score",font=("Ubuntu",20,"bold"))
txt=Text(cadreScore, height=1, width=4,font=("Ubuntu",20,"bold"))
lab.pack(side=LEFT)
txt.pack(side=LEFT)


 


dessin.mainloop()

