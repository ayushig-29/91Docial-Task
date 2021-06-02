import os
file_number = 0
file_size = 0
extension = ".txt"
while True:
 if file_size < 2e+6:
   try:
     file = open('%d.txt'%file_number, 'x')
   except:
      pass
   file = open('%d.txt'%file_number)
   text = file.read() + 'Hello World'
   file = open('%d.txt'%file_number, 'w')
   file.write(text)
 file_size = os.stat('%d.txt'%file_number) .st_size
 if file_size > 2e+6:
   file_number += 1
   file_size = 0