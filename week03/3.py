
import re


def three(id_card):

    pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}([0-9]|X)$'


    if re.match(pattern, id_card):
        return True
    else:
        return False
