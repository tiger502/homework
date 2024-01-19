
def one(decimal_num, num_places=8):
    binary_num = []
    whole_part = int(decimal_num)
    fractional_part = decimal_num - whole_part

    while whole_part > 0:
        remainder = whole_part % 2
        binary_num.insert(0, str(remainder))
        whole_part //= 2

    binary_num.append('.')

    for _ in range(num_places):
        fractional_part *= 2
        bit = int(fractional_part)
        binary_num.append(str(bit))
        fractional_part -= bit

    return ''.join(binary_num)
