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

while True:
    aantal = hoeveelijs()
    if aantal >= 1 and aantal <= 3:
        if YesOrNoVraag('Wilt u deze ' + str(aantal) +'  bolletje(s) in A) een hoorntje of B) een bakje?'):
            print('Hier us u hoorntje met ' + str(aantal) + ' zoveel bollen')
        else:
            print('Hier us u bakje met ' + str(aantal) + ' zoveel bollen')
        if YesOrNoVraag('Wil u meer ijs bestellen? yes or no: '):
            print("")
        else:
            print('Bedankt en totziens!')


