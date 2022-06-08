# Written by Kouzeru; 4 June 2022

import sys
from PIL import Image, ImageFilter, ImageMath

PIXELSIZE = 5

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


outputimage = inputimage.resize((inputimage.size[0]*PIXELSIZE,inputimage.size[1]*PIXELSIZE),Image.NEAREST)

blurredimage = outputimage.filter(ImageFilter.GaussianBlur(radius = 0))


lotofdot = Image.new("L",(PIXELSIZE,PIXELSIZE))
for b in range(lotofdot.size[1]):
 for a in range(lotofdot.size[0]):
  ex = PIXELSIZE/2-a%PIXELSIZE
  ey = PIXELSIZE/2-b%PIXELSIZE
  ez = (ex*ex+ey*ey)**0.5
  lotofdot.putpixel((a,b),int(256-(ez-1.5)*256))

while lotofdot.size[0]<outputimage.size[0]:
 newdots = Image.new("L",(lotofdot.size[0]*2,lotofdot.size[1]))
 newdots.paste(lotofdot,(lotofdot.size[0],0))
 newdots.paste(lotofdot,(0,0))
 lotofdot = newdots
 
while lotofdot.size[1]<outputimage.size[0]:
 newdots = Image.new("L",(lotofdot.size[0],lotofdot.size[1]*2))
 newdots.paste(lotofdot,(0,lotofdot.size[1]))
 newdots.paste(lotofdot,(0,0))
 lotofdot = newdots

newdots = Image.new("L",outputimage.size)
newdots.paste(lotofdot,(0,0))
lotofdot = newdots

dottedinputR = ImageMath.eval("a/2+b/2",a=blurredimage.getchannel(0),b=ImageMath.eval("convert(a*b/255,'L')",a=outputimage.getchannel(0),b=lotofdot))
dottedinputG = ImageMath.eval("a/2+b/2",a=blurredimage.getchannel(1),b=ImageMath.eval("convert(a*b/255,'L')",a=outputimage.getchannel(1),b=lotofdot))
dottedinputB = ImageMath.eval("a/2+b/2",a=blurredimage.getchannel(2),b=ImageMath.eval("convert(a*b/255,'L')",a=outputimage.getchannel(2),b=lotofdot))

partR = Image.new("L",outputimage.size)
partG = Image.new("L",outputimage.size)
partB = Image.new("L",outputimage.size)

partR.paste(dottedinputR,(-1,-1))
partG.paste(dottedinputG,( 0, 1))
partB.paste(dottedinputB,( 1,-1))

out = Image.merge("RGB",(partR,partG,partB))

zzz = open("output.png","wb")
out.save(zzz)
zzz.close()
out.show()
input("Done! output.png is the result")