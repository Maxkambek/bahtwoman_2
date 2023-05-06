import re


def card_number_validator(num: str):
    result_humo = re.match(pattern='^9860[0-9]{12}$', string=num)
    result_uz = re.match(pattern='^8600[0-9]{12}$', string=num)
    if result_humo or result_uz:
        return True
    else:
        return False


def expire_date_validator(num: str):
    res = re.match(pattern='^[0-9]{2}/[0-9]{2}$', string=num)
    if res:
        return True
    else:
        return False


def cvv_validator(num: str):
    res = re.match(pattern='^[0-9]{3}$', string=num)
    if res:
        return True
    else:
        return False