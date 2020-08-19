def autentifikace(pokusy):
    passwords = {'bob': '123', 'ann': 'pass123', ' mike': 'password123', 'liz': 'pass123'}
    for a in range(pokusy,0,-1):
        print('-' * 40)
        print('Welcome to the app. Please log in: ')
        user_name = str(input('USERNAME: '))
        psw = str(input('PASSWORD: '))
        print('-' * 40)
        if passwords.get(user_name) != psw:
            print('Wrong user name and/or password !')
            print('{} log remain'.format(a-1))
        else:
            print('User verified')
            return True
    return False

def textselection():
    TEXTS = ['''
    Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',

             '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

             '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
             ]

    print('We have 3 texts to be analyzed.')
    text = 0
    while text not in range(1,4):
        text = int(input('Enter a number btw. 1 and 3 to select: '))
    print('-' * 40)
    text = TEXTS[text - 1]
    slova = text.split()
    return slova

def analyza(slova):
    titlecase = 0
    uppercase = 0
    lowercase = 0
    digit = 0
    soucet = 0
    pocet_slov = len(slova)
    print('There are {} words in the selected text.'.format(pocet_slov))
    for slovo in range(pocet_slov):
        if slova[slovo].istitle():
            titlecase += 1
        if slova[slovo].isupper():
            uppercase += 1
        if slova[slovo].islower():
            lowercase += 1
        if slova[slovo].isdigit():
            digit += 1
            x = int(slova[slovo])
            soucet = soucet + x
    print('There are {} titlecase words'.format(titlecase))
    print('There are {} uppercase words'.format(uppercase))
    print('There are {} lowercase words'.format(lowercase))
    print('There are {} numeric strings'.format(digit))
    print('If we sum all the numbers in this text we get : {}'.format(soucet))

def grafy(slova):
    dict = {}
    for slovo in slova:
        if len(slovo) in dict.keys():
            dict[len(slovo)] += 1
        else:
            dict[len(slovo)] = 1

    for klic in sorted(dict.keys()):
        print(klic, "*" * dict[klic], dict[klic])

def main():
    pocet_pokusu = 3
    if autentifikace(pocet_pokusu):
        slova = textselection()
        analyza(slova)
        grafy(slova)
    else:
        print('Wrong authorisation')


if __name__ == '__main__':
    main()
