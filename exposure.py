# Written by Kouzeru; 8 June 2022

import sys
from PIL import Image, ImageMath
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
 
inpopacity = 0
while inpopacity == 0:
 try:
  inpopacity = int(input("Strength of image in %? [0 - 1000]: "))
  if inpopacity<   0: raise ValueError
  if inpopacity>1000: raise ValueError
 except:
  print("Invalid number!")
  inpopacity = 0

strpromp = "convert(a*"+str(inpopacity)+"/100,'L')"
partR = ImageMath.eval(strpromp,a=inputimage.getchannel(0))
partG = ImageMath.eval(strpromp,a=inputimage.getchannel(1))
partB = ImageMath.eval(strpromp,a=inputimage.getchannel(2))

out = Image.merge("RGB",(partR,partG,partB))

zzz = open("output.png","wb")
out.save(zzz)
zzz.close()
out.show()
input("Done! output.png is the result")