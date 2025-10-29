import unicodedata
import string
import sys
import os
import locale
import re
# import more_itertools

"""
\newline        Ignored (continuation line)
\\              Backslash (stores one\)
\'              Single quote (stores')
\"              Double quote (stores")
\a              Bell
\b              Backspace
\f              Formfeed
\n              Newline (linefeed)
\r              Carriage return
\t              Horizontal tab
\v              Vertical tab

x = "\tThis string starts with a \"tab\"."
x = "This string contains a single backslash(\\)."
x = "Don't need a backslash"
x = 'Can\'t get by without a backslash'
x = "Backslash your \" character!"
x = 'You can leave the " alone'

http://www.helldragon.eu/marcello/galli_python/07-Stringhe.html
https://www.tutorialspoint.com/python/python_strings.htm

Formatting
https://pyformat.info/ <<<
"""

print('m')
print('\155')
print('\x6D') #esadecimale

print(sys.version_info.major)

a,c, *b = 'spam'
print(a, b)

S = 'spam'
print(S[0] + S[-2])

print('spam'[1:3])
print('spam'[slice(1, 3)])
print('spam'[::-1])
os.environ["PYTHONIOENCODING"] = "utf-8"
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")
# --> https://www.w3schools.com/python/python_ref_string.asp

print(dir(str))

s4 = 'yhuiokgjkipr'
print(s4[::7])
print('---->', s4[::-1]) # inverte l'ordine della stringa


L = [5, 6, 7, 8, 9]
print(L[slice(None, None, 2)])

sa = 'Example'
print(sa.startswith('exa'))

#Trasforma in maiscole tutte le lettere iniziali
sa = 'example for string   '
print(sa.title())

#Conta il numero di orccorenze nella stringa dell'esspressione nella parentesi
print(sa.count('r'))

#elimina gli spazzi all'inizio e alla fine della frase
print(sa.strip())

#toglie gli spazi a sinistra
print(sa.lstrip())

#toglie gli spazi a destra
print(sa.rstrip())

sa_upper = sa.upper()
print(sa, ' <<<<<<')
print(sa_upper, ' <<<<<<')


print('stringa'.lstrip('atgrs')) #elimina i caratteri nella stringa

#Converte un ogggetto in una stringa
print(str(['a', 'b', 'c', 1, 2]))

print(unicodedata.name(u'A'))
print('\n{LATIN CAPITAL LETTER A}')
# smethods = [name for name in dir(str) if not name.startwith('__')]
# print(smethods)
# print(dir(string))
s1 = 'sono unA stringA, quindi Una  sequenza immutabile di caratteri'
# numero di occorenze
print(s1.replace('una','UNA',1))
print(s1)

# Required to call maketrans function.
intab = "ABC"
outtab = "abc"
trantab1 = str.maketrans(intab, outtab)

print (s1.translate(trantab1))

# da vedere
# trantab2 = maketrans({ord('i'):None})
# print s1.translate(trantab2)
# print(s1.maketrans({ord('i'):None}))

print("Method Split")

s0 = 'String methods in python'.split(' ', maxsplit=1)
print(s0)

s0 = 'String methods in python'.rsplit(' ', maxsplit=1)
print(s0)

s2 = 'Un giorno, se avro\' tempo, andro\' a correre'

split1 = s2.split()
print(split1)

split2 = s2.split(',')
print(split2)

split3 = s2.split('ro\'')
print(split3)

l1 = ["pippo", " ", "cade", " ", "dalla", " ", "bici" ]
print(" ".join(l1))

# aggiunge un carattere in prossimita' di un separatore
s3 = '-'.join(s2.split())
print(s3)

rds_instance = "db-rdsname"

splits = rds_instance.split('-')[1:]
print('-'.join(splits))


# rimuovono gli spazi
s4 = '    Stringa con    spazzi all \' interno'
print(s4.lstrip().strip())
print(s4.lstrip().rstrip())
# elimina i caratteri che corrispondono partendo in questo caso da sinistra
# ma ci devono essere se non non parte
print('cccccc pluto'.lstrip('c '))

