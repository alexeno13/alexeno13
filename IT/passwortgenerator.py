import random

def probably(chance):
    return random.random() < chance

def return_random_string_from_list(list):
    return list[random.randint(0,len(list)-1)]

def passwort_generieren(lenth = 12, k = None, g = None, z = None, s = None):
    buchstaben_klein = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    buchstaben_groß = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sonderzeichen = ["^", "@", "~", "#", "_", "-", "*", "+", ":", ";", ".", "/", "=", "%", "\\", "!", "?", "§", "&", "{", "[", "(", ")", "]", "}", "|", "<", ">", "$"]

    passwort = ""

    k = 1/3
    g = 1/3
    z = 1/3

    i = 0
    
    while i != lenth:
        if probably(k):
            passwort += return_random_string_from_list(buchstaben_klein)

        elif probably(g):
            passwort += return_random_string_from_list(buchstaben_groß)

        elif probably(z):
            passwort += return_random_string_from_list(zahlen)

        else:
            passwort += return_random_string_from_list(sonderzeichen)

        i += 1

    print("Passwort: " + passwort)

passwort_generieren()