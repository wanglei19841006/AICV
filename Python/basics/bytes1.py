b = b'hello'

s = 'hello'

print('b is', b)
print('s is ', s)


print('string to bytes')
# bytes(s, encoding='utf8')
s = str.encode(s)
print('s is ', s)


print('bytes to string')
# str(b, encoding='utf-8')
b = bytes.decode(b)
print('b is ', b)
