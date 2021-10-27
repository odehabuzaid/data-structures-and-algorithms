def valdid_bracketss(in_string):
    oc_pairs = dict(zip('({[',')}]'))
    c_values = list()
    for key in in_string:
        if key is re.match(r'(.*?)(\(|\[|\{||$)',key)[0]:
            c_values.append(oc_pairs[key])

        elif key is re.match(r'(.*?)(\)|\]|\}||$)',key)[0]:
            if not c_values or key is not c_values.pop():
                return False

    return not c_values


print(valdid_bracketss('{}(){}') )
print(valdid_bracketss('{}') )
print(valdid_bracketss('(){}[[]]') )
print(valdid_bracketss('{}{Code}[Fellows](())') )
print(valdid_bracketss('()[[Extra Characters]]') )
print('='*10)
print(valdid_bracketss('{(})') )
print(valdid_bracketss('(](') )
print(valdid_bracketss('{{} )]') )
print(valdid_bracketss('[({}]') )
