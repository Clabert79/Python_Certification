import sys


#Custom Exception
class RuntimeErrorWithCode(TypeError):
    """ This is a single-line docstring"""
    def __init__(self, message, code):
        super().__init__(f'Error code{code}: {message}')
        self.code = code
    
err = RuntimeErrorWithCode('An Custom error happened', 500)

class UncountableError(ValueError):
    def __init__(self, wrong_value) :
        super().__init__(f"Invalid value for n. {wrong_value}. N must be greate than 0")

def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)

count_from_zero_to_n(-5)

'''
try:
    x = float(input("Inserisci un numero: "))
    inverse = 1.0/x
    print("Inverse: ", inverse)
except ValueError:
    print("Il numero inserito deve essere un intero o un float !!!")
except ZeroDivisionError:
    print("Il numero non pio' essere '0'")
else:
    print("Oreazione completata con successo")
finally:
    print("Messaggio di Finally")

print("__debug__:", __debug__)

# deve eriditare da Exception
class MyException(Exception):
    pass

def fromsquare(seq, index):
    """ restituiece l'elemento della squenza di indice 'index**2'"""
    try:
        i = int(index)
        return seq[i**2]
        #except cattura tutte le eccezioni di questo tipo quindi anche quelle derivate
    except ValueError as ex:
        raise IndexError('La stringa non rappresenta un numero intero') from ex

    except TypeError as ex:
        raise IndexError("L'indice deve essere una stringa, un int o un float") from ex

    except Exception as ex:
        raise IndexError('Errore non previsto') from ex
try:
    pass
    ## fromsquare(['a','b', 'c'], 'due')
except IndexError as ex:
    print(type(ex),ex)


try:
    # solo in fase di debug
    assert 2 * 2 == 4, "Non mi tornano i conti..."
except AssertionError as ex:
    print(ex.args)
    raise

try:
    lst = ['Alice', 'Bob', 'Carl']
    print(lst[5])
except Exception as e:
    print(e) # recupero il messaggio

print('Am I executed?')

# visualizzare tutta la gerarchia di classe
for subclass in Exception.__subclasses__():
    print(subclass.__name__)

# raise MyException

class UserActionException(Exception):
    def __init__(self, message='', user_id='') -> None:
        Exception.__init__(self)
        self.user_id = user_id
        self.message = message
    def __str__(self) -> str:
        return type(self).__name__ + ' Occourred. Error message: ' + self.message + ', UserId: ' + self.user_id

class EmptyNameUserActionException(UserActionException):
    def __init__(self,  user_id='') -> None:
        super().__init__('An empty name was provided', user_id)

def say_hello(name, user_id):
    if name == '':
        raise EmptyNameUserActionException(user_id)
    print(f'Hello word {name} and user {user_id}')

try:
    say_hello('Adam','Dte82828')
    say_hello('', 'Dte82829')
except Exception as e:
    print(e)
    print('--->', e.args)

try:
    raise Exception("I don't like it")
except Exception as e:
    print(e.args)

# creo un'eccezione con argomenti

class DeviceError(Exception):
    def __init__(self, errno, msg):
         self.args = (errno, msg)
         self.errno = errno
         self.errmsg = msg

try:
    raise DeviceError(1, 'Not responding')
except Exception as e:
    print(e.args, e.errno, e.errmsg)

# creo una mia eccezzione partendo da qulla più simile a quello che mi serve
class AnimalValueError(ValueError):
    pass

def produce_animal_sound(animal_type):
    if animal_type == 'Dog':
        print('Woof, woof!')
    elif animal_type == 'Cat':
        print('Meow!')
    else:
        raise AnimalValueError('Incorrect animal !!')

# per sollevevere dei warnig
import warnings
warnings.warn("Attenzione, questo è deprecato", DeprecationWarning)

# per visualizzare i warning i python 3 questi sono i comandi
# python -W error -c (visualizza i warnig come fosserro errori)
# python -W all -c (visualizza i warnig ma non come errori)
# per approfondimenti http://docs.python.org/3/library/warnings.html.
'''

