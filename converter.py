from hexa_list_converter import *

def convert_from_decimal(val,base):
    current_val = val
    unsorted_ans = []

    while current_val >= base:
        unsorted_ans.append(current_val % base)
        current_val //= base
    unsorted_ans.append(current_val % base)
    current_val //= base

    sorted_ans = unsorted_ans[::-1]

    string_ans_list = [str(x) for x in sorted_ans]

    if base == 16:
        string_ans_list = convert_to_hex_list(string_ans_list)

    final_ans = ''.join(string_ans_list)
    
    print('------')
    print(final_ans)
    print('------')
    return final_ans

def convert_to_decimal(val,base):
    if not isinstance(val, str):
        string_val = str(val)
        val_list = list(string_val)
    else:
        val_list = list(val)

    if base == 16:
        val_list = convert_from_hex_list(val_list)    
        
    decimal_val = 0
    digit_counter = 0

    for digit in val_list:
        exponent = len(val_list) - digit_counter - 1
        decimal_val = decimal_val + int(digit)*(base**exponent)
        digit_counter += 1
    print(decimal_val)
    return(int(decimal_val))