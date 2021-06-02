with open('text.txt') as f:
   data = f.read()
   data.replace(",", " ")
   print(len(data.split(" ")))
