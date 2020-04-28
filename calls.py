import classes as personnes
k = personnes.Person
p1 = k("ahmed", 20)

def perso(nom,age):
    print('le nom est %s et son age est %s ' %(nom,age))  

print(p1.nom)
print(p1.age)
perso(p1.nom,p1.age)