# Python program to rename all file
# names in your directory
import os
 
os.chdir('C:\\Users\\bazariann\\Downloads\\rhesus macaque-20220218T033359Z-001\\rhesus macaque')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "macaque" + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
