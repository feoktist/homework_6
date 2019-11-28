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


purchase_items = []
purchase_history = {}

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
    print('4. проверка баланса')
    print('5. выход')
    print('\n')
    choice = input('Выберите пункт меню: ')
    print('\n')

# ------------- 1. Пополнение счета ------------
    if choice == '1':
        account_topup = int(input('Введите сумму пополнения: '))
        user_account = user_account + account_topup

# ------------ 2. Покупка ----------------------
    elif choice == '2':
        sum_purchase = int(input('Введите сумму покупки: '))
        
        if sum_purchase > user_account:
            print('Недостаточно средств')
        else:
            item = input('Введите название покупки: ')
            purchase_items.append(item)
            user_account = user_account - sum_purchase
            purchase_history[item] = sum_purchase

# ----------- 3. История покупок ---------------

    elif choice == '3':
        print('History of purchases: ')
        if len(purchase_history) == 0:
          print('No purchase history available')
        else:
          for k, v in purchase_history.items():
            print(k, v)

# ----------- 4. Проверка баланса --------------            

    elif choice == '4':
      print('Account balance: ', user_account)        

# ----------------- 5. ВЫХОД --------------------
    elif choice == '5':
      with open(USER_ACCOUNT, 'wb') as fa:
        pickle.dump(user_account, fa)
      
      with open(PURCHASE_HISTORY, 'wb') as fp:
        pickle.dump(purchase_history, fp)

      break

    else:
        print('Неверный пункт меню')

print('End of Program')