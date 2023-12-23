'''
ufficiale
https://docs.python.org/3/library/pathlib.html
https://realpython.com/python-pathlib/ <<<
https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern <<<

https://www.google.com/search?q=python+handle+IO+file+and+directory+in+deep&rlz=1C1CHBF_itIT1078IT1078&oq=python+handle+IO+file+and+directory+in+deep&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigAdIBCTI1NzcyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

shutil
https://www.pythonpool.com/python-shutil/ <<<

OS and Shutil Modules >> search


way to remove
os.remove('file_path')
os.unlink('file_path')
pathlib.Path("file_path").unlink()
os.rmdir('empty_dir_path')
pathlib.Path(empty_dir_path).rmdir()
shutil.rmtree('dir_path')

'''
import os
from pathlib import Path
from pathlib import PurePath
from pathlib import PurePosixPath
import shutil

print(Path.home())
print(os.getcwd())


p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])

'''
p_dir_1 = Path('Exercises')

print(p_dir_1.resolve())
print('Exist', p_dir_1.exists())
print('Is Dir', p_dir_1.is_dir())

p_dir_2 = PurePath('/Exercises')
print(p_dir_2.parts)

p_root = PurePosixPath('/Exercises').root
print(p_root)
'''

for folder, sub_folders, files in os.walk(os.getcwd()):

    if '.git' not in folder:

        print("-->>")
        print(f"in folder: '{folder}' ")

        if  sub_folders:
            print("---->>>>>>")
            print(f"the sub Folders: '{sub_folders}'")

        '''
    for file in files:
        if file.endswith('.py'):
            print(file)
    '''

print(os.getcwd())
file = open('test_1.txt', 'w+')
file.write('Subscribe to Techfitlab!')
file.close()
print(type(os.listdir()))
dir_ex_dir = str(os.path.join(str(os.getcwd()), "files_ex"))

path_ex = Path(dir_ex_dir)

if not path_ex.is_dir():
    print("NOT EXIST")
    os.mkdir(dir_ex_dir)
else:
    print("ALREADY EXIST")
    dir_ex_file = str(os.path.join(str(os.getcwd()), "files_ex", "test_1.txt"))
    path_ex_file = Path(dir_ex_file)

    if not path_ex_file.is_file() :
        shutil.move('test_1.txt', dir_ex_dir)
        
    
    print(os.listdir(dir_ex_dir))

    os.unlink(dir_ex_file)
    print(os.listdir(dir_ex_dir))

   # os.rmdir(dir_ex_dir)
    shutil.rmtree(dir_ex_dir)

print("**********************************************")
path_dir_files = str(os.path.join(str(os.getcwd()), "Files"))
dir_ex_file = str(os.path.join(str(os.getcwd()),"Files", "test_read_file.txt"))
path_ex_file = Path(dir_ex_file)

if path_ex_file.is_file():
    print("Exist File ", path_ex_file)
    path_copy = str(os.getcwd())
    print(os.listdir(path_dir_files))
    source =  str(os.path.join(str(os.getcwd()), "Files", "test_read_file.txt"))
    perms = os.stat(source).st_mode 
    print("File Permission mode:  ", perms, "\n") 
    destinationfile = str(os.path.join(str(os.getcwd()), "Files", "test_read_file_copy.txt"))
    dests = shutil.copy(source, destinationfile)
    print("After copying file: ")  
    print(os.listdir(path_dir_files)) 
    print("Delete file file: ") 
    Path(destinationfile).unlink() # <<<--- delete file
    print(os.listdir(path_dir_files))

'''
if not os.path.exists(dir_ex):
    print("NOT EXIST")
    os.mkdir(dir_ex)
else:
    print("EXIST")
'''


'''
import os

for dirpath, dirnames, filenames in os.walk("/<YOUR DIRECTORY STRUCTURE>/myfolder"):
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print(" ----------------- ")
    pass

# Get basename.. that's the file at the directory location given
print(os.path.basename("/bin/tools/myfile.txt"))

# Get the directory name only, not the file
print(os.path.dirname("/bin/tools/hello/balbala/myfile.txt"))

# Will give directory name and basename in a tuple
print(os.path.split("/bin/tools/hello/balbala/myfile.txt"))

# Check if the path exists on the computer
print(os.path.exists("/bin/tools/hello/balbala/myfile.txt"))

# used to check if file exists in the specified path
os.path.isfile("/bin/tools/hello/balbala/myfile.txt")

# used to check if directory exists in the specified path
os.path.isdir("/bin/tools/hello/balbala/myfile.txt")

# Get file with path and file extension in a tuple
print(os.path.splitext("/bin/tools/hello/balbala/myfile.txt"))

'''

