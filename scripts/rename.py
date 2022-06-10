# Python program to rename all file
# names in your directory
import os
 
os.chdir('C:\\Users\\bazariann\\Downloads\\nepalese people-20220603T203143Z-001\\nepalese people')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "nepalese" + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
