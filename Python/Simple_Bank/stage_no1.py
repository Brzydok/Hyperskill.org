import random


cards = dict()
while True:
    what_to_do = input('1. Create an account\n''2. Log into account\n''0. Exit\n')
    if what_to_do == '1':
        card_number = '400000' + str(random.randint(0, 10 ** 9)).zfill(9) + '0'
        pin = str(random.randint(0, 10 ** 3)).zfill(4)
        cards[card_number] = pin
        print(f'\nYour card has been created\nYour card number:\n{str(card_number)}\nYour card PIN:\n{str(pin)}\n')
    elif what_to_do == '2':
        _card_number = input('\nEnter your card number:\n')
        _pin = input('Enter your PIN:\n'); print('')
        if _card_number not in cards or cards[_card_number] != _pin:
            print('\nWrong card number or PIN!\n')
        else:
            print('You have successfully logged in!\n')
            further_actions = input('1. Balance\n''2. Log out\n''0. Exit\n')
            if further_actions == '1':
                print('Balance: 0')
            elif further_actions == '2':
                print('\nYou have successfully logged out!\n')
            elif further_actions == '0':
                break
    elif what_to_do == '0':
        print('\nBye!')
        break
