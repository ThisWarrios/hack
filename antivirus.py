import os
import hashlib

while True:
    file = input('Введите полный путь файла: ')

    with open(file, 'rb') as f:
        hsh = hashlib.sha256()
        while True:
            data = f.read()
            if not data:
                break
            hsh.update(data)
        result = hsh.hexdigest()
        print(result)

    with open('SHA256-signatures.txt', 'r') as r:
        signatures = r.readlines()

    if result in signatures:
        print('Найден вирус!')
        os.remove(file)
        print('Вирус был удален!')
    else:
        print('Вирус не обнаружен!')
