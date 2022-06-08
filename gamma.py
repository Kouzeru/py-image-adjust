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
  inputimage = blob.convert("RGB")
  blob.close()
 except:
  inputfile = input("Invalid file!\nInput file image A: ")
 
gamma = 0
while gamma == 0:
 try:
  gamma = float(input("Gamma correction? [0.25 - 4]: "))
  if gamma<  0: raise ValueError
  if gamma>100: raise ValueError
 except:
  print("Invalid number!")
  gamma = 0

out = inputimage.convert("RGB")

for y in range(inputimage.size[1]):
 for x in range(inputimage.size[0]):
  cR,cG,cB = inputimage.getpixel((x,y))
  cR = int((cR/255)**(gamma)*255)
  cG = int((cG/255)**(gamma)*255)
  cB = int((cB/255)**(gamma)*255)
  out.putpixel((x,y),(cR,cG,cB))

zzz = open("output.png","wb")
out.save(zzz)
zzz.close()
out.show()
input("Done! output.png is the result")