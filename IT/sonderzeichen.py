import random


sonderzeichen = ["^", "@", "~", "#", "_", "-", "*", "+", ":", ";", ".", "/", "=", "%", "\\", 
                 "!", "?", "'", '"', "§", "&", "{", "[", "(", ")", "]", "}", "|", "<", ">", "$"]
list = []
count = 0

passwort = input("Geben Sie das Passwort ein:")
for i in passwort:
    list.append(i)

for i in list:
    if i in sonderzeichen:
        count += 1

print("Anzahl der Sonderzeichen:" + str(count))

