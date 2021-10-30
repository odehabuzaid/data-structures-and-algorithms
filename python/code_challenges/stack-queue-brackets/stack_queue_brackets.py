import re


def validate_brackets(in_string):
    oc_pairs = dict(zip('({[',')}]'))
    c_values = list()
    for key in in_string:
        if key is re.match(r'(.*?)(\(|\[|\{||$)',key)[0]:
            c_values.append(oc_pairs[key])

        elif key is re.match(r'(.*?)(\)|\]|\}||$)',key)[0]:
            if not c_values or key is not c_values.pop():
                return False

    return not c_values


print(validate_brackets('{}(){}') )
print(validate_brackets('{}') )
print(validate_brackets('(){}[[]]') )
print(validate_brackets('{}{Code}[Fellows](())') )
print(validate_brackets('()[[Extra Characters]]') )
print('='*10)
print(validate_brackets('{(})') )
print(validate_brackets('(](') )
print(validate_brackets('{{} )]') )
print(validate_brackets('[({}]') )
