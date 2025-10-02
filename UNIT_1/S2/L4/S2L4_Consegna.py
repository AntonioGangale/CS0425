
# data una figura geometrica calcolane il perimetro

# quadrato = lato * 4
# cerchio = 2 * pi greco * r
# triangolo = base / 2 + altezza / 2

while True:
    figura = input('\nInserisci una figura geometrica: ').lower()

    if figura == 'quadrato':
        lato = int(input('\nInserisci il valore del lato: '))
        perimetro = lato * 4
        print(f'\nIl perimetro del quadrato è "{perimetro}"')

    elif figura == 'cerchio':
        pigreco = 3.14
        raggio = float(input('\nInserisci il valore del raggio: '))
        circonferenza =  float(2 * pigreco * raggio)
        print(f'\nLa circonferenza del cerchio è "{circonferenza:.3f}"')

    elif figura == 'rettangolo':
        base = int(input('\nInserisci il valore della base: '))
        altezza = int(input("\nInserisci il valore dell'altezza: "))
        perimetro = (base * 2) + (altezza * 2)
        print(f'\nIl perimetro del rettangolo è "{perimetro}"')

    else:
        print('\nFigura non valida, riprova.')
        continue  #se sbagliato continua il ciclo ripartendo dall'inizio

    scelta = input('\nVuoi fare un altro calcolo? (s/n): ').lower()
    if scelta == 'n' or scelta == 'no':
        print('\nArrivederci\n')
        break  #se si sceglie di non continuare il programma si ferma



# Prova dell'esercizio precedente ma con 
# try/except per chiedere di reinserire 
# il numero se viene usato un carattere
# o un numero minore di 1
'''
while True:
    figura = input('\nInserisci una figura geometrica: ').lower()

    if figura == 'quadrato':
        while True: #si avvia un altro ciclo per capire se l'input è un numero
            try:
                lato = int(input('\nInserisci il valore del lato: '))  
                if lato < 1 :  #if per capire se è positivo
                    print('\nErrore: inserisci un numero positivo.')
                    continue  #se è 0 il ciclo ricomincia finché non viene inserito un n positivo
                break  #se n è positivo si ferma
            except ValueError: #eccetto se viene inserito un carattere che non è un numero
                print('\nErrore: devi inserire un numero.') 
                #se viene inserito un carattere diverso da
                #un numero, python si blocca e da errore
        perimetro = lato * 4
        print(f'\nIl perimetro del quadrato è "{perimetro}"')

'''
