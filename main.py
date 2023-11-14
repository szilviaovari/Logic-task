# eloetel
zoldsegleves: str = None
husleves: str = None
gyumolcsleves: str = None

# foetel
sultcsirkecomb: str = None
sultCsirkemell: str = None
rakottzoldseg: str = None
spagetti: str = None
pizza: str = None

# koret
rizs: str = None
paroltzoldseg: str = None
gyumolcs: str = None
sultkrumpli: str = None
salata: str = None
kola: str = None

# menu

print("Kérem jelezze a menüben szereplő ételeket/köreteket! ( Amennyiben kér i betű amennyiben nem Enter-rel léphet tovább )")

print("Előétel:")

print(f"Zöldségleves[i]: ", end="")
zoldsegleves = str(input()).lower()

print(f"Húsleves[i]: ", end="")
husleves = str(input()).lower()

print(f"Gyümölcsleves[i]: ", end="")
gyumolcsleves = str(input()).lower()

print("Főétel:")

print(f"Sült Csirkecomb[i]: ", end="")
sultcsirkecomb = str(input()).lower()

print(f"Sült Csirkemell[i]: ", end="")
sultCsirkemell = str(input()).lower()

print(f"Rakottzöldség[i]: ", end="")
rakottzoldseg = str(input()).lower()

print(f"Spagetti[i]: ", end="")
spagetti = str(input()).lower()

print(f"Pizza[i]: ", end="")
pizza = str(input()).lower()

print("Köret:")

print(f"Rizs[i]: ", end="")
rizs = str(input()).lower()

print(f"Pároltzöldség[i]: ", end="")
paroltzoldseg = str(input()).lower()

print(f"Gyümölcs[i]: ", end="")
gyumolcs = str(input()).lower()

print(f"Sültkrumpli[i]: ", end="")
sultkrumpli = str(input()).lower()

print(f"Saláta[i]: ", end="")
salata = str(input()).lower()

print(f"Kóla[i]: ", end="")
kola = str(input()).lower()

# menu ertekelese
print("A menü értékelése:", end="")
if (zoldsegleves == "i" and pizza != "i" or spagetti != "i"):
    if (salata == "i" and gyumolcs == "i"):
        if (rizs == "i"):
            print(f"Fitnesz menü", end="")

    elif (zoldsegleves == "i" and gyumolcsleves != "i"):
        if (sultCsirkemell != "i" or sultkrumpli != "i" and salata == "i"):
            if (pizza != "i"):
                if(rakottzoldseg != "i"):
                    print(f"Kiváló", end="")

    elif (spagetti == "i"):
        if(gyumolcs == "i" and kola == "i"):
            if (salata != "i" and paroltzoldseg != "i"):
                print(f"Napi menü", end="")

    elif (gyumolcsleves == "i"):
        if(salata == "i" and gyumolcs != "i"):
            print(f"Vasárnapi menü", end="")    
else:
    print("Egyik kategória sem")

# A mai menu tartalma
print("")

print("A mai menü tartalma: ", end="")
if (zoldsegleves == "i"):
    print(f"Zöldségleves, ", end="")

if (husleves == "i"):
    print(f"Húsleves, ", end="")

if (gyumolcsleves == "i"):
    print(f"Gyümölcsleves, ", end="")

if (sultcsirkecomb == "i"):
    print(f"SültcsirkeComb, ", end="")

if (sultCsirkemell == "i"):
    print(f"Sült Csirkemell, ", end="")

if (rakottzoldseg == "i"):
    print(f"Rakottzöldség, ", end="")

if (spagetti == "i"):
    print(f"Spagetti, ", end="")

if (pizza == "i"):
    print(f"Pizza, ", end="")

if (rizs == "i"):
    print(f"Rizs, ", end="")

if (paroltzoldseg == "i"):
    print(f"Pároltzöldség, ", end="")

if (gyumolcs == "i"):
    print(f"Gyümölcs, ", end="")

if (sultkrumpli == "i"):
    print(f"Sültkrumpli, ", end="")

if (salata == "i"):
    print(f"Saláta, ", end="")

if (kola == "i"):
    print(f"Kóla, ", end="")