print(s4.title())
print(s4.strip().capitalize())
print(s4.upper())
print(s4.lower())
print('oggi una bella giornata'.startswith('oggi'))
print('1234bc'.isalnum()) #alfa numerici
print('abcc'.isalpha()) # alfabetici
#tutti i metodi delle stringh e di testo
##  print(set(smethods)-set(bmethods))
print('122'.isdigit)
## print('122'.isdecima
print(sys.maxunicode)
## decimals = [chr(c) for c in range(sys.maxunicode + 1) if(chr(c).isdecimal())]
## digits = [chr(c) for c in range(sys.maxunicode + 1) if(chr(c).isdigit())]
## numerics = [chr(c) for c in range(sys.maxunicode + 1) if(chr(c).isnumeric())]


# DA VEDERE --->
# rimuove il prefisso impostata
# nostarch_url = 'https://nostarch.com'
# nostarch_url = nostarch_url.removeprefix('https://') # lo ritorna come risultato non modifica la stringa in place

# print('NO PREFIX -->>', nostarch_url)
# DA VEDERE --->

#confronto tra string case sensitive
s1c = 'a presto Elisabetta'
s2c = s1c.title()
print(s1c, s2c, s1c == s2c)
# non ne tiene conto del case migliore di Upper e lower
print(s1c, s2c, s1c.casefold() == s2c.casefold())

# essendo immutabili vengono sempre restituite nuove stringhe
# %[(chiave)][opzione][profondita'][.precisione]tipo
# '%s' Stringhe
# '%d' Intero decimale con segno
# '%i' Intero decimale con segno
# '%o' Intero ottonale con segno
# '%x' Esaadecimale
# '%c' Carattere singolo
print("%s %d una meraviglia" % ('Python', 3))
print('%d|%o|%x|%X' % (12,12,12,12))

camels = 42
print('I have spotted %d camels.' % camels)

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))

#formattazione basata sui dizionari
print('%(name)s,%(pass)s,%(age)d' % {'age':27, 'name':'pippo', 'pass':'38388'})

# profondita' indica il numero minimo di caratteri
# puo' essere utile per incollonnare i valori in un file
print('>%d'%100)
print('>%17d'%100)

#metodo format (https://www.python.org/dev/peps/pep-3101/)
print('{name},  {0}, e nache una lista:{mylist}'.format(0,mylist=[0,1,2,3],name='Marco'))

import sys, os
# print("L'utente %s usa %s su %s" %(os.environ.get("USER"), os.environ['SHELL'],sys.platform))


print('{names[0]} usa {languages[1]}'.format(languages=('C++','Python'), names=('Marco', 'Leo')))

# per formattare numeri in maniera piu' leggibile
print('{:,d}'.format(100000000))
print('{:,.3f}'.format(100000000.00))
print('{:,f}'.format(10000.00 + 10000.00j))
from decimal import Decimal
print('{:,.3f}'.format(Decimal(100000000.30)))

# si puo' utilizzare la funzione format che e' equivalente
# la funzione built-in non fa altro che chiamare il metodo __format_()
# dell'oggetto
print(format(2/4,'.2f'))

print('--------------------------------------')
print('         Numeri')
print('--------------------------------------')

def listToString(s):

    str1 = ""

    return (str1.join(s))


decimals = [chr(c) for c in range(sys.maxunicode + 1) if chr(c).isdecimal()]
digits = [chr(c) for c in range(sys.maxunicode + 1) if chr(c).isdigit()]
numerics = [chr(c) for c in range(sys.maxunicode + 1) if chr(c).isnumeric()]

#print('decimals')
# print(decimals)

print('decimals')
#print(listToString(decimals).encode('utf-8', errors='ignore'))

print('digits')
#print(listToString(digits).encode('utf-8', errors='ignore'))

print('numerics')
#print(listToString(numerics).encode('utf-8', errors='ignore'))

