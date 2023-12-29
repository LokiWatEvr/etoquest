def generate_passwords(number,length):
        import random
        chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
        passwords = []

        for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
            passwords.append(password)

        return passwords

def generatetwo():
        number = input('количество паролей?'+ "\n")
        length = input('длина пароля?'+ "\n")
        number = int(number)
        length = int(length)

        passwords = generate_passwords(number,length)
        for password in passwords:
            print(password)
generatetwo()