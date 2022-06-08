# Written by Kouzeru; 8 June 2022

import sys
from PIL import Image, ImageFilter

inputfile = ""

if len(sys.argv)>1:
 inputfile = sys.argv[1]
else:
 inputfile = input("Input file: ")

inputimage = None
while not type(inputimage) == Image.Image:
 try:
  blob = Image.open(inputfile)
  inputimage = blob.convert("RGB")
  blob.close()
 except:
  inputfile = input("Invalid file!\nInput file: ")

inpradius = 0
while inpradius == 0:
 try:
  inpradius = float(input("Radius? [0.1 - 999.0]: "))
  if inpradius== 0: raise ValueError
  if inpradius>999: raise ValueError
 except:
  print("Invalid number!")
  inpradius = 0

out = inputimage.filter(ImageFilter.GaussianBlur(radius = inpradius))

zzz = open("output.png","wb")
out.save(zzz)
zzz.close()
out.show()
input("Done! output.png is the result")