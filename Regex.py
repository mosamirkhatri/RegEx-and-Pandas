text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

import re



# print(r'\tTab') #Raw String. It will print literally what is written in the quotes


#================================================================#
# pattern = re.compile(r'\bHa')
# matches = pattern.finditer(text_to_search)
# print(matches)
# for match in matches:
#     print(match)
#================================================================#

#================================================================#
# pattern1 = re.compile(r'[^b]at')
#(r'[^a-zA-Z]') #caret(^) inside the [] - character set will act as 'not matching the specified range'
#(r'[0-5]') for the range from 0 to 5
#(r'end$') for ends with
#(r'^Start') for starts with
# matches1 = pattern1.finditer(text_to_search)
# print(matches1)
# for match in matches1:
#     print(match)
#================================================================#

#================================================================#
pattern2 = re.compile(r"\d{3}.\d{3}.\d{4}") #(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')
matches2 = pattern2.finditer(text_to_search)
# for match in matches2:
#     print(match)
#================================================================#

#================================================================#
# with open('data.txt', 'r') as f:  #with open('data.txt', 'r', encoding='utf-8') as f: in case of encoding error
#     contents = f.read()
#
#     pattern3 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#
#     matches3 = pattern3.finditer(contents)
#
#     for match in matches3:
#         print(match)
#================================================================#

#================================================================#
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)
#================================================================#

#================================================================#
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net.in
'''
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# # pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# matches = pattern.finditer(emails)

# for match in matches:
    # print(match)

#================================================================#
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)
# matches = pattern.finditer(u  rls)
# a=[]
# for match in matches:
#     print(match.group(3))
#     a.append(match)
#================================================================#



# other methods with finditer.
# findall method returns (iterable) string of the matches but if groups are present it returns first group.
# match method returns the matches at the Beginning of the string. It returns only one object.
# search method returns the first match in the string. It returns only one object.
# Flags -- re.compile(r'start', re.IGNORECASE) ==> this flag will ignore cases of letters. also can be written as 're.I'
