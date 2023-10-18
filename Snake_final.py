from tkinter import *

from random import *



#Déclaration des fonctions

#fonction permettant le déplacement et l'allongement du serpent 

def deplacement():

    global dx,dy,X1,Y1,X2,Y2,a,b,c,d,u,v,repas,serpent,score,serpentx,flag

    i = len(serpent)

    #Si la tête du serpent sort de la zone de jeu

    if (zone_jeu.coords(serpent[0])[0] < 0) or (zone_jeu.coords(serpent[0])[1] < 0):

        defaite()

        return

    if (zone_jeu.coords(serpent[0])[2] > 400) or (zone_jeu.coords(serpent[0])[3] > 400):

        defaite()

        return

    #Si la tête du serpent rencontre la pomme 

    if (zone_jeu.coords(serpent[0])[0] == X1) and (zone_jeu.coords(serpent[0])[1] == Y1)\
    and (zone_jeu.coords(serpent[0])[2] == X2) and (zone_jeu.coords(serpent[0])[3] == Y2):

        zone_jeu.delete(repas)

        repas=pomme()

        u = zone_jeu.coords(serpent[i-1])[0]

        v = zone_jeu.coords(serpent[i-1])[1]

        create_rectangle()

        serpent.append(serpentx)

    a = zone_jeu.coords(serpent[0])[0]

    b = zone_jeu.coords(serpent[0])[1]

    zone_jeu.move(serpent[0],dx,dy)

    #Boucle qui gère le déplacement de tout le serpent

    for j in range(1,i):

        c = zone_jeu.coords(serpent[j])[0]

        d = zone_jeu.coords(serpent[j])[1]

        zone_jeu.coords(serpent[j],a,b,a+10,b+10)

        a = c

        b = d

    #Boucle qui gère la collision de la tête du serpent avec le reste de son corps

    for k in range(1,i):

        if (zone_jeu.coords(serpent[0])[0] == zone_jeu.coords(serpent[k])[0])\
           and (zone_jeu.coords(serpent[0])[1] == zone_jeu.coords(serpent[k])[1])\
        and (zone_jeu.coords(serpent[0])[2] == zone_jeu.coords(serpent[k])[2]) \
        and (zone_jeu.coords(serpent[0])[3] == zone_jeu.coords(serpent[k])[3]):

            defaite()

            return

    fen.after(80,deplacement)

    

#Fonctions servant à diriger le serpent    

def droite(event):

    global dx,dy

    dx = 10

    dy = 0



def gauche(event):

    global dx,dy

    dx = -10

    dy = 0

  

def bas(event):

    global dx,dy

    dx = 0

    dy = 10

    

def haut(event):

    global dx,dy

    dx = 0

    dy = -10



#Fonction permettant l'apparition aléatoire d'une pomme  

def pomme():

    global X1,Y1,X2,Y2,texte_score,score,flag

    X1 = randrange(100,380,100)

    Y1 = randrange(100,380,100)

    X2 = X1+10

    Y2 = Y1+10

    if flag == 1 and X1 == 90 and Y1 >= 150 and Y1 <= 250 and Y2 >= 150 and Y2 <= 250:

        X1 = X1+10

        X2 = X2+10

    if flag == 1 and X1 == 300 and Y1 >= 150 and Y1 <= 250 and Y2 >= 150 and Y2 <= 250:

        X1 = X1+10

        X2 = X2+10

    if flag == 1 and Y1 == 190 and X1 >= 170 and X1 <= 230 and X2 >= 170 and X2 <= 230:

        Y1 = Y1+10

        Y2 = Y2+10

    new_pomme = zone_jeu.create_oval(X1,Y1,X2,Y2,fill='#ff0000')

    texte_score.pack_forget()

    score = score+10

    texte_score = Label(fen, text = 'Score: ' + str(score))

    texte_score.pack()

    return new_pomme



#Fonction permettant la création du corps du serpent        

def create_rectangle():

    global serpentx,u,v

    serpentx = zone_jeu.create_rectangle(u,v,u+10,v+10,outline='red',fill='green')



#Fonction qui crée un fenêtre secondaire qui indique une fin de partie

def defaite():

    fen.destroy()

    fen4 = Tk()

    fen4.geometry('500x250')

    fen4.title('Fin de partie')

    texte_defeat = Label(fen4, text='Défaite, vous avez perdu ! N\'hésitez pas à recommencer une partie. ;)')

    texte_defeat.pack()

    texte_score = Label(fen4, text = 'Score: ' + str(score))

    texte_score.pack()

    Bouton = Button(fen4, text ='Quitter', command = fen4.destroy)

    Bouton.pack()





