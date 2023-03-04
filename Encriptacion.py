st = "\033[0m"
p = "\033[1;35m"
k = "\033[0;35m"
r = "\033[1;31m"
alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
moralf = [(".-", "A"), ("-...", "B"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"), ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"), ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"), ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-----", "0"), 
(".-.-.-", "."), ("--..--", ","), (".----.", "'"), ("---...", ":"), ("-....-", "-"), ("..--..", "?"), ("-..-.", "/"), (".--.-.", "@"), ("-...-", "="), ("-.-.--", "!"), ("-.--.", "("), ("-.--.-", ")"), (".-...", "&"), ("-.-.-.", ";"), (".-.-.", "+"), ("..--.-", "_"), (".-..-.", "\""), ("...-..-", "$"), (".--.-", "À"), (".-.-", "Ä"), (".--.-", "Å"), (".-.-", "Ą"), (".-.-", "Æ"), ("-.-..", "Ĉ"), ("-.-..", "Ć"), ("-.-..", "Ç"), ("----", "CH"), ("..-..", "Đ"), ("..--.", "Ð"), ("..-..", "É"), (".-..-", "È"), ("..-..", "Ę"), ("--.-.", "Ĝ"), 
("----", "Ĥ"), (".---.", "Ĵ"), (".-..-", "Ł"), ("--.--", "Ń"), ("--.--", "Ñ"), ("---.", "Ó"), ("---.", "Ö"), ("---.", "Ø"), ("...-...", "Ś"), ("...-.", "Ŝ"), ("----", "Š"), (".--..", "Þ"), ("..--", "Ü"), ("..--", "Ŭ"), ("--..-.", "Ź"), ("--..-", "Ż")]
atbp_1 = [p + "1:" + k, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
atbp_2 = [p + "2:" + k, "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
atbp_3 = [p + "3:" + k, "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", ".", ":", ";", "^", "!", "?", "¿", "=", "$", "%", "&", "/", "(", ")"]
atbp_4 = [p + "4:" + k, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
atbc_1 = [p + "1:" + k, "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
atbc_2 = [p + "2:" + k, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
atbc_3 = [p + "3:" + k, "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", ".", ":", ";", "^", "!", "?", "¿", "=", "$", "%", "&", "/", "(", ")"]
atbc_4 = [p + "4:" + k, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ciph = ["Text", "Decimal", "Caesar", "Hexadecimal", "Octal", "Binary", "Morse", "Atbash", "Roman numerals"]
ciph_m = ["t", "d", "c", "h", "o", "b", "m", "atb", "r"]
ind = [p + "Non-modifiable values:"]
cal = 0; indc = 0; key = 0; indi = 0; e = ""
sep = ""; shk = ""; lgk = ""; spc = ""
conc = []; conp = []; inte = 1; fog = 0     

#See how optimzed is the code, take a look
#Print the separation and the cipher alphabete used in the cipher

#Nuevos sistemas:
#   Roman numerals
#   Navajo code
#   Base64
#   Enigma
#   Vigenere cipher
#   Baudot murray code
#   Pigpen cipher
#   ADFGVX cipher
###   SHA-1
###   MD5
###   Affine cipher

def dms(t, x, e):
    global cal
    if e == 1:
        print(r + "\nIntroduce a valid value" + st)
        quit()
    if e == 2:
        print(r + "\nThe value must not contain duplicate characters" + st)
        quit()
    else:
        if isinstance(x, str):
            print(p + "\n\nInitial cipher: " + k + ciph[ciph_m.index(typ_i)])
            print(p + "Convertion cipher: " + k + ciph[ciph_m.index(typ_f)])
            if e == 3:
                print(p + "Plaintext: " + k + str(cp))
                print(p + "Ciphertext: " + k + str(cc))
            print(p + "\nOriginal string: " + k + org)
            print(p + "Converted string: " + k + t + st + "\n")
        else:
            if cal == 0:
                print(p + "\n\nInitial cipher: " + k + ciph[ciph_m.index(typ_i)])
                print(p + "Convertion cipher: " + k + ciph[ciph_m.index(typ_f)])
                if e == 3:
                    print(p + "Plaintext: " + k + str(cp))
                    print(p + "Ciphertext: " + k + str(cc))
                print(p + "\nOriginal string: " + k + org)
                print(p + "Converted string (Key: " + str(x) + "): " + k + t + st + "\n")
                cal = 1
            else:
                print(p + "Converted string (Key: " + str(x) + "): " + k + t + st + "\n")

def c_lim(v, l, s):
    i = 0
    while i < l:
            try:
                p = alf.index(v[i])
            except:
                if v[i] not in ind and v[i] != " " and v[i] != "\t":
                    ind.append(k + v[i] + st)
            i += 1
    if len(ind) != 1:
        t = ""
        for i in range(len(ind)):
            t = t + ind[i] + " "
        print(t + "\n")

def pri(er):
    if typ_f != "t":
        eval(func_f)
    else:
        dms(w, w, er)

def fin(io, er):
    if indi == 0:
        dms(io, io, er)
    else:
        io = io + r + "\n(" + w + ")"
        dms(io, key, er)

#Inicial: Cifrado a texto: ---------------------------------------->

def atbat():
    global w
    global cc; global cp
    alsp = [atbp_1, atbp_2, atbp_3, atbp_4]; alsc = [atbc_1, atbc_2, atbc_3, atbp_4]; alfc = ""; alfp = ""; conp = []; conc = []
    pla = 1; cif = 1
    op = input(p + "Wanna use the default settings? " + k).lower()
    if op == "no" or op == "n":
        print(p + "\nWhich one is your plaintext alphabet?" + k)
        for i in range(len(alsp)):
            print(*alsp[i], " ")
        try:
            pla = int(input(p + "Input (0 to costum alphabet): " + k)) - 1
        except:
            dms(0, 0, 1)
        if pla > len(alsp) - 1 or pla < -1:
            dms(0, 0, 1)
        else:
            if pla == -1:
                alfp = str(input(p + "Insert your own alphabet: " + k))
        print(p + "\nWhich one is your ciphertext alphabet?" + k)
        for i in range(len(alsc)):
            print(*alsc[i], " ")
        try:
            cif = int(input(p + "Input (0 to costum alphabet): " + k)) - 1
        except:
            dms(0, 0, 1)
        if cif > len(alsc) - 1 or cif < -1:
            dms(0, 0, 1)
        else:
            if cif == -1:
                alfc = str(input(p + "Insert your own alphabet: " + k))
        if pla == -1 and cif == -1:
            if len(alfp) < len(alfc):
                dms(0, 0, 1)
            else:
                conc = dup(alfc, conc)
                conp = dup(alfp, conp)
        elif pla == -1:
            if len(alfp) < len(alsc[cif]):
                dms(0, 0, 1)
            else:
                conp = dup(alfp, conp)
                conc = bor(conc, alsc, cif)
        elif cif == -1:
            if len(alfc) > len(alsp[pla]):
                dms(0, 0, 1)
            else:
                conc = dup(alfc, conc)
                conp = bor(conp, alsp, pla)        
        else:
            conc = bor(conc, alsc, cif)
            conp = bor(conp, alsp, pla)
    elif op == "yes" or op == "y" or op == "":
        conc = bor(conc, alsc, cif)
        conp = bor(conp, alsp, pla)
    else:
        dms(0, 0, 1)
    cc = conc; cp = conp; i = 0
    while len(conc) != len(conp):
        if not conp[i] in conc:
            conc.append(conp[i])
        i += 1
    print(p + "\nIndicate your case strategy: \n Mantaine case (1)\n Ignore case (2)\n Strict A ≠ a (3)" + k)
    try:
        inte = int(input(p + "Indicate your value: " + k))
        if inte > 3 or inte < 1: 
            dms(0, 0, 1)
    except ValueError:
        dms(0, 0, 1)
    print(p + "\nForeign characters: \n Include(1) \n Ignore(2)" + k)
    try:
        fog = int(input(p + "Indicate your value: " + k))
        if fog != 1 and fog != 0:
            dms(0, 0, 1)
    except ValueError:
        dms(0, 0, 1)
    x = w; t = ""
    for i in range(len(x)):
        try:
            if inte == 1:
                n = conp.index(x[i].lower())
                if x[i].isupper():
                    t = t + conc[n].upper()
                else:
                    t = t + conc[n]
            if inte == 2:
                x = x.lower()
                n = conp.index(x[i].lower())
                t = t + conc[n]
            if inte == 3:
                n = conp.index(x[i])
                t = t + conc[n]
        except:
            if fog == 1:
                t = t + x[i]
    w = t
    pri(3)

def mat():
    global w
    sep = " "; lgk = "-"; shk = "."; spc = "/"; cont = []
    qs = input(p + "Wanna use the default settings to convert? " + k).lower()
    if qs == "no" or qs == "n":
        sep = input(p + "Intra-character gap: " + k); cont.append(sep)
        shk = input(p + "Short mark: " + k); cont.append(shk)
        lgk = input(p + "Long mark: " + k); cont.append(lgk)
        spc = input(p + "Word space: " + k); cont.append(spc)
        for i in range(4):
            j = i + 1
            if cont[i] == "":
                dms(0, 0, 1)
            while j != 4:
                if cont[i] == cont[j]:
                    dms(0, 0, 1)
                j += 1
    elif qs != "yes" and qs != "y" and qs != "":
        dms(0, 0, 1)
    w = w.replace(lgk, "-").replace(shk, ".")
    for i in range(len(w)):
        if w[i] != "." and w[i] != "-" and w[i] != "/" and w[i] != " " and w[i] != "":
            dms(0, 0, 1)
    f = ""
    while w != "":
        lug = []; rep = 0
        n = w.find(sep); 
        if n == -1:
            e = w; w = ""
        else:
            e = w[:n]; w = w[n + 1:]
        if e == spc:
            f = f + " "
        else:
            for i in range(len(moralf)):
                if e == moralf[i][0]:
                    rep += 1
                    lug.append(i)
            if rep == 1:
                f = f + moralf[lug[0]][1]
            else:
                if len(lug) == 0:
                    f = f + "#"
                else:
                    f = f + "("
                    for j in range(len(lug)):
                        f = f + moralf[lug[j]][1]
                        if j != len(lug) - 1:
                            f = f + ","
                    f = f + ")"
    w = f
    pri(0)
    
def bat():
    global w
    e = input(p + "What's the separation used on the string? " + k)
    pb = w.replace(e, ""); z = 0; v = ""
    if pb == "":
        dms(0, 0, 1)
    for i in range(len(pb)):
        if pb[i] != "0" and pb[i] != "1":
            dms(0, 0, 1)
    if e != "":
        w = w.replace(e, " ")
    while w != "":
        z = w.find(" ")
        if z == -1:
            v = v + chr(int(w[0:], 2))
            w = ""
        else:
            v = v + chr(int(w[0:z], 2))
            w = w[z+1::]
    w = v
    pri(0)
    
def oat():
    global w
    n = 1; alg = ""
    e = input(p + "What's the separation used on the string? " + k)
    pb = w.replace(e, "")
    if pb == "":
        dms(0, 0, 1)
    for i in range(len(pb)):
        try:
            if int(pb[i]) < 0 and int(pb[i]) > 8:
                dms(0, 0, 1)
        except:
            dms(0, 0, 1)
    if e != "":
        w = w.replace(e, " ")
    while w != "":
        s = w.find(" ")
        if s == -1:
            v = w[0:]
            w = ""
        else:
            v = w[0:s]
            w = w[s+1::]
        vt = 0; n = 0
        while n < len(v):
            z = int(v[n])
            vt = vt + (z * (8 ** (len(v) - n - 1)))
            n += 1
        alg = alg + chr(vt)
    w = alg
    pri(0)

def dat():
    global w
    dec = []
    e = input(p + "What's the separation used on the string? " + k)
    pb = w.replace(e, "")
    if pb == "":
        dms(0, 0, 1)
    for i in range(len(pb)):
        try:
            if int(pb[i]) > 8 and int(pb[i]):
                dms(0, 0, 1)
        except:
            dms(0, 0, 1)
    if e != "":
        w = w.replace(e, " ")
    for i in range(w.count(" ")):
        s = w.find(" ")
        dec.append(w[0:s])
        w = w[s+1::]
    if w != "":
        dec.append(w)
    w = ""
    for i in range(len(dec)):
        x = chr(int(dec[i]))
        w = w + x
    pri(0)

def hat():
    global w
    n = 1; car = []
    e = input(p + "What's the separation used on the string? " + k)
    pb = w.replace(e, "")
    pb = pb.upper()
    for i in range(len(pb)):
        if pb[i] not in hex:
            dms(0, 0, 1)
    w = w.upper()
    if e != "":
        w = w.replace(e, " ")
    for i in range(w.count(" ")):
        s = w.find(" ")
        car.append(w[0:s])
        w = w[s+1::]
    if w != "":
        car.append(w)
    w = ""
    for i in range(len(car)):
        vt = 0; n = 0
        while n < len(car[i]):
            v = car[i][n]
            v = int(hex.index(v))
            vt = vt + (v * (16 ** (len(car[i]) - n - 1)))
            n += 1
        w = w + chr(vt)
    pri(0)

def cat():
    global w
    global key
    global indi
    indi = 1
    if org.replace(" ", "") == "" and typ_f == "t":
        dms(0, 0, 1)
    try:
        n = input(p + "Key: " + k).lower().replace(" ", "")
        if n != "all" and n != "t" and n != "todo" and n != "a":
            n = int(n)
        else:
            n = "t"
    except:
        dms(0, 0, 1)
    l = len(w)
    if n == "t":
        while key <= len(alf) / 4 - 1:
            w = c_des(org, l, key)
            if typ_f != "t":
                eval(func_f)
            else:
                dms(w, key, 0)
            key += 1 
        if typ_f == "t":
            c_lim(w, l, 1)
    else:
        while n > len(alf) / 4:
            n -= int(len(alf) / 4)
        key = n
        w = c_des(w, l, n)
        if typ_f != "t":
            eval(func_f)
        else:
            dms(w, n, 0)
        if typ_f == "t":
            c_lim(w, l, 0)

def c_des(x, l, o):
    i = 0
    while i < l:
        try:
            p = alf.index(x[i])
        except:
            i += 1
            continue
        if p == 104:
            i += 1
            continue
        x = x[:i] + alf[(p + (int(len(alf) / 4 - o)))] + x[i+1:]
        i += 1
    return x

#Final: Texto a cifrado: ---------------------------------------->

def taatb():
    global cc; global cp; global indc; global conc; global conp; global inte; global fog
    if indc == 0:
        alsp = [atbp_1, atbp_2, atbp_3, atbp_4]; alsc = [atbc_1, atbc_2, atbc_3, atbp_4]; alfc = ""; alfp = ""; conp = []; conc = []
        pla = 0; cif = 0
        op = input(p + "\nWanna use the default settings? " + k).lower()
        if op == "no" or op == "n":
            print(p + "\nWhich one is your plaintext alphabet?" + k)
            for i in range(len(alsp)):
                print(*alsp[i], " ")
            try:
                pla = int(input(p + "Input (0 to costum alphabet): " + k)) - 1
            except:
                dms(0, 0, 1)
            if pla > len(alsp) - 1 or pla < -1:
                dms(0, 0, 1)
            else:
                if pla == -1:
                    alfp = str(input(p + "Insert your own alphabet: " + k))
            print(p + "\nWhich one is your ciphertext alphabet?" + k)
            for i in range(len(alsc)):
                print(*alsc[i], " ")
            try:
                cif = int(input(p + "Input (0 to costum alphabet): " + k)) - 1
            except:
                dms(0, 0, 1)
            if cif > len(alsc) - 1 or cif < -1:
                dms(0, 0, 1)
            else:
                if cif == -1:
                    alfc = str(input(p + "Insert your own alphabet: " + k))
            if pla == -1 and cif == -1:
                if len(alfp) < len(alfc):
                    dms(0, 0, 1)
                else:
                    conc = dup(alfc, conc)
                    conp = dup(alfp, conp)
            elif pla == -1:
                if len(alfp) < len(alsc[cif]):
                    dms(0, 0, 1)
                else:
                    conp = dup(alfp, conp)
                    conc = bor(conc, alsc, cif)
            elif cif == -1:
                if len(alfc) > len(alsp[pla]):
                    dms(0, 0, 1)
                else:
                    conc = dup(alfc, conc)
                    conp = bor(conp, alsp, pla)        
            else:
                conc = bor(conc, alsc, cif)
                conp = bor(conp, alsp, pla)
        elif op == "yes" or op == "y" or op == "":
            conc = bor(conc, alsc, cif)
            conp = bor(conp, alsp, pla)
        else:
            dms(0, 0, 1)
        cc = conc; cp = conp; i = 0
        while len(conc) != len(conp):
            if not conp[i] in conc:
                conc.append(conp[i])
            i += 1
        print(p + "\nIndicate your case strategy: \n Mantaine case (1)\n Ignore case (2)\n Strict A ≠ a (3)" + k)
        try:
            inte = int(input(p + "Indicate your value: " + k))
            if inte > 3 or inte < 1: 
                dms(0, 0, 1)
        except ValueError:
            dms(0, 0, 1)
        print(p + "\nForeign characters: \n Include(1) \n Ignore(2)" + k)
        try:
            fog = int(input(p + "Indicate your value: " + k + "\n"))
            if fog != 1 and fog != 0: 
                dms(0, 0, 1)
        except ValueError:
            dms(0, 0, 1)
        indc = 1
    x = w; t = ""
    for i in range(len(x)):
        try:
            if inte == 1:
                n = conp.index(x[i].lower())
                if x[i].isupper():
                    t = t + conc[n].upper()
                else:
                    t = t + conc[n]
            if inte == 2:
                x = x.lower()
                n = conp.index(x[i].lower())
                t = t + conc[n]
            if inte == 3:
                n = conp.index(x[i])
                t = t + conc[n]
        except:
            if fog == 1:
                t = t + x[i]
    fin(t, 3)

def dup(ci, cf):
    for i in range(len(ci)):
        if ci[i].lower() in cf or ci[i].upper() in cf:
            dms(0, 0, 2)
        cf.append(ci[i])
    return(cf)

def bor(cf, ci, fc):
    del ci[fc][0]
    cf = ci[fc]
    return cf

def tam():
    global indc; global sep; global shk; global lgk; global spc
    if indc == 0:
        qs = input(p + "\nWanna use the default settings to convert? " + k).lower()
        sep = " "; lgk = "-"; shk = "."; spc = "/"
        if qs == "no" or qs == "n":
            sep = input(p + "Intra-character gap: " + k)
            shk = input(p + "Short mark: " + k)
            lgk = input(p + "Long mark: " + k)
            spc = input(p + "Word space: " + k)
        elif qs != "yes" and qs != "y" and qs != "":
            dms(0, 0, 1)
        indc = 1
    x = w.upper(); io = ""
    for i in range(len(x)):
        for j in range(len(moralf)):
            if x[i] == moralf[j][1]:
                io = io + moralf[j][0].replace(".", shk).replace("-", lgk) + sep
                break
            elif j == len(moralf) - 1:
                if x[i] == " ":
                    io = io + spc + sep
                else:
                    io = io + "#" + sep
    io = io[:len(io) - 1]
    fin(io, 0)

def tab():
    global indc; global e
    if indc == 0:
        e = input(p + "\nWhat separation you want to use? " + k)
        indc = 1
    io = ""
    for i in range(len(w)):
        u = ord(w[i])
        io = io + bin((u))[2:] + e
    if e != "":
        io = io[:len(io) - 1]
    fin(io, 0)

def tad():
    global indc; global e
    if indc == 0:
        e = input(p + "\nWhat separation you want to use? " + k)
        indc = 1
    x = ""
    for i in range(len(w)):
        u = ord(w[i])
        x = x + str(u) + e
    if e != "":
        x = x[:len(x) - 1]
    fin(x, 0)

def tao():
    global indc; global e
    if indc == 0:
        e = input(p + "\nWhat separation you want to use? " + k)
        indc = 1
    v = 0; n = 0; h = ""
    for i in range(len(w)):
        t = ""
        u = ord(w[i])
        n = u
        while n > 8:
            n = int(n / 8)
            v = u - n * 8
            t = str(v) + t
            u = n
        if n != 0:
            t = str(n) + t
        i += 1
        if i == len(w):
            h = h + t
        else:
            h = h + t + e
    fin(h, 0)

def tah():
    global indc; global e
    if indc == 0:
        e = input(p + "\nWhat separation you want to use? " + k)
        indc = 1
    v = 0; n = 0; h = ""
    for i in range(len(w)):
        t = ""
        u = ord(w[i])
        n = u
        while n > 16:
            n = int(n / 16)
            v = u - n * 16
            t = hex[v] + t
            u = n
        if n != 0:
            t = hex[n] + t
        i += 1
        if i == len(w):
            h = h + t
        else:
            h = h + t + e
    fin(h, 0)

def tac():
    if org.replace(" ", "") == "" and typ_i == "t":
        dms(0, 0, 1)
    try:
        n = input(p + "\nKey: " + k).lower()
        if n != "all" and n != "t" and n != "todo" and n != "a":
            n = int(n)
        else:
            n = "t"
    except:
        dms(0, 0, 1)
    l = len(w); o = 0
    if n == "t":
        while o <= len(alf) / 4 - 1:
            x = c_enc(w, l, o)
            dms(x, o, 0)
            o += 1
    else:
        while n > len(alf) / 4:
            n -= int(len(alf) / 4)
        x = c_enc(w, l, n)
        dms(x, n, 0)
    if typ_i == "t":
        c_lim(w, l, 0)

def c_enc(x, l, o):
    i = 0
    while i < l:
        try:
            p = alf.index(x[i])
        except:
            i += 1
            continue
        if p == 104:
            i += 1
            continue
        x = x[:i] + alf[int(p + o)] + x[i+1:]
        i += 1
    return x

print(p + "\nList:")
for i in range(len(ciph)):
    print(" ", ciph[i], "(" + ciph_m[i] + ")")
typ_i = str(input(p + "\nWhich is the cipher of your initial string? " + k)).lower()
typ_i = typ_i.replace(" ", "")

if typ_i in ciph_m:
    typ_f = str(input(p + "Which cipher you want to use to convert? " + k)).lower()
    if typ_f in ciph_m:
        if typ_f == typ_i:
            print(r + "\n   It's the same -_-\n" + st)
        else:
            org = input(p + "\nString: " + k)
            if org == "":
                dms(0, 0, 1)
            w = org
            func_i = typ_i + "at()"
            func_f = "ta" + typ_f + "()"
            if typ_i == "t":
                eval(func_f)
            else:
                eval(func_i)
    else:
        dms(0, 0, 1)
else:
    dms(0, 0, 1)