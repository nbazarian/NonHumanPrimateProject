import glob
import PIL
from PIL import Image

files = glob.glob('/Users/bazariann/Documents/MonkeyDeepLearnModel/NonHumanPrimateProject/test/*')
len(files)
for file in files:
    if '.jpg' in file:
        image = PIL.Image.open(file)
    if image.format not in ['JPG', 'JPEG']:
        print (file)
        image.convert('RGB').save(file, 'JPEG')