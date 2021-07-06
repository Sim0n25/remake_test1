#!/usr/bin/env python3

#een python toolscript om uw linux os te upgraden of maria db te installeren

import os

def main(): #functie

    # VARIABLES
    mariaDB ="sudo apt install mariadb-server"#variabele is mariaDB en die leest dat als mariadb-server

    # PRINTS
    print("upgrade = upgrade your linux")
    print("mariaDB = install mariadb")

    keuze = input("geef uw keuze ") #wat er geprint wordt
    if keuze == "upgrade": #als de keuze upgrade is gebeurt er iets, zo niet "foute keuze" door except line
        upgrade ="sudo apt update && sudo apt upgrade -y" #wanneer ik het woord upgrade schrijf in mijn script leest die dat als sudo apt.. upgrade is een variabele
        os.system(upgrade) #zo voer ik het door naar mijn systeem, op pc gaat niet, linux wel
        main()
    elif keuze == "mariaDB" : #else if, zelfde als if maar dan 2e keer. of 3e of 4e..
        os.system(mariaDB)
        main()
    else:
        print("foute keuze") #als mijn keuze upgrade is doet die dat. Als dat niet een vd ifs erboven is gaat die else doen
        main() #terug nr begin


if __name__ == '__main__':#als ik dit script run, runt de main
    main()