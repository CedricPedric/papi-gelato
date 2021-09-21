print("Welkom bij Papi Gelato.")

prijsBolletjes = 1.10
prijsHoorn = 1.25
prijsBakje = 0.75
totaalHoorn = 0
totaalBollen = 0
totaalBak = 0


def bonnetje():
    totaalPrijs = 0
    berekingBollen = totaalBollen * prijsBolletjes
    berekeningHoorn = totaalHoorn * prijsHoorn 
    berekeningBak = totaalBak * prijsBakje
    totaalPrijs = berekeningHoorn + berekeningBak + berekingBollen
    print('Bolletjes = ' + str(totaalBollen) + ' x ' + str(prijsBolletjes) + ' = '  + str(berekingBollen) )
    if totaalBak > 0:
        print('Bakjes = ' + str(totaalBak) +' x ' + str(prijsBakje) + ' = ' + str(berekeningBak))
    if totaalHoorn > 0:
        print('Hoorntjes = ' + str(totaalHoorn) + ' x ' + str(prijsHoorn)+ ' = ' + str(berekeningHoorn))
    print('Prijs in totaal = ' + str(totaalPrijs))
    

def hoeveelijs():
    while True:
        aantal = int(input('Hoeveel bolletjes wilt u?: '))
        if aantal < 8:
            return aantal
        else:
            print("Sorry zulke grote bakken hebben we niet!")

def YesOrNoVraag(vraag, optionsTrue = ['yes','ja', 'A'], optionsFalse = ['no', 'nee', 'B']):
    while True:
        antwoord = input(vraag)
        if antwoord in optionsTrue:
            return True
        elif antwoord in optionsFalse:
            return False
        else:
            print('Dat begrijp ik niet')

def smaak(smaakvraag):
    inputSmaak = input(smaakvraag)
    if inputSmaak == 'A':
        return 'Aardbei'
    elif inputSmaak == 'C':
        return 'Chocolade'
    elif inputSmaak == 'M':
        return 'Munt'
    elif inputSmaak == 'V':
        return 'Vanille'
    else:
        print('Sorry dat snap ik niet...')
        return smaak(smaakvraag)

while True:
    aantal = hoeveelijs()
    aantalbollen = aantal
    totaalBollen = totaalBollen + aantalbollen
    allesmaken = ""

    for x in range(aantalbollen):
        smaken = smaak('Welke smaak wilt u voor bolletje nummer '+ str(aantalbollen) + ' A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
        aantalbollen = aantalbollen - 1
        allesmaken = allesmaken + " " + smaken

    if aantal >= 1 and aantal <= 3:
        if YesOrNoVraag('Wilt u deze ' + str(aantal) +'  bolletje(s) in A) een hoorntje of B) een bakje?'):
            print('Hier us u hoorntje met ' + str(aantal) + ' bolletje(s) ')
            totaalHoorn = totaalHoorn + 1
            print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))
        else:
            print('Hier us u bakje met ' + str(aantal) + ' bolletje(s) ')
            totaalBak = totaalBak + 1
            print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))

        if YesOrNoVraag('Wil u meer ijs bestellen? yes or no: '):
            print("")
        else:
            bonnetje()
            print('Bedankt en totziens!')
            break

    elif aantal >=4:
        print('Hier us u bakje met ' + str(aantal) + ' bolletje(s) ')
        totaalBak = totaalBak + 1
        print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))

        if YesOrNoVraag('Wil u meer ijs bestellen? yes or no: '):
            print("")
        else:
            bonnetje()
            print('Bedankt en totziens!')
            break
