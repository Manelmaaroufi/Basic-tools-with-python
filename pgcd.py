a=int(input('a'))
b=int(input('b'))


def pgcd(a,b):
    while(a!=b):
        if (a>b):
            a=a-b
        else:
            b=b-a
    return  a

p=pgcd(a,b) 
print('le pgcd  est : ' +str(p))             

