owoce=['jablko','gruszka','sliwka'] 
owoce.append("pomarańcz")

print (owoce)
owoce += [owoce.pop(2)]
owoce[2] = ('cytryna')
print (owoce)
wybrany_obiekt = int(input("Podaj numer "))
print (wybrany_obiekt)
if wybrany_obiekt > len(owoce):
    print ("brawo, wypisales numer spoza listy...")
else:
 print(owoce[wybrany_obiekt])


