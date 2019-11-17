user_account = 0
purchases = []
history = {}
while True:
    print('\n')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    print('\n')

    if choice == '1':
        account_topup = int(input('Введите сумму пополнения: '))
        user_account = user_account + account_topup


    elif choice == '2':
        sum_purchase = int(input('Введите сумму покупки: '))
        if sum_purchase > user_account:
            print('Недостаточно средств')
        else:
            stuff = input('Введите название покупки: ')
            purchases.append(stuff)
            user_account = user_account - sum_purchase
            history[stuff] = sum_purchase



    elif choice == '3':

        print('Funds left: ', user_account)

        print('History of purchases: ')
        for k, v in history.items():
            print(k, v)


    elif choice == '4':
        break

    else:
        print('Неверный пункт меню')