import os
def main():
    os.system('cls||clear')
    print('''

·▄▄▄▄   ▄▄▄· ▄▄▄  ▄ •▄     ·▄▄▄▄  ▄• ▄▌ ▐ ▄  ▄▄ • ▄▄▄ .       ▐ ▄ 
██▪ ██ ▐█ ▀█ ▀▄ █·█▌▄▌▪    ██▪ ██ █▪██▌•█▌▐█▐█ ▀ ▪▀▄.▀·▪     •█▌▐█
▐█· ▐█▌▄█▀▀█ ▐▀▀▄ ▐▀▀▄·    ▐█· ▐█▌█▌▐█▌▐█▐▐▌▄█ ▀█▄▐▀▀▪▄ ▄█▀▄ ▐█▐▐▌
██. ██ ▐█ ▪▐▌▐█•█▌▐█.█▌    ██. ██ ▐█▄█▌██▐█▌▐█▄▪▐█▐█▄▄▌▐█▌.▐▌██▐█▌
▀▀▀▀▀•  ▀  ▀ .▀  ▀·▀  ▀    ▀▀▀▀▀•  ▀▀▀ ▀▀ █▪·▀▀▀▀  ▀▀▀  ▀█▄▀▪▀▀ █▪

          ''')
    name=input("What is your character's name? ")
    
    print('''
Choose a race:
1) Human (120hp, 12 strength, 120 mana, 18% dodge)
2) Elf (100hp, 8 strength, 160 mana, 24% dodge)
3) Dwarf (160hp, 14 strength, 80 mana, 0% dodge)
4) Gnome (100hp, 10 strength, 50 mana, 25% dodge)
          ''')
    race=''
    while(race!='1' and race!='2' and race!='3' and race!='4'):
        race=input("Race? (option 1,2,3,4): ")
    
    print('''
Choose a class:
1) Fighter (+40hp, +4 strength, +6 dodge)
2) Mage (1.5x spell damage, +60 mana, +6 dodge)
3) Barbarian (+80hp, +6 strength, -20 mana)
          ''')
    classa=''
    while(classa!='1' and classa!='2' and classa!='3'):
        classa=input("Class? (option 1,2,3): ")
        

    
main()