c1=int(input("ecris 0 pour false et 1 pour true"))
c2=int(input("ecris 0 pour false et 1 pour true"))
if c1 == 1 :
    c1=True
elif c1 ==0:
    c1 = False        
else:
    print("error")
if c2 == 1 :
    c2=True
elif c2 ==0:
    c2 = False        
else:
    print("error")

if c1 and c2 is True:
    resultat=False
else :
    resultat=True    
print(resultat)     