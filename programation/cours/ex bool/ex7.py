ligne = int(input("ligne : "))
colone = int(input("colone : "))

for i in range(1, ligne + 1):  
    for j in range(1, colone + 1):
            
        print("|{:{width}}".format(i * j, width=3), end=" | ")  
    print()
    print("-"*(colone*7))
        