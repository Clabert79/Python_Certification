import re

'''
https://regex101.com
http://www.regexlib.com
https://www.regular-expressions.info

'''

'Valido' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Non valido' # deve iniziare con la lettera Maiuscola e avere solo lettere

'Match' if re.fullmatch('[^a-z]', 'A') else 'No match' # '^' serve a negare quindi in questo caso che NON sono lettere minuscole

print('Match' if re.fullmatch('[x+$]', 'x') else 'No match') # ('[x+$]' deve contenere solo il carattere x (il primo carattere indicato) 

email = input("What's your email ?").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Not Valid")

name = input("What's your Name ?").strip()

'''
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
   name = matches.group(1) + " " + matches.group(2)
'''
# nuovo operatore semplifica
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(1) + " " + matches.group(2)
    
print(f"Hello, {name}")

url = input("URL:").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f"Username{username}")



c = re.compile(r"\b(?=\w{8}\b)\w{1,4}tex\w*") # la r sta per raw e indica al python di non eleborare backslash\
s = "texwille ritexwil ritexto 12tex345"

print(c.findall(s))


pattern = re.compile(r"(^[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[A-Za-z0-9-.]+$)")

s1 = 'Andrey@pippo.com'
print(pattern.search(s1))
print(pattern.fullmatch(s1))

# deve contenere caratteri + elenco speciali devono essere 6 + un numero finale
pattern2 = re.compile(r"([A-Za-z0-9$%#@]{6,}[0-9])")

password = "1234567#_4"

print(pattern2.fullmatch(password))

match = re.match('Hello[\t]*(.*)world', 'Hello pipoo pluto world')
print(match.group(1))

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())

print(re.split('[/:]', '/usr/home/lumberjack'))

text = '999-828-9282'

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

phone_results = re.search(phone_pattern, text)

print(phone_results.group())

print(phone_results.group(1))

print(re.findall("ab*c", "ABCacAbbbbbbc", re.IGNORECASE))

string = "Everything is <repleced> if it' s in a <TAG>."

string = re.sub("<.*>", "ELEPHANT", string)
print(string)

pattern_com = r'@\w+\.com'
check = re.search(pattern_com, 'pippo@gmail.com')
if check:
    print("OK")
else:
    print("Is not valid")

sentence = "XX1234"
pattern = r'\w{2}\d{4}'
check = re.search(pattern, sentence)
if check:
    print("Ok")
else:
    print("The zip code entered is not correct")

'''
da vedere <<<<
https://www.guru99.com/python-regular-expressions-complete-tutorial.html

https://www.evemilano.com/come-funzionano-le-espressioni-regolari-regex/
'''

response = 'Valido' if re.fullmatch(r'\d{5}', '10040') else 'Non Valido'
print(response)


'''
\d  ---> Qualsiasi cifra (0-9).
\D  ---> Qualsiasi carattere che non è una cifra.
\s  ---> Qualsiasi carattere di spaziatura (come spazi, tabulazioni e a capo).
\S  ---> Qualsiasi carattere non di spaziatura.
\w  ---> Qualsiasi carattere parola (detto anche carattere alfanumerico), ovvero
    qualsiasi lettera minuscola o maiuscola, qualsiasi cifra o trattino basso.
\W  ---> Qualsiasi carattere che non sia un carattere parola.
'''

'Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match' # --> un numero da 3 a 6 cifre
'Match' if re.fullmatch('famig?liare', 'famigliare') else 'No match' # --> ? 0 o una occrenza se sono maggiori da errore
'Valido' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Non valido' # --> '+' almeno una lettera Maiscola 

result = re.search('divertente$', 'Python è divertente') # $ --> restituice il valore se si trova alla FINE della stringa
print(result.group() if result else 'non trovato')

result = re.seresult = re.search('^Python', 'Python è divertente') # ^ --> restituice il valore se si trova alla INIZIO della stringa
print(result.group() if result else 'non trovato')

contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
re.findall(r'\d{3}-\d{3}-\d{4}', contact) # ['555-555-1234', '555-555-4321']

#  finditer agisce come findall, ma restituisce un iterabile lazy composto da oggetti match.

for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())

#Il metacarattere '^' posto all’inizio di un’espressione regolare (ma non tra parentesi quadre) 
#indica che l’espressione deve combaciare solo con l’inizio della stringa
print(result = re.search('^Python', 'Python è divertente')) # verifica che l'espressione inizi con Python 

#Il metacarattere '$' posto alla fine di un’espressione regolare (ma non tra parentesi quadre)
#indica che l’espressione deve combaciare solo con la fine della stringa
print(result = re.search('divertente$', 'Python è divertente')) # verifica che l'espressione finisca con divertente

#findall e finditer: trovare tutte le corrispondenze in una stringa 

contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'

telephone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', contact)

for number in telephone_numbers:
    print(number)

for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())

text = 'Charlie Cyan, e-mail: demo1@deitel.com'
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})' 

result = re.search(pattern, text)

result.groups() # restituisce una tupla con i gruppi trovati
result.group(1) # restituisce il primo gruppo trovato

result.group() # restituisce tutto il gruppo trovato 'Charlie Cyan, e-mail: demo1@deitel.com'
