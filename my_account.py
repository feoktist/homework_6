# Task 1.
# Добавляем сохранение суммы счета в файл.
# При первом открытии программы на счету 0 
# После пользования и выхода - сохраняем сумму счета
# При следующем открытии программы - читаем сохраненную сумму счета
# Task 2
# Добавить сохранение истории покупок в файл.

import os
import pickle

PURCHASE_HISTORY = 'purchase_history.data' 
USER_ACCOUNT = 'user_account.data'


# purchase_history = []
# orders = []

if os.path.exists(PURCHASE_HISTORY):
    with open(PURCHASE_HISTORY, 'rb') as fp:
        purchase_history = pickle.load(fp)



if os.path.exists(USER_ACCOUNT):
  with open(USER_ACCOUNT, 'rb') as fa:
    user_account = pickle.load(fa)
else:
   user_account = 0

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


#    elif choice == '2':
#        sum_purchase = int(input('Введите сумму покупки: '))
#        if sum_purchase > user_account:
#            print('Недостаточно средств')
#        else:
#            stuff = input('Введите название покупки: ')
#            purchases.append(stuff)
#            user_account = user_account - sum_purchase
#            history[stuff] = sum_purchase



    elif choice == '3':

        print('Funds left: ', user_account)

#        print('History of purchases: ')
#        for k, v in purchase_history.items():
#            print(k, v)


    elif choice == '4':
      with open(USER_ACCOUNT, 'wb') as fa:
        pickle.dump(user_account, fa)
        break

    else:
        print('Неверный пункт меню')