#formattazione

print("%s %d e meraviglioso" % ('Python',3))

num = 1.123456789

print('%f | %8.2f | %8.10f' % (num, num, num))

print('{name},{number} , e anche una lista:{mylist_f}'.format(mylist_f = [0,1,2,3],number = 33,name = 'Marco'))

s5 = 'shrubbery'
l5 = list(s5)

print(l5)
l5[1] = 'c'
#crea una nuova stringa
s5 = ''.join(l5)
print(list(s5))

print('Is Alpha: ' + str(s5.isalpha()))


word = 'pippo'
print(word.find('o'))
S = "s\tp\na\x00m"
print(len(S))
print(S)
S = "C:\\py\\code"
print(len(S))

S = "C:\py\code"
print(len(S))

path = r'C:\new\text.dat'
print(path)
print(len(path))
'''
myfile = open(r'C:\new\text.dat', 'w') <<<<
o
myfile = open('C:\\new\\text.dat', 'w')

'''

myjob = "hacker"
for c in myjob: print(c, end=' ')


# Formttare
z = 5
str1 = f"il quadro di {z} e' {z * z}"
print(str1)

# se ci sono caratteri no ASCCI '.encode('utf-8').strip()'

#trasformare un carattere in ascii
print(ord("P"))
print(chr(80))

#Float formatting follow "{value:with.precision f}"
res3 = 100 / 777
print('The result was {r:1.3f}'.format(r = res3))

print("Wandì è una rompi balle ?".isspace())

fruit = 'Banane'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index +=1

for char in fruit:
    print(char)

print(fruit[:3])
print(fruit[3:])

greeting = 'hello, world'
new_gretting = 'J' + greeting[1:]
print(new_gretting)
print('Capitalize', ' ', greeting.capitalize())

search_test = 'banana'

print(search_test.find('a'))
print(search_test.find('ba'))
print(search_test.find('na'))
print(search_test.find('ai'))

# Esempio di estrazione di carattrei

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
str_join = delimiter.join(t)

print(str_join)

#ricerca tuttue le stringhe che sembrano degli indirizzi mail e restituisce una lista

str2 = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'

lst = re.findall('\S+@\S+', str2)

print(lst)

str3 = 'We just received $10.00 for cookies.'
res4 = re.findall('\$[0-9.]+', str3)
print(res4)

str4 = "Io sono 'Pippo'"
print(str4)


str5 = "Super" + "    Pippo".lstrip()
print(str5)

str5 = "Pipppo     ".rstrip() + "?"
print(str5)

str5 = "P" + "  ipppo    Pluto   ".strip() + "?"
print(str5)

import re

# solo all'inizio
# str5 = re.sub(r"^\s+", "", str5, flags=re.UNICODE)

#Rimuve tutti gli spazzi
str5 = re.sub(r"\s+", "", str5, flags=re.UNICODE)

print(str5)


print("Extract sub string ...")

fullstring = "StackAbuse"
substring = "Abusex"

result = fullstring[fullstring.find(substring):len(fullstring)]

if fullstring.find(substring) != -1:
    print("Found! " + result)

else:
    print("Not found!")

print(fullstring.find(substring))

print('-'*10)

str6 = "Hello welcome to my word"

# print(str6.startswith("wel", 7, 20))

# print(str6.isdigit())


print('a' < 'b')

print('bbbbbbbbc' < 'bbbz')

print(42 != "42")


print(30.11E9)        # 30110000000.0
# print(30.11 * 10 ** 9)  # 30110000000.0

#per mantenere i bakslash nella stringa devo aggiungere 'r' all'inizio
str7 = (r"Orazio disse: \"Cogito ergo sum\" ")
print(str7)

# Slincing
# string_name[start_index: end_index: step]
p = 'Python'
print('Slincing: ', p[1: 4: 1]) # ---> yth

str8 = "I love Python"
try :
    print("index: ", str8.index("o")) # è case sensitive
    print("index: ", str8.index("0", 4))
