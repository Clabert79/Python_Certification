
# https://www.datacamp.com/community/tutorials/reading-writing-files-python?utm_source=adwords_ppc&utm_campaignid=9942305733&utm_adgroupid=100189364546&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=255798340456&utm_targetid=aud-517318241987:dsa-929501846124&utm_loc_interest_ms=&utm_loc_physical_ms=20609&gclid=CjwKCAjw8df2BRA3EiwAvfZWaHICHyRTZ58-qgFRUj0REIOenZqYlkMQiG3sFkf8s0bxWtCpc2xxhxoCSFIQAvD_BwE


'''
output = open(r'C:\spam', 'w')		Create output file ('w' means write)
input = open('data', 'r')			Create input file ('r' means read)
input = open('data')				Same as prior line ('r' is the default)
aString = input.read()				Read entire file into a single string
aString = input.read(N)				Read up to nextNcharacters (or bytes) into a string
aString = input.readline()			Read next line (including\nnewline) into a string
aList = input.readlines()			Read entire file into list of line strings (with \n)
output.write(aString)				Write a string of characters (or bytes) into file
output.writelines(aList)			Write all line strings in a list into file
output.close()						Manual close (done for you when file is collected)
output.flush()						Flush output buffer to disk without closing
anyFile.seek(N)						Change file position to offsetNfor next operation
for line in open('data'):			File iterators read line by line
open('f.txt', encoding='latin-1')	Python 3.X Unicode text files (str strings)
open('f.bin', 'rb')					ython 3.X bytes files (bytes strings)
'''

# modi:

# r (apertura in lettura del file dall'inizio)
# r+ (apertura in lettura e scrittura del file dall'inizio )
# w (apertura in scrittura, se il file già esiste lo sovrascrive altrimenti lo crea)
# w+ (apertura in scrittura e lettura, se il file già esiste lo sovrascrive altrimenti lo crea)
# x (l'apertura del file fallisce se il file esiste già)
# a (apertura in scrittura. Se il file esiste viene scritto dalla fine, se non esiste viene creato)
# a+ (apertura in scrittura e lettura. Se il file esiste viene scritto dalla fine, se non esiste viene creato)
# t (aperura di un file in modalità testo)
# b (apertura di un file in modalità binaria)

# giro completo
print('----------------------------------------')
myfile = open('myfile.txt', 'w')
print(myfile.write('hello text file\n'))
print(myfile.write('goodbye text file\n'))
myfile.close() # Flush output buffers to disk
myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(open('myfile.txt').read())
for line in open('myfile.txt'):
	print(line, end='')
print('----------------------------------------')
print('Binary')

file_wb_1 = open('data.bin', 'wb')	# Open binary output file
import struct
data_wb_1 = struct.pack('>i4sh', 7, b'spam', 8) # Make packed binary data
print(data_wb_1)
file_wb_1.write(data_wb_1)
file_wb_1.close()

file_wb_2  = open('data.bin', 'rb')
data_wb_2 = file_wb_2.read()
values = struct.unpack('>i4sh', data_wb_2)
print(values)

print('----------------------------------------')
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafiletype.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

# for line in open('datafiletype.txt'):
#	print(line.rstrip(), end='') # rstrip() elimina il carattere di a capo

chars = open('datafiletype.txt').read()
print(chars)

# ..
F = open('datafiletype.txt')
line = F.readline()
print(line)
print(line.rstrip())

line = F.readline()
print(line)
parts =  line.split(',')
print(parts)
print(int(parts[1]))

numbers = [int(P.rstrip()) for P in parts]
print(numbers)

line = F.readline()
print(line)
parts = line.split('$')
print(parts)
print(eval(parts[0])) #Using eval to convert from strings to objects

objects = [eval(P) for P in parts] #Using eval to convert from strings to objects
print(objects)
# ..

print('\n ----------------------------------------')
import os
import subprocess

filew_1 = open('myfile','w')
print(filew_1.mode)
print(filew_1.readable())

filew_1.write('testo') # restituisce il numero di caratteri

# file aperto in binary mode
filer_1 = open('myfile','rb') # la r sta per lettura la b finale sta per binary
filer_1.read()

filew_2 = open('myfile','wb')
filew_2.write(b'testo byte') # scriviamo una stringa di byte

filer_1.read(2) # legge 2 caratteri

# quando il file object non ha più etichette che fanno riferimanto svuota il file

# quando si raggiunge la fine del fil file.read() restituisce una stringa vuota
filew_2.seek(0) # svuota il buffer e ci posiziona all'inizio del file
filew_2.tell() # svuota il file e ci restituisce la posizione

