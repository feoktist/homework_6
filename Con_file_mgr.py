import os
import sys

# http://senkler.blogspot.com/2011/04/python.html

curDir = os.getcwd()
print(curDir)

while True:
    print('\n')
    print('1. Создать папку ')
    print('2. Удалить (файл/папку ')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Сохранение содержимого рабочей директории в файл ')
    print('13. Выход')

    choice = input('Выберите пункт меню: ')
    print('\n')

    if choice == '1':
        print('Creating a folder..')

        new_path = r'Macintosh HD\Users\feoktist\PycharmProjects\homework_5\new_folder'
        if not os.path.exists('new_folder'):
            os.mkdir('new_folder')
        print('Done!')

    # ----- 2. удалить файл или папку ----------------------------

    elif choice == '2':
        print('Removing a folder...')
        if os.path.exists('new_folder'):
            os.rmdir('new_folder')
            print('Done!')
        else:
            print('No such folder exists')



    # -------- 3. Копировать файл/папку --------------------

    elif choice == '3':

        print('Copying a file or folder')
        if os.path.exists('new_folder'):
            new_folder_copy = shutil.copy('new_folder')
        print(new_folder_path)

    # ----------- 4. Просмотр содержимого в рабочей директории ------------

    # https://www.geeksforgeeks.org/python-shutil-copyfile-method/

    elif choice == '4':
        print(os.getcwd())
        print(os.listdir())


    # ------------ 5. Просмотр только папок ---------------------
    elif choice == '5':
        print(os.listdir())

    # ------------ 6. Просмотреть только файлы ------------------
    elif choice == '6':
        print(os.listdir())
    # ------------ 7. Просмотр информации об ОС -----------------
    elif choice == '7':
        print(os.uname())
    # ------------ 8. Создатель программы -----------------------
    elif choice == '8':
        print(sys.copyright)
    # ------------ 9. Играть в виикторину --------------------
    elif choice == '9':
        from victorina import *

    # ------------- 10. Мой банковский счет -------------------
    elif choice == '10':
        from my_account import *

    # -------------- 11. Смена рабочей директории --------------
    elif choice == '11':
        ch_path = r'Macintosh HD\Users\feoktist\PycharmProjects\homework_4'
        curDir = os.chdir(ch_path)


    # -------------- 12. Сохранение содержимого в рабочей директории ----
    elif choice == '12':
      files = os.listdir(curDir)
      with open('listdir.txt', 'w') as f:
        f.write('dirs: ')
        f.write(curDir)
        f.write('\n')
        f.write('files: ')
        f.write(str(files))


    # -------------- 13. Выход --------------------------------
    else:
        print('See ya!')
        break