except ValueError:
    print("Not found element")

print("Count: ", str8.count("o"))
print("Count: ", str8.count("o", 4))

try :
    print(str8[2])
    print(str8[20])
except IndexError:
    print("Index Error occured")


str9 = 'pippo'
print(f"il mio nome è {str9.title()} !")

str10 = "pippo is a fool person but he is a young man "

pos = str10.rindex("is") # trova l'ultima occorrenza dei caratteri cercati

# import more_itertools

str11 = "Hello, World"
c = "o"

'''
index_tool = next(more_itertools.rlocate(str11, lambda x: x==c))

if index_tool != -1:
     print(f"Char '{c}' is found at index {index_tool}")    # Char 'o' is found at index 8
else:
    print("Char not found")

'''

str12 = "ABCDEFGHILMNO"

fragment = str12[2:len(str12):3] # [partenza:fine:salto] ---> CFIN
print(fragment)

fragment = str12[::-1] # inverte la stringa
print(fragment)


sentence = "Controlling complexity is the essence of programming"
pos_end = sentence.index(" ")
fragment = sentence[:pos_end]
print(fragment)

sentence = "pippo Never trust a computer you can't throw out a window"
fragment = sentence[2:len(sentence):3]
print(fragment)

haiku = '''
    Whitecaps on the bay:
    A broken signboard banging
    In the April wind.
    '''

if 'beach' not in haiku:
    print(True)
else:
    print(False)

word_list = ["Simple","is","better","than","complex."]
result = ' '.join(word_list)
print(result)

word_find = 'pippo'

is_found = word_find in sentence
dic = {True: "was", False: "was not"}

print(f"The word '{word_find}' {dic[is_found]} found in the text: '{sentence}'")


sentence = "When something is important enough, you do it even if the odds are against you"
word1 = "success"
word2 = "technology"

my_bool = (sentence.find(word1) <0) and (sentence.find(word2) < 0)

print(my_bool)
word = "Python"

text = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
clean_text = text.lstrip(",:%#__")
print(clean_text)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f'\"{self.title}\" , from {self.author}'

book = Book("IT", "King", 1000)

print(book)


text_split = 'a b c d'
print(text_split.split(' ', 1)) #['a', 'b c d']
print(text_split.split(' ', 2)) # 'a', 'b', 'c d']

text_split =  "Mississippi"
print(text_split.split("ss")) #['Mi', 'i', 'ippi']


print("".join(["Separated", "by", "nothing"]))
print("::".join(["Separated", "with", "colons"]))

str13 = "Mississippissss"
str13.find("ss", 3) #parte dalla posizione 3
str13.find("ss", 0, 3) #da a 

print(str13.count("ss"))
print(str13.endswith(("i", "u", "ss"))) #si possono inserire più valori


str14 = "Hello Sam!"
mytable = str14.maketrans("S", "P")
print(str14.translate(mytable))

str14= "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str14.maketrans(x, y)
print(str14.translate(mytable))

str15 = "47"
print(str15.zfill(4)) # riempie a sinistra di 0

str16 = "Hello,  World"
wordList = list(str16)
wordList[5:] = []
print(wordList)
wordList.reverse()
str16 = "".join(wordList)
print(str16)

str16_r = str16[::-1] #più veloce e comodo
print("Reverse ", str16_r)

test_list = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']

index = 0
for text in test_list:
    test_list[index]= text.replace('"', '')
    index += 1

print(test_list)


# rif https://pythonexamples.org/python-string-replace-character-at-specific-position/
str17 = "Mississippi"
pos = str17.rfind("p")
str17 = str17[ :pos] + "_" + str17[ pos + 1:]
print(str17)

print('############################################################')
print('                        FORMAT                              ')
print('############################################################')
# https://realpython.com/python-formatted-output/

print('{{ {0} }}'.format('foo')) #'{ foo }'
print('%d %s cost $%.2f' % (6, 'bananas', 1.748)) # '6 bananas cost $1.75' << arrontonda alla cifra scelta

