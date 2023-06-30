def check_special_char(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    return any(char in special_characters for char in password)


def check_upper_char(password):
    return any(char.isupper() for char in password)


def check_number(password):
    return any(char.isdigit() for char in password)


def password_strength(password):
    check_special = check_special_char(password)
    check_upper = check_upper_char(password)
    check_num = check_number(password)
    check_mark = "\u2713"  # Check mark (✓)
    exclamation_mark = "\u0021"  # Exclamation mark (!)
    cross_mark = "\u2717"  # Cross mark (✗)

    if len(password) > 10 and check_special and check_upper and check_num:
        strength = check_mark+check_mark+check_mark + "Strong Password"
        return strength
    elif len(password) > 9 and (check_special or check_upper or check_num):
        strength = exclamation_mark+exclamation_mark+exclamation_mark + "Moderate Password"
        return strength
    else:
        strength = cross_mark+cross_mark+cross_mark + "Weak Password"
        return strength
