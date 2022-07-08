# Python program to rename all file
# names in your directory
import os
 
os.chdir('C:\\Users\\bazariann\\Downloads\\nepal horse-20220610T181925Z-001\\nepal horse')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "horse" + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
