import athlete 
def categorie(age):
    if(age<12):
        print('le joueur est minime')
    elif(age<15): 
        print('le joueur est junior')   
    else:
        print('senior')    

a1=athlete.athletes('ahmed',14,'kick boxing')
a2=athlete.athletes('ameni',16,'kick boxing')
       
a1.affiche()
categorie(a1.age)
a2.affiche()
categorie(a2.age)
