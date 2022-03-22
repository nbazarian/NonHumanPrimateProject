import argparse
import os
import numpy as np
import pandas as pd
import xml.etree.ElementTree as et

column_names = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

def get_arguments():
    parser = argparse.ArgumentParser(description="XML to CSV converter for image annotations")
    parser.add_argument('-i', help="Path to the input directory containing all XML labels", metavar='<input_folder>')
    parser.add_argument('-o', help="CSV file you wish to be generated", metavar='<output_folder>')

    args = parser.parse_args()

    if args.i == None:
        parser.print_help()
        print("Error: argument '-i' is required")
        exit()

    if args.o == None:        
        c = input("CSV files will be generated in the current directory. Are you sure? [y/n] ")        
        if c.lower() == 'n':            
            exit()
        elif c.lower() == 'y':
            print(os.getcwd())
            return args.i, os.getcwd()

    return args.i, args.o

def parse_xml(file):
    # Order is that of the 'column_names' variable
    data = []

    tree = et.parse(file)
    root = tree.getroot()    

    for obj in root.findall('object'):
        row = []
        row.append(root.find('filename').text)

        for elem in root.iter('width'):
            row.append(int(elem.text))

        for elem in root.iter('height'):
            row.append(int(elem.text))
        
        for elem in obj.iter('name'):
            row.append(elem.text)        

        for elem in obj.iter('xmin'):
            row.append(int(elem.text))

        for elem in obj.iter('ymin'):
            row.append(int(elem.text))

        for elem in obj.iter('xmax'):
            row.append(int(elem.text))

        for elem in obj.iter('ymax'):
            row.append(int(elem.text))

        data.append(row)

    return(data)

def __main__():
    

    input_folder, output_folder = get_arguments()

    data = []

    for file in os.listdir(input_folder):
        row = parse_xml(os.path.join(input_folder, file))
        for element in row:
            data.append(element)
    
    df = pd.DataFrame(data, columns=column_names)

    if 'train' in str(input_folder):
        name = 'train'
    elif 'test' in str(input_folder):
        name = 'test'

    df.to_csv(name + '_labels.csv', index=False)
    

if __name__ == '__main__':
    __main__()
