# operasi biner atau binary

a = 9
b = 5

# bitwise or |
c = a | b
print('\n========OR=======\n')
print('nilai : ',a,', binary: ',format(a,'08b'))
print('nilai : ',b,', binary: ',format(b,'08b'))
print('===================(|)')
print('nilai : ',c,', binary: ',format(c,'08b'))


# bitwise AND (&)
c = a & b
print('\n========AND=======\n')
print('nilai : ',a,', binary: ',format(a,'08b'))
print('nilai : ',b,', binary: ',format(b,'08b'))
print('===================(&)')
print('nilai : ',c,', binary: ',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n========XOR=======\n')
print('nilai : ',a,', binary: ',format(a,'08b'))
print('nilai : ',b,', binary: ',format(b,'08b'))
print('===================(^)')
print('nilai : ',c,', binary: ',format(c,'08b'))

# bitwise NOT (~)
a = ~a
print('\n========NOT=======\n')
print('nilai : ',a,', binary: ',format(a,'08b'))
print('nilai : ',b,', binary: ',format(b,'08b'))
print('===================(^)')
print('nilai : ',c,', binary: ',format(c,'08b'))