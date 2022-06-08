# Written by Kouzeru; 8 June 2022

import sys
from PIL import Image
inputfile = ""

if len(sys.argv)>1:
 inputfile = sys.argv[1]
else:
 inputfile = input("Input file: ")

inputimage = None
while not type(inputimage) == Image.Image:
 try:
  blob = Image.open(inputfile)
  inputimage = blob.convert("L")
  blob.close()
 except:
  inputfile = input("Invalid file!\nInput file: ")

outputfile = open("output.png","wb")

inputimage.save(outputfile)
outputfile.close()
inputimage.show()
input("done!")
