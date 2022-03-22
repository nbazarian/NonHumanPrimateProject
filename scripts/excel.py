# Python program to rename all file
# names in your directory
import os
import openpyxl
os.chdir('C:\\Users\\bazariann\\Downloads\\test')
print(os.getcwd())

wb = openpyxl.Workbook()
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)

 
      
    # Get workbook active sheet 
    # from the active attribute 
    sheet = wb.active 
      
    # Cell objects also have row, column 
    # and coordinate attributes that provide 
    # location information for the cell. 
      
    # Note: The first row or column integer 
    # is 1, not 0. Cell object is created by 
    # using sheet object's cell() method. 
    c1 = sheet.cell(row = (count +1), column = 1) 
      
    # writing values to cells 
    c1.value = f_name;
    
    wb.save(filename="test.xlsx")

      
