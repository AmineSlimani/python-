# Debut de programme
casseur = "-"
casseur = casseur.center(70,"-")

print(casseur)

name = input("name : ")
name = str(name)

print(casseur)

francais = input("francais : ")
francais = float(francais)

print(casseur)

arabic = input("arabic : ")
arabic = float(arabic)

print(casseur)

math = input("math : ")
math = float(math)


print(casseur)

physics = input("physics : ")
physics = float(physics)

print(casseur)

svt = input(" Svt : ")
svt = float(svt)

print(casseur)

english = input(" English : ")
english = float(english)

print(casseur)

informatique = input("informatique : ")
informatique = float(informatique)

print(casseur)

education_islamic = input("Education islamic : ")
education_islamic = float(education_islamic)

print(casseur)

HG = input("HG : ")
HG = float(HG)

print(casseur)

sport = input("Sport : ")
sport = float(sport)

print(casseur)


somme_note = (francais + arabic + math)*5 + (HG*3) + (svt + education_islamic + sport + physics)*2 + (english + informatique)
somme_note = float(somme_note)

note = somme_note/28
note = float(note)



with open( "{}.pdf".format(name),"w") as std :

    std.write("\n Full name  : {} \n".format(name))
    std.write("\n {} \n".format(casseur))

    std.write("\n francais  : {} \n".format(francais))
    std.write("\n {} \n".format(casseur))

    std.write("\n arabic    : {} \n".format(arabic))
    std.write("\n {} \n".format(casseur))

    std.write("\n HG       : {} \n".format(HG))
    std.write("\n {} \n".format(casseur))

    std.write("\n EI      : {} \n".format(education_islamic))
    std.write("\n {} \n".format(casseur))

    std.write("\n sport   : {} \n".format(sport))
    std.write("\n {} \n".format(casseur))

    std.write("\n english : {} \n".format(english))
    std.write("\n {} \n".format(casseur))

    std.write("\n info    : {} \n".format(informatique))
    std.write("\n {} \n".format(casseur))

    std.write("\n svt {} \n".format(svt))
    std.write("\n {} \n".format(casseur))

    std.write("\n physics : {} \n".format(physics))
    std.write("\n {} \n".format(casseur))

    std.write("\n math : {} \n".format(math))
    std.write("\n {} \n".format(casseur))
    std.write("\n {} \n".format(casseur))


    std.write("\n somme note : {} \n".format(somme_note))
    std.write("\n {} \n".format(casseur))

    std.write("\n note : {} \n".format(note))
    std.write("\n {} \n".format(casseur))

# Fin de programme
