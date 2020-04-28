class athletes:
    def __init__(self,nom,age,sport):
        self.nom=nom
        self.age=age
        self.sport=sport

    def affiche(self):
        print('la personne %s d age %s joue au sport %s '% (self.nom,self.age,self.sport)) 
         
