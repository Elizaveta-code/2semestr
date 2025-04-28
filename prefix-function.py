def str_from_prefix(p):
    n = len(p)
    s = [''] * n
    s[0] = 'a'
    for i in range(1, n):
        if p[i] > 0:
            s[i] = s[p[i] - 1]
        else:
            s[i] = chr(ord('a') + i)
    return ''.join(s)
p = [0, 0, 1, 2, 3, 0, 1]
str = str_from_prefix(p)
print(str)