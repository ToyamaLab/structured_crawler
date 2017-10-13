import re
import unicodedata

# # 7-1
# mystery = '\U0001f4a9'
# print(mystery)
# print(unicodedata.name(mystery))
#
# # 7-2
# pop_bytes = mystery.encode('utf-8')
# print(pop_bytes)
#
# # 7-3
# pop_string = pop_bytes.decode('utf-8')
# print(pop_string)
# if mystery == pop_string:
#     print('same')

# # 7-4
# print('My kitty cat likes %s' % 'roast beaf')
# print('My kitty cat likes %s' % 'ham')
# print('My kitty cat fell on his %s' % 'head')
# print('And now thinks he\'s a %s.' % 'clam')
#
# # 7-5
# letter = """Dear {salutation} {name},
#
# Thank you for your letter. We are sorry that our {product} {verbed} in your
# {room}. Please note that it should never be used in a {room}, especially
# near any {animals}.
#
# Send us your receipt and {amount} for shipping and handling. We will send
# you another {product} that, in our tests, is {percent}% less likely to
# have {verbed}.
#
# Thank you for your support.
#
# Sincerely,
# {spokesman}
# {job_title}
# """
#
# #7-6
# response = {
#     'salutation': 'Colonel',
#     'name': 'Hackenbush',
#     'product': 'duck blind',
#     'verbed': 'imploded',
#     'room': 'conservatory',
#     'animals': 'emus',
#     'amount': '$1.38',
#     'percent': '1',
#     'spokesman': 'Edgar Schmelts',
#     'job_title': 'Licensed Podiatrist',
# }
#
# print(letter.format(**response))

# 7-7
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""
# # 7-(8-11)
# print(re.findall(r'\bc\w*', mammoth))
#
# print(re.findall(r'\bc\w{3}\b', mammoth))
#
# print(re.findall(r'\b[\w\']*r\b', mammoth))
#
# print(re.findall(r'\b\w*[aiueo]{3}[^aiueo\s]*\w*\b', mammoth))

# 7-12
import binascii
import struct
gif = binascii.unhexlify(b'474946383961010001008000000000ffffff21f9' +
                         b'0401000000002c0000000100010000020144003b')
print(gif)

print(gif[:6])

# width = struct.unpack('<H', gif[6:8])
# height = struct.unpack('<H', gif[8:10])
width, height = struct.unpack('<HH', gif[6:10])
print('width {} height {}'.format(width, height))