print('{quantity} {item} cost ${price}'.format(quantity=6,item='bananas', price=1.748))

print('{0}/{1}/{2}'.format('foo', 'bar', 'baz'))
print('{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz'))

print('{}/{}/{}'.format('foo', 'bar', 'baz')) # posizioni in automatico
print('{}{}'.format('foo', 'bar', 'baz'))
print('{x}/{y}/{z}'.format(x='foo', y='bar', z='baz'))
print('{0}{x}{1}'.format('foo', 'bar', x='baz'))

x = 'foo'
y = 'bar'
z = 'baz'
print('{0}/{1}/{s}'.format(x, y, s=z))

print('Stampa il codice: ',  ord('A')) #
print('Stampa il carattere: ', chr(65)) #


str18 = "pipppo is happy"
print(str18.index('is')) # se non lo trova va in errore <<
print(str18.find('ist')) #se non lo trova ripsonde con -1

print(10 == '10')
print(10 != '10')
# print(10 > '10') questo confronto non è supportato va in errore typError

#https://pynative.com/python-regex-split/
str19 = '52_841__63____24_76______49'
items = re.split('_+', str19) # genera una lista
print(items)
str19 = '63 41    92  81            69  70'
items = re.split(' +', str19)
print(items) 

str19 = "12, and45,78and85-17and89-97"
result = re.split(r"and|[\s,-]+", str19) # splitta per 'and' ',' e '-'

print(result)


first_num = 5
second_num = 3
second_num += 2

print(first_num is second_num) # true

first_str = "hello"
second_str = "hell"
second_str += "o"

print(first_str is second_str) # false python tratta le stringhe in maniare diversa perchè sono immutabili


print("Conversion String To Bytes")
str_bytes = '11110000'
int_bytes = int(str_bytes, 2) # vuol dire che converte la stringa in intero in base '2'
print(int_bytes)

'''
Return an array of bytes representing an integer.
If byteorder is “big”, the most significant byte is at the beginning of the byte array. 
If byteorder is “little”, the most significant byte is at the end of the byte array. 
The signed argument determines whether two’s complement is used to represent the integer
'''


'''
DA VEDERE ---->

bytes_result = int_bytes.to_bytes(1, byteorder='big', signed=False)
print(bytes_result) # b'\xf0'

#la funzione inversa
print(int.from_bytes(bytes_result))
DA VEDERE ---->

'''


# The repr() function takes a single parameter:
class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

print(repr(Person()))

x: str = 1 # dichiarazione con typing

