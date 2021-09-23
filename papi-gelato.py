print("Welkom bij Papi Gelato.")

prijsBolletjes = 1.10
prijsHoorn = 1.25
prijsBakje = 0.75

totaalHoorn = 0
totaalBollen = 0
totaalBak = 0

allesmaken = ""

prijsSlagroom = 0.50
prijsSprinkles = 0.30
prijsCaramelSausH = 0.60
prijsCaramelSausB = 0.90
prijsLiter = 9.80

CaramelSausBakje = 0
CaramelSausHoorntje = 0
slagroom = 0
sprinkles = 0


totaalLiter = 0


def toppings():
    while True:
        toppingsInput = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
        if toppingsInput == 'A':
            return
        elif toppingsInput == 'B':
            global slagroom
            slagroom = slagroom + 1
            return 'Slagroom'
        elif toppingsInput == 'C':
            global sprinkles
            sprinkles = sprinkles + 1
            return 'Sprinkels'
        elif toppingsInput == 'D':
            return'Caramel'
    

def bonnetje():
    totaalPrijs = 0
    berekingBollen = totaalBollen * prijsBolletjes
    berekeningHoorn = totaalHoorn * prijsHoorn 
    berekeningBak = totaalBak * prijsBakje
    berekeningSlagroom = slagroom * prijsSlagroom
    berekeningSprinkels = sprinkles * prijsSprinkles
    berekeningCarmelH = prijsCaramelSausH * CaramelSausHoorntje
    berekeningCarmelB = CaramelSausBakje * prijsCaramelSausB
    totaalPrijsTop = berekeningSlagroom +  berekeningSprinkels + berekeningCarmelH + berekeningCarmelB
    totaalPrijs = berekeningHoorn + berekeningBak + berekingBollen + totaalPrijsTop

    print('Bolletjes = ' + str(totaalBollen) + ' x ' + str(prijsBolletjes) + ' = '  + str(berekingBollen) )
    if totaalBak > 0:
        print('Bakjes = ' + str(totaalBak) +' x ' + str(prijsBakje) + ' = ' + str(berekeningBak))
    if totaalHoorn > 0:
        print('Hoorntjes = ' + str(totaalHoorn) + ' x ' + str(prijsHoorn)+ ' = ' + str(berekeningHoorn))
    if slagroom > 0 or sprinkles > 0 or CaramelSausBakje > 0 or CaramelSausHoorntje > 0:
        print('Prijs topings = ' + str(totaalPrijsTop))
    print('Prijs in totaal = ' + str(totaalPrijs))
    

def hoeveelijs():
    while True:
        aantal = int(input('Hoeveel bolletjes wilt u?: '))
        if aantal < 8:
            return aantal
        else:
            print("Sorry zulke grote bakken hebben we niet!")

def YesOrNoVraag(vraag, optionsTrue = ['yes','ja', 'A', '1'], optionsFalse = ['no', 'nee', 'B', '2']):
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


if YesOrNoVraag('Bent u 1) particulier of 2) zakelijk?: '):
    while True:
        aantal = hoeveelijs()
        aantalbollen = aantal
        totaalBollen = totaalBollen + aantalbollen
    
        for x in range(aantalbollen):
            smaken = smaak('Welke smaak wilt u voor bolletje nummer '+ str(aantalbollen) + ' A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
            aantalbollen = aantalbollen - 1
            allesmaken = allesmaken + " " + smaken
    
        if aantal >= 1 and aantal <= 3:
            if YesOrNoVraag('Wilt u deze ' + str(aantal) +'  bolletje(s) in A) een hoorntje of B) een bakje?'):
                print('Hier us u hoorntje met ' + str(aantal) + ' bolletje(s) ')
                totaalHoorn = totaalHoorn + 1
                print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))
                topping = toppings()
                if topping ==  'Caramel':
                    CaramelSausHoorntje = CaramelSausHoorntje + 1
            else:
                print('Hier us u bakje met ' + str(aantal) + ' bolletje(s) ')
                totaalBak = totaalBak + 1
                print('de smaken die u heeft gekozen zijn smaken ' + str(allesmaken))
                topping = toppings()
                if topping == 'Caramel':
                    CaramelSausBakje = CaramelSausBakje + 1
    
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
            topping = toppings()
            if topping == 'Caramel':
                CaramelSausBakje = CaramelSausBakje + 1
    
            if YesOrNoVraag('Wil u meer ijs bestellen? yes or no: '):
                print("")
            else:
                bonnetje()
                print('Bedankt en totziens!')
                break
else:
    while True:
        aantalLiter = int(input("Hoeveel Liter Ijs wilt u? "))
        LiterLoop = aantalLiter

        for z in range(aantalLiter):
            smaken = smaak('Welke smaak wilt u voor Liter '+ str(LiterLoop) + ' A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
            LiterLoop = LiterLoop - 1
            allesmaken = allesmaken + " " + smaken

        berekeningZakelijk = aantalLiter * prijsLiter
        btw = (berekeningZakelijk / 100) * 9
        print('Liter =  ' + str(totaalLiter) + " x " + str(prijsLiter) + ' = ' + str(berekeningZakelijk))
        print('BTW (9%) = ' + str(btw) )
        print('Bedankt en totziens!')
        break