#

import os

def main(): #functie
    print("upgrade = upgrade your linux")

    keuze = input("geef uw keuze ")#wat er geprint wordt
    if keuze == "upgrade":#als de keuze upgrade is gebeurt er iets, zo niet "foute keuze" door except line
        upgrade ="sudo apt update && sudo apt upgrade -y" #wanneer ik het woord upgrade schrijf in mijn script leest die dat als sudo apt.. upgrade is een variabele
        os.system(upgrade)#zo voer ik het door naar mijn systeem, op pc gaat niet, linux wel
    elif keuze ==  #else if, zelfde als if maar dan 2e keer. of 3e of 4e..


    else:
        print("foute keuze") #als mijn keuze upgrade is doet die dat. Als dat niet een vd ifs erboven is gaat die else doen
        main() #terug nr begin







if __name__ == '__main__':#als ik dit script run, runt de main
    main()