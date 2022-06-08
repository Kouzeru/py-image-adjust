# Written by Kouzeru; 8 June 2022

import sys
from PIL import Image, ImageMath
inputfile = ""

if len(sys.argv)>1:
 inputfile = sys.argv[1]
else:
 inputfile = input("Input file image A: ")

inputimage = None
while not type(inputimage) == Image.Image:
 try:
  blob = Image.open(inputfile)
  inputimage = blob.convert("RGB")
  blob.close()
 except:
  inputfile = input("Invalid file!\nInput file image A: ")
 

inputfile = ""

if len(sys.argv)>2:
 inputfile = sys.argv[2]
else:
 inputfile = input("Input file image B: ")

inputimage2 = None
while not type(inputimage2) == Image.Image:
 try:
  blob = Image.open(inputfile)
  inputimage2 = blob.convert("RGB")
  blob.close()
 except:
  inputfile = input("Invalid file!\nInput file image B: ")

inpopacity = 0
while inpopacity == 0:
 try:
  inpopacity = int(input("Strength of image B in %? [0 - 100]: "))
  if inpopacity<  0: raise ValueError
  if inpopacity>100: raise ValueError
 except:
  print("Invalid number!")
  inpopacity = 0

strpromp = "convert(a*"+str(100-inpopacity)+"/100+"+"b*"+str(inpopacity)+"/100,'L')"
partR = ImageMath.eval(strpromp,a=inputimage.getchannel(0),b=inputimage2.getchannel(0))
partG = ImageMath.eval(strpromp,a=inputimage.getchannel(1),b=inputimage2.getchannel(1))
partB = ImageMath.eval(strpromp,a=inputimage.getchannel(2),b=inputimage2.getchannel(2))

out = Image.merge("RGB",(partR,partG,partB))

zzz = open("output.png","wb")
out.save(zzz)
zzz.close()
out.show()
input("Done! output.png is the result")