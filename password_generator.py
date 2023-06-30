from random import choices, shuffle

def password_gen(num_of_letters, num_of_symbols, num_of_numbers, length_of_password):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = choices(letters, k=num_of_letters)
    password_symbols = choices(symbols, k=num_of_symbols)
    password_numbers = choices(numbers, k=num_of_numbers)

    password_list = password_letters + password_symbols + password_numbers
    password_list += choices(letters + numbers + symbols, k=length_of_password - len(password_list))
    shuffle(password_list)
    password = ''.join(password_list)

    return password


