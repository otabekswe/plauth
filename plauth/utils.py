from random import randint

def generate_token() -> str:
    '''
    Effortlessly generate 6-digit strings with or without leading zeros for versatile applications.
    '''
    return str("%06d" % randint(0, 999999))


def token_validator(token: str) -> bool:
    '''
    Validate a token to ensure it is length's 6 and contains only digits.
    '''
    return token.isdigit() and len(token) == 6