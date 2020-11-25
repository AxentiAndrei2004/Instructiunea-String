b=str(input('sirul de caractere este '))
Majuscule=0
Cifrele=0
Semnele=0
for n in b:
    if ord(n) in range (65,91):
        Majuscule+=1
    if ord(n) in range (97,122):
        Cifrele+=1
    if ord(n) in range(33,41) or ord(n) in range (58,64) or ord(n) in range (123,126):
        Semnele+=1
print ('Numarul de majuscule este %s' %(Majuscule))
print ('Numarul de cifre  este %s' %(Cifrele))
print ('Numarul de semne speciale este %s' %(Semnele))