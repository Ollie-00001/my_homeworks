def encrypt_caesar(text, shift):
    result = ''

    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            base = ord('А') if char.isupper() else ord('а')
            result += chr((ord(char) - base + shift) % 32 + base)
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

text = input("Введите текст: ")
try:
    shift = int(input("Введите сдвиг: "))
    encrypted_text = encrypt_caesar(text, shift)
    print("Зашифрованный текст:", encrypted_text)
except ValueError:
    print("Ошибка: сдвиг должен быть числом.")
