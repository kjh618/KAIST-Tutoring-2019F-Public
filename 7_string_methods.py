def str_in(needle, haystack):
    for i in range(len(haystack) - len(needle) + 1):
        is_equal = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                is_equal = False
        if is_equal:
            return True
    return False


def str_find(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        is_equal = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                is_equal = False
        if is_equal:
            return i
    return -1


def str_replace(self, string1, string2):
    ret = []
    cur_pos = 0
    while True:
        string1_pos = str_find(self[cur_pos:], string1) + cur_pos
        if string1_pos - cur_pos == -1:
            ret.append(self[cur_pos:])
            return str_join('', ret)
        ret.append(self[cur_pos:string1_pos])
        ret.append(string2)
        cur_pos = string1_pos + len(string1)


def str_split(self, sep):
    pass


def str_join(self, lst):
    if lst == []:
        return ''
    final = ''
    for i in range(len(lst) - 1):
        final += lst[i] + self
    final += lst[-1]
    return final


def str_format(self, vals): # only '%d'
    pass


str1 = 'Hello, world!'
str2 = 'abc|def|abc|ghi'
lst1 = ['q', 'w', 'e', 'r', 't', 'y']
lst2 = ['q']
lst3 = []

print('world' in str1, str_in('world', str1))
print(str1.find('world'), str_find(str1, 'world'))
print(str2.replace('abc', 'cba'), str_replace(str2, 'abc', 'cba'))
print(str2.split('|'), str_split(str2, '|'))
print(' + '.join(lst3), str_join(' + ', lst3))
print('%d + %d = %d' % (1, 2, 1 + 2), str_format('%d + %d = %d', (1, 2, 1 + 2)))
