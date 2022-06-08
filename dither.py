# Written by Kouzeru; 4 June 2022

import sys
from PIL import Image

matrices = [
 [ #2x2
  [0,2],
  [3,1],
 ],
 [ #4x2
  [0,4,1,5],
  [6,2,7,3],
 ],
 [ #4x4
  [ 0, 8, 2,10],
  [12, 4,14, 6],
  [ 3,11, 1, 9],
  [15, 7,13, 5],
 ],
 [ #8x4
  [ 0,16, 4,20, 1,17, 5,21,],
  [24, 8,28,12,25, 9,29,13,],
  [ 6,22, 2,18, 7,23, 3,19,],
  [30,14,26,10,31,15,27,11,],
 ],
 [ #8x8 Bayer matrix
  [ 0,32, 8,40, 2,34,10,42,], 
  [49,16,57,24,51,18,59,26,], 
  [12,44, 4,36,14,46, 6,38,], 
  [61,28,53,20,63,30,55,22,], 
  [ 3,35,11,43, 1,33, 9,41,], 
  [52,19,60,27,50,17,58,25,], 
  [15,47, 7,39,13,45, 5,37,], 
  [64,31,56,23,62,29,54,21,], 
 ]
]

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
  
matrix = matrices[4]
matrw = len(matrix[0])
matrh = len(matrix)
matrs = matrw*matrh

outputimage = inputimage.convert("RGB")

for y in range(inputimage.size[1]):
 for x in range(inputimage.size[0]):
  matv = (matrix[y%matrh][x%matrw]+1)/(matrs+1)
  cR,cG,cB = inputimage.getpixel((x,y))
  cR,cG,cB = cR/255,cG/255,cB/255
  cR = 0 if cR*cR < matv else 255
  cG = 0 if cG*cG < matv else 255
  cB = 0 if cB*cB < matv else 255
  outputimage.putpixel((x,y),(cR,cG,cB))

outputfile = open("output.png","wb")

outputimage.save(outputfile)
outputfile.close()
outputimage.show()
input("done!")
