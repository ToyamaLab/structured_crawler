# 8-1
text1 = 'This is a test of the emergency text system'
with open('test.txt', 'wt') as fout:
    fout.write(text1)

# 8-2
text2 = ''
with open('test.txt', 'rt') as fin:
    for line in fin:
        text2 += line

if text1 == text2:
    print("same")


# # 8-3
# import csv
# books = [
#     {"author": "J R R Tolkien", "book": "The Hobbit"},
#     {"author": "Lynne Truss", "book": "Eats, Shoots & Leaves"}
# ]
#
# with open('books.csv', 'wt') as fout:
#     cout = csv.DictWriter(fout, ['author', 'book'])
#     cout.writeheader()
#     cout.writerows(books)
#
# # 8-4
# with open('books.csv', 'rt') as fin:
#     cin = csv.DictReader(fin)
#     books2 = [row for row in cin]
#
# print(books2)
e = 'é'

# 8-5
'''title,author,year
The Weirdstone of Brisingame,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''
