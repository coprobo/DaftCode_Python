# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:04:35 2017

@author: piotr
"""

bool([])
#puste tuple, kolekcje, frozenset, set są False

bool({1,}) #to będzie prawdziwe


#typ None to jest brak wartosci
bool(None)

# dzielenie / jest typu float a dzielenie // jest typu 
#int (z zaokragleniem w dol)
#dzielenie z jedną i dwiema kreskami

#znajdowanie elementu w zbiorze
a = {1, 2, "ala, "m"}
1 in m
"b" not in a

a = [1, 2 ,4, 5.5, "asa", "ala"]
for i in a:
    print (i)

#enumerate pokazuje w ktorej ireracji sie jest
for x, i in enumerate(a):
    print(x, i)
    
#enumeracja w inny sposob

for m in enumerate(a):
    print(m[0],m[1])
    


# for else
for m in a:
    if m=='a':
        continue #mozna dac break
    print(m)
else: #to jest else dla for
    print("wszystko ok")