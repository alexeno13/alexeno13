import itertools


def passw_gen(stelle):
    zeichen = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
               "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "^", "@", "~", "#", "_", "-", "*", "+", ":", ";", ".", "/", "=", "%", "\\", "!", "?", "§", "&", "{", "[", "(", ")", "]", "}", "|", "<", ">", "$"]

    list = []

    for i in range(stelle):
        for j in itertools.product(zeichen, repeat=i):
            list.append("".join(j) + "\n")
        with open("IT/passwort.txt", "a") as f:
            f.writelines(list)
        list = []

if __name__ == "__main__":
    passw_gen(4)