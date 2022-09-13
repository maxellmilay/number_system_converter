def convert_from_hex_list(list):
    hexa_val_list = []
    for digit in list:
        if digit == 'A':
            hexa_val_list.append('10')
        elif digit == 'B':
            hexa_val_list.append('11')
        elif digit == 'C':
            hexa_val_list.append('12')
        elif digit == 'D':
            hexa_val_list.append('13')
        elif digit == 'E':
            hexa_val_list.append('14')
        elif digit == 'F':
            hexa_val_list.append('15')
        else:
            hexa_val_list.append(digit)
    return hexa_val_list

def convert_to_hex_list(list):
    hexa_val_list = []
    for digit in list:
        if digit == '10':
            hexa_val_list.append('A')
        elif digit == '11':
            hexa_val_list.append('B')
        elif digit == '12':
            hexa_val_list.append('C')
        elif digit == '13':
            hexa_val_list.append('D')
        elif digit == '14':
            hexa_val_list.append('E')
        elif digit == '15':
            hexa_val_list.append('F')
        else:
            hexa_val_list.append(digit)
    return hexa_val_list