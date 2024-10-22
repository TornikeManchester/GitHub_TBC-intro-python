#My way of task_4 solution
keyboard_mapping_e = {'q': 'w', 'w': 'e', 'e': 'r', 'r': 't', 't': 'y', 'y': 'u', 'u': 'i', 'i': 'o', 'o': 'p', 'p': 'q',
'a': 's', 's': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k', 'k': 'l', 'l': 'a',
'z': 'x', 'x': 'c', 'c': 'v', 'v': 'b', 'b': 'n', 'n': 'm', 'm': 'z'}

keyboard_mapping_d = {'q': 'p', 'w': 'q', 'e': 'w', 'r': 'e', 't': 'r', 'y': 't', 'u': 'y', 'i': 'u', 'o': 'i', 'p': 'o',
'a': 'l', 's': 'a', 'd': 's', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j', 'l': 'k',
'z': 'm', 'x': 'z', 'c': 'x', 'v': 'c', 'b': 'v', 'n': 'b', 'm': 'n'}

string = input('Enter the word: ')
action = input('Enter action e/d: ')

if action == 'e':
    result = ''
    for char in string:
        if char in keyboard_mapping_e:
            result += keyboard_mapping_e[char]
        else:
            result += char
    print(result)

if action == 'd':
    result = ''
    for char in string:
        if char in keyboard_mapping_d:
            result += keyboard_mapping_d[char]
        else:
            result += char
    print(result)