'''
GEARARCHIA DELLE CLASSI
BaseException
+------ SystemExit
+------ KeyboardInterrupt +------ GeneratorExit +------ Exception
+------ StopIteration +------ ArithmeticError
| +------ FloatingPointError | +------ OverflowError
| +------ ZeroDivisionError +------ AssertionError
+------ AttributeError +------ BufferError +------ EOFError +------ ImportError +------ LookupError
| +------ IndexError
| +------ KeyError +------ MemoryError +------ NameError
| +------ UnboundLocalError +------ OSError
| +------ BlockingIOError
| +------ ChildProcessError
| +------ ConnectionError
| | +------ BrokenPipeError
| | +------ ConnectionAbortedError | | +------ ConnectionRefusedError | | +------ ConnectionResetError
| +------ FileExistsError
| +------ FileNotFoundError
| +------ InterruptedError
| +------ IsADirectoryError
| +------ NotADirectoryError
| +------ PermissionError
| +------ ProcessLookupError
| +------ TimeoutError
542
+------ ReferenceError +------ RuntimeError
| +------ NotImplementedError +------ SyntaxError
| +------ IndentationError
| +------ TabError +------ SystemError +------ TypeError +------ ValueError
| +------ UnicodeError
| +------ UnicodeDecodeError | +------ UnicodeEncodeError
| +------ UnicodeTranslateError +------ Warning
+------ DeprecationWarning
+------ PendingDeprecationWarning +------ RuntimeWarning
+------ SyntaxWarning
+------ UserWarning
+------ FutureWarning
+------ ImportWarning
+------ UnicodeWarning
+------ BytesWarning
+------ ResourceWarning


Exception Class             Description
Baseexception               The root class for all exceptions
Exception                   Base class for all program-related errors
ArithmeticError             Base class for all math-related errors
ImportError                 Base class for import-related errors
LookupError                 Base class for all container lookup errors
OSError                     Base class for all system-related errors. IOError and EnvironmentError are aliases.
ValueError                  Base class for value-related errors, including Unicode
UnicodeError                Base class for a Unicode string encoding-related errors”
AssertionError              Failed assert statement
AttributeError              Bad attribute lookup on an object
EOFError                    End of file
MemoryError                 Recoverable out-of-memory error
NameError                   Name not found in the local or global namespace
NotImplementedError         Unimplemented feature
RuntimeError                A generic “something bad happened” error
TypeError                   Operation applied to an object of the wrong type
UnboundLocalError           Usage of a local variable before a value is assigned”
'''


try:
    # user_input = input('Please enter a number!')
    user_input = 'one'  # Just for convenience
    # user_input = 1
    num = 100 / int(user_input)
except TypeError:
    print('You need to use correct Type!')
except ValueError:
    print('You need to use digits!')
except : # deve sempre essere all'ultima posozione <<
    print('Error')
else:
    print('Result:', num)

import sys
import re

try:
    raise NotImplementedError("Not implemented")
except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print("Exception type: ", exception_type)
    print("File name: ", filename)
    print("Line number: ", line_number)

    print("Extract only Exception ... ")
    error_type_clean = str(exception_type)
    marker1 = "'"
    marker2 = "'"
    regexPattern = marker1 + '(.+?)' + marker2
    str_found = re.search(regexPattern, error_type_clean).group(1)

    print("--->>> ", str_found)

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


try:
    linux_interaction()
except AssertionError as error:
    print('-------------------------------------->>')
    print(getattr(error, 'message', repr(error)))
    print('-------------------------------------->>')
    print(getattr(error, 'message', str(error))) # messaggio pulito
    print('-------------------------------------->>')
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')


x = 10
if(x > 10):
    if x > 5:
        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))



