import time


def list_passwort_generator(stellen : int):
    zeichen = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "^", "@", "~", "#", "_", "-", "*", "+", ":", ";", ".", "/", "=", "%", "\\", "!", "?", "§", "&", "{", "[", "(", ")", "]", "}", "|", "<", ">", "$"]
    zahl = len(zeichen)

    datei = open("IT/passwort.txt", "w")

    for i in range(len(zeichen)):    
        datei.writelines(zeichen[i] + "\n")

    datei.close()

    with open("IT/passwort.txt", "+r") as f:
        for k in range(stellen):
            for i in range(zahl):
                a = next(f, "-1")[:-1]
                #print(a)
                with open("IT/passwort.txt", "a") as d:
                    for j in zeichen:
                        passw = a + j + "\n"
                        #print(passw)
                        d.write(passw)
                time.sleep(0.000000000000001)
            zahl = zahl**(k+1)
    return 0

if __name__ == "__main__":
    list_passwort_generator(4)