filew_1.writelines(['oggetto iterabile\n'])  # scrive su file un oggetto iterabile
										  # deve essere agiunto il carettre di new line in maniera esplicita

filer_1.readline() # legge una line per volta lasciado un cratere newline

# quando scriviamo un file si genera un buffering di scrittura in memoria
filer_1.flush() #svuota il file
filer_1.close() #svuota anche il file

# usare sempre la clausola with
with open('myfile_1.txt') as f:
	print(f.read())

'''
open(
	file,
	mode = 'r', --- > 'x' gestisce meglio la gestine del file
	buffering = -1
	encoding = None (di default uft 8 es encoding='latin1')
	errors = None, (errors='ignore', errors='replace')
	newline = None,
	closefd = True,
	opener = None ) -> Object deve essere None oppure un oggetto callable
'''

open('myfile_utf_16','w',encoding='utf-16').write('Pyhton 3')
print(open('myfile_utf_16','rb').read())
print(open('myfile_utf_16','rb').read(2))
print(open('myfile_utf_16',encoding='utf-16').read())

import os, stat

filew_3 = open('foo.bash','w')
filew_3.write('testo di prova')
# imposta i permessi
open('foo.bash', opener=lambda file,flags: os.open(file, flags, 0o777))
mode = os.stat('foo.bash').st_mode
print(stat.filemode(mode))

print(" lettura file riga per riga ")
for line in open("Files/test_read_file.txt"):
	line_str = str(line) # devo trasformarla per poterla elaborarere
	print(line_str, end='')

## Quando si apre un file è buona pratica aprirlo con with perchè gestiste da solo la procedura di chiusura

with open("Files/test_read_file.txt") as f_with:
	data = f_with.read();
	print(data)

print(f_with.closed)


print(" Componente subprocess ... ")
subprocess.call('pwd')

print('---------------------------')
print('Ciclo File ...')
print('---------------------------')

print('Create File ...')
f1 = open('data.txt', 'w')
f1.write('Hello\n')
f1.write('world\n')
f1.close()
print('Finish create File')
print('Read File ...')
f2 = open('data.txt')
text = f2.read()
print(text)
print(text.split())
print('Read Line ...')
for line in open('data.txt'): print(line)

print('---------------------------')
print('Fine')
print('---------------------------')
print('Metodi File')
print(dir(f2))

'''
"r+", "rb+" ---> lettura/scrittura
"w+", "wb+", ---> lettura/scrittura
"a+", "ab+" ----> append/scrittura
'''

# https://coderslegacy.com/python/python-advanced-file-handling/
# https://realpython.com/read-write-files-python/

with open("isolamisteriosa.txt", "rt") as f_in,\
	open("outputfileisola.txt", "w") as f_out:
	lines = f_in.readlines()
	flag = True
	counter = 1
	for line in lines:
		if flag == True:
			f_out.write(f"{counter} : {line}")
		flag = not flag
		counter += 1

print('Read File outputfileisola.txt ...')
f_out_r = open('outputfileisola.txt')
text = f_out_r.read()
print(text)		


with open("isolamisteriosa.txt", "rt") as f_in,\
	open("outputfileisola.txt", "a") as f_out:
	lines = f_in.readlines()
	flag = False
	counter = 1
	for line in lines:
		if flag == True:
			f_out.write(f"{counter} : {line}")
		flag = not flag
		counter += 1

print('Read File outputfileisola.txt ...')
f_out_r = open('outputfileisola.txt')
text = f_out_r.read()
print(text)	

print('Read File testo.txt ...')
filer_2 = open("testo.txt", "r", encoding='utf-8')
for line in filer_2:
 print(line, end="")
filer_2.close()

my_file = open('my_file_1.txt','w')
my_file.write("New text")
my_file.close()

my_file = open('my_file_1.txt','r')
print(my_file.read())
my_file.close()

record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]
file = open("my_file_1", "a")
file.writelines("\t".join(record_last_session))
file.close()
file = open("my_file_1", "r")
print(file.read())

# SEEK 
# https://pynative.com/python-file-seek/
# f.seek(offset, whence)

# whence '0' means from the beginning of the file.
# whence '1' uses the current file position
# whence '2' uses the end of the file as the reference point.

with open(r'sample.txt', "r") as fp:
    # Moving the file handle to 6th character 
    fp.seek(6) # sposta la partenza della lettura successiva di 6 caratteri
    # read file
    print(fp.read())

print('-------------------------------------------')

with open(r'sample.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2) # sposta il puntatore alla fine

    # Inserting new content to the end of the file
    fp.write("\nThis content is added to the end of the file")

    # moving to the beginning 
    # again read the whole file
    fp.seek(0)
    print(fp.read())