#Fonction qui crée une nouvelle fenêtre   
def nouveaujeu():

    global dx,dy,X1,Y1,X2,Y2,repas,serpent,texte_score,score,zone_jeu,fen,flag

    #Attribution des valeurs initiales

    dx = 0

    dy = 0

    score = 0

    x1,y1,x2,y2 = 20,20,30,30

    X1,Y1,X2,Y2 = 210,210,220,220



    #Création de la fenêtre principale

    fen = Tk()

    fen.geometry('400x600')

    fen.title('Snake')



    #Création du canevas 

    zone_jeu = Canvas(fen,width=400,height=400,bg="grey")

    zone_jeu.pack()



    #Création d'éléments dans le canevas

    repas = zone_jeu.create_oval(X1,Y1,X2,Y2,fill='red')

    serpent1 = zone_jeu.create_rectangle(x1,y1,x2,y2,outline='red',fill='green')

    

    #Création de la liste correspondant au corps du serpent

    serpent = []

    serpent.append(serpent1)



    #Création des boutons et de l'interface des paramètres

    texte_limit = Label(fen, text='-------------------------------------Paramètres :------------------------------------')

    texte_limit.pack()

    texte_leave = Label(fen, text='Appuyer sur le bouton pour quitter le jeu')

    texte_leave.pack()

    Bouton = Button(fen, text ='Quitter', command = fen.destroy)

    Bouton.pack()

    texte_rule = Label(fen, text='Si vous désirez connaître les règles du jeu:')

    texte_rule.pack()

    Bouton1 = Button(fen, text ='Règles', command = règles)

    Bouton1.pack()

    texte_help = Label(fen, text='Si vous désirez connaître les commandes du jeu:')

    texte_help.pack()

    Bouton2 = Button(fen, text ='Commandes', command = commandes)

    Bouton2.pack()

    texte_score = Label(fen, text = 'Score: ' + str(score))

    texte_score.pack()



    #Affectation des fonctions liées au mouvement aux flèches directionnelles du clavier

    zone_jeu.bind_all('<Right>', droite)

    zone_jeu.bind_all('<Left>', gauche)

    zone_jeu.bind_all('<Down>', bas)

    zone_jeu.bind_all('<Up>', haut)

    

#Fonction qui crée un fenêtre secondaire contenant les commandes à utiliser 

def commandes():

     fen2 = Tk()

     fen2.geometry('600x150')

     fen2.title('Menu des commandes')

     texte_space = Label(fen2, text='')

     texte_space.pack()

     texte_help1 = Label(fen2, text='Les commandes du serpent sont:')

     texte_help1.pack()

     texte_help2 = Label(fen2, text='Haut   => Flèche directionnelle du haut')

     texte_help2.pack()

     texte_help3 = Label(fen2, text='Bas    => Flèche directionnelle du bas')

     texte_help3.pack()

     texte_help4 = Label(fen2, text='Droite => Flèche directionnelle de droite')

     texte_help4.pack()

     texte_help5 = Label(fen2, text='Gauche => Flèche directionnelle de gauche')

     texte_help5.pack()



#Fonction qui crée un fenêtre secondaire contenant les règles du jeu 

def règles():

    fen3 = Tk()

    fen3.geometry('600x150')

    fen3.title('Règles du jeu')

    texte_space = Label(fen3, text='')

    texte_space.pack()

    texte_rule1 = Label(fen3, text='Les règles du jeu SNAKE sont :')

    texte_rule1.pack()

    texte_rule2 = Label(fen3, text='1 => Consommer les pommes rouges pour obtenir 1 point sur le compteur.')

    texte_rule2.pack()

    texte_rule3 = Label(fen3, text='2 => Eviter les exrémités de la zone de jeu pour ne pas mourir.')

    texte_rule3.pack()

    texte_rule4 = Label(fen3, text='3 => Le serpent ne doit pas se toucher lui-même.')

    texte_rule4.pack()

    texte_rule5 = Label(fen3, text='4 => Attention: Si vous dirigez le')
    texte_rule5.pack()
    texte_rule6 = Label(fen3,text='serpent dans la direction opposée\
de son sens de déplacement, il va toucher son propre corps.')
    texte_rule6.pack()

    
flag = 0

nouveaujeu()


deplacement()

fen.mainloop()
