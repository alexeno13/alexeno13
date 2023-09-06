import random
import math

def passwort_generieren(lenth = 12):
    buchstaben_klein = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    buchstaben_groß = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sonderzeichen = ["^", "@", "~", "#", "_", "-", "*", "+", ":", ";", ".", "/", "=", "%", "\\", "!", "?", "§", "&", "{", "[", "(", ")", "]", "}", "|", "<", ">", "$"]

    sum = buchstaben_klein + buchstaben_groß + zahlen + sonderzeichen

    k_min = math.floor(lenth * (len(buchstaben_klein)/len(sum)))
    g_min = math.floor(lenth * (len(buchstaben_groß)/len(sum)))
    z_min = math.floor(lenth * (len(zahlen)/len(sum)))
    s_min = math.floor(lenth * (len(sonderzeichen)/len(sum)))

    passwort = random.choices(buchstaben_klein, k = k_min) + random.choices(buchstaben_groß, k = g_min) + random.choices(zahlen, k = z_min) + random.choices(sonderzeichen, k = s_min)\
          + random.choices(sum, k = lenth - k_min - g_min - z_min - s_min)

    random.shuffle(passwort)

    return "".join(passwort)

    

print(passwort_generieren())