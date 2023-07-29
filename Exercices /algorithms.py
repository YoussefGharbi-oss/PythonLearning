#Cryptage cesar level 1
ch1="ahmed"

ch2 = ""
for i in ch1:
    print(ord(i))

    if (ord(i) + 3 > 90) and (ord(i) + 3 < 97) :
        ch2=ch2+chr(ord(i)-23)
    elif(ord(i)+3 > 122)  :
        ch2 = ch2+chr(ord(i)-23)
    else:
       ch2 = ch2 + chr(ord(i)+3)

print(ch2)