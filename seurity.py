bofore_key = {
    'А': 'М',
    'Б': 'Ь',
    'В': 'Ж',
    'Г': 'Ф',
    'Ґ': 'Д',
    'Д': 'Б',
    'Е': 'З',
    'Є': 'Й',
    'Ж': 'О',
    'З': 'Ї',
    'И': 'П',
    'І': 'В',
    'Ї': 'Г',
    'Й': 'Л',
    'К': 'Р',
    'Л': 'У',
    'М': 'Ч',
    'Н': 'Н',
    'О': 'Й',
    'П': 'І',
    'Р': 'Х',
    'С': 'Ґ',
    'Т': 'Ц',
    'У': 'Т',
    'Ф': 'К',
    'Х': 'Е',
    'Ц': 'Ю',
    'Ч': 'С',
    'Ш': 'Я',
    'Щ': 'И',
    'Ь': 'Я',
    'Ю': 'Щ',
    'Я': 'А'
}
password = bofore_key.copy()
for key, value in bofore_key.items():
    password[key.lower()] = value.lower()

my_input = 'Йбпнпл бвбтґя ж нмявл рйчімяюв'

def encrypting(my_input, password, output=''):
    for symbol in my_input:
        try:
            new_symbol = password[symbol]
            output += new_symbol
        except KeyError:
            output += symbol

    return output


def deciphering(my_input, password, output=''):
    password = {value: key for key, value in password.items()}
    for symbol in my_input:
        try:
            new_symbol = password[symbol]
            output += new_symbol
        except KeyError:
            output += symbol

    return output


# print(encrypting(my_input, password))
print(deciphering(my_input, password))