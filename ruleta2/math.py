import random

def hra_rulety(pocatecni_penize):
    penize = pocatecni_penize
    
    
    pravdepodobnost_cervena = 18 / 37
    pravdepodobnost_cierna = 18 / 37
    pravdepodobnost_zelena = 1 / 37
    
    while penize > 0:
        print(f"Stav vašich peněz: {penize} Kč")
        
        
        sazka = int(input("Sázíte kolik? "))
        
        
        if sazka > penize:
            print("Nemáte dostatek peněz na tuto sázku.")
            continue
        
        
        vysledek_rulety = random.randint(0, 36)
        
        
        if vysledek_rulety == 0:
            barva = "zelena"
        elif vysledek_rulety % 2 == 1:
            barva = "cervena"
        else:
            barva = "cerna"
        
       
        volba = input("Sázíte na červenou nebo černou? ").lower()
        
       
        if volba == barva:
            print(f"Padlo {barva}, vyhráli jste!")
            penize += sazka
        else:
            print(f"Padlo {barva}, prohráli jste.")
            penize -= sazka
        
    print("Hra skončila. Nemáte dostatek peněz na další sázky.")

if __name__ == "__main__":
    pocatecni_penize = int(input("Zadejte počáteční stav peněz: "))
    hra_rulety(pocatecni_penize)