def tutte_maiuscole_verbose(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def tutte_maiscole_contratta(t):
    return [s.capitalize() for s in t]

def solo_maiuscole_verbose(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def solo_maiuscole_contratta(t):
    return [s for s in t if s.isupper()]

firstfive = slice(0, 5) # prende i caratteri indicati
s = 'pippo hello world'
print(s[firstfive])

# Estrazione di una stringa tra 2 marcatori
import re
sampleStr = 'ilearncodingfrom;thispointer.com/articles'
try :
    # here ; and / are our two markers
    # in which string can be found.
    marker1 = ';'
    marker2 = '/'
    regexPattern = marker1 + '(.+?)' + marker2
    str_found = re.search(regexPattern, sampleStr).group(1)
except AttributeError:
    # Attribute error is expected if string
    # is not found between given markers
    str_found = 'Nothing found between two markers'
print(str_found)


sentence = "The sum of {0} + {2} + {1}".format(5, 25, 15)

print(sentence)


str20 = "pippo !!!2"
print(str(str20))


# grinning face
print("\U0001f600")
 
# grinning squinting face
print("\U0001F606")
 
# rolling on the floor laughing
print("\U0001F923")

str19 = " pippo pluto   paperino "

# Leading and trailing whitespaces are removed
print("1) ", str19.strip())

str19 = " xoe  oopippo plutoo  xoe  "
# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print("2) ",str19.strip(' xoe')) # --->> pippo plut

str20 = str19.replace(" ","") #ripulisce tutti gli spazi
print("3) ",str19)
print("4) ",str20) 

str21 = str19.translate({ord(c): None for c in string.whitespace})
print("5) ", str21) #ripulisce tutti gli spazi

#Remove Duplicate Spaces and Newline Characters Using the join() and split() Methods
str19 = '  Hello  World   From DigitalOcean \t\n\r\tHi There  '

str20 = " ".join(str19.split())

print("6) ", str20)

'''
'ascii'     Character values in the range [0x00, 0x7f].
'latin1'    Character values in the range [0x00, 0xff]. Also known as 'iso-8859-1'.
'utf-8'     Variable-length encoding that allows all Unicode characters to be represented.
'cp1252'    A common text encoding on Windows.
'macroman'  A common text encoding on Macintosh.
'''

text_1 = 'hello'                  # Text
byte_1 = text_1.encode('utf-8')   # Encode to bytes

byte_2 = b'world'                  # Bytes
text_1 = byte_2.decode('utf-8')   # Decode to text

'''
d       Decimal integer or long integer.
b       Binary integer or long integer.
o       Octal integer or long integer.
x       Hexadecimal integer or long integer.
X       Hexadecimal integer (uppercase letters).
f, F    loating point as [-]m.dddddd.
e       Floating point as [-]m.dddddde±xx.
E       Floating point as [-]m.ddddddE±xx.
g, G    Use e or E for exponents less than [nd]4 or greater than the precision; otherwise use f.
n       Same as g except that the current locale setting determines the decimal point character.
%       Multiplies a number by 100 and displays it using f format followed by a % sign.
s       String or any object. The formatting code uses str() to generate strings.
c       Single character
'''

# https://realpython.com/python-formatted-output/
# https://docs.python.org/3/library/string.html#formatspec Ufficiale

x = 123.456
format(x, '0.2f')       # '123.46'
format(x, '10.4f')      # '  123.4560'
# format(x, '<*10.2f')    # '123.46****' NON FUNZIONA

x = 123.456
    # '123.46****'
print(format(x, '10.4f')) #123.4560
print(format(x, '>#016.4f')) #00000000123.4560
print(format(x, '<#010.4f')) #123.456000

# print('Value is {val:<*10.2f}' .format(val=x))

name = 'Bill Doe'
balance = 13.566
# indica la direzione dove verrà indentato '>' tutto a destra
print(f"- {name:>12}")      #-     Bill Doe
print(f"- {balance:>12}")   #-       13.566

print(f"- {name:<12}")      #- Bill Doe 
print(f"- {balance:<12}")   #- 13.566

x = 123456.78
format(x, '16,.2f')   # '      123,456.78'

name = 'Elwood'
r = format(name, '<10')     # r = 'Elwood    '
r = format(name, '>10')     # r = '    Elwood'
r = format(name, '^10')     # r = '  Elwood  '
r = format(name, '*^10')    # r = '**Elwood**'

x = 42
r = format(x, '10d')        # r = '        42'
r = format(x, '10x')        # r = '        2a'
r = format(x, '10b')        # r = '    101010'
r = format(x, '010b')       # r = '0000101010'

y = 3.1415926
r = format(y, '10.2f')      # r = '      3.14'
r = format(y, '10.2e')      # r = '  3.14e+00'
r = format(y, '+10.2f')     # r = '     +3.14'
r = format(y, '+010.2f')    # r = '+000003.14'
r = format(y, '+10.2%')     # r = '  +314.16%'

x = 123.456
print(f'Value is {x:0.2f}')         # 'Value is 123.46'
print(f'Value is {x:10.4f}')        # 'Value is   123.4560'
print(f'Value is {2*x:*<10.2f}')    # 'Value is 246.91****'

y = 3.1415926
width = 8
precision=3

r = f'{y:{width}.{precision}f}'   # r = '   3.142'

name = 'Dave'

#b'Hello %s' % name                    # TypeError!
result = b'Hello %s' % name.encode('utf-8')    # Ok
print(result)
'''
# -----------------------------------------------
txt = "pippo+pluto+pluto+pippo"

list_name = txt.split("+")

for name in list_name:

    names_clear = txt.replace('pippo', '').replace('++','+')

    first_character = names_clear[0:1]
    print("First Character: " + first_character)

    if(first_character == '+'):
        print("Start to clear ..." , len(names_clear))

        names_clear = names_clear[1:len(names_clear)]

    last_character = names_clear[len(names_clear)- 1: len(names_clear)]

    print("Last Character: " + last_character)

    if(last_character == '+'):
        names_clear = names_clear[0:len(names_clear) - 1]

    print(names_clear)

'''

symbol = '>'

symbol *= 5

print(symbol)

name = 'Pan'
name += ' Black'
bar = '*'
bar *= len(name)

print(f'{bar}\n {name}\n{bar}')

'''
title: impone tutti i primi caratteri a Maiuscolo e i seguenti a minuscolo
capitalize: prima lettera maiscola
https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/title/python-string-title/#:~:text=title()%20%E2%80%93%20Python%20title(),uppercase%20and%20others%20to%20lowercase.
'''

txt = 'i have to reach office by 9:00'
print('Title --->> ', txt.title())
print('Capitalize --->> ', txt.capitalize())
print('>>>')

txt = 'HELLO Students, WELcome BAck'
print('Title --->> ', txt.title())
print('Capitalize --->> ', txt.capitalize())
print('>>>')

txt = '101hacks with python'
print('Title --->> ', txt.title())
print('Capitalize --->> ', txt.capitalize())
print('>>>')

sentence = 'to be or not to be that is the question'

sentence.count('to') # 2 occorenze
sentence.count('to', 12) # partendo da 12 ne trova solo 1

sentence.count('that', 12, 25) #inizio fine
sentence.index('be') # 3 posizione

sentence.rindex('be') # 16 partendo da destra

print('that' in sentence) #True
print('THAT' in sentence) #False

print('THAT' not in sentence) # True

sentence.startswith('to') #True
values = '1\t2\t3\t4\t5'
values.replace('\t', ',')
print(values) # '1,2,3,4,5'

letters_list = ['A', 'B', 'C', 'D']

letters = ','.join(letters_list)

sequence_numbers = ','.join([str(i) for i in range(10)])
print(sequence_numbers)

student_votes = 'Amanda: 89, 97, 92'

student_votes_tuple = student_votes.partition(': ')

print(type(student_votes_tuple), '--->>' , student_votes_tuple)

print("ISALNUM ...")

print('A9876'.isalnum())
print('20100 Milano'.isalnum()) #False ci sono gli spazi
print('20100Milano'.isalnum())  #True

'''
isalnum() : Restituisce True se la stringa contiene solo caratteri alfanumerici (cioè cifre e lettere).

isalpha() : Restituisce True se la stringa contiene solo caratteri alfabetici (cioè lettere).

isdecimal() : Restituisce True se la stringa contiene solo caratteri interi decimali (in base 10) e
non contiene i simboli + o -.

isdigit() : Restituisce True se la stringa contiene solo cifre .

isidentifier() : Restituisce True se la stringa rappresenta un identificatore valido

islower() : Restituisce True se tutti i caratteri alfabetici nella stringa sono minuscoli.

isnumeric() : Restituisce True se i caratteri nella stringa rappresentano un valore numerico
senza + o - e senza punto decimale

isspace() : Restituisce True se la stringa contiene solo caratteri di spaziatura.

istitle() : Restituisce True se il primo carattere di ogni parola nella stringa è un carattere maiuscolo
isupper() : Restituisce True se tutti i caratteri alfabetici nella stringa sono maiuscoli.

'''

sentence = 'to be or not to be that is the question'

print('Index', sentence.index('be')) 

print('Find', sentence.find('be'))

try:
    print('Index', sentence.index('bex')) 
except ValueError:
    print('Value Error index not found')

print('Find', sentence.find('bex')) # -1 se non viene trovato

print('that' in sentence) # per cercare le sotto stringhe

sentence.startswith('to')
sentence.endswith('question')

#Rimpiazzare le sottostringhe

values = '1\t2\t3\t4\t5'
replace_value = values.replace('\t', ',') 

print(replace_value)

result_partion = 'Amanda: 89, 97, 92'.partition(': ')

print(result_partion) # divide la stringa in 3 parti

lines = """Questa è la riga 1
Questa è la riga 2
Questa è la riga 3"""

lines_split = lines.splitlines()

print(type(lines_split), lines_split)

', '.join(reversed('Pamela White'.split()))


file_content = """hi there and welcome.
... this is a special hidden file with a secret secret.
... i don't want to tell you the secret,
... but i do want to secretly tell you that i have one."""

file_content.index("secret") # prima posizione della stringa
file_content.index("secret", 60) # prima posizione della stringa a partire da
file_content.count("secret") # quante volte è usato 
[word for word in file_content.split() if "secret" in word]

m = re.search(r"secret\w+", file_content)

print(m.group())
print(m.span())

url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

rest_of_url, separator, document = url.rpartition('/')

print(rest_of_url, " <<-->> " , separator , " <<-->> ", document) # <<-->> / <<-->> table_of_contents.html

lines = """Questa è la riga 1
        Questa è la riga 2
        Questa è la riga 3"""

result_lines = lines.splitlines() # se si passa True lines.splitlines(True) si mantiene lo spazio finale '\n'

print(type(result_lines), result_lines)

result_reverse =  ', '.join(reversed('Pamela White'.split()))
print(result_reverse) # White, Pamela

'''
isalnum()       ---> Restituisce True se la stringa contiene solo caratteri alfanumerici (cioè cifre e lettere).
isalpha()       ---> Restituisce True se la stringa contiene solo caratteri alfabetici (cioè lettere).
isdecimal()     ---> Restituisce True se la stringa contiene solo caratteri interi decimali (in base 10) e 
                non contiene i simboli + o -.
isdigit()       ---> Restituisce True se la stringa contiene solo cifre . 
isidentifier()  ---> Restituisce True se la stringa rappresenta un identificatore valido.   
islower()       ---> Restituisce True se tutti i caratteri alfabetici nella stringa sono minuscoli.
isnumeric()     ---> Restituisce True se i caratteri nella stringa rappresentano un valore numerico
                senza + o - e senza punto decimale. 
isspace()       ---> Restituisce True se la stringa contiene solo caratteri di spaziatura.
istitle()       ---> Restituisce True se il primo carattere di ogni parola nella stringa è un carattere maiuscolo.
isupper()       ---> Restituisce True se tutti i caratteri alfabetici nella stringa sono maiuscoli.
'''


print('--------------------------------------------------------------------------')
print('Performance Uso di JOIN')
print('--------------------------------------------------------------------------')

import timeit
import matplotlib.pyplot as plt

strings = ["Hello", "World"] * 10000

setup = """
strings = {0}
""".format(strings)

concat_with_plus = """
result = ""
for string in strings:
    result += string + " "
"""

concat_with_join = """
result = " ".join(strings)
"""
iterations = list(range(100, 1100, 100))

time_plus = []
time_join = []

for number in iterations:
    time_plus.append(timeit.timeit(concat_with_plus, setup=setup, number=number))
    time_join.append(timeit.timeit(concat_with_join, setup=setup, number=number))

plt.figure(figsize=(12, 8))
plt.plot(iterations, time_plus, label='+ operator', marker='o', color='tab:orange')
plt.plot(iterations, time_join, label='join() method', marker='o', color='tab:blue')
plt.xlabel('Number of iterations', fontsize=14)
plt.ylabel('Execution time (seconds)', fontsize=14)
plt.title('Comparison of Execution Time: + Operator vs join() Method', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()