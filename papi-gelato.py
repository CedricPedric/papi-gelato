print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

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
    allesmaken = ""

    for x in range(aantalbollen):
        smaken = smaak('Welke smaak wilt u voor bolletje nummer '+ str(aantalbollen) + ' A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
        aantalbollen = aantalbollen - 1
        allesmaken = allesmaken + " " + smaken

    if aantal >= 1 and aantal <= 3:
        if YesOrNoVraag('Wilt u deze ' + str(aantal) +'  bolletje(s) in A) een hoorntje of B) een bakje?'):
            print('Hier us u hoorntje met ' + str(aantal) + ' bolletje(s) ')
            print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))
        else:
            print('Hier us u bakje met ' + str(aantal) + ' bolletje(s) ')
            print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))

        if YesOrNoVraag('Wil u meer ijs bestellen? yes or no: '):
            print("")
        else:
            print('Bedankt en totziens!')
            break

    elif aantal >=4:
        print('Hier us u bakje met ' + str(aantal) + ' bolletje(s) ')
        print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))
        if YesOrNoVraag('Wil u meer ijs bestellen? yes or no: '):
            print("")
        else:
            print('Bedankt en totziens!')
            break
